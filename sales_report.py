import csv
def parse_price(value):
    return float(value)
with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    total = 0
    count = 0
    highest_price = 0
    highest_customer = ""
    keyboard_count = 0
    keyboard_total = 0
    high_value_count = 0
    invalid_count = 0
    missing_price_count = 0

    for row in reader:
        product = row["product"].strip().lower()

        if row["price"].strip() == "":
            missing_price_count = missing_price_count + 1
            continue

        try:
            price = parse_price(row["price"])
            total = total + price
            count = count + 1

            if price >= 50:
                high_value_count = high_value_count + 1

            if price > highest_price:
                highest_price = price
                highest_customer = row["customer"]
            if product == "keyboard":
                keyboard_count = keyboard_count + 1
                keyboard_total = keyboard_total + price
        except ValueError:
            print("Invalid price:", row["customer"], "-", row["price"])
            invalid_count = invalid_count + 1

    if count > 0:
        average_order_value = total / count
    else:
        average_order_value = 0

print("Total sales:", total)
print("Number of orders:", count)

if count > 0:
    print("Most expensive order:", highest_customer, "-", highest_price )
else:
    print("Most expensive order: No orders")

print("Keyboard count:", keyboard_count)
print("Keyboard sales:", keyboard_total)
print("Average order value:", average_order_value)
print("Orders of 50 or more:", high_value_count)
print("Invalid records:", invalid_count)
print("Missing price records:", missing_price_count)

with open("sales_report.txt", "w") as report_file:
    report_file.write("Sales report\n")
    report_file.write(f"Total sales: {total}\n")
    report_file.write(f"Number of orders: {count}\n")
    report_file.write(f"Keyboard sales: {keyboard_total}\n")
    report_file.write(f"Keyboard count: {keyboard_count}\n")
    report_file.write(f"Average order value: {average_order_value}\n")
    report_file.write(f"Orders of 50 or more: {high_value_count}\n")

    if count > 0:
        report_file.write(f"Most expensive order: {highest_customer} - {highest_price}\n")
    else:
        report_file.write("Most expensive order: No orders\n")

    report_file.write(f"Invalid records: {invalid_count}\n")
    report_file.write(f"Missing price records: {missing_price_count}\n")
