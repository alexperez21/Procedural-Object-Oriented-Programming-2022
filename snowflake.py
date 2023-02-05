n = int(input("Enter odd integer: "))

a = [['.'] * n for i in range(n)]

for i in range(n):
  a[n // 2][i], a[i][n // 2], a[i][i], a[i][n - 1 - i] = '*' * 4
print('\n'.join([' '.join(a[i]) for i in range(n)]))
