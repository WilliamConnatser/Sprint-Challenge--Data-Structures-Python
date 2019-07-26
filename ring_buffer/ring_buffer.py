class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  '''
    The append method adds elements to the buffer.
  '''
  def append(self, item):
    if None in self.storage:
      self.storage[self.storage.index(None)] = item
      self.current += 1
    else:
      if self.current == self.capacity:
        self.current = 0
      self.storage[self.current] = item
      self.current += 1


  '''
    The get method returns all of the elements in the buffer in
    a list in their given order. It should not return any None
    values in the list even if they are present in the ring buffer.
  '''
  def get(self):
    if None in self.storage:
      result = self.storage.copy()
      while None in result:
        result.pop()
      return result
    return self.storage
