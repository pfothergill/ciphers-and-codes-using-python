import os
import sys
import time
import random
from caesarShift import printLetters as printLetters
from caesarShift import Caesar as Caesar
from caesarShift import clear as clear

class Setup:
    def __init__(self):
        self.counter = 0
        self.password_hint = ["This password does not contain any numbers! It is ONE word!", 
                            "I tell you that you are ___ all the time...",
                            "It starts with the letter B.",
                            "It rhymes with mad, sad, or rad."]
        self.question1_hint = ["This should be a month (ex: Jan) followed by a space and then a 2 digit day (ex: 01). After you type both of these, and only after, press enter! (ex: Jan 01 --> press enter).",
                            "Ask someone who would know! (you do have my mom's number)",
                            "I'm disappointed but I will tell you that the month is August.",
                            "It's in the middle of August."]
        self.question2_hint = ["It's one of the most popular languages for Machine Learning (google it)",
                            "There is a species of snake with the same name",
                            "Really...This one should be easy...",
                            "What is a keyword that we used while searching for jobs at Principal?"]
        self.question3_hint = ["It's a single-digit integer",
                            "What two whole, positive numbers that have a one-digit answer when multiplied and a two-digit answer when added? My favorite number is the greater of the two.",
                            "What is the last digit of my gmail address before the @gmail.com",
                            "If you flip this number upside-down, it equals a different number"]
        self.finalQuestion_hint = ["It's located on the North-side of Ottumwa.",
                                "I went to Eisenhower Elementary",
                                "The street is located near Northgate Pizza Hut",
                                "The street is between Northgate St. & W. Rochester Rd."]
        self.run()
    
    def run(self):
        errorCode = "\nYou exceeded the maximum number of attempts. Please try again.\n"
        if self.password() == 0:
            printLetters(errorCode)
            return
        if self.question1() == 0:
            printLetters(errorCode)
            return
        if self.question2() == 0:
            printLetters(errorCode)
            return
        if self.question3() == 0:
            printLetters(errorCode)
            return
        if self.finalQuestion() == 0:
            printLetters(errorCode)
            return
        clear()
        forYourEyesOnly()

    def password(self):
        currQuestionCounter = 0
        clear()
        while True and self.counter < 5:
            if self.counter >= 1:
                printLetters("\nAttempts remaining: {}\n".format(5-self.counter))
            printLetters("\nEnter a password: ", 0.01)
            password = input("")
            if password.upper() == "BAD":
                printLetters("\nCorrect!!!\n", 0.06)
                time.sleep(2)
                return 1  
            elif self.counter == 4:
                return 0
            
            printLetters("\nIncorrect. Would you like a hint? (Y/n) ")
            hint = input("")
            
            if hint.upper() == "Y":
                printLetters("\n{}\n".format(self.password_hint[currQuestionCounter]))
            self.counter += 1
            currQuestionCounter += 1

    def question1(self):
        clear()
        currQuestionCounter = 0
        while True and self.counter < 5:
            if self.counter >= 1:
                printLetters("\nAttempts remaining: {}\n".format(5-self.counter))
            printLetters("\nWhat is the 3 letter month & 2 digit day of my birthday? (Example: Jan 01) Do not include year: ", 0.018)
            birthStuff = input("")
            try:
                birthMonth, birthDay = birthStuff.split()
                if birthMonth.upper() == "AUG" and birthDay == "15":
                    printLetters("\nCorrect!!!\n", 0.06)
                    time.sleep(2)
                    return 1                    
            except ValueError:
                pass
            if self.counter == 4:
                return 0
            printLetters("\nIncorrect. Would you like a hint? (Y/n) ")
            hint = input("")                    
            if hint.upper() == "Y":
                printLetters("\n{}\n".format(self.question1_hint[currQuestionCounter]))
            self.counter += 1
            currQuestionCounter += 1

    def question2(self):
        clear()
        currQuestionCounter = 0
        while True:
            if self.counter >= 1:
                printLetters("\nAttempts remaining: {}\n".format(5-self.counter))
            printLetters("\nWhat is my favorite programming language? ")
            language = input("")
            if language.upper() == "PYTHON":
                printLetters("\nCorrect!!!\n", 0.06)
                time.sleep(2)
                return 1  
            else:
                if self.counter == 4:
                        return 0
                printLetters("\nIncorrect. Would you like a hint? (Y/n) ")
                hint = input("")                    
                if hint.upper() == "Y":
                    printLetters("\n{}\n".format(self.question2_hint[currQuestionCounter]))
            self.counter += 1
            currQuestionCounter += 1

    def question3(self):
        clear()
        currQuestionCounter = 0
        while True:
            if self.counter >= 1:
                printLetters("\nAttempts remaining: {}\n".format(5-self.counter))
            printLetters("\nWhat is my favorite number? ")
            favNumber = input("")
            try:
                int(favNumber)
                if int(favNumber) == 9:
                    printLetters("\nCorrect!!!\n", 0.06)
                    time.sleep(2)
                    return 1
                else:
                    if self.counter == 4:
                        return 0
                    printLetters("\nIncorrect. Would you like a hint? (Y/n) ")
                    hint = input("")                    
                    if hint.upper() == "Y":
                        printLetters("\n{}\n".format(self.question3_hint[currQuestionCounter]))
            except ValueError:
                printLetters("\nIt's a number not a word. Duh.\n")
                printLetters("\nWould you like a hint? (Y/n) ")
                hint = input("")                    
                if hint.upper() == "Y":
                    printLetters("\n{}\n".format(self.question3_hint[currQuestionCounter]))
            self.counter += 1
            currQuestionCounter += 1
    
    def finalQuestion(self):
        clear()
        currQuestionCounter = 0
        while True:
            if self.counter >= 1:
                printLetters("\nAttempts remaining: {}\n".format(5-self.counter))
            printLetters("\nWhile growing up, on what street was my first home located? ")
            street = input("")
            if street.split()[0].upper() == "BRYAN":
                printLetters("\nCorrect!!! Very nice. Now ya know :)\n", 0.06)
                time.sleep(2)
                return 1
            else:
                if self.counter == 4:
                    return 0
                printLetters("\nIncorrect. Would you like a hint? (Y/n) ")
                hint = input("")                    
                if hint.upper() == "Y":
                    printLetters("\n{}\n".format(self.finalQuestion_hint[currQuestionCounter]))
            self.counter += 1
            currQuestionCounter += 1
            
