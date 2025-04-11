def findMean(marks):
        sorted_marks = sorted(marks)
        mean = 0
        sum = 0
        for mark in sorted_marks:
            sum += mark
        mean = sum / len(marks)
        
        return mean


print("Enter student marks one at a time. Type 'end' when you want to stop the program or if you want to start again type back.")


