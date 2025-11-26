# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)


print(search.rya_graph_search(ab).path())
print(search.ryasub_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

print("--------------------------------------------------------------------------")
ab = search.GPSProblem('T', 'M'
                       , search.romania)


print(search.rya_graph_search(ab).path())
print(search.ryasub_graph_search(ab).path())

print("--------------------------------------------------------------------------")

ab = search.GPSProblem('Z', 'D'
                       , search.romania)


print(search.rya_graph_search(ab).path())
print(search.ryasub_graph_search(ab).path())

print("--------------------------------------------------------------------------")

ab = search.GPSProblem('A', 'Z'
                       , search.romania)


print(search.rya_graph_search(ab).path())
print(search.ryasub_graph_search(ab).path())