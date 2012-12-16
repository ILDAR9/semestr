def decode(code, dict):
    start = 0
    length = 1
    ans = ''
    while (start < len(code)):
        temp = code[start:start + length]
        if (temp in dict):
            ans = ans + (str(dict[temp]) + " ")
            start = start + length
            length = 1
        else:
            length = length + 1
    return ans
#print decode('1001110100100001',{'11': 34, '01': 43, '001': 50, '000': 90, '100': 10, '101': 235})