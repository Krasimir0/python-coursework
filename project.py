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
        sum = 0
        if sorted_marks_length % 2 == 0:
                mid1 = sorted_marks[sorted_marks_length // 2 - 1]
                mid2 = sorted_marks[sorted_marks_length // 2]
                median = (mid1 + mid2) / 2
                print(median)
        else:
                median = sorted_marks[sorted_marks_length // 2]
        
        return median

print("Enter student marks one at a time. Type 'end' when you want to stop the program or if you want to start again type back.")

while True:
    user_input =  input("Enter marks or type 'end': ")
    if user_input.lower() == 'end':
            break
    if user_input.lower() == 'back':
            continue
    user_input_marks = list(map(float, user_input.split(',')))
    if len(user_input_marks) < 2:
                print("Please enter at least two numbers before proceeding.")
                continue
    mean = findMean(user_input_marks)
    median = findMedian(user_input_marks)

