#!/usr/bin/python3

class cipher:

    def __init__(self, phrase):
        self.phrase = phrase
        self.length = len(phrase)
        self.bracketedWords = []        

    def printPhrase(self):
        return self.phrase

    def validate(self):
        if self.length % 8 == 0:
            return
        else:
            if self.length < 8:
                numDots = 8 - self.length
            else:
                incrementer = 8
                while self.length > incrementer:
                    incrementer += 8
                numDots = incrementer % self.length
            request = input("Is it okay to add {} dots/periods ({}) to your phrase? (Y/n) ".format(numDots, self.phrase + "."*numDots))
            if request.upper() == "N":
                return "Try again and pick a new phrase!"
            self.phrase += "."*numDots
            self.length = len(self.phrase)

    def splitUp(self):
        splitList = list(self.phrase)
        tempWord = ""
        while len(splitList) > 0:
            for x in range(8):
                tempWord += splitList.pop(0)
            self.bracketedWords.append(tempWord)
            tempWord = ""

    def rearrange(self):
        cipherString = ""
        for x in range(len(self.bracketedWords)):
            cipherString += self.bracketedWords[x][7]+self.bracketedWords[x][1:3]+self.bracketedWords[x][4]+self.bracketedWords[x][3]+self.bracketedWords[x][5:7]+self.bracketedWords[x][0]
        return cipherString


while True:
    while True:
        chooseMethod = input("Encode or Decode? (E/d) ")
        if (chooseMethod.upper() == "E") or (chooseMethod.upper() == "D"):
            break
        else:
            print("Please choose a valid method! Try Again.")
    if chooseMethod.upper() == "E":
        phrase = input("\nDecrypted Phrase: ")
        try:
            int(phrase)
        except ValueError:
            runCipher = cipher(phrase)
            runCipher.validate()
            runCipher.splitUp()
            print("\nDecrypted Phrase: {}".format(runCipher.printPhrase()))
            print("Encrypted Phrase: {}".format(runCipher.rearrange()))
    elif chooseMethod.upper() == "D":
        phrase = input("Encrypted Phrase: ")
        try:
            int(phrase)
        except ValueError:
            runCipher = cipher(phrase)
            runCipher.splitUp()
            print("\nEncrypted Phrase: {}".format(runCipher.printPhrase()))
            print("Decrypted Phrase: {}".format(runCipher.rearrange()))
    break
    print("Try again.")



