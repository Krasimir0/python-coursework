def findMean(marks):
        sorted_marks = sorted(marks)
        mean = 0
        sum = 0
        for mark in sorted_marks:
            sum += mark
        mean = sum / len(marks)
        
        return mean

def findMedian(marks):
        sorted_marks = sorted(marks)
        sorted_marks_length = len(sorted_marks) 
        median = 0

        if sorted_marks_length % 2 == 0:
                mid1 = sorted_marks[sorted_marks_length // 2 - 1]
                mid2 = sorted_marks[sorted_marks_length // 2]
                median = (mid1 + mid2) / 2
        else:
                median = sorted_marks[sorted_marks_length // 2]

        return median

def findMode(marks):
        marksObj = {}
        for mark in marks:
            if mark in marksObj:
                    marksObj[mark] += 1
            else:
                   marksObj[mark] = 1
        
        max_count = max(marksObj.values())

        modes = [mark for mark, count in marksObj.items() if count == max_count]

        if len(modes) == 1:
                return modes[0]
        else:
                return modes
        
                

print("Enter student marks one at a time. Type 'exit' when you want to stop the program or if you want to start again type back.")

user_input_marks = []

while True:
        
        if len(user_input_marks) == 0:
                user_input =  input("Enter marks: ")
                user_input_marks = list(map(float, user_input.split(',')))
                
                if len(user_input_marks) < 2:
                        print("Please enter at least two numbers before proceeding.")
                        continue

                print(f"You have entered {len(user_input_marks)} marks.")

        print("\nChoose an option:")
        print("1. Print mean")
        print("2. Print median")
        print("3. Print mode")
        print("4. Enter a new set of marks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
                mean = findMean(user_input_marks)
                print(mean)
                continue
        if choice == "2":
                median = findMedian(user_input_marks)
                print(median)
                continue
        if choice == "3":
                mode = findMode(user_input_marks)
                print(mode)
                continue
        if choice == "4":
                user_input_marks = []
                continue
        if choice == "5":
                break