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
last_room = None

while len(visited) < len(world.room_grid):

#DFS until deadend
    s = Stack()
    s.push([player.current_room.id])
    while s.size() > 0:
        path = s.pop()
        v = path[-1]
        last_room = v
        if v not in visited:
            exits = player.current_room.get_exits()
            visited[v] = {}
            if 'n' in exits:
                visited[v]['n'] = '?'
            if 's' in exits:
                visited[v]['s'] = '?'
            if 'w' in exits:
                visited[v]['w'] = '?'
            if 'e' in exits:
                visited[v]['e'] = '?'
            for exit in exits:
                new_room = player.current_room.get_room_in_direction(exit).id
                visited[v][exit]= new_room
                traversal_path.append(exit)
                path_copy = list(path)
                path_copy.append(new_room)
                s.push(path_copy)


#Find another room that's not visited_rooms
    for i in range(len(world.room_grid)):
        if i not in visited:
            player.current_room.id = i
            break

#Move back to previous room

    # print(f"Last room is: {last_room}")
    # player.current_room.id = last_room
    # counter = -1
    #
    # while player.current_room.id in visited:
    #     if traversal_path[counter] == "n":
    #         player.travel("s")
    #     elif traversal_path[counter] == "s":
    #         player.travel("n")
    #     elif traversal_path[counter] == "e":
    #         player.travel("w")
    #     elif traversal_path[counter] == 'w':
    #         player.travel("e")

#BFS from last room visited

    #print(f"BFT starting from: {player.current_room.id}")
    q = Queue()
    q.enqueue([player.current_room.id])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            exits = player.current_room.get_exits()
            visited[v] = {}
            for exit in exits:
                visited[v][exit]= player.current_room.get_room_in_direction(exit).id
                traversal_path.append(exit)
                path_copy = list(path)
                path_copy.append(player.current_room.id)
                q.enqueue(path_copy)
# #


print(f"Visited: {visited}")
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
