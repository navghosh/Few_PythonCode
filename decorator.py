def div(a,b):
    print(a/b)

def smart_div(x):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return x(a,b)
    return inner

new_div = smart_div(div)
new_div(3,9)