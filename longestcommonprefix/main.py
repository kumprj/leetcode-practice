
def main():
    # # This works to compare 2 strings, but we need to compare all of them.
    # dict = []
    # strs = ["flower","flow","flight", "flee"]
    # # strs = ["racecar","tiger","poop", "flee"]
    # output = ""
    # count = 0
    # max = 0
    # i = 0
    # for substr in range(len(strs[i])):
    #     if strs[i+1].startswith(strs[i][0:substr+1]):
    #         count += 1
    #         continue
    #     else:
    #         if max <= count:
    #             max = count
    #             output = strs[i][0:substr]

    #     i += 1
    #     count = 0
    #     if i+1 == len(strs): # does this work?
    #         break
    # print(f'Final count is {max} letters.')
    # print(f'Output is {output}')
    # return output # or max

    # Try 2
    output = ""
    strs = ["flower","flow","flight", "flee"]
    for current_string in strs:
        print(current_string)
        max = len(current_string)
        incr = 1
        print(current_string[0:incr])
        if current_string[0:incr] in strs[::1]:
            print('hi')
            pass
        # for curr_letters in current_string:
        #     # print(i)
        #     print(curr_letters)
        #     min += 1
        #     # if curr_letters in strs:
        #     #     min+=1
        #     #     print(curr_letters)
        #     #     continue
        #     # else: 
        #     #     min+=1
        #     #     continue
        #         # print('here')
    # print(output)

if __name__ == "__main__":
    main()