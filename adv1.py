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
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
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

visited = {}#dictionary to keep track of rooms visited+ direction explored
rooms_completed = 0


while rooms_completed < len(world.room_grid):
    moved = False
    exits = player.current_room.get_exits()
    room_id = player.current_room.id
    #initialize
    if room_id not in visited:
        visited[room_id] = {}
        for exit in exits:
            visited[room_id][exit] = '?'

    for k, v in visited[room_id].items():
        if v == '?':
            visited[room_id][k] = player.current_room.get_room_in_direction(k).id
            traversal_path.append(k)
            player.travel(k)
            moved = True
            break
    if moved == False:
        last_move = traversal_path[-1]
        if last_move == 'n':
            back_move = 's'
        elif last_move == 's':
            back_move = 'n'
        elif last_move == 'e':
            back_move = 'w'
        elif last_move == 'w':
            back_move = 'e'
        player.travel(back_move)
        del traversal_path[-1]
        rooms_completed += 1


print(f"visited: {visited}")
print(f"traversal_path: {traversal_path}")

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
