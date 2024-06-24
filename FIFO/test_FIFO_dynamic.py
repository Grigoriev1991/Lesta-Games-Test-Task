import unittest

from FIFO.FIFO_dynamic import DinamicBuffer


class TestDinamicBuffer(unittest.TestCase):

    def test_enqueue(self):
        q = DinamicBuffer(5)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.buffer, [1, 2, None, None, None])
        self.assertEqual(q.count, 2)

    def test_dequeue(self):
        q = DinamicBuffer(5)
        q.enqueue(1)
        q.enqueue(2)
        data = q.dequeue()
        self.assertEqual(data, 1)
        self.assertEqual(q.buffer, [None, 2, None, None, None])
        self.assertEqual(q.count, 1)

    def test_buffer_upgrade(self):
        q = DinamicBuffer(2)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.size, 4)
        self.assertEqual(q.buffer[:q.count], [1, 2, 3])

    def test_dequeue_empty_buffer(self):
        q = DinamicBuffer(5)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_enqueue_dequeue_full_buffer(self):
        q = DinamicBuffer(2)
        q.enqueue(1)
        q.enqueue(2)
        q.dequeue()
        q.enqueue(3)
        self.assertEqual(q.buffer[:q.count], [3, 2])


if __name__ == '__main__':
    unittest.main()
