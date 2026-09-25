### Read the README.md for the complete explanation about f-strings. 
### Each format specifiers are specified inside {}, richt next to the variable indicator. Using this structure: {var:(Here we specify the format options we desire)}.
### We have 4 specifiers that follow the following order:

x = "Format Specified"

### 1. Flags: modifies the allignment and padding.

print(f"{x:>}")   # right aligned
print(f"{x:<}")   # left aligned
print(f"{x:^}")   # centered
print(f"{x:0>}")  # fill with zeros on the left