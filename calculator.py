def add (a,b):
  return a+b 



def subtract (a,b):
  return a-b


   
def multiply (a,b):
  return a*b



def divide (a,b):
    if b==0:
      return "Error!Division by zero is not allowed"
    else:
        return a/b


def calculator():
    print("select operation:")
    print("1.Addition")
    print("2.Addition")
    print("3.Addition")
    print("4.Divide")

    choice  = input("Enter choice (1/2/3/4)")
    num1=float(input("Enter first number:"))

    num2=float(input("Enter second number:"))


    if choice=='1':
      print(f"The result is: {add(num1,num2)}")

    elif choice=='2':
          print(f"The result is: {subtract(num1,num2)}")

    elif choice=='3':
      print(f"The result is: {multiply(num1,num2)}")

    elif choice=='4':
      print(f"The result is: {divide(num1,num2)}")
 
    else:
     print("Invalide input")
