
def main():
    no_string()
    as_string()

def as_string():
    if x < 0:
        return False
    word = str(x)
    word_reverse = word[::-1]
    if word == word_reverse:
        return True
    else:
        return False
def no_string():
    if (x < 0):
        return False
    palindromeList = []
    while x > 0:
        print(x % 10)
        palindromeList.append(x % 10)
        x = x // 10

    i = len(palindromeList)

    while i > 1:
        ending = palindromeList.pop()
        beginning = palindromeList.pop(0)
        i = len(palindromeList)

        if (ending == beginning):
            continue
        else:
            return False

    return True
if __name__ == "__main__":
    main()
