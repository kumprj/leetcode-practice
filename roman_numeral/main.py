

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
IX = 9
IV = 4
XL = 40
XC = 90
CD = 400
CM = 1000

# dict = {'IV': 4, 'V': 5, 'L': 50, 'X' : 10, 'IX' : 9, 'I' : 1, 'C' : 100}
dict = {'V': 5, 'L': 50, 'X' : 10, 'I' : 1, 'C' : 100, 'D' : 500, 'M' : 1000}

def main():
    s = 'LVIII'
    roman_numeral(s)

def roman_numeral(s):
    sum = 0
    # Look for instances of IV, IX, count them, and replace them with blank string.
    count_iv = s.count('IV')
    count_ix = s.count('IX')
    count_xl = s.count('XL')
    count_xc = s.count('XC')
    count_cd = s.count('CD')
    count_cm = s.count('CM')
    s = s.replace('IV','')
    s = s.replace('IX','')
    s = s.replace('XL','')
    s = s.replace('XC','')
    s = s.replace('CD','')
    s = s.replace('CM','')

    sum += count_iv * IV
    sum += count_ix * IX
    sum += count_xl * XL
    sum += count_xc * XC
    sum += count_cd * CD
    sum += count_cm * CM
    # Then sum rest of the normal numbers.
    for roman_num in s[::1]:
        sum += dict.get(roman_num)
        # Get item from dictionary to add to sum
        # sum += *Look up the value to add*
        # continue # fix this
    # return the sum
    print(sum)


if __name__ == "__main__":
    main()
