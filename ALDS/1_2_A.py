N = int(input())
A = list(map(int, input().split()))

def bubble_sort(A, N):
  sw = 0
  falg = 1
  i = 0
  while falg:
    falg = 0
    for j in range(N-1, i, -1):
      if A[j] < A[j-1]:
        A[j], A[j-1] = A[j-1], A[j]
        falg = 1
        sw += 1
    i += 1
  return sw

sw = bubble_sort(A, N)
L = [str(a) for a in A]
L = " ".join(L)
print(L)
print(sw)
