
list = [0, 1, 2, 3]
def main():
    curr_list1 = 0
    index1 = 0
    
    for n in nums:
        index2 = 1
        curr_list2 = 1
        for j in nums[curr_list1+1:]:
            print(f'L1 is {n}')
            print(f'L2 is {j}')
            if (n + j) == target:
                # curr_list2+=1
                return [index1, index2] 
            index2+=1
        index1+=1

def o_of_n_squared():
    pass


if __name__ == "__main__":
    main()
