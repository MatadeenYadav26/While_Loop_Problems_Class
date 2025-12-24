#Promblem-01

# a = int(input("Input: "))
# while a > 0:
#     print(a%10)
#     a = a//10

#Problem-02

# n = int(input("tell digit: "))
# s = 0
# while n > 0 :
#     print(n%10)
#     s = s+ n%10
#     n = n//10

# print(f"Sum is: {s}.")

#Problem-03 : Reverse digits of a number from input

# n = int(input("tell digit: "))
# rev = 0
# while n > 0 :
#     print(n%10)
#     rev = rev * 10 + n%10
#     n = n//10

# print(f"Reverse is: {rev}.")

#problem-4 : Palindrome Number Check

# n = int(input("tell digit: "))
# copy = n
# rev = 0
# while n > 0 :
#     rev = rev * 10 + n%10
#     n = n//10   

# print(f"Reverse is: {rev}.")

# if copy == rev :
#     print("This number is a pallindrome.")
# else:
#     print("This number is not apallindrome.")

#Problem - 05 : Automorphic Number :- when we do sq of a number eg (25) we get (625) , here last 2 digits of sq and result is same ie. 625 and 25. eg :- 5,625 and 625,390625 and 6,36 .

# a = int(input("Enter: "))
# dup = a

# sq = a**2

# count = 0 

# while a > 0 :
#     count = count+1
#     a = a//10

# print(count)

# extract = sq % (10**count)

# print(extract)

# if dup == extract:
#     print("Your number is Automorphic.")

# else:
#     print("Your number is not Automorphic.")