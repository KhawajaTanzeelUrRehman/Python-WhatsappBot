import pywhatkit

print(b)
for i in range(len(b)):
    c = str(b[i])
    print(c)
    pywhatkit.sendwhatmsg(f'+923038406887', c, 14, 41)
