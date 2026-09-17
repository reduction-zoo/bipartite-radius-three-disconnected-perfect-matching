---
status: ready-for-attempt
openness: supported-within-search-coverage
difficulty: low
importance: moderate
tags: [graph-cuts, NP-hardness, bipartite, radius]
last-literature-check: 2026-09-15
---

# Bipartite radius-four Disconnected Perfect Matching → radius three

[Board](../../research/open-problems/README.md) · [Karp contract](../../research/open-problems/README.md#shared-karp-contract)

| Assessment | Evidence |
|---|---|
| Difficulty | Low, provisional: a localized reservoir repair has a checked extension route |
| Importance | Moderate: settle the corresponding bipartite radius threshold |
| Proof readiness | All six gates pass after the reservoir exercise |

**Exact language.** A graph is YES if it has a perfect matching M for which
G−M is disconnected. Equivalently, M contains all edges of some nontrivial cut.
The cut need not itself cover every vertex. Both endpoints impose their stated
bipartite radius bounds.

**Evidence.** R3, Table 1, Corollary 17 and Section 5, Open Problem 1: radius two
is polynomial, four is hard, and three remains open.

**Executed proof exercise.** For any fixed matching cut C, it extends to a perfect
matching exactly when the vertices not incident to C have perfect matchings
within their respective sides. This follows by deleting C from such a matching,
and conversely adjoining the two internal matchings to C. The probe uses this
criterion and verifies that C6 is YES here but NO for Perfect Matching Cut.
The radius-three tree P7 plus an extra leaf at vertex 1 is YES for Matching Cut
but NO here. Thus neither identity substitution among the three variants works.

**Route.** A radius connector must preserve the residual perfect-matching
condition as well as the cut relation. At the earlier screening, no such connector was validated; reuse the semantic counterexamples when testing it.

## Primary sources

- **R3.** Lucke,
  [Matching Cut and Variants on Bipartite Graphs of Bounded Radius and Diameter](https://arxiv.org/html/2501.08735),
  arXiv:2501.08735v1, 15 January 2025, Table 1, Theorems 18–19,
  Corollary 17, Section 5, Open Problems 1–2.

## Research history

- [Recorded probe](../../research/evidence/cut-and-augmentation-probes.py). Finite checks do not prove a reduction.

- 2026-09-14: Web and arXiv update queries: `"Disconnected Perfect Matching" "radius 3" bipartite`; `"Perfect Matching Cut" "diameter" "open" 2026`; `"Matching Cut" "radius 3" 2026 bipartite`.
  No exact resolution was located within this search; unpublished, unindexed,
  and overlooked results remain outside the supported openness claim.

## Current screening and handoff — 2026-09-15

The [previous interface finding](../../research/experience/dual-reservoir-matching-cut-interfaces.md)
supplies the binary/selector mechanism, not a perfect-matching extension theorem.
A [bounded exercise](../../research/evidence/bipartite-radius-three-disconnected-perfect-matching/reservoir.py)
compared the joined K3,3 pair with a pair of K4,3 reservoirs. Removing the joined
center endpoints leaves ten vertices and maximum matching size four in the first,
but twelve vertices with a perfect matching in the second. Both have eccentricity
three at the first center. [Results](../../research/evidence/bipartite-radius-three-disconnected-perfect-matching/results.json).
The change adds one vertex to the distinguished side of each biclique. Existing
interface forcing survives because the old K3,3 remains embedded and each added
vertex has three monochromatic neighbors. Full source encoding and universal
recovery from an arbitrary target perfect matching remain to be established.

All six gates pass provisionally. Endpoints are connected simple bipartite graphs
at the fixed radii, with perfect-matching edge lists as witnesses. Encode source
matching-edge variables and nonconstant cut colors; enforce exactly one selected
edge per vertex and require every crossing edge selected. Reuse the Boolean
interfaces with the enlarged reservoirs. Recover a target cut from a component
of the graph after removing the supplied matching, then decode source matching
variables. Both maps must be deterministic, polynomial and total as specified.

Difficulty is low provisionally: the new obligation is localized, supported by
the reservoir exercise. Importance is moderate: another named radius boundary.
This closely overlaps the preceding Matching Cut result and should be treated
as a related extension, not claimed as an independent paper or unrelated idea.

Primary recheck: https://arxiv.org/html/2501.08735, Table 1, Corollary 17,
Section 5 Open Problem 1. Queries: `"Disconnected Perfect Matching" "radius three"`
and `"Disconnected Perfect Matching" "radius 3" bipartite 2026`. No later exact
resolution was located within coverage. The published maximum-size variant is
not this decision question. Unindexed, unpublished and overlooked work remains
possible; secondary open-problem aggregators were not used as proof of openness.
The user authorized forty exploration rounds; stop early on complete results.
