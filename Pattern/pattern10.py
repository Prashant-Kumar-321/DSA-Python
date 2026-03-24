import sys
sys.stdout = open("Pattern/output.txt", "w")
sys.stdin = open("Pattern/input.txt", "r")


def main(): 
    n = int(input())
    print_pattern(n)

def print_pattern(n): 
    """Print hollow diamond"""
    def print_upper(n): 
        for i in range(n-1, -1, -1): # Iterate reverse
            for j in range(2*n): 
                if j <= i or j >= (2*n-1)-i: 
                    print("*", end="")
                else: 
                    print(" ", end="")
            
            print()
    
    def print_lower(n): 
        for i in range(n): 
            for j in range(2*n): 
                if j <= i or j >= (2*n-1)-i: 
                    print("*", end="")
                else: 
                    print(" ", end="")
                
            print()

    print_upper(n)
    print_lower(n)

if __name__ == "__main__": 
    main()