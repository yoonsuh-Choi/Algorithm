def gcd(a, b): #최대 공약수
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b): #최소 공배수
    return int(a * b / gcd(a, b))

def solution(numer1, denom1, numer2, denom2): # 1/2 + 3/4
    answer = []
    
    denom3 = lcm(denom1, denom2) #분모
    a = numer1*(denom3//denom1) #분자1
    b = numer2*(denom3//denom2) #분자2
    numer3 = a + b
    gcd_n = gcd(numer3, denom3)
    
    if numer3 % gcd_n == 0 and denom3 % gcd_n == 0:
        answer.append(numer3//gcd_n)
        answer.append(denom3//gcd_n)
        
    return answer
