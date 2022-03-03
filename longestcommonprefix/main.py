
def main():
    # This works to compare 2 strings, but we need to compare all of them.
    dict = []
    strs = ["flower","flow","flight", "flee"]
    # strs = ["racecar","tiger","poop", "flee"]
    output = ""
    count = 0
    max = 0
    i = 0
    for substr in range(len(strs[i])):
        if strs[i+1].startswith(strs[i][0:substr+1]):
            count += 1
            continue
        else:
            if max <= count:
                max = count
                output = strs[i][0:substr]

        i += 1
        count = 0
        if i+1 == len(strs): # does this work?
            break
    print(f'Final count is {max} letters.')
    print(f'Output is {output}')
    return output # or max

if __name__ == "__main__":
    main()