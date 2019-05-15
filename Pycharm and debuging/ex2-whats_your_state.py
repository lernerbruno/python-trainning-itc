"""
Very badly-written code, just as a debugging exercise.

Author: Omer Rosenbaum
"""

def function_3(k):
    m = k % 19
    return m

def function_2(n):
    for j in range(1,10000, n):
        function_3(j)

def function_1():
    for i in range(17, 400, 4):
        function_2(i*3)

if __name__ == '__main__':
    function_1()