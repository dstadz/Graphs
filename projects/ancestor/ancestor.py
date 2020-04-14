
#def, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual.
def earliest_ancestor(ancestors, starting_node):
    family = Graph()
    for pc in ancestors:
        family.add(pc)
    # for f in family.members:
    #     print(f, family.members[f])
    if not len(family.members[starting_node]):
        return -1

    depth = 0
    oldest = []
    grands = []
    grands.append(starting_node)
    while len(grands):
        print(depth, grands)#, end='')
        cur = grands.pop()
        if type(cur) is not int:
            depth += 1
            for c in cur:
                grands.append(c)
        if type(cur) is int:
            depth += 1
            if family.get_parents(cur) is -1:
                oldest.append((depth,cur))
                continue
            grands.append(family.get_parents(cur))
        print(f'oldest is {oldest}')
    '''
    while stack:
        x = pop
        add parents of x to stack
        if x has no parents, add x to list, eldest
    '''



# If more than one ancestor tied for "earliest", return lowest numeric ID.
    # return min(oldest)

class Graph:
    def __init__(self):
        self.members = {}

    def add(self, parchi):
        parent = parchi[0]
        child = parchi[1]

        if parent not in self.members:
            self.members[parent] = set()

        if child not in self.members:
            self.members[child] = set()

        if child in self.members:
            self.members[child].add(parent)

    def get_parents(self, child):
        if len(self.members[child]):
            return self.members[child]
        else:
            return -1

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors,6)