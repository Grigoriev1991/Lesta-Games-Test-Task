import unittest

from FIFO.FIFO_static_overwrite import StaticBufferOverwrite


class TestStaticBufferOverwrite(unittest.TestCase):
    def setUp(self):
        self.buff = StaticBufferOverwrite(5)

    def test_enqueue(self):
        self.buff.enqueue(1)
        self.buff.enqueue(2)
        self.assertEqual(self.buff.buffer, [1, 2, None, None, None])
        self.assertEqual(self.buff.current_size(), 2)

    def test_dequeue(self):
        self.buff.enqueue(1)
        self.buff.enqueue(2)
        self.assertEqual(self.buff.dequeue(), 1)
        self.assertEqual(self.buff.buffer, [None, 2, None, None, None])
        self.assertEqual(self.buff.current_size(), 1)

    def test_is_empty(self):
        self.assertTrue(self.buff.is_empty())
        self.buff.enqueue(1)
        self.assertFalse(self.buff.is_empty())

    def test_is_full(self):
        self.assertFalse(self.buff.is_full())
        for i in range(5):
            self.buff.enqueue(i)
        self.assertTrue(self.buff.is_full())

    def test_peek(self):
        self.buff.enqueue(1)
        self.buff.enqueue(2)
        self.assertEqual(self.buff.peek(), 1)
        self.buff.dequeue()
        self.assertEqual(self.buff.peek(), 2)

    def test_current_size(self):
        self.assertEqual(self.buff.current_size(), 0)
        self.buff.enqueue(1)
        self.assertEqual(self.buff.current_size(), 1)
        self.buff.enqueue(2)
        self.assertEqual(self.buff.current_size(), 2)

    def test_clear(self):
        for i in range(5):
            self.buff.enqueue(i)
        self.buff.clear()
        self.assertEqual(self.buff.buffer, [None, None, None, None, None])
        self.assertTrue(self.buff.is_empty())
        self.assertFalse(self.buff.is_full())

    def test_dequeue_underflow(self):
        with self.assertRaises(IndexError):
            self.buff.dequeue()


if __name__ == '__main__':
    unittest.main()
