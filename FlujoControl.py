edad = 6
if edad == 18:
    print ("Mayor de edad")
elif edad < 18:
    print ("Niño")
else:
    print ("Muy viejo")

spam = 0
while spam < 5:
    print ("Hello, world.")
    spam = spam +1

print()

for i in range(5): #[0,1,2,3,4]
    print(f"Will stop at 5! or 4? ({i})")
    
print()

for i in range(3, -2 , 1):
    print(f"Será: ({i})")