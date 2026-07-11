records = []


def add(text):
    records.append(text)


def show():

    print("\nHistory")
    print("-" * 20)

    for record in records:
        print(record)

    print(f"\n{len(records)} conversions completed.")
