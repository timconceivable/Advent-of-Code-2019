def main():
    input_data = open(r'day01-input.txt')
    total_1 = 0
    total_2 = 0

    for item in input_data:
        mass = int(item.strip())
        total_1 += mass // 3 - 2
        while mass >= 9:
            fuel = mass // 3 - 2
            total_2 += fuel
            mass = fuel
    input_data.close()
    print("part 1:", total_1)
    print("part 2:", total_2)


if __name__ == "__main__":
    main()