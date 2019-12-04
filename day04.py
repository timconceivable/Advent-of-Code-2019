def main():
    part1 = []
    part2 = []
    for number in range(171309,643604):
        num = str(number)                    
        increasing = True
        has_double = False
        single_dub = False
        for i in range(5):
            if int(num[i]) > int(num[i+1]):
                increasing = False
                break
            if num[i] == num[i+1]:
                has_double = True
                if num.count(num[i]) == 2:
                    single_dub = True
        if increasing and has_double:
            part1.append(num)
            if single_dub:
                part2.append(num)
    print("part 1:",len(part1))
    print("part 2:",len(part2))


if __name__ == "__main__":
    main()