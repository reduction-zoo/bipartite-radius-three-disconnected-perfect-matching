# Bipartite radius-three Disconnected Perfect Matching

Status: ready_for_expert_review. Allocation: 40 rounds; 1 started/completed,
39 unused. Screening probes preceded the campaign and are separately recorded.

[Algorithm](work/algorithm.py) and [proof](work/proof.md): a deterministic Karp
reduction from bipartite radius-four DPM to radius three, with recovery from every
valid target perfect matching. Both maps have polynomial bit-time bounds; output
order and edge count are O(n^3). The theorem would close the cited radius boundary.

| Round | Result |
|---|---|
| [001](rounds/001/round.md) | One balanced-reservoir mechanism; full rule, checks, review and paper completed |

Prepared checks: 9 cases/16 recovery calls. Additional checks: 15 cases/14 calls.
Independent reviewer: 3 new full cases/3 distinct recoveries, plus exhaustive local
checks and invalid inputs. These are overlapping suite executions, not distinct
source totals. [Verification](work/verification.md) links commands and raw evidence.
Zero algorithm/checker repairs or inconclusive runs; no timeout.

[Independent review](reviews/complete-rule/review.md): advance, no repair.
[Paper](work/manuscript.pdf): 8 pages, 3 exact vector figures; [Typst source](work/manuscript.typ)
and [inspection](work/evidence/paper-inspection.txt). No mathematical or executable
changes followed review. Human expert validation remains outstanding.

Novelty is supported within the dated primary coverage, with failed publisher
access and overlooked-work limits explicit. Importance is moderate: a related
extension of the preceding Matching Cut result, best assessed together. No known
agent-side proof gap remains; stop early. Human review outcome is unknown.

Post-campaign experience closeout: **1 new entry, 1 existing entry updated,
0 pending**; shared collection total **9 entries**, excluding README.
[New residual-matching finding](../../research/experience/balanced-reservoir-perfect-matching-extension.md);
[updated interface use history](../../research/experience/dual-reservoir-matching-cut-interfaces.md).
