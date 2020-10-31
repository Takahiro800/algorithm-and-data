S = list(input().split())
N = len(S)

def is_int(str):
  try:
    int(str)
    return True
  except ValueError:
    return False


class Stack:
  def __init__(self, max):
    self.size = max
    self.top = 0
    self.stack = [None] * self.size

  def is_empty(self):
    return self.top == 0

  def push(self, arg_object):
    self.top += 1
    self.stack[self.top] = arg_object

  def pop(self):
    self.top -= 1
    return self.stack[self.top+1]

NUM = Stack(N)

for i in range(N):
  ch = S[i]
  if ch in ['+', '-', '*']:
    num_2 = NUM.pop()
    num_1 = NUM.pop()
    if ch == '+':
      num = num_1 + num_2
    elif ch == '-':
      num = num_1 - num_2
    else:
      num = num_1 * num_2
    NUM.push(num)
  else:
    NUM.push(int(ch))
print("%d" %(NUM.pop()))
