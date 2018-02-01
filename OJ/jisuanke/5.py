# M, N, T = map(int, input().split())

# a = [[[] for j in range(N)] for i in range(M)]  # marix M*N

# if T == 1:
#     # 上下翻转
#     pass
# elif T == 0:
#     # 左右翻转
#     pass

n,matrix=int(input()),[]
for i in range(n):
    matrix.append(input().split())
print(matrix)
for i in zip(*matrix):
    print(" ".join(i))
print(*matrix)