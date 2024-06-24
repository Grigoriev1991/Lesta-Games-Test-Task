class DinamicBuffer:
    def __init__(self, size: int) -> None:
        self.size = size
        self.front = 0
        self.rear = 0
        self.count = 0
        self.buffer = [None] * size

    def enqueue(self, data):
        if self.count == self.size:
            self._upgrade()
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

    def _upgrade(self):
        new_size = self.size * 2
        new_buffer = [None] * new_size
        for i in range(self.count):
            new_buffer[i] = self.dequeue()
        self.buffer = new_buffer
        self.size = new_size
        self.front = len([el for el in new_buffer if el is not None])
        self.count = self.front
        self.rear = 0

    def __repr__(self) -> str:
        return f"{self.buffer}"


if __name__ == "__main__":
    q = DinamicBuffer(5)
    for i in range(5):
        q.enqueue(i)
    print(q.buffer)
    q.enqueue('six')
    print(q.buffer)
