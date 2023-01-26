import unittest
import my_log


class MyLogCase(unittest.TestCase):
    def test_my_log(self):
        log = my_log.Log("logTestPath")
        log.info("info")
        log.error("error")


if __name__ == '__main__':
    unittest.main()
