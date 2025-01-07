def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d[1:len(d)])


def percent_to_float(p):
    temp="0."+p
    return float(temp[0:len(temp)-1])


main()
