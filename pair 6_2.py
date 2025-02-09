ch1 = float(input("vvedit 1 chislo: "))
ch2 = float(input("vvedit 2 chislo: "))

try:
    result = ch1/ch2
    print(result)
except:
    print(f"vi namagalis' podiliti {ch1} na {ch2} i otrimali pomilku")
    if ch2 == 0:
        print("na 0 diliti ne mojna")
else:
    print("end")