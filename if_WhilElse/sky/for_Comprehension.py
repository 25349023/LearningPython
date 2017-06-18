import sys

squares = [int(arg) ** 2 for arg in sys.argv[1:] if int(arg) % 2 == 0]
print(squares)

ma = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newMa = [ele for row in ma for ele in row]
print(newMa)
