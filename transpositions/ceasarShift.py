
import os
import sys
import time
import random

class CeasarShift:
    
    def __init__(self, phrase, shiftLength):
        self.phrase = phrase
        self.alphaNumerics = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
                                "j", "k", "l", "m", "n", "o", "p", "q", "r", 
                                "s", "t", "u", "v", "w", "x", "y", "z", " ", 
                                "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                ".", ",", "!", "@", "#", "$", "%", "^", "&",
                                "*", "(", ")", "-", "_", "+", "=", "<", ">",
                                "{", "}", "[", "]", "'", "/", ":", ";", "?",
                                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.shiftLength = shiftLength

    def getRandomLetter(self):
        return random.choice(self.alphaNumerics)

    def shiftRight(self):
        cipherText = ""
        for char in self.phrase:
            index = self.alphaNumerics.index(char)
            newCharPosition = index + self.shiftLength
            if newCharPosition >= 89:
                newCharPosition -= 89
            cipherText += self.alphaNumerics[newCharPosition]
        return cipherText

    def shiftLeft(self):
        cipherText = ""
        for char in self.phrase:
            index = self.alphaNumerics.index(char)
            cipherText += self.alphaNumerics[index - self.shiftLength]
        return cipherText


def setup():
    while True:
        method = input("Encrypt or Decrypt? (E/d) ")
        if (method.upper() == "E") or (method.upper() == "D"):
            break
        else:
            print("Please choose either ENCRYPT (E) or DECRYPT (D)!")
    while True:
        if method == "E":
            method_literal = "encrypt"
        else:
            method_literal = "decrypt"
        phrase = input("Phrase to {}: ".format(method_literal))
        if phrase != "":
            break
    while True:
        shiftLength = input("Shift length: (int value > 0) ")
        try:
            int(shiftLength)
            if int(shiftLength) <= 89:
                shiftLength = int(shiftLength)
                break
        except ValueError:
            print("Please choose an INTEGER value")
    while True:
        shiftDirection = input("Shift right or shift left? (R/l) ")
        if (shiftDirection.upper() == "R") or (shiftDirection.upper() == "L"):
            break
        else:
            print("Please choose to shift either RIGHT (R) or LEFT (L)!")
    return method, phrase, shiftLength, shiftDirection

def main():
    method, phrase, shiftLength, shiftDirection = setup()
    if method.upper() == "E":
        encode = CeasarShift(phrase, shiftLength)
        if shiftDirection.upper() == "R":
            print("\nYour encoded phrase is: {}\n".format(encode.shiftRight()))
        else:
            print("\nYour encoded phrase is: {}\n".format(encode.shiftLeft()))
    else:
        decode = CeasarShift(phrase, shiftLength)
        if shiftDirection.upper() == "R":
            print("\nYour decoded phrase is: {}\n".format(decode.shiftRight()))
        else:
            print("\nYour decoded phrase is: {}\n".format(decode.shiftLeft()))


def automateDecrypt():
    phrase = input("Phrase to decrypt: ")
    for x in range(89):
        decodeRight = CeasarShift(phrase, x)
        print(decodeRight.shiftRight()+"\n")
        time.sleep(0.3)


def larissaOnly():
    printLetters("\nPhrase to decrypt: ")
    phrase = input("")
    print('\n')
    for x in range(89):
        decodeRight = CeasarShift(phrase, x)
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

def printLetters(inputString, sleep_time=0.03):
    for letter in inputString:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(sleep_time)


def clear(): 
    os.system('cls')


if __name__ == "__main__":
    printLetters("\nAutomate a decode process? (Y/n) ")
    automate = input("")
    if automate.upper() == "Y":
        printLetters("\nFor Larissa ONLY! Are you Larissa? (Y/n) ")
        larissa = input("")
        if larissa.upper() == "Y":
            counter = 0
            while True and counter < 5:
                printLetters("\nEnter a password: ", 0.01)
                password = input("")
                try:
                    int(password)
                    printLetters("\nThis password does not contain any numbers!\n")
                    printLetters("\nWould you like a hint? (Y/n) ")
                    hint = input("")
                    if hint.upper() == "Y":
                        printLetters("\nI tell you that you are ___ all the time...\n")
                except ValueError:
                    if password.upper() == "BAD":
                        while True:
                            printLetters("\nWhat is the 3 letter month & 2 digit day of my birthday? (Example: Jan 01) Do not include year: ", 0.02)
                            birthStuff = input("")
                            try:
                                birthMonth, birthDay = birthStuff.split()
                                if birthMonth.upper() == "AUG" and birthDay == "15":
                                    while True:
                                        printLetters("\nWhat is my favorite programming language? ")
                                        language = input("")
                                        if language.upper() == "PYTHON":
                                            while True:
                                                printLetters("\nWhat is my favorite number? ")
                                                favNumber = input("")
                                                try:
                                                    int(favNumber)
                                                    if int(favNumber) == 9:
                                                        larissaOnly()
                                                        break
                                                    else:
                                                        printLetters("\nIncorrect. I don't think I've ever told you this but what better way to learn? :) Would you like a hint? (Y/n) ")
                                                        hint2 = input("")
                                                        if hint2.upper() == "Y":
                                                            printLetters("\nThe way you pronounce this number in English has a meaning in the German language. Good luck. You're almost there!\n")
                                                        else:
                                                            printLetters("\nAlrighty then...\n")
                                                except ValueError:
                                                    printLetters("\nIt's a number not a word. Duh.\n")
                                            break
                                        else:
                                            printLetters("\nReally...This one should be easy...\n")
                                    break
                                else:
                                    printLetters("\nIncorrect. Think harder and try again!\n")
                            except ValueError:
                                printLetters("\nThis should be a month (ex: Jan) followed by a space and then a 2 digit day (ex: 01). After you type both of these, and only after, press enter! (ex: Jan 01 --> press enter)\n", 0.02)
                        break
                    elif counter < 4:
                        printLetters("\nThe password is incorrect. Please try again!\n")
                        time.sleep(0.3)
                        printLetters("\nWould you like a hint? (Y/n) ")
                        hint = input("")
                        if hint.upper() == "Y":
                            printLetters("\nI tell you that you are ___ all the time...\n")
                        else:
                            printLetters("\nOkay, try again!\n")
                counter += 1
            if counter == 5:
                printLetters("\n\nToo many incorrect attempts! Try again from the beginning. :)\n", 0.1)
        else:
            automateDecrypt()
    else:
        main()

    

    



