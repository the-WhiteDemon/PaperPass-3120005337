import unittest
import src.main as main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.calcuate_similarity(['这是', '一个', '软件工程', '作业', '的', '测试用例'],
                                                  ['这是', '一个', '软件工程', '的', '测试用例']), 0.912871)


if __name__ == '__main__':
    unittest.main()
