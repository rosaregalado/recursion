# Compute the Factorial of a number N. F act(N) = N × (N −1)· · · 1

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))


# Compute the sum of natural numbers until N

def sum_natural_nums(n):
  if n == 1:
    return 1
  else:
    return n + sum_natural_nums(n-1)

print(sum_natural_nums(5))


# Write a function for mutliply(a, b), where a and b are both positive
# integers, but you can only use the + or − operators.

def mutliply(a, b):
  # base case
  if a == 0 or b == 0:
    return 0

  return a + mutliply(a, b-1)


# write a recursive function that allows raising to a negative integer power

def power(base, exponent):
  # base case
  if exponent == 0:
    return 1
  # if exponent is positive
  elif exponent > 0:
    return base * power(base, exponent - 1)
  # if exponent is negative
  else:
    return 1 / power(base, -exponent)

print(power(2, -3))


# Find Greatest Common Divisor (GCD) of 2 numbers using recursion.

def greatest_common_divisor(a, b):
  # base case
  if b == 0:
    return a
  else:
    return greatest_common_divisor(b, a % b)

print(greatest_common_divisor(60, 48))


# Write a recursive function to reverse a string. Write a recursive
# function to reverse the words in a string, i.e., ”cat is running”
# becomes ”running is cat”

def reverse_string(str):
  # base case
  if len(str) == 0:
    return str
  else:
    i = str.find(' ')
    if i == -1:
      return reverse_string('') + str
    else:
      return reverse_string(str[i+1:]) + ' ' + reverse_string(str[:i])

str = 'cat is running fast'
print(reverse_string(str))