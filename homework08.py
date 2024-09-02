items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
income = 0  # Initialize income outside the loop

for item in items.keys():
    qty = int(input(f"How many {item}s have you sold? "))  # Convert input to integer
    income += qty * items[item]  # Use += for incrementing income

print(f"\nThe income is: {income}")

def get_integer_input():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


number = get_integer_input()
print("You entered:", number)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:  # Compare arr[j] with arr[min_index]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the elements
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)



