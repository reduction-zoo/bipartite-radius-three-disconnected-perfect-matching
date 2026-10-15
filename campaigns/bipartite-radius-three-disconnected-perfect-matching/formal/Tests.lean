import Challenge
open BipartiteRadiusThreeDisconnectedPerfectMatching
example : disconnectedMatching ⟨4, [(0,1),(1,2),(2,3)]⟩ [(0,1),(2,3)] = true := by native_decide
example : disconnectedMatching ⟨4, [(0,1),(1,2),(2,3)]⟩ [(0,1)] = false := by native_decide
