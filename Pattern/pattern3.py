import sys
sys.stdout = open('Pattern/output.txt', 'w')
sys.stdin = open('Pattern/input.txt', 'r')

def main(): 
    n = int(input())
    print_pattern(n)

def print_pattern(n): 
    # """Up-Side down Number triangle"""

    # *************** #
    # 12345
    # 1234
    # 123
    # 12
    # 1
    # ************* #

    for i in range (n, 0, -1): # [n, 1]
        for j in range(1, i+1): # [1, i] 
            print(j, end="")

        print()


if __name__ == "__main__": 
    main()