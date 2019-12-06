def parse_data(filename):
    data = open(filename)
    code = data.readline().split(',')
    data.close()
    for n in range(0,len(code)):
        code[n] = int(code[n])
    #print(code)
    return code


def run_code(code):
    for n in range(0,len(code)):
        opcode = code[n]
        if (n % 4 == 0) and (n+4 <= len(code)):
            if opcode == 99:
                #print(n,"OPCODE :",val,"/ STOP")
                break
            p1 = code[n+1]
            p2 = code[n+2]
            p3 = code[n+3]
            if opcode == 1:
                code[p3] = code[p1] + code[p2]
                #print(n,"OPCODE :",code[p1],"+",code[p2])
            if opcode == 2:
                code[p3] = code[p1] * code[p2]
                #print(n,"OPCODE :",code[p1],"x",code[p2])
        else:
            pass #print(n,":",val)    
    return code[0]


def main():
    for noun in range(100):
        for verb in range(100):
            intcode = parse_data(r'day02-input.txt')
            intcode[1] = noun
            intcode[2] = verb
            alarm = 100 * noun + verb
            address_0 = run_code(intcode)
            if address_0 == 19690720:
                #print("noun:",noun,"verb:",verb)
                break
            else:
                if alarm == 1202:
                    print("part 1:",address_0)
                #print("nope")
        if address_0 == 19690720:
            print("part 2:",alarm)
            break

if __name__ == "__main__":
    main()