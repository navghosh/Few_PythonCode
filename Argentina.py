"""you are in a hat store in argentina. the prices are listed in US Dollars and Argentina Pesos.
you have both, but you want to make sure you pay the lower price!.
do you pay in dollars or pesos? the exchange rate is 2 cents for every peso.

Create a program that takes two prices and tells you which one is lower after conversion

two integer values, first one is in pesos and second in dollars."""

pesos = float(input("enter your pesos value: "))
dollars = float(input("enter your dollar value: "))

payment = dollars*50

if payment<pesos:
    print(f"{dollars} dollars")
else:
    print(f"{pesos} pesos")