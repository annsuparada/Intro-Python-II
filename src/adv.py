from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# [X] Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * [X] Prints the current room name
# * [X] Prints the current description (the textwrap module might be useful here).
# * [X] Waits for user input and decides what to do.
#
# [x] If the user enters a cardinal direction, attempt to move to the room there.
# [x] Print an error message if the movement isn't allowed.
#
# [x] If the user enters "q", quit the game.

player1 = Player("Ann", room['outside'])


def game():
    print(f"You are at\n {player1.current_room}\n")

    for x in room.values():
        direction = input('Enter your direction n, s, e, w: --> ')

        if direction == "n":
            if x.n_to != None:
                player1.current_room = x.n_to
                print(player1.current_room)
            else:
                print('\n There is no room that way. Try again!\n')
        elif direction == "s":
            if x.s_to != None:
                player1.current_room = x.s_to
                print(player1.current_room)
            else:
                print('\n There is no room that way. Try again!\n')
        elif direction == "w":
            if x.w_to != None:
                player1.current_room = x.w_to
                print(player1.current_room)
            else:
                print('\n There is no room that way. Try again!\n')
        elif direction == "e":
            if x.e_to != None:
                player1.current_room = x.e_to
                print(player1.current_room)
            else:
                print('\n There is no room that way. Try again!\n')
        elif direction == "q":
            print("Bye :)")
            break
        else:
            print(f"\nPlease enter the corect command or 'q' to Quite")


game()
