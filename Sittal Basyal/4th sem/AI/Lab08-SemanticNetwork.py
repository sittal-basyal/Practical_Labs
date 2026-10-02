"""
Lab 08 (ii) - Program to illustrate the concept of Semantic Network

A semantic network represents knowledge as a directed graph where
nodes are concepts/objects and edges are labeled relationships
(e.g., "is-a", "has", "can", "part-of") between them.

We build a small semantic network about animals using the
`networkx` graph library, print its relationships, and demonstrate
simple inference by traversing "is-a" edges (property inheritance).
"""
import networkx as nx

G = nx.DiGraph()

relations = [
    ("Sparrow", "is-a", "Bird"),
    ("Bird", "is-a", "Animal"),
    ("Bird", "has", "Wings"),
    ("Animal", "can", "Move"),
    ("Sparrow", "can", "Fly")
]


for a, r, b in relations:
    G.add_edge(a, b, relation=r)

print("Semantic Network:")
for a, b, d in G.edges(data=True):
    print(f"{a} --[{d['relation']}]--> {b}")


def infer(node):
    properties = []

    while node:
        for _, target, d in G.out_edges(node, data=True):
            if d["relation"] in ["has", "can"]:
                properties.append((d["relation"], target))

        parent = next(
            (b for _, b, d in G.out_edges(node, data=True)
             if d["relation"] == "is-a"), None
        )
        node = parent

    return properties


for animal in ["Sparrow", "Penguin", "Salmon"]:
    print(f"\n{animal} properties:")
    for p in infer(animal):
        print("->", p)