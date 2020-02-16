def is_palindrome():
    info = input('Write something: ')
    if info == info[::-1]:
        return 'True'
    else:
        return 'False'

print(is_palindrome())