weather_data = {}

def add_weather():
    city = input("Enter city name: ")
    condition = input("Enter weather condition: ")
    temperature = input("Enter temperature: ")
    weather_data[city] = {"condition": condition, "temperature": temperature}
    print("Weather data saved")

def view_weather():
    city = input("Enter city name to view: ")
    if city in weather_data:
        info = weather_data[city]
        print("City:", city)
        print("Condition:", info["condition"])
        print("Temperature:", info["temperature"])
    else:
        print("No weather data for this city")

def main():
    while True:
        print("1. Add Weather Data")
        print("2. View Weather Data")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_weather()
        elif choice == "2":
            view_weather()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
