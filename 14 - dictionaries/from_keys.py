# initialise a pretend game's variables, in a dictionary, using the fromkeys() function

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

init = 0

# fromkeys(keys, value to initialise to)

initial_game_state = dict.fromkeys(game_properties, init)