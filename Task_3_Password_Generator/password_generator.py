from random import randint

characters_count = int(input('Enter count of symbols:'))
generated_password = ""
while len(generated_password) < characters_count:
    generated_password += chr(randint(33, 127))

print(generated_password)

