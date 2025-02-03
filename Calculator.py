def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def sub(a,b):
    return a-b

dic = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul,  
       }


def main(operator,a,b):
    if operator in dic:
        return print(dic[operator](a,b))
    


def new_func():
    return int(input("Enter the first number: "))

first_num = new_func()
second_num = int(input("Enter the second number: "))
op = input("""Enter the opeator you want to chose
           "+"
           "-"
           "*"
           "/"\n
           """)

if op == '+':
    main("+",a = first_num, b = second_num)
    value = add(first_num,second_num)
elif op == '-':
    main("-",a = first_num, b = second_num)
    value = sub(first_num,second_num)
elif op == '*':
    main("*",a = first_num, b = second_num)
    value = mul(first_num,second_num)
elif op == '/':
    main("/",a = first_num, b = second_num)
    value = div(first_num,second_num)
else:
    print("Invalid operator selected")
    
print(f"""Your answer is: {value}""")
music = True
while music:
    ri = input("If you want to continue to work with previous result then enter [Y] and if not enter [N]").lower()
    if ri == 'y':
        
        print(f"The previous answer : {value}")
        Next_num = int(input("Enter your next number: "))
        op = input("""Enter the opeator you want to chose
           "+"
           "-"
           "*"
           "/"\n
           """)
       
        if op == '+':
            main("+",a = value ,b = Next_num)
            value = add(value,Next_num)
        elif op == '-':
            main("-",a = value, b = Next_num)
            value = sub(value,Next_num)
        elif op == '*':
            main("*",a = value, b = Next_num)
            value = mul(value,Next_num)
        elif op == '/':
            main("/",a = value, b = Next_num)
            value = div(value,Next_num)
        else:
            print("Invalid operator selected")

        print(f"""Your answer is: {value}""")
    
    else:
        first_num = int(input("Enter the first number: "))
        second_num = int(input("Enter the second number: "))
        op = input("""Enter the opeator you want to chose
                "+"
                "-"
                "*"
                "/"\n
                """)

        if op == '+':
            main("+",a = first_num, b = second_num)
            value = add(first_num,second_num)
        elif op == '-':
            main("-",a = first_num, b = second_num)
            value = sub(first_num,second_num)
        elif op == '*':
            main("*",a = first_num, b = second_num)
            value = mul(first_num,second_num)
        elif op == '/':
            main("/",a = first_num, b = second_num)
            value = div(first_num,second_num)
        else:
            print("Invalid operator selected")
            
        print(f"""Your answer is: {value}""")