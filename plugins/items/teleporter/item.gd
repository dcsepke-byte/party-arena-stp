## Stern-Teleporter (Party Arena Item)
## item-system.md §3.1, item-teleporter.md
##
## Sofort wirksames (immediate) Item. Teleportiert den Spieler direkt
## zu einem Sternen-Shop-Feld mit verfügbarem Stern, statt zu würfeln
## und sich zu bewegen.
##
## Preis: 8 Münzen
## Aktivierung: Phase 0 (vor dem Würfeln, statt Würfeln+Bewegung)
extends Item


func _init() -> void:
	super(TYPES.ACTION, "Stern-Teleporter")
	item_id = "teleporter"
	item_effect_type = EFFECT_TYPES.IMMEDIATE
	is_consumed = true
	can_be_bought = true
	item_price = 8


func get_description() -> String:
	return "Teleportiere dich zu einem Sternen-Shop mit verfügbarem Stern."


## Aktiviert den Teleporter. Die eigentliche Teleport-Logik (Zielauswahl,
## Stern-Verfügbarkeit, Bewegung) wird vom Controller abgewickelt.
func activate(_player: Node3D, _controller: Node3D):
	# Gibt den item_id zurück, damit der Controller die Teleporter-Logik
	# von einem normalen Wurf unterscheiden kann.
	return {action = "teleport", item_id = "teleporter"}
