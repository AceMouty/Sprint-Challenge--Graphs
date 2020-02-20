
'''
* Fill out a list with traversal that will visit all rooms atleast once

* Commands:
    - player.current_room.id: This will give us the current room id

    - player.current_room.get_exits(): Will return a list of possible moves we can make

    - player.travel(directon, [boolean: wil display room info to us]): This will allow us to move / traverse rooms

* Create an array with a valid move set: We can achieve this with the player.current_room.get_exits()

* Graph Class
    - Will need a verticies attr that is a dict (complete)
        - the keys will be a room id
        - the values will be a dict, this will hold n,s,e,w whose values will be the room id for the possible move
    - The vertex will be the current room ID
    - The edges will be the rooms that the room ID connects to
    - some function: We will need the player instance passed to us so that we have a way to move around the player
    - We need a BFT fn for us to move around and traverse the map
'''


class Graph:

    # init a graph
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        '''
        Add a vertex to the graph
        '''
        # the vertex passed to us is going to be a room id number
        if vertex not in self.verticies:
            self.verticies[vertex] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}

    def add_edge(self, vertex, key, value):
        '''
        Add an edge to the vertex

        The vertex passed should be a room id
        The key passed should be a string of n,s,e,w
        The value is going to be a room id as well

        This will allow us to index a room and apply a room id to a direction of the current room
        '''
        self.verticies[vertex][key] = value
