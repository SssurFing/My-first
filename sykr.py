import sys

# Increase recursion depth just in case, though not used
sys.setrecursionlimit(2000)


def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        T_str = next(iterator)
    except StopIteration:
        return

    T = int(T_str)
    out_lines = []

    for _ in range(T):
        try:
            n = int(next(iterator))
            x = int(next(iterator))
            y = int(next(iterator))
            A = int(next(iterator))
            B = int(next(iterator))
            C = int(next(iterator))
            D = int(next(iterator))
        except StopIteration:
            break

        # Special cases for A=1 or C=1
        if A == 1 or C == 1:
            if C == 1:
                cycles = n // A
                x += cycles
                y += cycles * A
                n %= A

                if n > 0:
                    current_y_mod = y % A
                    # distance to first B
                    dist = (B - current_y_mod + A) % A
                    if dist < n:
                        cnt = 1 + (n - 1 - dist) // A
                        x += cnt
                    y += n
            elif A == 1:

                cycles = n // C
                x += cycles * C
                y += cycles
                n %= C


                if n > 0:
                    target = D
                    start_val = x + 1
                    current_mod = start_val % C
                    dist = (target - current_mod + C) % C
                    if dist < n:  # dist is 0-indexed offset. max index n-1.
                        # actually if dist <= n-1
                        if dist <= n - 1:
                            cnt = 1 + (n - 1 - dist) // C
                            y += cnt
                    x += n

            out_lines.append(f"{x} {y}")
            continue

        # General Case A > 1, C > 1

        y_mod_A = y % A
        x_mod_C = x % C


        if y_mod_A != B and x_mod_C != D:
            out_lines.append(f"{x} {y}")
            continue



        dist = 0
        state_type = 0  # 0: S0, 1: X-mid, 2: Y-mid

        if y_mod_A == B and x_mod_C == D:
            state_type = 0
            dist = 0
        elif y_mod_A == B:

            k_x = (D - x_mod_C + C) % C

            dist = k_x + (A - 1)
            state_type = 1
        else:

            k_y = (B - y_mod_A + A) % A
            # Since y_mod_A != B, k_y in [1, A-1].
            dist = k_y
            state_type = 2

        if n <= dist:
            if state_type == 1:
                k_x = (D - x_mod_C + C) % C
                if n < k_x:
                    x += n
                elif n == k_x:
                    x += k_x
                    y += 1
                else:  # k_x < n <= dist
                    x += k_x
                    y += 1
                    rem = n - k_x
                    y += rem
            elif state_type == 2:
                y += n

        else:
            # Jump to S0
            if state_type == 1:
                k_x = (D - x_mod_C + C) % C
                x += k_x
                y += 1  # from the (1,1) step
                y += (A - 1)  # from Y-phase
                n -= dist
            elif state_type == 2:
                k_y = (B - y_mod_A + A) % A
                y += k_y
                n -= dist


            cycle_len = A + C - 2
            cycles = n // cycle_len
            x += cycles * (C - 1)
            y += cycles * A
            n %= cycle_len


            if n > 0:

                x += 1
                n -= 1


                k_x_new = C - 1

                if n < k_x_new:
                    x += n
                elif n == k_x_new:
                    x += k_x_new
                    y += 1
                else:
                    x += k_x_new
                    y += 1
                    rem = n - k_x_new
                    y += rem

        out_lines.append(f"{x} {y}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
    solve()