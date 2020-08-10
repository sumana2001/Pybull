# print all positive numbers in a range
def fibonacci(num):
    n1=0
    n2=1
    count=0
    if num<=0:
        print("Enter a positive number")
    elif num==1:
        print(n1)
    else:
        while count<num:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1



if __name__ == "__main__":
    n = int(input("Enter a number : "))
    fibonacci(n)
