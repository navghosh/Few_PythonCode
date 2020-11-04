import pyautogui as p
import time
import webbrowser as w
import re

opn = open(r"C:\Users\pc\Desktop\cond.txt",'r').read()
s1 = re.search('s =(.+)',opn).group(1)
s2 = re.search('c =(.+)',opn).group(1)
s3 = re.search('x =(.+)',opn).group(1)
s4 = re.search('y =(.+)',opn).group(1)
s = int(s1)
c = int(s2)
x = s3
y = s4
msg = "The message '%s' will be sent to '%s' at %s:%s" %(y,x,s,c)
print(msg)
q = s

if (s == 00):
    q = 24

if (c == 00):
    c = 60
    s = q-1

while True:
    l = time.localtime(time.time())
    if(l.tm_hour == s)&(l.tm_min == c-1):
        w.open('https://web.whatsapp.com/send?phone='+x+'&text='+y)
        time.sleep(60)
        p.press('enter')
        break;
    else:
        opn = open(r"C:\Users\pc\Desktop\cond.txt",'r')
        cond = opn.read()
        if (cond == "break"):
            break