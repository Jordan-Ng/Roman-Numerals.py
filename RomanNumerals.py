user_input = input("enter a number from 1 to 3999")
roman_numerals = [['M', 'MM', 'MMM'],
                  ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                  ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                  ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']]


if user_input.isdigit():
    # numbers greater than 1000
    if int(user_input) >= 1000:
        roman_output = [" ", " ", " ", " "]
        listify_input = list(user_input)

        for index, unit in enumerate(roman_output):
            # for ind, rom in enumerate(unit):
            print(user_input[index])
            if user_input[index] != "0":
                roman_output[index] = roman_numerals[index][int(
                    user_input[index])-1]
                final_roman_output_val = ''.join(roman_output)
        print(final_roman_output_val)

    # numbers from 100-999
    elif int(user_input) >= 100 and int(user_input) <= 999:
        roman_output = [" ", " ", " "]
        listify_input = list(user_input)
        print(listify_input)

        for index, unit in enumerate(roman_output):
            if user_input[index] != "0":
                roman_output[index] = roman_numerals[index +
                                                     1][int(user_input[index])-1]
                final_roman_output_val = ''.join(roman_output)
        print(final_roman_output_val)

    # numbers from 10-99
    elif int(user_input) >= 10 and int(user_input) <= 99:
        roman_output = [" ", " "]
        listify_input = list(user_input)
        print(listify_input)

        for index, unit in enumerate(roman_output):
            if user_input[index] != "0":
                roman_output[index] = roman_numerals[index +
                                                     2][int(user_input[index])-1]
                final_roman_output_val = ''.join(roman_output)
        print(final_roman_output_val)

    # numbers from 1-9
    elif int(user_input) >= 1 and int(user_input) <= 9:
        roman_output = [" "]
        listify_input = list(user_input)
        print(listify_input)

        for index, unit in enumerate(roman_output):
            if user_input[index] != "0":
                roman_output[index] = roman_numerals[index +
                                                     3][int(user_input[index])-1]
                final_roman_output_val = ''.join(roman_output)
        print(final_roman_output_val)

else:
    print("Please enter a number from 1 to 3999")
