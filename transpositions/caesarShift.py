
import os
import sys
import time
import random
import caesarHelper

class Caesar:
    
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


def setupRegular():
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

def automateDecrypt():
    phrase = input("Phrase to decrypt: ")
    for x in range(89):
        decodeRight = Caesar(phrase, x)
        print(decodeRight.shiftRight()+"\n")
        time.sleep(0.3)

def printLetters(inputString, sleep_time=0.03):
    for letter in inputString:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(sleep_time)

def clear(): 
    os.system('cls')

def main():
    method, phrase, shiftLength, shiftDirection = setupRegular()
    if method.upper() == "E":
        encode = Caesar(phrase, shiftLength)
        if shiftDirection.upper() == "R":
            print("\nYour encoded phrase is: {}\n".format(encode.shiftRight()))
        else:
            print("\nYour encoded phrase is: {}\n".format(encode.shiftLeft()))
    else:
        decode = Caesar(phrase, shiftLength)
        if shiftDirection.upper() == "R":
            print("\nYour decoded phrase is: {}\n".format(decode.shiftRight()))
        else:
            print("\nYour decoded phrase is: {}\n".format(decode.shiftLeft()))


if __name__ == "__main__":
    clear()
    printLetters("\nAutomate a decode process? (Y/n) ")
    automate = input("")

    if automate.upper() == "Y":
        printLetters("\nFor Larissa ONLY! Are you Larissa? (Y/n) ")
        larissa = input("")

        if larissa.upper() == "Y":
            caesarHelper.Setup()

        else:
            automateDecrypt()
    else:
        main()

    

    



