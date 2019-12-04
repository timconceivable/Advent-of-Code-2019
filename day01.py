def calc_fuel(mass):
    return mass // 3 - 2


def calc_extra_fuel(mass, fuel_sum):
    fuel = calc_fuel(mass)
    if fuel > 0:
        fuel_sum += fuel
        return calc_extra_fuel(fuel, fuel_sum)
    else:
        return fuel_sum


def main():
    input_data = open(r'day01-input.txt')
    total_1 = 0
    total_2 = 0
    for item in input_data:
        mass = int(item.strip())
        #print(mass)
        total_1 += calc_fuel(mass)
        total_2 += calc_extra_fuel(mass, 0)
    input_data.close()
    print("part 1:", total_1)
    print("part 2:", total_2)


if __name__ == "__main__":
    main()