def printOutMessage(myString):
    myStringList = myString.split()
    letterSpeed = 0.06
    punctionSpeed = 0.17
    commaSpeed = 0.1
    enterSpeed = 0.75
    emoticonSpeed = 0.3
    for i in myStringList:
        if i.isupper() and len(i) > 1:
            printLetters(i + " ", letterSpeed + 0.5)
        elif i == ":)":
                for x in i:
                    printLetters(x, letterSpeed)
                    time.sleep(emoticonSpeed)
        elif i[len(i)-3:len(i)] == "...":
            letterSpeed = 0.1
            punctionSpeed = 0.22
            commaSpeed = 0.13
            enterSpeed = 1
            emoticonSpeed = 0.8
            for x in i:
                if x == ".":
                    printLetters(x, letterSpeed)
                    time.sleep(1)
                else:
                    printLetters(x, letterSpeed)
            
            printLetters(" ", 0.06)
        else:
            printLetters(i + " ", letterSpeed)
            if i[len(i)-1] == "!" or i[len(i)-1] == ".":
                time.sleep(punctionSpeed)
            elif i[len(i)-1] == ",":
                time.sleep(commaSpeed)
        if i[len(i)-1] == ":":
            printLetters('\n', enterSpeed)
            printLetters('\n', enterSpeed)
    print("\n")
    printLetters("\n\nPress ENTER to exit. There might be a delay but it'll exit!")
    input("")

def forYourEyesOnly():
    printLetters("\nPhrase to decrypt: ")
    phrase = input("")
    print('\n')
    for x in range(89):
        decodeRight = Caesar(phrase, x)
        if x < 87 and x != 62:
            # clear()
            print(decodeRight.shiftRight()+"\n")
            time.sleep(0.3)
        else:
            decodedPhrase = decodeRight.shiftRight() + '\n'
    clear()
    time.sleep(3)
    printLetters("You figured it out!!!")
    time.sleep(3)
    clear()
    time.sleep(2)
    printOutMessage(decodedPhrase)
    time.sleep(5)