def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Example usage
print(is_prime(29))  # True


def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


# Example usage
print(reverse_string("hello"))  # "olleh"


def are_anagrams(str1, str2):
    return sorted(str1.replace("listen").lower()) == sorted(str2.replace("silent").lower())


# Example usage
print(are_anagrams (srt1="listen",srt2="silent"))  # True


def count_words(s):
    return len(s.split())


# Example usage
print(count_words("This is a test string"))  # 5
import csv
import json


def calculate_revenue(sales_file, products_file, output_file):
    with open(products_file, 'r') as f:
        products = json.load(f)

    product_revenue = {product['id']: 0 for product in products}

    with open(sales_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product_id = row['product_id']
            quantity = int(row['quantity'])
            price = next(product['price'] for product in products if product['id'] == product_id)
            product_revenue[product_id] += quantity * price

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['product_id', 'revenue'])
        for product_id, revenue in product_revenue.items():
            writer.writerow([product_id, revenue])


# Example usage
calculate_revenue(sales_file='sales.csv', products_file='products.json')
import csv
import json


def low_stock_report(inventory_file, output_file):
    with open(inventory_file, 'r') as f:
        inventory = json.load(f)

    low_stock_items = [item['name'] for item in inventory if item['quantity'] < 10]

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['product_name'])
        for item in low_stock_items:
            writer.writerow([item])


# Example usage
low_stock_report(inventory_file='inventory.json', output_file='low_stock.csv')


def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []


# Example usage
print(two_sum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
