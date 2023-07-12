print("current and previous numbers and their sum in the range (10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num+i
    print("Current_Number", i, "Previous_Number ",
          previous_num, "Sum: ", x_sum)
# modify previous number
# set it to the current number
    previous_num = i
