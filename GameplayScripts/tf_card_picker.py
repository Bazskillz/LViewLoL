from lview import *

lview_script_info = {
	"script": "Twisted Fate Card Picker",
	"author": "leryss",
	"description": "Picks specific cards for twisted fate",
	"target_champ": "TwistedFate"
}

key_blue, key_red, key_yellow = 0, 0, 0
card_to_lock = None
key_w = 17

def lview_load_cfg(cfg):
	global key_blue, key_red, key_yellow
	key_blue   = cfg.get_int("key_blue", 0)
	key_red    = cfg.get_int("key_red", 0)
	key_yellow = cfg.get_int("key_yellow", 0)
	
def lview_save_cfg(cfg):
	global key_blue, key_red, key_yellow
	cfg.set_int("key_blue",   key_blue)
	cfg.set_int("key_red",    key_red)
	cfg.set_int("key_yellow", key_yellow)
	
def lview_draw_settings(game, ui):
	global key_blue, key_red, key_yellow
	key_blue   = ui.keyselect("Key blue card", key_blue)
	key_red    = ui.keyselect("Key red card", key_red)
	key_yellow = ui.keyselect("Key yellow card", key_yellow)
	
def lview_update(game, ui):
	global key_blue, key_red, key_yellow, key_w
	global card_to_lock
	
	if card_to_lock is not None:
		if card_to_lock == game.local_champ.W.name:
			game.press_key(key_w)
			card_to_lock = None
	elif game.local_champ.W.get_current_cooldown(game.time) == 0:
		key_to_press = None
		if game.was_key_pressed(key_blue):
			card_to_lock = "BlueCardLock"
			key_to_press = key_blue
			print('b')
		elif game.was_key_pressed(key_red):
			card_to_lock = "RedCardLock"
			key_to_press = key_red
			print('r')
		elif game.was_key_pressed(key_yellow):
			card_to_lock = "GoldCardLock"
			key_to_press = key_yellow
			print('y')
		if key_to_press:
			game.press_key(key_w)