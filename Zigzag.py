def print_zigzag(rows):
    if rows < 3:
        print("Please enter a number of rows greater than or equal to 3 for a proper zigzag.")
        return

    n = (rows + 1) // 2  # Number of columns in the repeating unit

    for i in range(rows):
        for j in range(n * (rows - 1)):  # Total columns needed
            if (i % (rows - 1) == 0 and j % (rows - 1) == 0) or \
               (i % (rows - 1) == (rows - 2) and (j + 1) % (rows - 1) == 0) or \
               (0 < i % (rows - 1) < (rows - 2) and j % (rows - 1) == i % (rows - 1)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O')
    num_rows = int(input("Enter the number of rows for the zigzag pattern: "))
    print_zigzag(num_rows)
