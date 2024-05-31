# Import the os module, which provides a way to use operating system dependent functionality
import os

# Define a class called SumCalculatorNew
class SumCalculatorNew:
    # The __init__ method is a special method that is automatically called when an object of the class is created
    def __init__(self, input_file):
        # Set the input_file attribute of the class to the input_file parameter
        self.input_file = input_file
        # Call the get_total_sum method and set the total_sum attribute of the class to its return value
        self.total_sum = self.get_total_sum()

    # Define a method called get_total_sum
    def get_total_sum(self):
        # Initialize a variable called total_sum to 0
        total_sum = 0
        # Open the file specified by self.input_file in read mode
        with open(self.input_file, "r") as file:
            # Iterate over each line in the file
            for line in file:
                # Remove any leading or trailing whitespace from the line
                line = line.strip()
                # Check if the line contains a digit
                if line.isdigit():
                    # Add the integer value of the line to total_sum
                    total_sum += int(line)
        # Return the total_sum
        return total_sum

    # Define a method called print_solution
    def print_solution(self):
        # Print a message that includes the total_sum
        print(f"The total sum from the given input file {self.input_file} is {self.total_sum}")

# Define a function called main
def main():
    # Set the input_file variable to "134.txt"
    input_file = "134.txt"
    # Check if the file specified by input_file exists
    if os.path.exists(input_file):
        # Create an object of the SumCalculatorNew class, passing input_file as a parameter
        calculator = SumCalculatorNew(input_file)
        # Call the print_solution method of the calculator object
        calculator.print_solution()
    else:
        # If the file does not exist, print an error message
        print(f"File {input_file} not found.")

# Check if this script is being run directly (not being imported as a module)
if __name__ == "__main__":
    # Call the main function
    main()