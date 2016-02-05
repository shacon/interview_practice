import unittest

def has_repeats(str):
    """
    takes a string and returns True if that string has
    repeats and False otherwise
    """
    if len(str) == 0:
        return False
    if len(str) == 1:
        return False
    else:
        for char in str[1:]:
            if str[0] == char:
                return True
            else:
                return has_repeats(str[1:])



class TestRepeatMethods(unittest.TestCase):


    def test_has_repeats(self):
        self.assertEqual(has_repeats("stop"), False)
        self.assertEqual(has_repeats("p"), False)
        self.assertEqual(has_repeats(""), False)
        self.assertEqual(has_repeats("allen"), True)
        self.assertEqual(has_repeats("sally"), True)
        self.assertEqual(has_repeats("QQQQQQ"), True)




if __name__ == '__main__':
    unittest.main()