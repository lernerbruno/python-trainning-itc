"""
Script that selects my hobbies from a list of hobbies

Author: Bruno Lerner
"""


def define_my_hobbies():
    my_hobbies = ["music", "reading", "drinking with friends", "dancing", "netflix"]
    for hobby in my_hobbies:
        if hobby == "dancing":
            my_hobbies.remove("dancing")
    return my_hobbies

if __name__ == "__main__":
   print(define_my_hobbies())