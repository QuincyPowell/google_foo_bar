def elimiate_div_and_multiples(div:int, possible_divs:list[int]) -> None:
    multiplyer = 1
    while True:
        current_div = div * multiplyer
        if (not current_div in possible_divs):
            break
        possible_divs.remove(current_div)
        multiplyer += 1

def check_div(div:int, s:str) -> bool:
    div_width = len(s) // div_width
    if (len(s) % div_width != 0):
        return False
    
    for n in range(0, div_width):
        ltr = s[n]
        multiplyer = 1
        while True:
            ptr = (div_width * multiplyer) + n
            if (ptr >= len(s)):
                break
            if(s[ptr] != ltr):
                return False
        return True

def check_div1(s:str) -> bool:
    ltr = s[0]
    for n in range (1, len(s)):
        if (ltr != s[n]):
            return False
    return True
                            
def solution(s:str) -> int:
    if (not s):
        return 0
    if (len(s) == 1):
        return 1
    if (check_div1(s)):
        return 1
    
    possible_divs = range(2, len(s))
    ptr = 0
    while True:
        if (ptr >= len(possible_divs)):
            break
        if (not check_div(possible_divs[ptr], s)):
            elimiate_div_and_multiples(possible_divs[ptr], possible_divs)
        ptr += 1
    
    if (possible_divs):
        return possible_divs[-1]
    else:
        return 1
