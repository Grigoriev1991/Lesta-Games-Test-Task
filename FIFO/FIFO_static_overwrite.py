class StaticBufferOverwrite:
    def __init__(self, size: int) -> None:
        self.size = size
        self.front = 0
        self.rear = 0
        self.count = 0
        self.buffer = [None] * size

    def enqueue(self, data):
        if self.count == self.size:
            self.rear = (self.rear + 1) % self.size
        else:
            self.count += 1
        self.buffer[self.front] = data
        self.front = (self.front + 1) % self.size

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
    q = StaticBufferOverwrite(2)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q)
