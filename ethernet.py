# solution based on disjoint-set
# the solution has complexity O(N*log(N))
﻿def solution(data: str) -> (int, int):
	pass
	

# solution based on python structure 'set' 
# the solution has complexity O(N^2)
﻿def solution_old(data: str) -> (int, int):
    # read data
    rows = data.split('\n')
    tops_num, edges_num = map(int, rows[0].split())

    # list of lists [one_top, another_top, edge_weight] sorted by edge_weight ('if row' for last empty line in file)
    edges_sorted = sorted([list(map(int, row.split())) for row in rows[1:] if row], key=lambda item: item[2])

    # list of sets, where each set includes tops from one tree
    forest = []

    edges_used_num = 0
    sum_weight = 0

    # add edge with minimal weight to the forest if it doesn't produce cycle
    for edge in edges_sorted:
        top_1 = edge[0]
        top_2 = edge[1]

        cycle_check_result = set()
        for tree, tree_number in zip(forest, range(len(forest))):
            # check whether this edge forms a cycle, if it does we get 'there_is_cycle'
            if top_1 in tree and top_2 in tree:
                cycle_check_result = 'there_is_cycle'
                break

            # if adding the edge doesn't form cycle, we return the indexes of trees to which this edge is attached
            if top_1 in tree or top_2 in tree:
                cycle_check_result.add(tree_number)

        if cycle_check_result == 'there_is_cycle':
            continue
        else:
            # forming updated_tree
            updated_tree = {top_1, top_2}
            for tree_num in cycle_check_result:
                updated_tree |= forest[tree_num]

            # drop trees, which are involved in forming updated_tree, and add updated_tree to forest
            forest = [forest[tree_num] for tree_num in range(len(forest)) if tree_num not in cycle_check_result]
            forest.append(updated_tree)

        edges_used_num += 1
        sum_weight += edge[2]

    # one tree has edges_num = tops_num - 1, so we may count trees in forest this way
    trees_num = tops_num - edges_used_num

    return trees_num, sum_weight


if __name__ == '__main__':
    for num in range(1, 11):
        input_data = open(f'tests/{num}.in', 'r').read()

        for number in solution(input_data):
            print(number, end=' ')
        print()
