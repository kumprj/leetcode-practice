
list = [0, 1, 2, 3]
def main():
    curr_list1 = 0
    index1 = 0

    for n in nums:
        index2 = index1 + 1
        curr_list2 = 1
        for j in nums[index2:]:
            #print(f'L1 is {n}')
            #print(f'L2 is {j}')
            # print(f'index1 is {index1}')
            # print(f'index2 is {index2}')
            if (n + j) == target:
                # print('got here')
                return [index1, index2] 
            index2+=1
        index1+=1

def o_of_n():
    prevTable = {}

    for i,currVal in enumerate(nums):
        complement = target - currVal
        if complement in prevTable:
            return [prevTable[complement],i]
        prevTable[currVal] = i


if __name__ == "__main__":
    main()
