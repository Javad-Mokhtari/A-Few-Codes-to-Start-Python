def gray_code(n):
    if n == 0:
        return ['']
    code1 = graycode(n - 1)
    code2 = code1[::-1]
    for i in range(len(code1)):
        code1[i] = '0' + code1[i]
    for i in range(len(code2)):
        code2[i] = '1' + code2[i]
    return code1 + code2


def main():
    num = int(input('Please enter n:'))
    print(gray_code(num))


if __name__ == "__main__":
    main()
