import sys
sys.stdout = open('Pattern/output.txt', 'w')
sys.stdin = open('Pattern/input.txt', 'r')

def main(): 
    n = int(input())
    print_pattern(n)
    reverse_equilateral_tri(n)

def print_pattern(n): 
    """Equilateral Triangle"""
    for i in range(n): # [0, 4]
        for j in range(n+i): # [0, 8]
            if j >= n-i-1: 
                print("*", end="")
            else: 
                print(" ", end="")
        
        print()
    
def reverse_equilateral_tri(n): 
    """reverse equilateral triangle"""
    # *************** # 

    # *********
    #  *******
    #   *****
    #    ***
    #     *

    # **************** # 

    
    # n = 5
    for i in range(n-1, -1, -1): # [4, 0]
        for j in range(n+i): 
            if j >= n-i-1: 
                print('*', end='')
            else:
                print(' ', end='')
        
        print()


    pass 


if __name__ == "__main__": 
    main()