from room import Room
from player import Player
from world import World
from queue import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# player = Player("Enter Name", world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
path = []
visited = {}
#reversing directions
def opposite_dirs(direction):
    reverse_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    print('opposite_directions', reverse_directions[direction])
    return reverse_directions[direction]

#move forward to a new room
# updates visited from previous rooms before the forward move takes place
def forward_move(direction):
    path.append(direction)
    traversal_path.append(direction)
    current_room = player.current_room.id
    prev_room = current_room
    player.travel(direction)
    new_room = player.current_room.id
    visited[prev_room][direction] = new_room
    print('visited', visited)

#move backwards
def backward_move():
    # removes last path entry
    last_direction = path.pop()
    # copy traversal??
    next_direction = opposite_dirs(last_direction)
    traversal_path.append(next_direction)

    current_room = player.current_room.id

    prev_room = current_room
    player.travel(next_direction)
    next_room = player.current_room

    if visited[prev_room][next_direction] == '?': visited[prev_room][next_direction] = next_room

# show all unexplored places you have not been
def unexplored_places():
    unexplored = set()
    existing_exits = player.current_room.get_exits()
    for ex in existing_exits:
        if visited[player.current_room.id][ex] == '?':
            unexplored.add(ex)
    #print('unexplored: ', unexplored)
    return unexplored

def add_visited():
    existing_exits = player.current_room.get_exits()
    visited[player.current_room.id] = {}
    for ex in existing_exits:
        visited[player.current_room.id][ex] = '?'

def traverse_graph():
    while len(visited) != len(room_graph):

        if player.current_room.id not in visited:

            add_visited()
            # make next move decision
            unexplored = unexplored_places()
            # double check for anything not explored yet
            direction_of_choice = unexplored.pop()
            # move forward
            forward_move(direction_of_choice)

        # if room is in visited, this gets run
        else:
            unexplored = unexplored_places()

            if len(unexplored) > 0:
                unexplored = unexplored_places()
                print('unexplored rooms in traverse graph second if state,', unexplored)

                direction_of_choice = unexplored.pop()
                forward_move(direction_of_choice)
            # elif current_room doesn't have exits not yet explored
            elif len(path) > 0 and len(unexplored) is 0:
                backward_move()

traverse_graph()


# TRAVERSAL TEST - to have all visited_rooms be full with rooms
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
