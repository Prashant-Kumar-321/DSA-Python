import sys
sys.stdout = open('Pattern/output.txt', 'w')
sys.stdin = open('Pattern/input.txt', 'r')

def main(): 
    n = int(input())
    print_pattern(n)


def print_pattern(n): 
    """Print square"""

    # # ********************* # 
    #     *****
    #     *   *
    #     *   *
    #     *   *
    #     *****
    # ********************* # 
    for i in range(n): 
        for j in range(n): 
            if i == 0 or i == n-1: 
                print("*", end="")
            else:
                if j == 0 or j == n-1: 
                    print("*", end="")
                else: 
                    print(" ", end="")

        print()  




if __name__ == "__main__": 
    main()