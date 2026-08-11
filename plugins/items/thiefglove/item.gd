## Dieb-Handschuh (Party Arena Item)
## item-system.md §3.1, item-thiefglove.md
##
## Sofort wirksames (immediate) Item. Stiehlt von einem anderen Spieler
## entweder 1 zufälliges Item aus dessen Inventar oder 5–15 Münzen.
##
## Preis: 10 Münzen
## Aktivierung: Phase 2 (nach dem Würfeln, vor der Bewegung)
extends Item


func _init() -> void:
	super(TYPES.ACTION, "Dieb-Handschuh")
	item_id = "thiefglove"
	item_effect_type = EFFECT_TYPES.IMMEDIATE
	is_consumed = true
	can_be_bought = true
	item_price = 10


func get_description() -> String:
	return "Stiehl ein Item oder 5–15 Münzen von einem Gegner."


## Aktiviert den Dieb-Handschuh. Die Diebstahl-Logik (Zielauswahl,
## Moduswahl Item/Münzen, Auflösung) wird vom Controller abgewickelt.
func activate(_player: Node3D, _controller: Node3D):
	return {
		action = "thiefglove",
		item_id = "thiefglove",
		coin_steal_min = 5,
		coin_steal_max = 15
	}
