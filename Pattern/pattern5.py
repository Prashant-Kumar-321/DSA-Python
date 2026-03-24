import sys
sys.stdout = open('Pattern/output.txt', 'w')
sys.stdin = open('Pattern/input.txt', 'r')

def main(): 
    n = int(input())
    print_pattern(n)


def print_pattern(n): 
    """Right pointed equilateral triangle"""
    errect_tri(n)
    upsidedown_tri(n-1)


def errect_tri(n): 
    """Print straight right angled triangle"""
    for i in range(n): 
        for j in range(i+1): 
            print("*", end="")
        print()


def upsidedown_tri(n): 
    """Print upside down right angled triangle"""
    for i in range(n, -1, -1):
        for j in range(i): 
            print("*", end="")
        
        print()
    



if __name__ == "__main__": 
    main()