n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

def binary_search(A, key):
  left = 0
  right = len(A)

  while left < right:
    mid = (left + right) // 2
    if A[mid] == key:
      return 1
    elif A[mid] > key:
      right = mid
    else:
      left = mid + 1
  return -1

ans = 0

for i in range(q):
  key = T[i]
  ret = binary_search(S, key)
  if ret == 1:
    ans += 1

print(ans)