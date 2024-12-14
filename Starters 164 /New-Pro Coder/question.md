# New-Pro Coder

**Hola a todos, espero que todo vaya bien!!**

Ved claims to be a pro at programming, but his friend Varun disagrees. To settle the debate, they decided to seek advice from their mentor. The mentor proposed a simple challenge:

Ved must write a program containing `N` lines of code. When the code is compiled, the compiler will indicate how many of those lines have errors, denoted as `M`. Based on the results:

- If errors are present in **at least half** of the total lines, Ved will be labeled as a `NEWBIE`.
- Otherwise, he will be called a `PRO`.

After compiling Ved's code, the compiler reported errors in `M` lines. Determine Ved's skill category based on this evaluation.

---

## Input Format
The input contains two space-separated integers:
- `N` — the number of lines of code written by Ved.
- `M` — the number of lines of code containing errors.

---

## Output Format
Output:
- `PRO` if Ved is a pro, else output `NEWBIE`.

**Note:** It is allowed to print each character in either case. For example, `pro`, `PRo`, and `pRo` will all be accepted.

---

## Constraints
- \(1 \leq N \leq 1000\)
- \(1 \leq M \leq 1000\)
- \(M \leq N\)

---

## Sample Input and Output

### Input 1

10 6

### Output 1

NEWBIE

**Explanation:**  
There were `10` lines and Ved has errors in `6` of them. Since \(6 \geq 5\), where \(5\) is half of \(10\), Ved is a newbie due to having errors in at least half the lines.

---
