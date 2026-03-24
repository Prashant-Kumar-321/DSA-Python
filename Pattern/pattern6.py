import sys
sys.stdout = open('Pattern/output.txt', 'w')
sys.stdin = open('Pattern/input.txt', 'r')


def main(): 
    n = int(input())
    print_pattern(n)


def print_pattern(n): 
    """Print alternative binary right angled triangle"""
    def toggle_digit(bin_digit): 
        return 0 if bin_digit == 1 else 1

    row_bin_digit = 1
    for i in range(n): 
        col_bin_digit = row_bin_digit
        for j in range(i+1):
            print(col_bin_digit, end=' ')
            col_bin_digit = toggle_digit(col_bin_digit)
        
        row_bin_digit = toggle_digit(row_bin_digit)

        print()



if __name__ == "__main__": 
    main()