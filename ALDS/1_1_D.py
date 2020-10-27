n = int(input())
minR = int(input())
maxR = -2000000000

for i in range(n-1):
  k = int(input())
  maxR = max(maxR, k - minR)
  minR = min(minR, k)

print(maxR)
