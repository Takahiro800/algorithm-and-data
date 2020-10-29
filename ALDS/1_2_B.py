N = int(input())
A = list(map(int, input().split()))

def selection_sort(N, A):
  ans = 0
  for i in range(N):
    tmp_min = i
    for j in range(i, N):
      if A[j] < A[tmp_min]:
        tmp_min = j
    if A[i] > A[tmp_min]:
      A[i], A[tmp_min] = A[tmp_min], A[i]
      ans += 1
  return ans

ans = selection_sort(N, A)

L = [str(a) for a in A]
L = " ".join(L)
print(L)
print(ans)