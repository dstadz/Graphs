
#def, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual.

def earliest_ancestor(ancestors, starting_node):
    family = Graph()
    for pc in ancestors:
        family.add(pc)
    # for f in family.members:
    #     print(f, family.members[f])
    # if not len(family.members[starting_node]):
    #     return -1

    answer = [None, None]

    stack = []
    visited = set()
    stack.append(starting_node)
    while len(stack):
        child = stack.pop()
        if child != starting_node:
            while True:
                stack_2 = []
                visited_2 = set()
                stack_2.append([child])
                while len(stack_2):
                    current_path = stack_2.pop()
                    current_node = current_path[-1]
                    if current_node == starting_node:
                        if answer[0] is None:
                            answer[0] = child
                            answer[1] = len(current_path)
                        elif answer[1] < len(current_path):
                            answer[0] = child
                            answer[1] = len(current_path)
                        elif answer[1] == len(current_path) and answer[0] > child:
                            answer[0] = child
                            answer[1] = len(current_path)
                    if current_node not in visited_2:
                        visited_2.add(current_node)
                        if current_node in family.members:
                            edges = family.members[current_node]
                            for edge in edges:
                                stack_2.append(current_path + [edge])
                break
        for item in family.members:
            if child in family.members[item] and item not in visited:
                visited.add(item)
                stack.append(item)

    if answer[0] is not None:
        return answer[0]
    else:
        return -1

        return -1 
    # family = Graph()
    # for pc in ancestors:
    #     family.add(pc)
    # # for f in family.members:
    # #     print(f, family.members[f])
    # if not len(family.members[starting_node]):
    #     return -1

    # depth = 0
    # oldest = []
    # stack = []
    # stack.append(starting_node)
    # while len(stack):
    #     print(depth, stack)#, end='')
    #     cur = stack.pop()

    #     # {x,y} => x,y => into stack
    #     if type(cur) is not int:
    #         for c in cur:
    #             stack.append(c)
    #             depth += 1

    #     #x into stack
    #     if type(cur) is int:
    #         if family.get_parents(cur) is -1:
    #             depth -= 1
    #             oldest.append({cur:depth})
    #             continue
    #         stack.append(family.get_parents(cur))
    #         depth += 1





# If more than one ancestor tied for "earliest", return lowest numeric ID.
    #return min(oldest)

class Graph:
    def __init__(self):
        self.members = {}

    def add(self, parchi):

        if parchi[0] in self.members:
            self.members[parchi[0]].add(parchi[1])
        else:
            self.members[parchi[0]] = set()
            self.members[parchi[0]].add(parchi[1])

        # if child not in self.members:
        #     self.members[child] = set()

        # if child in self.members:
        #     self.members[child].add(parent)

    def get_parents(self, child):
        if len(self.members[child]):
            return self.members[child]
        else:
            return -1

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
start = 6
print(earliest_ancestor(test_ancestors,start))