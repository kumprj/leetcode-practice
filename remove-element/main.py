from typing import List

def removeElement(nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)

def main():
    arr = [3,2,2,3]
    val = 3
    print(removeElement(arr, val))


if __name__ == "__main__":
    main()