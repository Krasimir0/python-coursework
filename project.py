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
    mode = findMode(user_input_marks)
    print(mean)
    print(median)
    print(mode)

