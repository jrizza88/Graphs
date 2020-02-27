import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            # passing in user into add_user
            self.add_user(user)

        # Create friendships

        ## Create a list with all possible friendships
        possible_friendships = []
        
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                possible_friendship = (user, friend)
                possible_friendships.append(possible_friendship)
           # (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3,4)
        ## then shuffle it randomly
        random.shuffle(possible_friendships)
        ## and only take as many as we need,
        total_friendships = num_users * avg_friendships // 2 # because each friendship is bidirectional, so we only call the function half of the time
        random_friendships = possible_friendships[:total_friendships]
        ## and add those friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # get all the friends of the user
        queue = Queue()
        visited[user_id] = [user_id]
        queue.enqueue(user_id)

        # while the queue is not empty:
        while queue.size() > 0:
            #dequeue the first instance
            current_friend = queue.dequeue()
            # If that vertex has not been visited...
            if current_friend not in visited:
                print('print current friend', current_friend)
               # self.friendships[user_id].add(friend_id)
                friends = self.friendships[current_friend]
                visited[current_friend].add(current_friend)
                
                for friend in friends:
                    add_friend = current_friend[:]
                    add_friend.append(friend)
                    queue.enqueue(add_friend)
                    print('friend', friend)
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
