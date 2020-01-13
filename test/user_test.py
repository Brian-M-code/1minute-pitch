import unittest
from app.models import User


class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password = '12345678')
        
        self.assertTrue(self.new_userTrue, False)


if __name__ == '__main__':
    unittest.main()
