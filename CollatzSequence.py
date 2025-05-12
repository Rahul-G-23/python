def collatz_sequence(n):
    if not isinstance(n, int) or n <= 0:
        print("Please enter a positive integer.")
        return

    print(n, end=" ")
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n, end=" ")
    print()  

if __name__ == "__main__":
    print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O')
    start_number = int(input("Enter a positive integer to start the Collatz sequence: "))
    collatz_sequence(start_number)
