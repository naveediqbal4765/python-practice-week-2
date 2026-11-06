# A safe number. Write to_int(text) that returns the text as a whole number, 
# or None if it isn't one. Test it with "42", " 7 ", "4.5", "abc" and "". Which ones surprised you?

def to_int(text):
    return int(text)

textList = ["42", " 7 ", "4.5", "abc" , ""]

for x in textList:
    try:
        print(to_int(x))
    except:  # noqa: E722
        print(f"{x} is not a whole number")