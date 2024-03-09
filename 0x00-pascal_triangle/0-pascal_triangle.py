def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == i:
                row.append(1)
            elif j > 1 and i > 1:
                row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            else:
                row.append(i**j)
        triangle.append(row)
    return triangle
