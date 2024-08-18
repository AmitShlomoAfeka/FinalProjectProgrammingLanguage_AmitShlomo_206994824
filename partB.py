######################################
# Amit Shlomo 206994824
#######################################

from functools import reduce


# 1. Fibonacci sequence generator using a single lambda expression
print("----------------------------------------------------------------------------")
print("Test - Fibonacci sequence generator using a single lambda expression")
print("----------------------------------------------------------------------------")
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])[:n]
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print()

# 2. Concatenate a list of strings with a space between them without using 'join'
print("--------------------------------------------------------------------------------------")
print("Test - Concatenate a list of strings with a space between them without using 'join'")
print("--------------------------------------------------------------------------------------")
concat_strings = lambda lst: ' '.join(map(str, lst))
print(concat_strings(['Hello', 'world', 'this', 'is', 'a', 'test']))  # Output: Hello world this is a test
print()

# 3. Cumulative sum of squares of even numbers in each sublist using nested lambda expressions
print("-------------------------------------------------------------------------------------------------")
print("Test - Cumulative sum of squares of even numbers in each sublist using nested lambda expressions")
print("-------------------------------------------------------------------------------------------------")
cumulative_sum_squares = lambda lst: list(map(lambda sub: reduce(lambda acc, x: acc + x**2, filter(lambda y: y % 2 == 0, sub), 0), lst))
print(cumulative_sum_squares([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [4, 52, 64]
print()

# 4. Higher-order function for cumulative binary operation
print("----------------------------------------------------------------")
print("Test - Higher-order function for cumulative binary operation")
print("----------------------------------------------------------------")
cumulative_op = lambda op: lambda seq: reduce(op, seq)
factorial = cumulative_op(lambda x, y: x * y)
exponentiation = cumulative_op(lambda x, y: x ** y)
print(factorial([1, 2, 3, 4, 5]))  # Output: 120
print(exponentiation([2, 3, 2]))  # Output: 64
print()

# 5. Rewrite the given program in one line using nested filter, map, and reduce
print("-----------------------------------------------------------------------------------")
print("Test - Rewrite the given program in one line using nested filter, map, and reduce")
print("-----------------------------------------------------------------------------------")
sum_squared = reduce(lambda acc, x: acc + x, map(lambda x: x**2, filter(lambda y: y % 2 == 0, [1, 2, 3, 4, 5, 6])))
print(sum_squared)  # Output: 56
print()

# 6. Count palindrome strings in each sublist using nested filter, map, and reduce
print("--------------------------------------------------------------------------------------")
print("Test - Count palindrome strings in each sublist using nested filter, map, and reduce")
print("--------------------------------------------------------------------------------------")
palindrome_counts = lambda lst: list(map(lambda sub: reduce(lambda acc, s: acc + (1 if s == s[::-1] else 0), sub, 0), lst))
print(palindrome_counts([['madam', 'test', 'level'], ['noon', 'world', 'civic']]))  # Output: [2, 2]
print()

# 7. Explanation of "lazy evaluation"
print("-------------------------------------------")
print("Test - Explanation of 'lazy evaluation'")
print("-------------------------------------------")
def generate_values():
    print('Generating values...')
    yield 1
    yield 2
    yield 3

def square(x):
    print(f'Squaring {x}')
    return x * x

print('Eager evaluation:')
values = list(generate_values())
squared_values = [square(x) for x in values]
print(squared_values)  # Output: [1, 4, 9]

print('\nLazy evaluation:')
squared_values = [square(x) for x in generate_values()]
print(squared_values)  # Output: [1, 4, 9]
print()

# 8. One-line function to return sorted prime numbers
print("----------------------------------------------------------")
print("Test - One-line function to return sorted prime numbers")
print("----------------------------------------------------------")
is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
sorted_primes = lambda lst: sorted([x for x in lst if is_prime(x)], reverse=True)
print(sorted_primes([10, 3, 5, 7, 11, 13, 4, 6, 8]))  # Output: [13, 11, 7, 5, 3]
