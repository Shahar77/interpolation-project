def lagrange_interpolation(x, y, x_interp):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_interp - x[j]) / (x[i] - x[j])
        result += term
    return result


def neville_interpolation(x, y, x_interp):
    n = len(x)
    Q = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        Q[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            Q[i][j] = ((x_interp - x[i + j]) * Q[i][j - 1] + (x[i] - x_interp) * Q[i + 1][j - 1]) / (x[i] - x[i + j])
    return Q[0][n - 1]


def print_table(x, y):
    print("Input table (x, y):")
    for xi, yi in zip(x, y):
        print(f"({xi}, {yi})")


def main():
    x_vals = [1, 2, 3, 4]
    y_vals = [1, 4, 9, 16]
    x_to_interp = 2.5

    print_table(x_vals, y_vals)

    result_lagrange = lagrange_interpolation(x_vals, y_vals, x_to_interp)
    result_neville = neville_interpolation(x_vals, y_vals, x_to_interp)

    print(f"\nLagrange result at x = {x_to_interp}: {result_lagrange}")
    print(f"Neville result at x = {x_to_interp}: {result_neville}")


if __name__ == "__main__":
    main()


def lagrange_interpolation(x, y, x_interp):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_interp - x[j]) / (x[i] - x[j])
        result += term
    return result


def neville_interpolation(x, y, x_interp):
    n = len(x)
    Q = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        Q[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            Q[i][j] = ((x_interp - x[i + j]) * Q[i][j - 1] + (x[i] - x_interp) * Q[i + 1][j - 1]) / (x[i] - x[i + j])
    return Q[0][n - 1]


def print_table(x, y):
    print("Input table (x, y):")
    for xi, yi in zip(x, y):
        print(f"({xi}, {yi})")


def main():
    x_vals = [1, 2, 3, 4]
    y_vals = [1, 4, 9, 16]
    x_to_interp = 2.5

    print_table(x_vals, y_vals)

    result_lagrange = lagrange_interpolation(x_vals, y_vals, x_to_interp)
    result_neville = neville_interpolation(x_vals, y_vals, x_to_interp)

    print(f"\nLagrange result at x = {x_to_interp}: {result_lagrange}")
    print(f"Neville result at x = {x_to_interp}: {result_neville}")


if __name__ == "__main__":
    main()
