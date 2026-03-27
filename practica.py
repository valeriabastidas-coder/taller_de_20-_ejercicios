def cangrejo(a, b):
    #a es edad
    #b es tipode sangre
    
    if a >= 18 and a <= 28:
        if b == "A":
            return True
    return False

print("el chico no1", cangrejo(19, "A"))
print("el chico no2", cangrejo(17, "A"))
print("el chico no3", cangrejo(20, "AB"))
print("el chico no4", cangrejo(16, "A"))
print("el chico no5", cangrejo(18, "AB"))
print("el chico no6", cangrejo(25, "A"))

