from room import Room
from player import Player
from world import World
from graph import Graph
from util import Stack
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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
def build_path(graph):
    """
    Traverse maze in a DFT.
    """

    # stack that contains our current path
    s = Stack()
    # array that contains our returned path
    moves = []
    # helps us determine if we hit a dead end
    visited = set()
    # initialize traversal with the 0 index room
    s.push(0)

    while len(visited) < len(graph):
        # get the id of the current room in the stack
        id = s.tail()
        # mark as visited
        visited.add(id)
        # get information on the current room (tuple data)
        current_room = graph[id]
        # dict of possible moves
        rooms_dict = current_room[1]
        # array to track if a room has not been visited yet
        undiscovered = []
        # store undiscovered rooms in relationship to the current room
        for direction, room_id in rooms_dict.items():
            if room_id not in visited:
                undiscovered.append(room_id)
        # assign the next room
        # if we reached a dead end, back track
        if len(undiscovered) > 0:
            next_room = undiscovered[0]
            s.push(next_room)
        else:
            s.pop()
            next_room = s.tail()

        # survey the rooms around our current room. if the next move matches the room_id, add that to moves and walk
        for direction, adjacent_id in rooms_dict.items():
            if adjacent_id == next_room:
                moves.append(direction)

    return moves


traversal_path = build_path(room_graph)

# TRAVERSAL TEST
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
# breakpoint()
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
