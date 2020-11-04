message = input(">> ")
letters = list('QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm ')


def function(x):
    for char in x:
        if char not in letters:
            x = x.replace(char, '')
    return x


print(function(message[::-1]))
