### Read the README.md for the explanation about f-strings. 

age = 10
name = "Tomas"

message1 = f"My name is {name} and I am {age} years old." #This is a f-string, it allows you to use variables inside strings, using {}.
message2 = F"My name is {name} and I am {age} years old." #This is also a f-string, but with an uppercase F, wich is also valid.

message3 = f"My name is {name.upper()} and I am {age + 5} years old." #You can also use functions inside the {}.

messages = message1 + "\n" + message2 + "\n" + message3
print(messages)