# Day Translation

def translate_day(day):

    translations = {
        "sunday": "Yom Rishon",
        "monday": "Yom Shenee",
        "tuesday": "Yom Shlishee",
        "wednesday": "Yom Revi'ee",
        "thursday": "Yom Chameeshee",
        "friday": "Yom Sheeshee",
        "saturday": "Yom Shabat",
    }

    print(translations[day.lower()])

def print_friday_message():
    # I could change here, but its better to add protection within the function
    translate_day( "Friday" )

print_friday_message()


# Empty List

lst = list(range(1,10))

for i in range(len(lst)):
    del lst[:1]

print(lst)


# Is there a bird in here?

def is_bird_in_list(lst):
    lower_list = [a.lower() for a in lst]

    if "bird" in lower_list:
        foo = "I found a bird!"
        print(foo)

is_bird_in_list([ "boy","girl" ,"lady" ,"dog" ,"pie"])

# Fix me

for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if(number % 3) == 0:
        message = 'a'
    else:
        message = "b"
    print(message)


