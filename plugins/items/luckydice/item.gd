## Glücks-Würfel (Party Arena Item)
## item-system.md §3.1, item-luckydice.md
##
## Sofort wirksames (immediate) Item. Ersetzt den normalen Würfelwurf (1–6)
## durch einen festen Wurf von 5 Feldern.
##
## Preis: 5 Münzen
## Aktivierung: Phase 0 (vor dem Würfeln)
extends Item


func _init() -> void:
	super(TYPES.DICE, "Glücks-Würfel")
	item_id = "luckydice"
	item_effect_type = EFFECT_TYPES.IMMEDIATE
	is_consumed = true
	can_be_bought = true
	item_price = 5


func get_description() -> String:
	return "Würfle eine feste 5 statt 1–6."


## Aktiviert den Glücks-Würfel: gibt fest 5 zurück (bzw. 10 bei Verdoppler)
func activate(_player: Node3D, _controller: Node3D):
	return 5
