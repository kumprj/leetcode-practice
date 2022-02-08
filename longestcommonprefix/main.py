
def main():
    dict = []
    strs = ["flower","flow","flight"]
    output = ""
    count = 0
    max = 0
    for item in strs[0[::1]]: # each item in the first element
        dict[item] = True

    # Loop through rest of the elements. 
    # # this pseudo code cant be right
    for item in strs[1[::1]]:
        if dict[item] == True:
            count += 1
        else:
            if count > max: max = count
            count = 0

if __name__ == "__main__":
    main()