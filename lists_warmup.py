numbers = [3, 1, 4, 1, 5, 9, 2]


numbers[0] """output is 3"""
numbers[-1] """output is 2"""
numbers[3] """output is 1"""
numbers[:-1] """output is [3, 1, 4, 1, 5, 9]"""
numbers[3:4] """output is [1]"""
5 in numbers """True"""
7 in numbers """False"""
"3" in numbers """False"""
numbers + [6, 5, 3] """output is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]"""

numbers[0] = "ten" """1.Change the first element of numbers to "ten" (the string, not the number 10)"""
numbers[-1] = 1 """2.change the last element of numbers to 1"""
numbers[2:] """3.get all the elements from numbers except the first two(slice)"""
9 in numbers """check if 9 is an element of numbers"""