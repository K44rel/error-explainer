import unittest
from temp.test_utils import run_test_scenario
from messages import get_formatted_message


class QuotesTest(unittest.TestCase):

    def test_no_new_indentation(self):
        path = "tests/quotes_test/samples/simple_missing_double_after.py"
        expected_message = get_formatted_message("invalid_quotes", line=1, quote="'", pos=10)
        run_test_scenario(self, path, 1, expected_message)


if __name__ == '__main__':
    unittest.main()
