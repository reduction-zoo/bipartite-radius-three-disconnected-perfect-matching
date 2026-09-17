# Testing foundation

The independent Z3 oracle uses one edge-selection bit per edge and one cut bit
per vertex. Exactly one selected edge touches each vertex; every edge joining
opposite cut bits must be selected. Both colors occur, with vertex zero normalized
to zero. This is equivalent to a perfect matching whose deletion disconnects the
graph: a union of deletion components supplies the cut in the reverse direction.
Models are blocked by matching edge bits, not cut choices. Only UNSAT is NO;
unknown or execution failure raises an error. Returned matchings are recounted
and their deletion connectivity is tested directly with NetworkX.

Before any candidate construction, --self-test passed on every connected
bipartite atlas graph through six vertices: 28 source and 28 target graphs,
16 exhaustive valid matching witnesses, 9 stored cases, 3 incorrect programs
rejected (invalid graph, wrong decision, invalid recovery). Exhaustive enumeration
uses edge subsets of cardinality floor(n/2), independent of the solver encoding.
Z3 version 5.1.0. [Raw result](../history/campaigns/bipartite-radius-three-disconnected-perfect-matching/work/evidence/preparation/self-test.json).

Run from repository root:
python3 campaigns/bipartite-radius-three-disconnected-perfect-matching/work/check.py --self-test

Prepared cases distinguish DPM from Matching Cut (P3 and the eight-vertex leaf
example) and PMC (C6). The suite has four YES and five NO inputs. Two distinct
solver matchings per YES target, each also passed with reversed edge-list order,
exercise recovery; reversal is serialization symmetry, not a distinct matching.
The target graph-domain check searches for a radius-three center and asserts
simplicity, connectedness and bipartiteness. No timeout or random generation.
Finite exhaustive coverage does not verify the solver for all sizes.
