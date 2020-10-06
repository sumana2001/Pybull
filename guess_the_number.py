num=random.randint(0,20)
print("enter a number between 0 to 20:")
user_num=int(input())
if(user_num<num):
  print("number is smaller than guessed number")
elif(user_num>num):
  print("number is greater than guessed number")
else:
  print("correct number!!!")
