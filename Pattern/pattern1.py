import sys
sys.stdout = open('Pattern/output.txt', 'w')
sys.stdin = open('Pattern/input.txt', 'r')

def main(): 
    n = int(input())
    print_pattern(n)

def print_pattern(n): 
    """triangle"""
    for i in range(n, 0, -1): 
        for j in range(i): 
            print("*", end="")
        
        print()
        



if __name__ == "__main__": 
    main()