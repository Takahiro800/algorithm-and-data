N = int(input())
A = list(map(int, input().split()))

for i  in range(1, N):
  L = [str(a) for a in A]
  L = " ".join(L)
  print(L)
  v = A[i]
  j = i -1
  while j >= 0 and A[j] > v:
    A[j+1] = A[j]
    A[j] = v
    j -= 1
L = [str(a) for a in A]
L = " ".join(L)
print(L)