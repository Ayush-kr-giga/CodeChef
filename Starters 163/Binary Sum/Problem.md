Link to the problem :
https://www.codechef.com/problems/BINARYSUM


You're given two integers N and K. Your task is to determine if there exists a binary string S of length N such that:

S+S+S3+...+SNK, i.e, the sum of all the digits of the string equals K; and • SiS+1 for every 1 < i < N, meaning that no two adjacent digits are equal.

Input Format

* The first line of input will contain a single integer T', denoting the number of test cases.

* The first and only line of each test case contains two space-separated integers N and K.

Output Format

For each test case, output on a new line a single string denoting the answer: "YES" if a valid binary string exists, and "NO" otherwise (without quotes).

Each character of the output may be printed in either uppercase or lowercase, l.e., the strings NO, No, no, and no will all be treated as equivalent.

Constraints

* 1≤T≤100

* 1 ≤ N ≤ 100

* 0 ≤ K≤100



SAMPLE INPUT :

5
5 2
7 5
9 5
12 7
82 41

SAMPLE OUTPUT :

YES
NO
YES
NO
YES
