graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# def dfs_stack(adjacent_graph, start_node):
#
#     while stack:
#         current_node = stack.pop()
#         visited.append(current_node)
#         for adjacent_node in adjacent_graph:
#     return
for kk in graph:
    print(kk, graph[kk])

#
# print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# # [1, 9, 10, 5,