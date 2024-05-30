def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error!"
    else:
        return x / y
    
def expo(x,y):
    return x ** y
    
def calculator():
    while True:
        print("Select Operation: ")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponential")
        print("6. Exit")
        
        choice = input("Enter your choice(1/2/3/4/5/6:)")
        
        if choice in ("1/2/3/4/5"):
            num1 = (float(input("Enter first number:")))
            num2 = (float(input("Enter second number:")))
            
            if choice =='1':
                print(num1,'+',num2,'=',add(num1,num2))
                
            elif choice =='2':
                print(num1,'-',num2,'=',sub(num1,num2))
                
            elif choice =='3':
                print(num1,'*',num2,'=',multiply(num1,num2))
                
            elif choice =='4':
                print(num1,'/',num2,'=',divide(num1,num2))
                
            elif choice =='5':
                print(num1, '**' ,num2, '=',expo(num1,num2))
                
        elif choice =='6':
            print("Exiting the calculator. GOODBYE! Please Continue..")
        else:
            print("You entered the INVALID input.")
            
calculator()