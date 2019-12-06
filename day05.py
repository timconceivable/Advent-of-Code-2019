def parse_data(filename):
    data = open(filename)
    code = data.readline().split(',')
    data.close()
    for n in range(0,len(code)):
        code[n] = int(code[n])
    return code


def run_code(code,sys_id):
    i = 0
    for n in range(0,len(code)):
        full_op = "{0:0=6d}".format(code[n]).strip('-')
        opcode = int(str(full_op)[-2:])
        if opcode == 99:
                print("!") #(n,"- STOP")
                break
        mode1 = int(str(full_op)[-3])
        mode2 = int(str(full_op)[-4])
        mode3 = int(str(full_op)[-5])
        if n == i and (n+2 <= len(code)):
            p1 = code[n+1]
            if mode1 == 1:
                p1 = n+1
            if (opcode > 2):
                if opcode == 3:
                    code[p1] = sys_id
                    i += 2
                if opcode == 4:
                    print(code[p1],"",end='')
                    i += 2
            elif (n+4 <= len(code)):
                p2 = code[n+2]
                if mode2 == 1:
                    p2 = n+2
                p3 = code[n+3]
                if opcode == 1:
                    code[p3] = code[p1] + code[p2]
                    i += 4
                if opcode == 2:
                    code[p3] = code[p1] * code[p2]
                    i += 4
    return code[0]


def main():
    intcode = parse_data(r'C:\Users\Tim Conceivable\CODE\Advent-of-Code-2019\day05-input.txt')
    sys_id = 1 #int(input("please enter the ID of the system to test:"))
    diagnostic = run_code(intcode,sys_id)
    #print(diagnostic)


if __name__ == "__main__":
    main()