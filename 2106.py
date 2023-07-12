
def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome('лепсспел'))

x = input('введите слово:')

def palindromss(x):
    return x[::-1] == x
while True:
    if palindromss(x):
        print(f'{x} "это палиндромом"')
        break
    else:
        print("Это не полиндромом")
        break
