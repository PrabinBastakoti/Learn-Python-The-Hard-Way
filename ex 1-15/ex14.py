from sys import argv
script, first_name, last_name= argv
prompt = '> '
print(f"Hi {first_name} {last_name}, I'm the {script} script. ")
print("I'd like to ask you a few questions.")
print(f"Do you like me {first_name} {last_name}?", end=' ')
likes = input(prompt) # Inside Input is just message shown while running script.


print(f"Where do you live {first_name} {last_name}?",end=' ')
lives = input (prompt)

print("What kind of computer you have?", end = ' ')
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
