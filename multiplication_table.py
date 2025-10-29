def multiplication_table(n):
    print(f"\nMultiplication Table of {n}:")
    for i in range(1, 11):
        print(f"{n:2} x {i:2} = {n*i:3}")

num = int(input("Enter number: "))
multiplication_table(num)
