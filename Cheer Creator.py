"""You are cheering on your fav team. after each play, if your team got over 10 yards further
down the field, you stand up and give your friend a 'high five'. if they don't move forward by
at least a yard you stay quiet and say 'shh' and if they move fwd 10 yards or less, you say 'Ra!'
for every yard."""


yard = int(input(">> "))
if yard>10:
    print("High Five")

elif yard<1:
    print("shh")

elif yard>=1 and yard<=10:
    print(f"{yard*'Ra!'}")