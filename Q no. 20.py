def fill_2d_list(m, n):
    arr = [[0] * m for _ in range(n)]
    layers = (min(m, n) + 1) // 2
    
    for layer in range(layers):
        value = layer + 1
        for i in range(layer, m - layer):
            arr[layer][i] = value          # Top row
            arr[n - layer - 1][i] = value  # Bottom row
        for j in range(layer + 1, n - layer - 1):
            arr[j][layer] = value          # Left column
            arr[j][m - layer - 1] = value  # Right column
    
    return arr


m = 10
n = 9
result = fill_2d_list(m, n)
for row in result:
    print(row)
