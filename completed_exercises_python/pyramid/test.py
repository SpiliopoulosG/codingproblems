from unittest.mock import patch
import io
import unittest
import types
from main import pyramid


class TestPyramids(unittest.TestCase):

    def test_steps_exist(self):
        self.assertIsInstance(pyramid, types.FunctionType)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        pyramid(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_one_pyramid(self):
        self.assert_stdout(1, "#\n")

    def test_two_pyramid(self):
        self.assert_stdout(2, " # \n###\n")

    def test_two_pyramid(self):
        self.assert_stdout(3, "  #  \n ### \n#####\n")

    def test_two_pyramid(self):
        self.assert_stdout(4, "   #   \n  ###  \n ##### \n#######\n")


if __name__ == '__main__':
    unittest.main()
