# Swap and Flip

Given a binary string `S` of length `N`, check if you can transform it to another binary string `T` (also of length `N`) by using either of the following operations as many times as needed:

1. **Swap**: Pick `(i, j)` such that \(1 \leq i < j \leq N\) and swap `Si` and `Sj`.
2. **Flip**: Pick `(i, j)` such that \(1 \leq i < j \leq N\) and flip both `Si` and `Sj`.  
   (To flip \(x\), it means converting it to \(1 - x\).)

---

## Input Format
- The first line of input will contain a single integer `T`, denoting the number of test cases.
- Each test case consists of multiple lines of input:
  - The first line contains `N` — the length of the strings `S` and `T`.
  - The second line contains `S` — a binary string of size `N`.
  - The third line contains `T` — a binary string of size `N`.

---

## Output Format
For each test case, output `YES` if it is possible to convert `S` to `T` using the operations several times. Otherwise, output `NO`.

It is allowed to output each character in either case. For example, `YES`, `yes`, and `YeS` will all be accepted.

---

## Constraints
- \(1 \leq T \leq 100\)
- \(1 \leq N \leq 100\)
- \(|S| = |T| = N\)
- \(Si \in \{0, 1\}\)
- \(Ti \in \{0, 1\}\)

---

## Sample Input and Output

### Input

4
2
00
11
2
00
01
1
0
0
4
0010
1101

### Output

YES
NO
YES
YES

---

## Explanation

### Test Case 1:
Choose \(i = 1, j = 2\) and flip them. Then, `S` becomes `11`, equal to `T`.  
Output: `YES`.

---

### Test Case 2:
It is not possible to make `S` equal to `T` using the given operations.  
Output: `NO`.

---

### Test Case 4:
We perform the following sequence of operations:  
1. Choose \(i = 3, j = 4\) and swap them. Then, `S` becomes `0001`.  
2. Choose \(i = 1, j = 2\) and flip them. Then, `S` becomes `1101`.  
Thus, `S` is made equal to `T`.  
Output: `YES`.