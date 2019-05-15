n = 5
i = 1
goingUp = True
while i > 0:
    toBeWritten = ''

    for j in range(0,i):
        toBeWritten += '*'

    print(toBeWritten)

    if (goingUp):
        i += 1
    else:
        i-=1

    if (i == n):
        goingUp = False
