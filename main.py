### Import tkinter Library
from tkinter import Tk

### Code
string = input("String: ")
print("\nInput String: " + string)

print("\nReplacing spaces with \", \"")
string = string.replace(" ", ", ")
print(string)

print("\nReplacing \"_\" with \" \":")
string = string.replace("_", " ")
print(string)


print("\nFinal string: " + string)

print("\n\nCopying string to clipboard...")
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(string)
r.update()
if r.clipboard_get() == string:
    print("Successfully copied to clipboard")
else:
    print("bruh")