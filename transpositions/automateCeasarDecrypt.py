import ceasarShift as ceasar

with open("output.txt", "w") as f:
    phrase = input("Phrase to decrypt: ")

    for x in range(89):
        decodeRight = ceasar.CeasarShift(phrase, x)
        f.write(decodeRight.shiftRight()+"\n")
