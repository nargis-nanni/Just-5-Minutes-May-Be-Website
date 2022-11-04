import time
import pyaudio
import pyttsx3

def TaskExe():
    speak("hello,i am quiz.")
    speak("how Can i help you?") 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",180)    


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

n=("Welcome to the Simple Quiz Game!")
time.sleep(1)
print(n)
speak(n)



#Chances
chances = 1
n=("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)
print(n)
speak(n)

#Score
score = 0

#question number 1
question_1 = n= ("1) what is the base language of python?\n(a) JSS\n(b) C \n(c) C++\n(d) PHP\n\n ")
answer_1 = "c"
print(n)
speak(n)


for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Execlent.\n")
       
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)


#question number 2
question_2 = n=("2) who is the father of python?\n(a)Guido van Rossum \n(b) james gosling\n(c) Larry page\n(d) Just Van Ross \n\n ")
answer_2 = "a"
print(n)
speak(n)

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Great.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)



#question number 3
question_3 = n=("3) how many reserve keywords in python ?\n(a) 67\n(b) 33\n(c) 107\n(d) 95\n(e) 81\n(f) 62\n\n ")
answer_3 = "b"
print(n)
speak(n)


for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)

#question number 4
question_4 = n=("4) when python language was invented ?\n(a) January21,1919\n(b) Feruary17,1876\n(c) February 20,1991\n(d) March17,2004\n\n ")
answer_4 = "c"
speak(n)
print(n)

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! VeryGood.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)



#question number 5
question_5 = n=("5) Wwen was python 3 version invented ?\n(a) December 1,2008\n(b) December 2,2008\n(c) December 5,2008\n(d) December3,2008\n\n ")
answer_5 = "d"
print(n)
speak(n)

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Outstanding.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_5, "\n\n")

time.sleep(1)


#print the score
while score >= 4:
    n=("Well done! Your score was", score)
    print(n)
    speak(n)
    break

while score <= 3:
    n=("Better luck next time! Your score was", score)
    print(n)
    speak(n)

    break
#Goodbye message
n=("Thank you for playing the Simple Quiz Game!") 
print(n)
speak(n)
