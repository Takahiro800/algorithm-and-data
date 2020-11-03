from sys import stdin

class Node:
  def __init__(self, num, prv=None, nxt=None):
    self.num = num
    self.prv = prv
    self.nxt = nxt

class DoublyLinkedList:
  def __init__(self):
    self.start = self.last = None

  def insert(self, num):
    elem = Node(num)

    if self.start is None:
      self.start = self.last = elem
    else:
      self.start.prv = elem
      elem.nxt = self.start
      self.start = elem

  def delete_start(self):
    if self.start == self.last:
      self.start = self.last = None
    else:
      self.start = self.start.nxt
      self.start.prv = None

  def delete_last(self):
    if self.start == self.last:
      self.start = self.last = None
    else:
      self.last = self.last.prv
      self.last.nxt = None

  def delete_num(self, num):
    it = self.start

    while it is not None:
      if num == it.num:
        if it.prv is None:
          self.start = it.nxt
        else:
          it.prv.nxt = it.nxt

        if it.nxt is None:
          self.last = it.prv
        else:
          it.nxt.prv = it.prv

        break
      it = it.nxt

  def get_content(self):
    ret = []
    it = self.start
    while it is not None:
      ret.append(it.num)
      it = it.nxt

    print(' '.join(ret))


def _main():
  n = int(input())
  lst = DoublyLinkedList()

  for _ in range(n):
    cmd = list(stdin.readline().split())
    if cmd[0] == 'insert':
      lst.insert((cmd[1]))
    elif cmd[0] == 'delete':
      lst.delete_num((cmd[1]))
    elif cmd[0] == 'deleteFirst':
      lst.delete_start()
    else:
      lst.delete_last()

  lst.get_content()

if __name__ == '__main__':
  _main()