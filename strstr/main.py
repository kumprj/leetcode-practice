def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    needle_len = len(needle)
    index = 0
    for substr in haystack:
        if needle == haystack[0:needle_len]:
            return index
        haystack = haystack[1:]
        index+=1
    
    return -1

def main():
    haystack = "wasadawdaw"
    needle = "aw"
    print(strStr(haystack, needle))

if __name__ == "__main__":
    main()

