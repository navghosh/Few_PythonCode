"""you are a secret agent and you receive an encrypted message that needs to be decoded.
the code that is being used flips the message backwards and inserts non-alphabetic characters
in the message to make it hard to decipher."""

msg = input(">> ")
letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')


def func(i):
    for char in i:
        if char not in letters:
            i = i.replace(char, '')
    return i


print(func(msg[::-1]))