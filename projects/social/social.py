import random
import time

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

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

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships

        ## create a list with all possible friendships
        possible_friendships = []
        for user in range(1, self.last_id + 1): # + 1 so we include self.last_id
            for friend in range(user + 1, self.last_id + 1):
                possible_friendship = (user, friend)
                possible_friendships.append(possible_friendship)

        ## then shuffle it randomly
        random.shuffle(possible_friendships)

        ## and only take as many as we need,
        total_friendships = num_users * avg_friendships
        number_of_friend_pairs_needed = total_friendships // 2
        random_friendships = possible_friendships[:number_of_friend_pairs_needed]

        ## and add those friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])


    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for user in range(num_users):
            self.add_user(user)

        target_friendships = num_users * avg_friendships
        friendships_successfully_added = 0
        failures = 0

        # continue this until we have as many friendships as we need:
        while friendships_successfully_added < target_friendships:
        ## choose two random numbers (integers) between 1 and self.last_id
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            ## try to make that friendship!
            added_friendship = self.add_friendship(user_id, friend_id)

            ## if it works, increment the friendship counter
            if added_friendship:
                friendships_successfully_added += 2
            else:
                failures += 1

    def get_friendships(self, user_id):
        return self.friendships[user_id]

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        queue = Queue()

        path = [user_id]
        queue.enqueue(path)

        while queue.size() > 0:

            current_path = queue.dequeue()
            new_user_id = current_path[-1]

            if new_user_id not in visited:
                visited[new_user_id] = current_path

                friends = self.get_friendships(new_user_id)
                for friend in friends:
                    path_copy = list(current_path)
                    path_copy.append(friend)
                    queue.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()

    num_users = 2000
    avg_friendships = 1000

    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Quadratic time: {total_time} seconds")

    start_time = time.time()
    sg.populate_graph_linear(num_users, avg_friendships)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Linear time: {total_time} seconds")

    # connections = sg.get_all_social_paths(1)
    # total_paths_length = 0
    # for user_id in connections:
    #     total_paths_length += len(connections[user_id])
    # average_degree_of_separation = total_paths_length / len(connections)

    # print(average_degree_of_separation)