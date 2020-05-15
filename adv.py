from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#My code starts here

def dft_recursive(current_room, visited=None):

    if visited is None:
        visited = {}

    if current_room.id not in visited:
        visited[current_room.id] = {}
        exits = current_room.get_exits()
        for exit in exits:
            visited[current_room.id][exit] = '?'

    for exit in current_room.get_exits():
        path = [exit]
        go_to_room = current_room.get_room_in_direction(exit)
        if go_to_room.id not in visited:
            new_path = dft_recursive(go_to_room, visited)
            if exit == 'n':
                opp_of_exit = 's'
            elif exit == 's':
                opp_of_exit = 'n'
            elif exit == 'w':
                opp_of_exit = 'e'
            elif exit == 'e':
                opp_of_exit = 'w'
            path = path + new_path + [opp_of_exit]
        else:
            return []
    return path

dft_recursive(player.current_room)

print(f"Traversal_path: {traversal_path}")

#My code ends here

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
