def check_divisor(div, s):
    div_width = len(s) // div
    if (len(s) % div_width != 0):
        return False
    
    for n in range(0, div_width):
        ltr = s[n]
        multiplier = 1
        while True:
            idx = (div_width * multiplier) + n
            if (idx >= len(s)):
                break
            if(s[idx] != ltr):
                return False
            multiplier += 1
        return True

def find_next_divisor(s):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    prime_idx = 0
    
    max_divisor = len(s) // 2
    
    while (max_divisor >= primes[prime_idx]):
        if (len(s) % primes[prime_idx] != 0):
            prime_idx += 1
            continue
        if (check_divisor(primes[prime_idx], s)):
            return primes[prime_idx]
        else:
            prime_idx +=1
            continue
    return None
        

def check_all_same_char(s):
    ltr = s[0]
    for n in range (1, len(s)):
        if (ltr != s[n]):
            return False
    return True
                            
def solution(s):
    if (not s):
        return 0
    if (len(s) == 1):
        return 1
    if (check_all_same_char(s)):
        return len(s)
    
    divisors = [1,]
    next_divisor = find_next_divisor(s)
    while (next_divisor is not None):
        division_width = len(s) // next_divisor
        divisors.append(next_divisor)
        s = s[0:division_width]
        next_divisor = find_next_divisor(s)
        
    total_divisions = divisors.pop(0)
    while (divisors):
        total_divisions *= divisors.pop()
    return total_divisions
