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
        if n == i:
            full_op = "{0:0=5d}".format(code[n])
            print(n,full_op)
            opcode = int(str(full_op)[-2:])
            mode1 = int(str(full_op)[-3])
            mode2 = int(str(full_op)[-4])
            mode3 = int(str(full_op)[-5])
            if opcode == 99:
                print(n,"- STOP")
                break
            else:
                if (opcode <= 2) and (n+4 <= len(code)):
                    p1 = code[n+1]
                    if mode1 == 0: 
                        p1 = code[code[n+1]]
                    p2 = code[n+2]
                    if mode2 == 0: 
                        p2 = code[code[n+2]]
                    p3 = code[n+3]
                    if mode3 == 0: 
                        p3 = code[code[n+3]]
                    #print(n,code[n],"params:",mode1,":",p1,mode2,":",p2,mode3,":",p3)
                    if opcode == 1:
                        p3 = p1 + p2
                        #print(n,code[n],"- op1:",full_op)
                        i += 4
                    if opcode == 2:
                        p3 = p1 * p2
                        #print(n,code[n],"- op2:",full_op)
                        i += 4
                elif (n+2 <= len(code)):
                    p1 = code[n+1]
                    if opcode == 3:
                        code[p1] = sys_id
                        #print(n,code[n],"- op3:",full_op)
                        i += 2
                    if opcode == 4:
                        #print(n,code[n],"- op4:",full_op," - output:",code[p1])
                        print(code[p1])
                        i += 2
    return code[0]


def main():
    intcode = parse_data(r'C:\Users\Tim Conceivable\CODE\Advent-of-Code-2019\day05-input.txt')
    sys_id = 1 #int(input("please enter the ID of the system to test:"))
    diagnostic = run_code(intcode,sys_id)
    #print(diagnostic)

if __name__ == "__main__":
    main()