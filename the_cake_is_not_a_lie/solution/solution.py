def eliminate_div_and_multiples(div, possible_divs):
    multiplier = 1
    while True:
        current_div = div * multiplier
        if (not current_div in possible_divs):
            break
        possible_divs.remove(current_div)
        multiplier += 1

def check_div(div, s):
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

def check_div1(s):
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
    if (check_div1(s)):
        return len(s)
    
    possible_divs = list(range(2, len(s)))
    idx = 0
    while True:
        if (idx >= len(possible_divs)):
            break
        if (not check_div(possible_divs[idx], s)):
            eliminate_div_and_multiples(possible_divs[idx], possible_divs)
        else:
            idx += 1
    
    if (possible_divs):
        return possible_divs[-1]
    else:
        return 1
