mobs.onMobKilled(CHICKEN, function () {
	
})
player.onItemInteracted(DIAMOND_SWORD, function () {
	
})
loops.forever(function () {
	
})
player.onChat("jump and run skip an", function (num1) {
    loops.pause(100)
    gameplay.setWeather(THUNDER)
    agent.teleportToPlayer()
    blocks.place(PLANKS_OAK, pos(6, 3, 0))
    agent.move(FORWARD, 57)
})
