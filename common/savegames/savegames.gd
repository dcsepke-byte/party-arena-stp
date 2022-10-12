class_name SaveGameLoader

const SAVEGAME_DIRECTORY = "user://saves/"

# Versioned savegame data
# Will make it easier to load old savegame formats in the future (if necessary)
class SaveGamePlayerStateV1:
	var player_name := ""
	var is_ai := false
	var ai_difficulty: int = Lobby.Difficulty.NORMAL
	var space: NodePath
	var character := ""
	var cookies := 0
	var cakes := 0

	var items := []
	var roll_modifiers := []

class SaveGameBoardStateV1:
	var board_path := ""
	var cake_space := NodePath()
	var player_turn := 1
	var turn := 1
	var trap_states := []

class SaveGameMinigameStateV1:
	var minigame_config
	var minigame_type := -1
	var minigame_teams := []
	var has_reward := false
	var duel_reward := -1
	var item_reward: Dictionary = {}

class SaveGame:
	# Version of the savegame format
	var version := 1

	var players := []
	var board_state := SaveGameBoardStateV1.new()
	var minigame_state := SaveGameMinigameStateV1.new()
	var settings := {}

	func add_player() -> SaveGamePlayerStateV1:
		var playerstate := SaveGamePlayerStateV1.new()
		self.players.append(playerstate)
		return playerstate

	func serialize() -> Dictionary:
		var save_dict: Dictionary = inst2dict(self)
		
		# 'inst2dict()' is not recursive. Serialize nested objects.
		var players_serialized := []
		for player in self.players:
			players_serialized.append(inst2dict(player))
		save_dict["players"] = players_serialized
		save_dict["board_state"] = inst2dict(self.board_state)
		save_dict["minigame_state"] = inst2dict(self.minigame_state)
		
		return save_dict
	
	static func from_data(data: Dictionary) -> SaveGame:
		var savegame: SaveGame = dict2inst(data)
		if not savegame:
			return null
		if not "players" in data:
			return null
		for i in data["players"].size():
			savegame.players[i] = dict2inst(data["players"][i])
			if not savegame.players[i]:
				return null
		for property in ["board_state", "minigame_state"]:
			if not property in data:
				return null
			savegame.set(property, dict2inst(data[property]))
			if not savegame.get(property):
				return null
		return savegame

var savegames: Dictionary

func read_savegames() -> void:
	savegames.clear()

	var dir := Directory.new()
	if dir.open(SAVEGAME_DIRECTORY) != OK:
		return

	dir.list_dir_begin(true)

	while true:
		var filename: String = dir.get_next()

		if filename == "":
			break

		var file := File.new()
		var path := SAVEGAME_DIRECTORY + filename
		var err: int = file.open(path, File.READ)
		if err != OK:
			print("Couldn't open file '%s'" % path)
			continue

		var savegame_var = file.get_var()
		if typeof(savegame_var) != TYPE_DICTIONARY:
			print("File '%s' is not a valid save" % path)
			continue

		file.close()

		var savegame = SaveGame.from_data(savegame_var)
		if not savegame:
			print("File '%s' is not a valid save" % path)
			continue
		savegames[filename] = savegame

	dir.list_dir_end()

func _init():
	read_savegames()

func get_num_savegames() -> int:
	return savegames.size()

func get_filename(i) -> SaveGame:
	return savegames.keys()[i]

func get_savegame(i) -> SaveGame:
	return savegames.values()[i]

# Returns true on success.
func save(filename: String, savegame: SaveGame) -> bool:
	# insert new savegame or overwrite previous savegame of that name
	savegames[filename] = savegame

	var dir := Directory.new()
	if not dir.dir_exists(SAVEGAME_DIRECTORY):
		var err: int = dir.make_dir_recursive(SAVEGAME_DIRECTORY)
		if err != OK:
			print("Failed to create directory '%s'" % SAVEGAME_DIRECTORY)
			return false

	var file := File.new()
	var path: String = SAVEGAME_DIRECTORY + filename
	var err: int = file.open(path, File.WRITE)
	if err != OK:
		print("Failed to open file '%s'" % path)
		return false

	file.store_var(savegame.serialize())
	file.close()
	return true

func delete_savegame(filename: String) -> void:
	if not savegames.has(filename):
		return

	savegames.erase(filename)

	var directory := Directory.new()
	var path := SAVEGAME_DIRECTORY + filename
	var err: int = directory.remove(path)
	if err != OK:
		print("Failed to delete file '%s'" % path)
