import sys
sys.stdout = open('Pattern/output.txt', 'w')
sys.stdin = open('Pattern/input.txt', 'r')

def main(): 
    n = int(input())
    print_pattern(n)


def print_pattern(n): 
    """Print the number mountain pattern"""

    # ************************ # 
    # 1                 1 
    # 1 2             2 1 
    # 1 2 3         3 2 1 
    # 1 2 3 4     4 3 2 1 
    # 1 2 3 4 5 5 4 3 2 1 
    # ************************ # 

    left = 1
    right = 1

    for i in range(n): 
        left = 1
        right = i+1
        for j in range(2*n): 
            if j <= i: 
                print(left, end=" ")
                left += 1
            elif j >= 2 * n - 1 - i: 
                print(right, end=" ")
                right -= 1
            else: 
                print(" ", end=" ")
        
        print()




if __name__ == "__main__": 
    main()