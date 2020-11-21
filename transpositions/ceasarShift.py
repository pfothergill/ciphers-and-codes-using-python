#!/usr/bin/python3

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
    phrase = input("Phrase to decrypt: ")
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
    youWon = "You figured it out!!!"
    for i in youWon:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(3)
    clear()
    time.sleep(2)
    for letter in decodedPhrase:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.15)
    time.sleep(5)

    # for x in range(len(decodedPhrase)):
    #     clear()
    #     # print(decodedPhrase[:x] + untruePhrase[x:len(untruePhrase)])
    #     random_str = ""
    #     for y in range(len(decodedPhrase)-x):
    #         random_str += decodeRight.getRandomLetter()
    #     print(decodedPhrase[:x] + random_str)
    #     # if decodedPhrase[x] == " ":
    #     #     clear()
    #     #     decryptedText = decodedPhrase[:x] + decodedPhrase[x] + untruePhrase[x+1:len(untruePhrase)]
    #     #     print(decryptedText)
    #     time.sleep(0.2)
    # clear()
    # print(decodedPhrase + '\n')
    # time.sleep(5)


def clear(): 
    os.system('cls')


if __name__ == "__main__":
    automate = input("Automate a decode process? (Y/n) ")
    if automate.upper() == "Y":
        larissa = input("For Larissa ONLY! Are you Larissa? (Y/n) ")
        if larissa.upper() == "Y":
            counter = 0
            while True and counter < 5:
                password = input("\nEnter a password: ")
                try:
                    int(password)
                    print("\nThis password does not contain any numbers!")
                    hint = input("\nWould you like a hint? (Y/n) ")
                    if hint.upper() == "Y":
                        print("\nI tell you that you are ___ all the time...")
                except ValueError:
                    if password.upper() == "BAD":
                        larissaOnly()
                        break
                    elif counter < 4:
                        print("\nThe password is incorrect. Please try again!")
                        time.sleep(0.8)
                        hint = input("\nWould you like a hint? (Y/n) ")
                        if hint.upper() == "Y":
                            print("\nI tell you that you are ___ all the time...")
                        else:
                            print("\nOkay, try again!")
                counter += 1
            if counter == 5:
                print("\n\nToo many incorrect attempts! Try again from the beginning. :)\n")
        else:
            automateDecrypt()
    else:
        main()

    

    



