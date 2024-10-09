def on_mob_killed_chicken():
    pass
mobs.on_mob_killed(CHICKEN, on_mob_killed_chicken)

def on_item_interacted_diamond_sword():
    pass
player.on_item_interacted(DIAMOND_SWORD, on_item_interacted_diamond_sword)

def on_forever():
    pass
loops.forever(on_forever)

def on_on_chat(num1):
    loops.pause(100)
    gameplay.set_weather(THUNDER)
    agent.teleport_to_player()
    blocks.place(PLANKS_OAK, pos(6, 3, 0))
    agent.move(FORWARD, 57)
player.on_chat("jump and run skip an", on_on_chat)
