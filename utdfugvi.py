def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs - 1) + ways(stairs - 2)

n = int(input("Enter the number of steps: "))
guess = int(input(f"What is the ways of {n}: "))
print(f"Ways({n}) = {ways(n)}, your guess: {guess}")

if guess == ways(n):
    print("Your guess was correct")
else:
    print("Your guess was wrong")