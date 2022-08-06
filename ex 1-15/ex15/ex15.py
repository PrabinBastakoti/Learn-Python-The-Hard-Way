from sys import argv
script, filename = argv
#giving filename via argument
txt = open(filename)

print(f"Here's the file {filename}:")
print(txt.read())
txt.close()

print("Type filename again", end=" ")
#giving filename via input()
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()