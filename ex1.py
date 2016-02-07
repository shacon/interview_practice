import unittest

def has_repeats(str):
    """
    takes a string and returns True if that string has
    repeats and False otherwise - (0)n running time
    """
    #assuming that the string contains an ASCII character (of which there are 128)
    if len(str) > 128:
        return True
    else:
        char_dict = {}
        for char in str:
            char_dict[char] = False
        for char in str:
            if char_dict[char] == True:
                return True
            else:
                char_dict[char] = True
        return False




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