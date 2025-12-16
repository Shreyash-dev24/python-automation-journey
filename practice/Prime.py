a = [1,2,65,474,5,6,7,8,9,10,11]

for i in a:
    if i <= 1:
        print(f"{i} not a prime")
    else:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{i} prime number")
        else:
            print(f"{i} not a prime")
