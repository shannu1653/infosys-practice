# Infosys Round 2 Coding — FINAL Question List (Basic → Advanced)
**Prepare ONLY these. This is the complete, consolidated list — nothing more needed.**

---

## HOW THE ROUND ACTUALLY RUNS (confirmed pattern)
- 3–4 problems, 90–180 minutes total.
- Problems escalate: Easy → Easy/Medium → Medium (Greedy) → Hard (DP/Graph).
- Partial scoring exists (Easy needs 100% test cases, Medium ~80%, Hard ~75%) — **always submit something for every question, even incomplete.**
- Languages: C, C++, Java, Python, JavaScript — pick ONE and stick to it.

---

## LEVEL 1 — BASIC (Master these first — Day 1–2, must be 100% solid)

1. Reverse a string / array (in-place)
2. Palindrome check (including "sentence palindrome" — ignore spaces/punctuation/case)
3. Check for Anagram
4. Count vowels, consonants, word frequency in a string
5. Pangram check — verify all 26 letters appear, list missing ones
6. Fibonacci series (iterative + recursive + memoized)
7. Factorial, prime check, GCD/LCM
8. FizzBuzz and number-pattern printing (pyramid, diamond, Pascal's triangle)
9. Find max/min/second-largest in an array
10. Array rotation (left/right by k) — both brute force and O(n) reversal-trick method
11. Find missing number / duplicate number in an array (1 to N range)
12. Matrix transpose, spiral print, row/column sum
13. Basic unit conversion / simulation programs (e.g., Fahrenheit ↔ Celsius)
14. Sort an array (implement bubble/selection once, then just know when to use built-in sort)
15. Binary search (iterative + recursive) and its variants (first/last occurrence, floor/ceiling)

---

## LEVEL 2 — EASY-MEDIUM (Day 3, hashing/two-pointer/sliding window — this is now a very common Q2 slot)

1. Two Sum (hashmap approach)
2. Subarray Sum Equals K (prefix sum + hashmap) — **real recent Infosys question**
3. Container With Most Water (two-pointer) — **real recent Infosys question, often paired with #2**
4. Count Subarrays with Odd Sum (prefix-sum parity tracking) — **real recent Infosys question**
5. Longest substring without repeating characters (sliding window)
6. Maximum/minimum sum subarray of size k (sliding window)
7. Frequency array optimization — count frequencies, then greedily process/reorder — **real recent Infosys question ("Maximum Count of Processed Numbers")**
8. Merge two sorted arrays/lists
9. Move zeros to end / segregate 0s and 1s
10. Kadane's Algorithm (max subarray sum) — extremely high-frequency topic

---

## LEVEL 3 — MEDIUM (Day 4, Linked List / Stack-Queue / Greedy — this is your Q2/Q3 slot)

**Linked List**
1. Reverse a linked list (iterative + recursive)
2. Detect and remove a cycle (Floyd's algorithm)
3. Merge two sorted linked lists
4. Find middle of linked list

**Stack/Queue**
5. Valid parentheses / balanced brackets
6. Next greater element
7. Min stack (O(1) getMin)

**Greedy (this is almost always the "medium" question)**
8. Job sequencing with deadlines
9. Activity selection / minimum meeting rooms
10. Merge overlapping intervals
11. Minimum adjacent swaps to group pairs together — **real recent Infosys question**
12. Stable shipment partition (sort + greedy partitioning) — **real recent Infosys question**
13. Maximum XOR subset (choose ≤ N/2 elements to maximize XOR) — **real recurring Infosys SP question**
14. Minimum "work" to redistribute values across positions until balanced (the wine/gift redistribution pattern) — **real recurring Infosys SP question**

**String + Math**
15. Next Palindrome (smallest palindrome strictly greater than N) — **real recent Infosys question**
16. Balanced string / string inversions check — **real recent Infosys question**

---

## LEVEL 4 — HARD (Day 5–6, this is the "cracker" question — DP/Graph, now often blended with newer twists)

**Classic DP (still the foundation — learn these before the newer variants)**
1. 0/1 Knapsack + Unbounded Knapsack
2. Coin Change (min coins / number of ways)
3. Longest Common Subsequence / Longest Common Substring
4. Longest Increasing Subsequence
5. Edit Distance
6. Matrix/grid min-cost path DP
7. Word Break

**Newer DP variants actually seen in 2025–26 Infosys OAs (don't skip these — they're replacing the old-style ones)**
8. DP combined with Bit Manipulation ("Array Sequence Optimization") — **real recent Infosys question**
9. Matrix Chain Multiplication variant combined with binary-string subsequence logic ("BinStr Subsequence") — **real recent Infosys question**
10. K-partition problem: split array into K consecutive groups where each group's value = count of distinct elements, maximize total (DP + sliding window + hashmap) — **real recent Infosys question**

**Graph (increasingly common as the hard slot)**
11. BFS/DFS basics — connected components, number of provinces (Union-Find/DSU)
12. Strongly Connected Components (Kosaraju's/Tarjan's basic idea) — **real recent Infosys question**
13. Dijkstra's algorithm (shortest path, non-negative weights)
14. Graph traversal combined with a divisibility/number condition ("Lucky Path Tree") — **real recent Infosys question**
15. **Tree DP with re-rooting technique** — **real recent Infosys question (Feb 2026 OA)** — this is the single newest/most advanced pattern showing up; learn the standard "compute DP rooted at node 0, then re-root to every other node in O(N) total" trick.

---

## LEVEL 5 — "STORY-WRAPPED" PROBLEM RECOGNITION (important — don't panic at flavor text)

Infosys frequently dresses standard DSA problems in narrative wrapping. Recent real examples:
- "Space X – The Oracle of Eldoria" → turned out to be a simulation/greedy problem
- "Hero Duel Intensity" → greedy/simulation with experience-point thresholds (monster-defeating pattern: sort by required threshold, greedily accumulate)
- "Smart Square" → precomputation + permutations problem

**Strategy:** ignore the story, extract the input/output format and constraints, and map it to one of the patterns in Levels 1–4 above. 90% of "creative" Infosys problems are a reskinned version of something on this list.

---

## YOUR ACTUAL 8-DAY EXECUTION PLAN (final, locked)

| Day | Do this and ONLY this |
|---|---|
| 1 | Level 1, items 1–15. Time-box: 10 min each. |
| 2 | Level 1 review + Level 2, items 1–5. |
| 3 | Level 2, items 6–10 + Level 3 Linked List/Stack items 1–7. |
| 4 | Level 3 Greedy + String items 8–16 — this is your highest-yield day. |
| 5 | Level 4 classic DP, items 1–7. Write the recurrence on paper before coding, every time. |
| 6 | Level 4 new DP variants (8–10) + Graph (11–15), especially tree re-rooting. |
| 7 | Full mock: pick 4 random problems (1 from each Level 2/3/3/4), solve in 2.5 hrs timed, no notes. |
| 8 | Redo only what you got wrong. Skim Level 5 patterns once. Rest early. |

---

## FINAL RULES FOR THE ROUND ITSELF
1. Solve Easy (Level 1/2 style) first, fully — it's guaranteed points.
2. Never leave the Hard question blank — partial credit (~75% threshold) is real money on the table.
3. State time/space complexity out loud/in comments even if not asked.
4. Handle edge cases explicitly: empty input, single element, all-duplicates, negative numbers.
5. If it's an in-person round, expect 1–2 quick OOPs/DBMS/OS questions blended in — know CPU scheduling basics, normalization (3NF/BCNF), and abstract class vs interface.

This is the complete list. Nothing outside this document is needed — go execute it.
