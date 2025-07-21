def spiral_order(matrix):
    if not matrix:
        return []

    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])
    result = []

    while top < bottom and left < right:
        # Traverse from Left to Right
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        # Traverse from Top to Bottom
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        # Traverse from Right to Left
        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

        # Traverse from Bottom to Top
        if left < right:
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Spiral Order:", spiral_order(matrix))
