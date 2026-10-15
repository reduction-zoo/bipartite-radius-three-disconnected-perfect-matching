# Rule contract

Both graph encodings are exactly {"n": positive integer, "edges": list of pairs}.
Vertices are 0 through n-1; pairs contain actual integers u<v, with no duplicates.
Legal graphs are connected, simple and bipartite, with radius at most four for
the source and at most three for the target. Every legal NO input must still
produce a legal target graph. Invalid source strings map to {}, outside the target.

A witness is a list of distinct ordered graph edges forming a perfect matching M
such that deleting those edges disconnects the graph. Every vertex appears exactly
once. No cut colors are supplied in the witness; the extractor must recover from
any such matching, including ones whose deletion has more than two components.

algorithm.py reads a source JSON object and emits the target graph. With --extract,
it reads {"source": original source, "target_solution": target matching edges}
and emits one source matching. The supplied target witness is promised valid.
Both deterministic polynomial-time maps work in fresh processes, use no solvers,
and have polynomial output bit size. Tests execute the candidate without imports.
