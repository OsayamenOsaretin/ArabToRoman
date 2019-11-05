import unittest
from function import arabic_to_roman_converter, value_converter, validate_argument


class ArabToRomanTest(unittest.TestCase):
    def test_arabic_to_roman_converter(self):
        nums = {
            5: "V",
            11: "XI",
            25: "XXV",
            30: "XXX",
            300: "CCC",
            700: "DCC",
            1009: "MIX",
            3222: "MMMCCXXII"
        }
        for key, val in nums.items():
            self.assertEqual(arabic_to_roman_converter(key, 1000), val)

    def test_value_converter(self):
        values = {
            1000: [{
                3: 'MMM'
            }],
            100: [{1: 'C'}, {5: 'D'}],
            1: [{4: 'IV'}]
        }
        for denom_key, denom_values in values.items():
            for values in denom_values:
                for key, value in values.items():
                    self.assertEqual((value_converter(key, denom_key)), value)

    def test_validate_argument(self):
        invalid_arguments = [-1, 0, 4000, 'some string']
        valid_arguments = ['1', '10', '1000']

        for arg in invalid_arguments:
            self.assertEqual(validate_argument(
                arg), (None, 'Invalid argument, value must be an Integer between 1 and 3999'))

        for arg in valid_arguments:
            self.assertEqual(validate_argument(arg), (int(arg), None))

if __name__ == '__main__':
    unittest.main()
