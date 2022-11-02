class DisjointSet:
    def __init__(self, elems):
        self.parent = {elem: elem for elem in elems}
        self.height_by_key = {elem: 1 for elem in elems}

    def find_key(self, elem):
        return elem if self.parent[elem] == elem else self.find_key(self.parent[elem])

    def union_by_height(self, key1, key2):
        if self.height_by_key[key2] < self.height_by_key[key1]:
            key1, key2 = key2, key1

        self.parent[key1] = key2
        self.height_by_key[key2] = max(self.height_by_key[key2], self.height_by_key[key1] + 1)


def solution(data: str) -> (int, int):
    # read data
    rows = data.split('\n')
    tops_num, edges_num = map(int, rows[0].split())

    # tree initializing
    forest = DisjointSet(list(range(tops_num)))

    # list of lists [fr, to, weight] sorted by edge_weight ('if row' for last empty line in file)
    edges_sorted = sorted([list(map(int, row.split())) for row in rows[1:] if row], key=lambda item: item[2])

    edges_used_num = 0
    sum_weight = 0

    # add edge with minimal weight to the forest if it doesn't produce cycle
    for edge in edges_sorted:
        fr, to, weight = edge
        key1 = forest.find_key(elem=fr)
        key2 = forest.find_key(elem=to)

        if key1 != key2:
            forest.union_by_height(key1, key2)
            edges_used_num += 1
            sum_weight += weight

    # one tree has edges_num = tops_num - 1, so we may count trees in forest this way
    trees_num = tops_num - edges_used_num

    return trees_num, sum_weight


if __name__ == '__main__':
    for num in range(1, 11):
        input_data = open(f'tests/{num}.in', 'r').read()

        for number in solution(input_data):
            print(number, end=' ')
        print()
