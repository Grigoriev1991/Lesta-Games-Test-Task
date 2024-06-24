class StaticBuffer:
    def __init__(self, size: int) -> None:
        self.size = size
        self.front = 0
        self.rear = 0
        self.count = 0
        self.buffer = [None] * size

    def enqueue(self, data):
        if self.count == self.size:
            raise OverflowError('Buffer is Full')
        self.buffer[self.front] = data
        self.front = (self.front + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError('Buffer contains no elements')
        data = self.buffer[self.rear]
        self.buffer[self.rear] = None
        self.rear = (self.rear + 1) % self.size
        self.count -= 1
        return data

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.size

    def peek(self):
        if self.count == 0:
            raise IndexError('Buffer contains no elements')
        return self.buffer[self.rear]

    def current_size(self) -> int:
        return self.count

    def clear(self) -> None:
        self.front = 0
        self.rear = 0
        self.count = 0
        self.buffer = [None] * self.size

    def __repr__(self) -> str:
        return f"{self.buffer}"


if __name__ == "__main__":
    q = StaticBuffer(5)
    for i in range(5):
        q.enqueue(i)
    print(q.current_size())
