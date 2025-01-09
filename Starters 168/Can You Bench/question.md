# Make Odd

You are given two binary strings `A` and `B` of the same length `N`. Your task is to determine whether it is possible to achieve an **odd score** by selecting `N` elements such that:

- For each index `i` (1 ≤ i ≤ N), you will select either `A[i]` or `B[i]`.
- If the character you select is equal to `1`, add `1` to the score. If the character is `0`, add nothing.

Your goal is to determine whether it is possible to make the score an **odd number**. If it is possible, print **YES**, otherwise print **NO**.

---

## Input Format

1. The first line contains an integer `T`, the number of test cases.
2. For each test case:
   - The first line contains an integer `N`, the length of the strings `A` and `B`.
   - The second line contains `N` characters representing the binary string `A`.
   - The third line contains `N` characters representing the binary string `B`.

---

## Output Format

For each test case, output on a new line:
- "YES" if it is possible to make the score an odd number.
- "NO" otherwise.

You may print each character of the output in any case (e.g., "YES", "yes", or "Yes" will all be treated as identical).

---

## Constraints

- \( 1 \leq T \leq 3 \times 10^5 \)
- \( 1 \leq N \leq 20 \)
- The sum of \( N \) over all test cases does not exceed \( 3 \times 10^5 \).
- \( A[i], B[i] \in \{0, 1\} \) for all \( i \).

---

## Example

### Input