import sys 
sys.stdout = open('Recursion/output.txt', 'w')
sys.stdin = open('Recursion/input.txt', 'r') 

def reverse(arr:list):
    """Iterative method"""

    # Pointer variable
    p1 = 0          # first element
    p2 = len(arr)-1 # last element

    while p1 < p2: 
        # swap arr[p1] and arr[p2]
        arr[p1], arr[p2] = arr[p2], arr[p1]

        p1 += 1
        p2 -= 1
    
def reverse(arr:list, p1, p2):
    if p1 >= p2: return

    # Swap arr[p1] and arr[p2]
    arr[p1], arr[p2] = arr[p2], arr[p1]

    reverse(arr, p1+1, p2-1)
    



if __name__ == "__main__": 
    n = int(input())
    arr = list(map(int, input().split(sep=" ")))

    reverse(arr, 0, n-1)
    # arr.reverse() # built-in method
    print(arr)