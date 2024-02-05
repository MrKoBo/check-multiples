import random
def check_multiples(number, divisor):
    if number % divisor == 0:
        print(f"{number} is divisible by {divisor}")
    else:
        print(f"{number} is not divisible by {divisor}")

number = random.randint(1, 100)

divisor = random.randint(1, 10)
check_multiples(number, divisor)