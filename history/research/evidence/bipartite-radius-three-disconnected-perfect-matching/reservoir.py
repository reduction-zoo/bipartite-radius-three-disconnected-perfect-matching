import itertools
import json
import networkx as nx

records=[]
for balanced in (False,True):
    g=nx.Graph();g.add_edges_from(itertools.product(range(3),range(3,6)));g.add_edges_from(itertools.product(range(6,9),range(9,12)));g.add_edge(0,6)
    if balanced:g.add_edges_from([(12,i) for i in (3,4,5)]+[(13,i) for i in (9,10,11)])
    residual=g.copy();residual.remove_nodes_from([0,6])
    matching=nx.algorithms.matching.max_weight_matching(residual,maxcardinality=True)
    extends=len(matching)*2==len(residual)
    assert extends==balanced
    assert nx.is_bipartite(g) and nx.eccentricity(g,0)<=3
    if extends:
        full=matching|{(0,6)};h=g.copy();h.remove_edges_from(full)
        assert nx.is_perfect_matching(g,full) and not nx.is_connected(h)
    records.append({'reservoir':'K4,3' if balanced else 'K3,3','vertices':len(g),'residual_order':len(residual),'residual_matching_size':len(matching),'extends_center_cut':extends,'eccentricity_zero':nx.eccentricity(g,0)})
print(json.dumps(records,indent=2))
