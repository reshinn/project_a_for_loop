num=12345  #declare a variable
sum=0      #declare sum as 0
for i in range(len(str(num))): #convert from integer form to string to measure the length
    temp=num%10  #select the last one
    num=num//10  #to fil
    print(num)
    sum+=temp
    print(sum)