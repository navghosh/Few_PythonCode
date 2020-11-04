"""You and your friend are going to europe! you have made plans to travel around europe
with your friends, but one thing you need to take into account so that everything goes
according to plan, is that the format of their date is different than from what is used in
the united states. your job is to convert all dates from mm/dd/yyyy to dd/mm/yyyy.
"""

input = input(">>").split()

result = ""

if "/" in input[0]:
    # Removes each "/" to get the month, day, and year separated.
    input[0] = input[0].replace("/", " ")
    # Puts the month, day, and year into an array.
    x = input[0].split()
    # Swaps the month and day positions.
    y, z = x[0], x[1]
    x[0] = z
    x[1] = y
    # Puts each "/" back and joins the day, month, and year into one string.
    for i in range(len(x) - 1):
        x[i] = x[i] + "/"
    for i in x:
        result += i
    print(result)

else:
    # Removes the comma after the day.
    input[1] = input[1].replace(",", "")
    # Replaces the month with it's position on the calendar.
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    for i in range(len(months)):
        if input[0] == months[i]:
            input[0] = str(months.index(months[i]) + 1)
    # Swaps the position of the month and the day.
    y, z = input[0], input[1]
    input[0] = z
    input[1] = y
    # Puts a "/" after the day, month, and year and puts it back into a string.
    for i in range(len(input) - 1):
        input[i] = input[i] + "/"
    for i in input:
        result += i
    print(result)
