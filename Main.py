import time

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Category: {self.category}"

def load_products_from_file(filename):
    products = []
    with open(filename, 'r') as file:
        for line in file:
            fields = line.strip().split(',')
            products.append(Product(fields[0], fields[1], float(fields[2]), fields[3]))
    return products

def insert_product(products, product):
    products.append(product)

def update_product(products, product_id, new_product):
    for i, product in enumerate(products):
        if product.product_id == product_id:
            products[i] = new_product
            return True
    return False

def delete_product(products, product_id):
    for i, product in enumerate(products):
        if product.product_id == product_id:
            del products[i]
            return True
    return False

def search_product_by_id(products, product_id):
    for product in products:
        if product.product_id == product_id:
            return product
    return None

def search_product_by_name(products, product_name):
    matching_products = []
    for product in products:
        if product_name.lower() in product.name.lower():
            matching_products.append(product)
    return matching_products


def quick_sort_products(products, low, high):
    if low < high:
        pi = partition(products, low, high)
        quick_sort_products(products, low, pi-1)
        quick_sort_products(products, pi+1, high)

def partition(products, low, high):
    pivot = products[high].price
    i = low - 1
    for j in range(low, high):
        if products[j].price < pivot:
            i += 1
            products[i], products[j] = products[j], products[i]
    products[i+1], products[high] = products[high], products[i+1]
    return i + 1

def sort_and_display_products_by_price(products):
    quick_sort_products(products, 0, len(products)-1)
    for product in products:
        print(product)

def measure_sort_time(products):
    start_time = time.time()
    quick_sort_products(products, 0, len(products) - 1)
    end_time = time.time()
    return end_time - start_time

products = load_products_from_file('product_data.txt')  # Assuming 'product_data.txt' is correctly formatted and available

while True:
    print("\nData Manipulation Operations:")
    print("1. Insert a new product")
    print("2. Update an existing product")
    print("3. Delete a product")
    print("4. Search for a product by ID")
    print("5. Search for products by name")
    print("6. Sort and display products by price")
    print("7. Check sorting time on current products list")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")
        new_product = Product(product_id, name, price, category)
        insert_product(products, new_product)
        print("Product inserted successfully.")
    elif choice == '2':
        product_id = input("Enter product ID to update: ")
        name = input("Enter new product name: ")
        price = float(input("Enter new product price: "))
        category = input("Enter new product category: ")
        new_product = Product(product_id, name, price, category)
        if update_product(products, product_id, new_product):
            print("Product updated successfully.")
        else:
            print("Product not found.")
    elif choice == '3':
        product_id = input("Enter product ID to delete: ")
        if delete_product(products, product_id):
            print("Product deleted successfully.")
        else:
            print("Product not found.")
    elif choice == '4':
        product_id = input("Enter product ID to search: ")
        product = search_product_by_id(products, product_id)
        if product:
            print(product)
        else:
            print("Product not found.")
    elif choice == '5':
        product_name = input("Enter product name to search: ")
        matching_products = search_product_by_name(products, product_name)
        if matching_products:
            print(f"Found {len(matching_products)} matching product(s):")
            for product in matching_products:
                print(product)
        else:
            print("No products found with that name.")
    elif choice == '6':
        print("Sorting products by price...")
        sort_and_display_products_by_price(products)
    elif choice == '7':
        sorting_time = measure_sort_time(products)
        print(f"Time taken to sort: {sorting_time:.6f} seconds")
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
