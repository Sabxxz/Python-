def process_items(items_list):
    for item in items_list:
        print(f"processing {item}")
        if item == "milk":
            print(f"Donot forget to refrigerate {item}")
        elif item == "egg":
            print(f"Donot forget to store {item} in egg tray")


items_list = ["milk","egg","cake","banana"]

process_items(items_list)