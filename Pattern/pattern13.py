import sys
sys.stdout = open("Pattern/output.txt", "w")
sys.stdin = open("Pattern/input.txt", "r")


def main(): 
    n = int(input())
    # print_pattern(n)
    print_pattern_1(n)

def print_pattern(n): 
    """Print alphabet  equilateral triangle pattern"""
    for i in range(n):
        letter = 65 
        for j in range(n+i): 
            if j >= n-1-i: 
                print(chr(letter), end="")

                if j < n-1: letter += 1 
                else: letter -= 1

            else: print(" ", end="")
        
        print()

def print_pattern_1(n): 
    """Print a reverse alphabet triangle pattern"""
    letter = 64 + n
    for i in range(n): 
        col_letter = letter 
        for j in range(i+1): 
            print(chr(col_letter), end="")
            col_letter += 1  
        
        print()
        letter -= 1

            
if __name__ == "__main__": 
    main()

