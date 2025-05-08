#Input the value of terms

n=int(input("Enter the value of terms: "))

sum=0
i=1
while i<=n: #loop will run prom 1 to n
    sum=sum+i
    i=i+1

print("\nsum=",sum)

# The sum over here is 55 if you give n as 10

#INFINITY LOOP

#p=0
#while p<=0:
 #   print("I WILL RUN FOREVER")
#This program will keep on going forever because the conditions can never be met as i is always 0


#armstrong number
#sum of cube of numbers which is equal to the number again is called armstrong number

#step 1:Take input from user
num = int(input("Enter a number :"))

#step 2:initialise sum
sum=0

#step 3:Find the sum of cube of each digit
temp = num
while temp>0:
    digit=temp%10
    sum +=digit **3
    temp//=10\
    
#display the result
if num==sum:
    print(num,"is an armstrong number")

else:
    print(num,"is not an armstrong number")




