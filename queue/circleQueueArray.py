class CircleQueueArray:
    def __init__(self, capacity):
        assert(capacity > 1)
        self._data = []
        self._count = 0
        self._head = 0
        self._tail = 0
        self._n = capacity
    
    def enQueue(self, item):
        if (self._tail + 1) % self._n == self._head:
            print ("Enqueue failed. The queue is full.")
            return False

        self._data.insert(self._tail, item)
        self._tail = (self._tail + 1) % self._n

        print ("Enqueue:", item)

        return True
    
    def deQueue(self):
        if self._head == self._tail:
            print ("Dequeue failed. The queue is empty.")
            return False
        else:
            item = self._data[self._head]
            self._head = (self._head + 1) % self._n

            print ("Dequeue:", item)

            return item

if __name__ == "__main__":
    q = CircleQueueArray(5)
    q.enQueue(1)
    q.enQueue(10)
    q.enQueue(5)
    q.enQueue(4)
    q.enQueue(6)
    q.enQueue(6)
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.enQueue(1)
    q.enQueue(10)
    q.enQueue(5)
    q.enQueue(4)
    q.enQueue(6)
    q.enQueue(6)
    q.enQueue(1)