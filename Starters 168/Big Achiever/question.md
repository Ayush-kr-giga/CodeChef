# Big Achiever

## Problem Description

Given \( N \) students standing in a row, each student \( i \) has a distinct achievement score \( A[i] \) provided in an array \( A = [A_1, A_2, \dots, A_N] \). The array \( A \) consists of distinct integers from \( 1 \) to \( N \).

A student \( i \) (\( 1 \leq i \leq N \)) will be **happy** if their achievement score \( A[i] \) is greater than the achievement scores of all the students standing **before** them in the array.

The task is to determine whether each student is happy or not.

---

## Input Format

- The first line contains a single integer \( T \), denoting the number of test cases.
- Each test case consists of two lines:
  - The first line contains \( N \), the number of students.
  - The second line contains \( N \) space-separated integers \( A_1, A_2, \dots, A_N \), denoting the achievement scores of the students.

---

## Output Format

For each test case, print a single line containing \( N \) integers. The \( i^{th} \) integer should be:
- `1` if the \( i^{th} \) student is happy,
- `0` otherwise.

Each test case's output should be on a new line, with the integers separated by spaces.

---

## Constraints

- \( 1 \leq T \leq 4 \times 10^5 \)
- \( 1 \leq N \leq 10 \)
- \( 1 \leq A[i] \leq N \)
- The sum of \( N \) over all test cases does not exceed \( 4 \times 10^5 \).

---

## Example

### Input