items = []

#Module1: Add Item
def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    items.append(item)
    print("Item added successfully!")

#Module2: Display items
def display_items():
    if len(items) == 0:
        print("no items added.")
        return
    print("\n----Items----")
    for item in items:
        print("Item:", item["name"])
        print("Price:", item["price"])
        print("Quantity:", item["quantity"])

#Module3: Calculate total
def calculate_total():
    total = 0
    for item in items:
        total = total + (item["price"] * item["quantity"])
    return total

#Module4: Display bill
def display_bill():
    if len(items) == 0:
        print("No items in the bill.")
        return
    total = calculate_total()
    print("\n BILL")
    for item in items:
        amount = item["price"] * item["quantity"]
        print(
            item["name"], 
            "-",
            item["quantity"],
            "X",
            item["price"],
            "=",
            amount
        )    
    print("Total Amount:", total)

#Main module
def main():
    while True:
        print("\n SHOPPING MENU ")
        print("1. Add Item")
        print("2. Display Items")
        print("3. Display Bill")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            display_items()
        elif choice == "3":
            display_bill()
        elif choice == "4":
            print("Thank You!")
            break
        else:
            print("Invalid choice!")

#Start program
main()
