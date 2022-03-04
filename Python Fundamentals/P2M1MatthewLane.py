#Matthew Lane P2M1 Required
quote = input("Quote: ")
word = ""
for item in quote:
    if item.isalpha():
        word += item
    elif word.lower() >= "h":
        print(word.upper())
        word = ""
    else:
        word = ""

if word.lower() >= "h":
    print(word.upper())
