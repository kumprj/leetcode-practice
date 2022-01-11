
nums = [3, 2, 4]
target = 6
def main():
    slower = o_of_n2()
    print(slower)
    faster = o_of_n()
    print(faster)

def o_of_n2():
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
    iterated_over = {}

    for i,current in enumerate(nums):
        sum = target - current
        if sum in iterated_over:
            return [iterated_over[sum],i]
        iterated_over[current] = i


if __name__ == "__main__":
    main()
