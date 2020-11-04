f = open("poems.txt","r")
a = f.read()

if "navneet" in a:
    print("navneet is present in poems.txt file")
else:
    print("navneet is not present in poems.txt file")

f.close()
