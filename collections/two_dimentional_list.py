# two dimensional array
grid = [
    [1, 2, 3], # each element is an array itself
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(grid)
print(grid[0][0]) # print single element

for row in grid:
    for item in row:
        print(item)