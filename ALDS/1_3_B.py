N, LIMIT = map(int, input().split())

class Queue:
  def __init__(self, limit_int):
    self.head = self.tail = 0
    self.limit_int = limit_int
    self.list = [None] * limit_int

  def is_empty():
    return self.head == self.tail

  def enqueue(self, num):
    self.list[self.tail] = num
    if self.tail + 1 == self.limit_int:
      self.tail = 0
    else:
      self.tail += 1

  def dequeue(self):
    list_head = self.list[self.head]
    if self.head + 1 == self.limit_int:
      self.head = 0
    else:
      self.head += 1
    return list_head

fin_order = [None] * N
order_list = Queue(N)
time_list = Queue(N)

for i in range(N):
  tmp_num, quon_time = input().split()
  order_list.enqueue(tmp_num)
  time_list.enqueue(int(quon_time))

current_time = 0
fin_count = 0
while fin_count < N:
  a = time_list.dequeue()
  b = order_list.dequeue()
  if a > LIMIT:
    current_time += LIMIT
    a -= LIMIT
    time_list.enqueue(a)
    order_list.enqueue(b)
  else:
    current_time += a
    fin_count += 1
    print(b, current_time)
