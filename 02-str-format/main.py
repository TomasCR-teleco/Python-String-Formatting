### Read the README.md for the explanation about f-strings. 
age = 10
name1 = "Tomas"

message1 = "we are: {0}, and {1}, and we are {2} years old".format(name1, "John", age) #This is a string that uses the format() method, which allows you to insert variables into strings using {} and specifying their order with numbers.

message2 = "we are: {0}, and {1}, and we are {2} years old".format(name1.upper(), "John".lower(), age + 5) #You can also use functions inside the {}.

messages = message1 + "\n" + message2
print(messages)