IV = 4
V = 5
L = 50
X = 10
IX = 9 # Is this a thing? Validate these numbers.
I = 1
C = 100
def main():
    numeral_string = 'LVIV'
    roman_numeral(numeral_string)

def roman_numeral(numeral_string):
    sum = 0
    # Look for instances of IV, IX, count them, and replace them with blank string.
    count_iv = numeral_string.find('IV')
    count_ix = numeral_string.find('IX')
    numeral_string = numeral_string.replace('IV','')
    numeral_string = numeral_string.replace('IX','')

    sum += count_iv * IV
    sum += count_ix * IX
    # Then sum rest of the normal numbers.
    for item in numeral_string[::1]:
        # Get item from dictionary to add to sum
        # sum += *Look up the value to add*
        continue # fix this
    # return the sum


if __name__ == "__main__":
    main()
