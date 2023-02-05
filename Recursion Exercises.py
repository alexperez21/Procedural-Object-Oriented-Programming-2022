# Complete each of the functions below following the instructions.
# All functions must be accomplished recursively!
# Test by running unit tests.

# Part 1
# Write a recursive function to sum up all digit of a non-negative integer.
def sum_digits(n):
  if n == 0:
    return 0
  else: 
    return (n%10) + sum_digits(n//10)

print(sum_digits(345))  # 12
print(sum_digits(45))  # 9


# Part 2
# Write a recursive function to calculate the harmonic sum of n-1.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example n=4: 1 + 1/2 + 1/3 + 1/4 = 2.08333
# Example n=7: 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 = 2.59285
def harmonic_sum(n):
    if n < 2:
      return 1 
    else:
      return 1 / n + (harmonic_sum(n - 1))

print(harmonic_sum(7))  # 2.5928571428571425
print(harmonic_sum(4))  # 2.083333333333333


# Part 3
# Write a recursive function to calculate the value of 'a' raised to the power 'b'.
# Don't use exponentiation operator.
def power(a, b):
  if b == 0:
    return 1
  return (a*power(a, b-1)) 

print(power(3, 4))  # 81
print(power(4, 3))  # 64


# Optional!
# Write a recursive function to find the greatest common divisor (gcd) of two integers.
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

print(gcd(12, 14))  # 2
print(gcd(8, 12))  # 4
