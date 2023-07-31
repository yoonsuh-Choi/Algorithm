def n_factory(n):
    i = 1
    n_fac = 1
    while i <= n:
        n_fac = n_fac * i
        i += 1
    return n_fac

def solution(balls, share):
    answer = 0
    n = balls
    m = share
    
    #순열과 조합
    # 5! = 5*4*3*2*1 =5*4! 
    # 5개 중 3개 뽑는 조합 : 5! / 2!*3!
    
    # n! = n * n-1! 
    
    answer = n_factory(n) / (n_factory(n-m) * n_factory(m))
    
        
    return answer