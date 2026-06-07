vehicles = ['car','bike']


print("Fill the slip about your Vehicle")


v_no = input("Enter Vehicle No: ")
v_type = input("Enter vehicle type: ")
if v_type in vehicles:
    v_p_time = int(input("Enter parking hours: "))

if v_type.lower() in vehicles[0]:
    charge = v_p_time * 100
    print(charge)
elif v_type.lower() in vehicles[1]:
    charge = v_p_time * 50
    print(charge)
else:
    print("Invalid input")

print("-------------PARKING SLIP-----------")
print(f"\tVEHICLE NO    : {v_no}")
print(f"\tVEHICLE TYPE   : {v_type}")
print(f"\tPARKING HOURS : {v_p_time}")
print(f"\tTOTAL CHARGES : {charge}")
print("------------------------------------")

