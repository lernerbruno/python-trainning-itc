"""
Script that selects my hobbies from a list of hobbies

Author: Bruno Lerner
"""


def define_my_hobbies():
    my_hobbies = ["music", "reading", "drinking with friends", "dancing", "netflix"]
    for i in range(len(my_hobbies)):
        if my_hobbies[i] == "dancing":
            my_hobbies.remove("dancing")
    return my_hobbies

if __name__ == "__main__":
   print(define_my_hobbies())