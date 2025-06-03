#if else statement
light=input("Enter the color of light::").strip().capitalize()

if light == "Green":
    print("Go")
elif light == "Red":
    print("Stop!")
elif light == "Yellow":
    print("Wait")
else:
    print("Lights are not working !")