#importing random number generator module
import random

#input the name of the questioner
name = "Hanah"

#the question you want to ask the magic 8-ball
question = "Do you like him?"

#initial answer of the magic 8-ball
answer = ""

#variable to store the randomly generated number
random_number = random.randint(1,10)
#print(random_number)

#assigning answer to each number
if random_number == 1:
  answer="Yes - definitely."

elif random_number == 2:
  answer="It is decidedly so."

elif random_number == 3:
  answer="Without a doubt."

elif random_number == 4:
  answer="Reply hazy, try again."

elif random_number == 5:
  answer="Ask again later."

elif random_number == 6:
  answer="Better not tell you now."

elif random_number == 7:
  answer="My sources say no."

elif random_number == 8:
  answer="Outlook not so good."

elif random_number == 9:
  answer="Very doubtful."

elif random_number == 10:
  answer="Lah masalah aku masalah kau."

else:
  answer="Error"

#executing the answers^^
if name !="" and question !="":
  print("---------------------------------------")
  print(name,"asks:",question)
  print("Magic 8-Ball's answer: {}".format(answer))

elif name =="" and question !="":
  print("Question: {}".format(question))
  print("Magic 8-Ball's answer: {}".format(answer))

elif name !="" and question=="":
  print("Please ask me something sire.")
