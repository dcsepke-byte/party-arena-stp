## Schutzschild (Party Arena Item)
## item-system.md §3.1, item-shield.md
##
## Passiv wirkendes (passive) Item. Blockt automatisch einen einzigen
## negativen Effekt vollständig und wird dabei selbst verbraucht.
##
## Blockbare Effekte: Dieb-Handschuh (Item+Münzen), Pech-Feld, negative Events.
## Nicht blockbar: Event-Teleportation, Positions-Tausch, normale Spielmechaniken.
##
## Preis: 6 Münzen
## Aktivierung: passiv (nie manuell)
extends Item


func _init() -> void:
	super(TYPES.ACTION, "Schutzschild")
	item_id = "shield"
	item_effect_type = EFFECT_TYPES.PASSIVE
	is_consumed = true  # Wird erst bei Auslösung verbraucht
	can_be_bought = true
	item_price = 6


func get_description() -> String:
	return "Blockt automatisch den nächsten negativen Effekt."


## Schutzschild ist passiv — keine manuelle Aktivierung.
## Gibt den item_id zurück, damit der Controller den Schild-Zustand prüfen kann.
func activate(_player: Node3D, _controller: Node3D):
	return {action = "shield_check", item_id = "shield"}
