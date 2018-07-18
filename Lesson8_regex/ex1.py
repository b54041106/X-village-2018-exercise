import re

a = input("input:")
b = input("input:")
c = input("input:")

pattern=r'(?P<first_name>\w\w\w) (?P<last_name>\w\w\w\w)'

match1= re.search(pattern,a)
match2= re.search(pattern,b)
match3= re.search(pattern,c)

print(match1.groupdict())
print(match2.groupdict())
print(match3.groupdict())
