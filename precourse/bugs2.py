# List of zeros

def to_zeros(lst):
    lst[:] = [0*x for x in lst]

lst = [ 1 ,  2 ,  3 ,  4 ,  4 ,  5 ,  9 ,  8  , 7 ,  9 ]
to_zeros(lst)
print(lst)

# I, Follow my Js

lst = []
for i in ["i"]*10:
    for j in ["j"]* 10:
        lst.append(j)
    lst.append(i)
print(lst)

# Make me pass

FAILED = True
n_tests = 4
tot_grade = 220
while FAILED:
    grade_str = input("What is the new grade that you got?")
    while not grade_str.isdigit():
        grade_str = input("You did not submit a number. What is your new grade")
    grade_int = int(grade_str)
    n_tests += 1
    tot_grade += grade_int
    average = round(tot_grade / float(n_tests),  1)
    print("Your new average score is: ", round(tot_grade / float(n_tests),  1))
    FAILED = False if average >= 60 else True
    if FAILED:
        print("You still Failed")
    else:
        print("You Passed!")

# Plan my day

curr_t_str = input("What time is it now (hour)?")
while not curr_t_str.isdigit():
    curr_t_str = input("You did not submit a number. What time is it now (hour)?")
curr_t_int = int(curr_t_str)
wait_t_str = input("How long do you want to wait (hours)")
while not curr_t_str.isdigit():
    wait_t_str = input("You did not submit a number. How long do you want to wait (hours)")
wait_t_int = int(wait_t_str)
final_t_int = (curr_t_int + wait_t_int) % 24
print("Yo will leave at: ", final_t_int)