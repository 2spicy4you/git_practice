"""Random Password Generator"""

from random import choice

length = int(input("Please Specify Password Length: "))

elements = ['1','2','3','4','5','6','7','8','9',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
            'p','q','r','s','t','u','v','w','x','y','z',
            '!','#','$','%','^','&','*']
result = ""

for i in range(length):
  char = choice(elements)
  result += char

print(result)
