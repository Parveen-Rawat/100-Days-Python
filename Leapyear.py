def is_leap_year(year):
    if year % 4 == 0:
        if year%100 ==0:
            if year%400 ==0:
                return "Leap year"
            else:
                return "Not a leap year"
        else:
            return "leap year"
    else:
        return "Not a leap year"
        

print(is_leap_year(int(input("Enter the year in numbers "))))