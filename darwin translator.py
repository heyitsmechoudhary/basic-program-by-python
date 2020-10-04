#it is use for replace all the vowels it a basic darwin translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"



        else:
            translation = translation + letter
    return translation
print(translate(input("enter a phrase : ")))
