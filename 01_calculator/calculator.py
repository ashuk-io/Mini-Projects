a = input ( "Enter first number: " ) 
b = input ( "Enter second number: " ) 

operation = input ( "Enter operation (+, -, *, /): " )

if a == 'quit' or b == 'quit' or operation == 'quit':
    print("Exiting the calculator...")
    exit()

elif a =='':
    a = 0
elif b =='':
    b = 0

a = float(a)
b = float(b)


while True:
    match(operation):
        case "+":
            print ( f"Result: {a + b}" )
            break
        case "-":
            print ( f"Result: {a - b}" )
            break
        case "*" | "x":
            print ( f"Result: {a * b}" )
            break
        case "/":
            if b != 0:
                print ( f"Result: {a / b}" )
            else:
                print ( "Error: Division by zero is not allowed." )
            break
        case '^':
            print ( f"Result: {a ** b}" )
            break
        case '%':
            print(f'Result : {a%b}')
            break
        case '//':
            print (f'Result :{a//b}')
            break
        case 'quit':
            print("Exiting the calculator...")
            break
        case _:
            operation = input ( "Invalid operation. Please enter one of (+, -, *, /): " )
