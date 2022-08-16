
num1=int(input("aswin enter a number1:"))
print(num1)

num2=int(input("aswin enter a number2:"))
print(num2)
replace1=""
print("these are the operator you can use:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication ")
print("4. Division")
print("5. Modulus")
result=0
operator=input("please choose an option from these (1,2,3,4,5):")
if operator == "1":
    replace1="addition"
    result=num1+num2
if operator == "2":
    if num1<num2:
        print("cannot calculate")
    else:
     result=num1-num2
    print("the result of substraction of",num1, "and",num2,"is",result)
if operator=="3":
    if num2==0 or num1==0:
        print("cannot multiply by zero")
    else:
        result=num1*num2
        print("The result of multiplication of ",num1,"and",num2,"is",result)
if operator=="4":
      if num2==0:
          print("cannot divide")
      else:
             result=num1//num2
             print("The result of division of",num1,"and",num2,"is",result)
if operator=="5":
    replace1="modulus"
    result=num1%num2
    print("The result of modulus of",num1,"and",num2,"is",result)


