import sys
sys.stdout = open("Pattern/output.txt", "w")
sys.stdin = open("Pattern/input.txt", "r")


def main(): 
    n = int(input())
    # print_pattern(n)
    # print_alphabet_pattern(n)
    print_upside_down_alphabet_triangle(n)


def print_pattern(n): 
    """Print number pattern"""
    num = 1
    for i in range(n): 
        for j in range(i+1): 
            print(num, end=" ")
            num += 1
        
        print()
    
def print_alphabet_pattern(n): 
    """Print alphabet triangle"""
    for i in range(n):
        letter = 65 
        for j in range(i+1):
            letter_tmp = letter % 91
            if letter_tmp < 65: letter_tmp += 65
            print(chr(letter_tmp), end=" ")
            letter += 1
        
        print()

def print_upside_down_alphabet_triangle(n): 
    """Print alphabet upside down right angled triangle"""

    for i in range(n-1, -1, -1): 
        letter = 65 
        for j in range(i): 
            print(chr(letter), end="")
            letter += 1

        print()


            
if __name__ == "__main__": 
    main()

