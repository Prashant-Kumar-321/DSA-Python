import sys
sys.stdout = open('Pattern/output.txt', 'w')
sys.stdin = open('Pattern/input.txt', 'r')

def main(): 
    n = int(input())
    print_pattern(n)

def print_pattern(n): 
    # """Number triangle"""

    # ***************** #
    # 1
    # 12
    # 123
    # 1234
    # 12345
    # 123456
    # 1234567
    # 12345678
    # ***************** #
    
    for i in range(1, n+1): # 1, 2, 3
        for j in range(1, i+1): # 1, (1, 2)
            print(j, end="")
        
        print()

    # ****************** # 
    # 1
    # 22
    # 333
    # 4444
    # 55555
    # 666666
    # 7777777
    # 88888888
    # **************** # 
    for i in range(1, n+1): # n = 5, [1, 2, 3, 4, 5]
        for j in range(i): # i = 5, [0, 1, 2, 3, 4] i # of times
            print(i, end="")
        
        print()
        



if __name__ == "__main__": 
    main()