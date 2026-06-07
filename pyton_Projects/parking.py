# user input name, mobile no, car name, car type, parking duration
# output name, car type, price, your car parked for x hours in zeta parking

def user_log(message):
    with open(R"F:\DATA SCIENCE 2\PYTHON\app.log","a") as file:
        file.write(message + "\n")


def rent_counter(duration,vehicle):
    if vehicle.lower() == "bike":
        return duration * 50
    elif vehicle.lower() == "car":
        return duration * 100
    else:
        return "we only park the cars or biks"




user_log("app start")
# Input page
print("========= Welcome To Zeta Parking ===========")
name = input("Enter your Name: ")
mobile_no = input("Enter your Mobile No: ")
vehicle_type = input("Enter your Vehicle Type car/bike: ")
car_type = input("Enter your Car Model: ")
parking_duration = int(input("Enter your Parking Duration: "))
print("=============================================")

message = {"name": name,
           "Mobile No": mobile_no, 
           "Vehicle Type": vehicle_type,
           "Car Model": car_type,
           "Parking Duration": parking_duration
           }
user_log(f'Processed Order: {message}')

# Output page
print("===========================================")
print(f"############## Welcome {name} ##############")
print(f"\tYou parked {vehicle_type}: model : {car_type} \n\tfor {parking_duration} hours")
print(f"\twith Price {rent_counter(parking_duration,vehicle_type)} PKR")
print("===========================================")
user_log("app stoped")




