import copy

N = int(input())
A = list(input().split())


def bubble_sort(C, N):
  for i in range(N):
    for j in range(N-1, i, -1):
      if C[j][-1] < C[j-1][-1]:
        C[j],C[j-1] = C[j-1],C[j]
  return C

def selection_sort(C, N):
  for i in range(N):
    minj = i
    for j in range(i,N):
      if C[j][-1] < C[minj][-1]:
        minj = j
    C[i],C[minj] = C[minj],C[i]
  return C


def print_list(A):
  L = [str(a) for a in A]
  L = " ".join(L)
  print(L)

B = copy.copy(A)
C = copy.copy(A)
A_b = bubble_sort(B, N)
A_s = selection_sort(C, N)
print_list(A_b)
print('Stable')
print_list(A_s)
print('Stable' if (C == B) else 'Not stable')
