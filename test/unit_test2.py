import unittest
import src.main as main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.calcuate_similarity(['今天','是','星期天','天气','晴','今天','晚上','我','要去','看电影'],
                                                  ['今天','是','周天','天气','晴朗','我','晚上','要去','看电影']),0.76980036)  # add assertion here


if __name__ == '__main__':
    unittest.main()
