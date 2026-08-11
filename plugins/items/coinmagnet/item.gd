## Münz-Magnet (Party Arena Item)
## item-system.md §3.1, item-coinmagnet.md
##
## Verzögert wirkendes (delayed) Item. Verdoppelt alle eigenen Münz-Gewinne
## des Spielers für 3 eigene Züge.
##
## Verdoppelt: Münz-Bonus-Felder, Glück-Felder (positiv), Minispiel-Belohnungen,
##   Event-Münzen (positiv).
## Nicht verdoppelt: Pech-Verluste, Stern-Kauf (20), Item-Preise, gestohlene Münzen.
##
## Preis: 4 Münzen
## Aktivierung: Phase 0 (vor dem Würfeln)
extends Item


func _init() -> void:
	super(TYPES.ACTION, "Münz-Magnet")
	item_id = "coinmagnet"
	item_effect_type = EFFECT_TYPES.DELAYED
	is_consumed = true
	can_be_bought = true
	item_price = 4


func get_description() -> String:
	return "Verdoppelt alle Münz-Gewinne für 3 Züge."


## Aktiviert den Münz-Magnet. Die Wirkung (3 Züge, Verdopplung) wird
## vom Controller als separater Zustand am Spieler geführt.
func activate(_player: Node3D, _controller: Node3D):
	return {action = "coinmagnet", item_id = "coinmagnet", duration = 3, multiplier = 2}
