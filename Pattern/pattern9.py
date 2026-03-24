import sys
sys.stdout = open('Pattern/output.txt', 'w')
sys.stdin = open('Pattern/input.txt', 'r')

def main(): 
    n = int(input())
    print_pattern(n)


def print_pattern(n): 
    """Print number spiral square"""

    # ************** #
    # 3 3 3 3 3 
    # 3 2 2 2 3 
    # 3 2 1 2 3 
    # 3 2 2 2 3 
    # 3 3 3 3 3 
    # *************** #


    top,left,bottom,right = 0,0,0,0

    for i in range(2*n-1): 
        for j in range(2*n-1): 
            top = i 
            left = j 
            bottom = (2*n-2) - i
            right = (2*n-2) - j

            curr_num = n - min(top, left, bottom, 
            right)

            print(curr_num, end=" ")
    
        print()






if __name__ == "__main__": 
    main()