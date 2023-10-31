def main():
    # While loop example
    num = 1
    while num <= 5:
        print(f"While loop: {num}")
        num += 1

    # For loop example
    for i in range(1, 6):
        print(f"For loop: {i}")

    # For loop over a collection
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"For loop over collection: {fruit}")

    # Using the break statement
    for i in range(1, 11):
        if i == 5:
            break
        print(f"Break statement: {i}")

    # Using the continue statement
    for i in range(1, 6):
        if i == 3:
            continue
        print(f"Continue statement: {i}")

    # Using enumerate to get index
    items = ["item1", "item2", "item3"]
    for index, item in enumerate(items):
        print(f"Index: {index}, Value: {item}")

if __name__ == "__main":
    main()
