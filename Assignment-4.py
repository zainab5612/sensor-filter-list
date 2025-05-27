"""
Assigment 4: Creating a Sensor List and Filter List
Submitted by Zainab Abdulhasan
Submitted: October 13, 2024

Assignment 3: Implementing a Menu

Assignment 2: This assignment adds code to prompt the user for a temperature in Celsius and
then converts that temperature to a specified different temperature unit.

Assigment 1: This program demonstrates printing lines of text to the screen
"""


def print_header():
    """
    This function prints the title and name at the top of the program.
    """
    print("STEM Center Temperature Project")
    print("Zainab Abdulhasan")  # Changed the name to Mike Murphy


def convert_units(celsius_value, units):
    """
    This function converts temperature from Celsius to either Fahrenheit or Kelvin,
    depending on the choice.

    arguments:
    celsius_value (float): The temperature in Celsius
    units (int): The units to convert to (0 = no conversion, 1 = Fahrenheit, 2 = Kelvin).

    Returns:
    float: The converted temperature, or None if it is an invalid input.
    """
    if units == 0:
        return int(celsius_value)
    elif units == 1:
        return float((celsius_value * 9 / 5) + 32)
    elif units == 2:
        return float(celsius_value + 273.15)
    else:
        return None


def print_menu():
    """
    This function prints the main menu options for the user to choose from.
    """
    print("""
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
""")


def new_file(dataset=None):
    """
    Placeholder function for when we need to process a new data file.
    """

    print("New File Function Called, dataset:", dataset)

def choose_units():
    """
    Placeholder function for choosing units (like Fahrenheit or Celsius).
    """

    print("Choose Units Function Called")

def change_filter(sensor_list=None, active_sensors=None):
    """
    Placeholder function to change the filter for room sensors.
    """

    print("Change Filter Function Called, sensor_list:", sensor_list, "active_sensors:", active_sensors)

def print_summary_statistics(dataset=None, active_sensors=None):
    """
    Placeholder function for printing summary stats about sensor data.
     """

    print("Summary Statistics Function Called, dataset:", dataset, "active_sensors:", active_sensors)

def print_temp_by_day_time(dataset=None, active_sensors=None):
    """
    Placeholder function to show temperature data by day and time.
    """

    print("Print Temp by Day/Time Function Called, dataset:", dataset, "active_sensors:", active_sensors)

def print_histogram(dataset=None, active_sensors=None):
    """
    Placeholder function to print a histogram of temperatures.
    """

    print("Print Histogram Function Called, dataset:", dataset, "active_sensors:", active_sensors)


def test_sensors(sensors, sensor_list, filter_list):
    """
    This function checks if the sensors, sensor_list, and filter_list are set up correctly.
    It prints "Pass" if everything is good, and "Fail" if something's wrong.
    """

    print("Testing sensors:")
    # Check if the "STEM Center" and "Outside" sensors are correctly set up
    if sensors["4213"][0] == "STEM Center" and sensors["Out"][1] == 5:
        print("Pass")
    else:
        print("Fail")
    # Check if sensor_list has exactly 6 items (one for each sensor)
    print("Testing sensor_list length:")
    if len(sensor_list) == 6:
        print("Pass")
        print("Testing sensor_list content:")
        # Make sure the room descriptions in sensor_list match what's in the sensors dictionary
        for item in sensor_list:
            if item[1] != sensors[item[0]][0]:
                print("Fail")
                break
        else:
            print("Pass")
    else:
        print("Fail")
    # Check if filter_list has 6 items
    print("Testing filter_list length:")
    if len(filter_list) == 6:
        print("Pass")
    else:
        print("Fail")

    # Check if the sum of the filter_list is 15 (0+1+2+3+4+5 = 15)
    print("Testing filter_list content:")
    if sum(filter_list) == 15:
        print("Pass")
    else:
        print("Fail")


def main():
    """
     Main function that runs the whole program.
    This is where the dictionary, list, and filter list are created.
    Then the menu is displayed so the user can interact with the program.
    """
    # Step 1: Create the sensors dictionary.
    # This dictionary links room numbers (keys) to room descriptions and sensor numbers (values).
    sensors = {
        "4213": ("STEM Center", 0),
        "4201": ("Foundations Lab", 1),
        "4204": ("CS Lab", 2),
        "4218": ("Workshop Room", 3),
        "4205": ("Tiled Room", 4),
        "Out": ("Outside", 5)
    }

    # Step 2: Create the sensor_list using list comprehension.
    # Each item is a tuple with (Room Number, Room Description, Sensor Number)
    sensor_list = [(room_number, sensors[room_number][0], sensors[room_number][1]) for room_number in sensors]

    # Step 3: Create the filter_list using list comprehension.
    # This list will just contain the sensor numbers.
    filter_list = [sensors[room_number][1] for room_number in sensors]

    # Step 4: Run the unit test to check if everything is set up correctly
    test_sensors(sensors, sensor_list, filter_list)

    # Print the program's title and name
    print_header()

    # Start the menu loop
    while True:
        print_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                new_file(None)
            elif choice == 2:
                choose_units()
            elif choice == 3:
                change_filter(None, None)
            elif choice == 4:
                print_summary_statistics(None, None)
            elif choice == 5:
                print_temp_by_day_time(None, None)
            elif choice == 6:
                print_histogram(None, None)
            elif choice == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break
            else:
                print("Invalid Choice, please enter an integer between 1 and 7.")

        except ValueError:
            print("*** Please enter a number only ***")

        print()


if __name__ == "__main__":
    main()


"""

"C:\\Users\\zandu\\python projects\\pythonProject+\\.venv\\Scripts\\python.exe" "C:\\Users\\zandu\\python projects\\pythonProject+\\Assignment-4.py" 
Testing sensors:
Pass
Testing sensor_list length:
Pass
Testing sensor_list content:
Pass
Testing filter_list length:
Pass
Testing filter_list content:
Pass
STEM Center Temperature Project
Zainab Abdulhasan

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit


Enter your choice: 7
Thank you for using the STEM Center Temperature Project

Process finished with exit code 0

"""