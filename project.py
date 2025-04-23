# Function to calculate the mean (average) of marks
def findMean(marks):
        sorted_marks = sorted(marks)  # Sort the marks in ascending order
        mean = 0
        sum = 0
        for mark in sorted_marks:     # Loop through each mark
            sum += mark               # Add each mark to the total sum
        mean = sum / len(marks)       # Divide the sum by total number of marks
        return mean                   # Return the mean value

# Function to calculate the median of marks
def findMedian(marks):
        sorted_marks = sorted(marks)                 # Sort the marks in ascending order
        sorted_marks_length = len(sorted_marks)      # Get the number of marks
        median = 0

        if sorted_marks_length % 2 == 0:             # If even number of marks
                mid1 = sorted_marks[sorted_marks_length // 2 - 1]  # First middle value
                mid2 = sorted_marks[sorted_marks_length // 2]      # Second middle value
                median = (mid1 + mid2) / 2            # Average the two middle values
        else:
                median = sorted_marks[sorted_marks_length // 2]   # Take middle value

        return median

# Function to calculate the mode (most frequent number)
def findMode(marks):
        marksObj = {}                                 # Dictionary to store frequency of each mark
        for mark in marks:
            if mark in marksObj:
                    marksObj[mark] += 1               # If mark exists, increase count
            else:
                   marksObj[mark] = 1                 # If mark doesn't exist, set count to 1
        
        max_count = max(marksObj.values())            # Find the highest frequency

        # Find all marks that appear with max frequency
        modes = [mark for mark, count in marksObj.items() if count == max_count]

        if len(modes) == 1:
                return modes[0]                       # Return single mode value
        else:
                return modes                          # Return list of modes (if multiple)

# Function to calculate skewness of the data (asymmetry of distribution)
def findSkewness(mean, numbers):
       distance_of_each_point = []                    # Store squared distances from mean
       points_sum = 0
       cubed_scores_sum = 0

       for number in numbers:
             square_distance = (number - mean) ** 2   # Calculate square of difference from mean
             distance_of_each_point.append(square_distance)

       for point in distance_of_each_point:
              points_sum += point                     # Sum of squared distances
       
       population = points_sum / len(distance_of_each_point)  # Variance
       deviation = population ** 0.5                  # Standard deviation

       # Calculate cubed z-scores for each number
       cubed_z_scores = [((number - mean) / deviation) ** 3 for number in numbers]

       for cubed_score in cubed_z_scores:
              cubed_scores_sum += cubed_score         # Sum of cubed z-scores

       skewness = cubed_scores_sum / len(numbers)     # Final skewness value
       return skewness

def calculateFile(filename):
        try:
            with open(filename, "r") as file:                 # Open the file in read mode
                content = file.read()                         # Read the content
                numbers = [float(num.strip()) for num in content.split(",")]  # Convert to float list
                user_input_marks.extend(numbers)              # Add to main list
                print(user_input_marks)                       # Print the updated list
        except Exception as e:
            print("Error reading file:", e)                   # Handle any errors


# Introduction message
print("Enter student marks one at a time. Type 'exit' when you want to stop the program")

user_input_marks = []  # List to store all marks entered

# Main program loop
while True:
        # If first time or reset triggered by options 4 or 6
        if len(user_input_marks) == 0 or len(user_input_marks) == 1 or choice == "4" or choice == "6": 
            if len(user_input_marks) == 1:
                   user_input_marks = []  # Reset if only one mark was entered
            while True:
                        mark = input("Enter marks: ")

                        if mark == "":
                               continue     # Skip empty input
                        if mark == "done":
                                break       # Exit mark entry loop

                        if "," in mark:
                               try:
                                        # Split by commas, strip whitespace, convert to float
                                        numbers = [float(x.strip()) for x in mark.split(",")]
                                        user_input_marks.extend(numbers)  # Add to mark list
                               except ValueError:
                                        print("Invalid input. Please enter valid numbers separated by commas.")
                        else:
                                try:
                                        decimal_mark = float(mark)  # Convert single input to float
                                        user_input_marks.append(decimal_mark)
                                except ValueError:
                                        print("Invalid input. Please enter a valid number.")

        print(f"You have entered {len(user_input_marks)} marks.")  # Show total entered

        # Ensure at least 2 marks are present before proceeding
        if len(user_input_marks) < 2:
              print("Please enter at least two numbers before proceeding.")
              continue

        # Display menu
        print("\nChoose an option:")
        print("1. Print mean")
        print("2. Print median")
        print("3. Print mode")
        print("4. Enter a new set of marks")
        print("5. Print skewness")
        print("6. Add more numbers")
        print("7. Get numbers from file")
        print("8. Exit")

        choice = input("Enter your choice: ")

        # Handle each menu option
        if choice == "1":
                mean = findMean(user_input_marks) # Calculate mean
                print(mean)
                continue
        if choice == "2":
                median = findMedian(user_input_marks) # Calculate median
                print(median)
                continue
        if choice == "3":
                mode = findMode(user_input_marks) # Calculate mode
                print(mode)
                continue
        if choice == "4":
                user_input_marks = []  # Reset the data
                continue
        if choice == "5":
                mean = findMean(user_input_marks)  # Calculate mean
                skewness = findSkewness(mean, user_input_marks) # Calculate skewness
                print(skewness)
        if choice == "6":
                continue  # Continue lets the user add more numbers
        if choice == "8":
                break     # Exit the program
        if choice == "7":
                 filename = input("Enter file name: ")  # Ask user for file name
                 calculateFile(filename)                # Load data from file