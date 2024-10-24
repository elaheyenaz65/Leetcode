def isunique(data: str) -> bool:
    if len(data) > 128:  # assuming ASCII
        return False
    a = 0
    
    for ch in data:
        num = ord(ch)
        temp = 1 << num
        if a & temp:  # if the bit is already set
            return False
        a |= temp  # set the bit for the current character
    return True

if __name__ == '__main__':  # corrected
    print(isunique('abcdef'))
