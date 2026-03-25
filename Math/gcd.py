import sys 
sys.stdout = open('Math/output.txt', 'w')
sys.stdin = open('Math/input.txt', 'r')

def gcd(a:int, b:int)->int: 
    """Calculate GCD value of a and b"""
    if a < b: 
        a, b = b, a
    
    while b != 0: 
        temp = a % b
        a = b 
        b = temp 
    
    return a

def gcd(a:int, b:int)->int:
    """Recursive defintion of euclid gcd algorithm"""
    if b == 0: return a 
    return gcd(b, a%b)

# Time Complexity Analyse later

if __name__ == "__main__": 
    a,b = map(int, input().split())
    res = gcd(a, b)
    print(res)

