def parse_data(filename):
    data = open(filename)
    code = data.readline().split(',')
    data.close()
    for n in range(0,len(code)):
        code[n] = int(code[n])
    return code


def run_code(code,sys_id):
    n = 0
    while n < len(code):
        full_op = "{0:0=6d}".format(code[n]).strip('-')
        opcode = int(str(full_op)[-2:])
        if opcode == 99:
                #print("( STOP",n,")")
                n = len(code)
                break
        mode1 = int(str(full_op)[-3])
        mode2 = int(str(full_op)[-4])
        mode3 = int(str(full_op)[-5])
        if (n+4 <= len(code)):
            p1 = n+1 if mode1 == 1 else code[n+1]
            p2 = n+2 if mode2 == 1 else code[n+2]
            p3 = code[n+3]
            if opcode == 1:
                code[p3] = code[p1] + code[p2]
                n += 4
            if opcode == 2:
                code[p3] = code[p1] * code[p2]
                n += 4
            if opcode == 3:
                code[p1] = sys_id
                n += 2
            if opcode == 4:
                print(code[p1],"",end='')
                n += 2
            if opcode == 5:
                n = code[p2] if code[p1] != 0 else n + 3
            if opcode == 6:
                n = code[p2] if code[p1] == 0 else n + 3
            if opcode == 7:
                code[p3] = 1 if code[p1] < code[p2] else 0
                n += 4
            if opcode == 8:
                code[p3] = 1 if code[p1] == code[p2] else 0
                n += 4


def main():
    intcode = parse_data(r'day05-input.txt')
    sys_id = int(input("enter the system ID to test:"))
    run_code(intcode,sys_id)


if __name__ == "__main__":
    main()