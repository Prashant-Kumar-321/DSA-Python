import sys
import math

sys.stdout = open('Math/output.txt', 'w')
sys.stdin = open('Math/input.txt', 'r')

def divisors(n: int)->int: 
    '''
    x = 28: divisors: [1, 2, 4, 7, 14, 28]
    '''

    sq_root = int(math.sqrt(n))
    divs = []

    for i in range(1, sq_root+1):
        if n % i == 0: 
            corr = n // i 

            if i != corr: 
                divs.append(corr)

            divs.append(i)

        
    return divs

def is_prime(n: int) -> bool: 
    """ Check given number is prime """
    sq_root = int(math.sqrt(n))

    for i in range(2, sq_root+1): 
        if n % i == 0: return False 
    
    return True 



if __name__ == "__main__": 
    n = int(input())
    # res = divisors(n)
    res = is_prime(n)
    print(res)



