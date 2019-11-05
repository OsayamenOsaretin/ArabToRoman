roman_numerals_mapping = {
    1000: ['M'],
    100: ['C', 'D', 'M'],
    10: ['X', 'L', 'C'],
    1: ['I', 'V', 'X']
}


def value_converter(value, denominator):
    """ 
    Converts the integer value given using the denominator

    Parameters:
    value (int): Integer value to convert to arabic equivalent
    denominator(int): Index to roman numeral mapping.

    Returns:
    roman_value (string): roman value equivalent for value

    >>> [value_converter(number, 100) for number in [1,5,9]]
    ['C', 'D', 'CM']
    >>> [value_converter(number, 10) for number in [1,5,9]]
    ['X', 'L', 'XC']
    """
    romans_at_denominator = roman_numerals_mapping[denominator]

    if denominator == 1000:
        return value * romans_at_denominator[0]

    if value == 4:
        roman_value = ''.join(romans_at_denominator[:2])
        return roman_value
    if value == 9:
        roman_value = ''.join(romans_at_denominator[0::2])
        return roman_value
    if value < 5:
        roman_value = romans_at_denominator[0] * value
        return roman_value
    if value >= 5:
        five_value = romans_at_denominator[1]
        roman_value = five_value + value_converter(value - 5, denominator)
        return roman_value


def arabic_to_roman_converter(number, denominator=1000):
    """
    Converts arabic numbers to roman numerals

    Parameters:
    number (int): arabic number to convert to roman
    denominator (int): integer multiple of ten that indexes roman numeral values

    Returns:
    roman_value (int): roman numeral equivalent for number


    >>> [arabic_to_roman_converter(number) for number in [1, 15, 200, 259]]
    ['I', 'XV', 'CC', 'CCLIX']
    """
    if denominator == 1:
        return value_converter(number, 1)
    else:
        quotient, remainder = divmod(number, denominator)
        quotient_in_roman = value_converter(quotient, denominator)
        remainder_in_roman = arabic_to_roman_converter(
            remainder, denominator/10)
        return quotient_in_roman + remainder_in_roman


def validate_argument(maybe_number):
    """ 
    Validates arguments to make sure they are valid integers

    Parameters:
    maybe_number (int): possible integer value to be validated

    Returns:
    (value, error) (int, string): tuple that can contain error if validation fails or value if it passes

    >>> [validate_argument(maybe_number) for maybe_number in ['10', 'invalid string', '4001']]
    [(10, None), (None, 'Invalid argument, value must be an Integer between 1 and 3999'), (None, 'Invalid argument, value must be an Integer between 1 and 3999')]

    """
    try:
        value = int(maybe_number)
        if value < 1 or value > 3999:
            raise ValueError()
        return (value, None)
    except ValueError:
        return (None, 'Invalid argument, value must be an Integer between 1 and 3999')


def collect_user_argument():
    """
    Collects user input

    Returns:
    value (int): user value after validation and type casting
    """
    number = raw_input(prompt_message)
    value, error = validate_argument(number)
    if error:
        print(error)
        collect_user_argument()
    else:
        return value


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    prompt_message = "Enter a number, e.g 1, 10, 222: "
    rerun_message = "Convert another number? (Y/n): "
    playing = True

    while playing:
        number = collect_user_argument()
        print(arabic_to_roman_converter(number))
        rerun = raw_input(rerun_message)
        if rerun.lower() != 'y':
            playing = False
