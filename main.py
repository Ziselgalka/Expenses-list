import json
import math
import os
import sys

expenses_list = []
file_path = "saved_data.json"

def expenses_add():
    while True:
        name_input = input("Enter expense name:").lower().strip()
        if name_input == "":
            print("Invalid input")
            continue
        else:
            break

    while True:
        try:
            amount_input = round(float(input("Enter amount:").strip()), 2)
            if math.isfinite(amount_input) != True:
                print("Invalid input")
                continue
            break
        except ValueError:
            print("Invalid input")

    comment_input = input("Enter comment (optional, '0' to leave):").strip()
    if comment_input == "0":
        comment_input = ""

    expenses_list.append({"Category": name_input, "Amount": amount_input, "Comment": comment_input})

    save_data()

def expenses_show():
    if len(expenses_list) > 0:
        for i in range(len(expenses_list)):
            if expenses_list[i]["Comment"] == "" :
                print(f"{i + 1}. {expenses_list[i]["Category"]} - {expenses_list[i]["Amount"]}")
            else:
                print(f"{i + 1}. {expenses_list[i]["Category"]} - {expenses_list[i]["Amount"]} - {expenses_list[i]["Comment"]}")
    else:
        print("There are no expenses")

def expenses_total():
    expenses_total = []

    for item in expenses_list:
        for i in range(len(expenses_total)):
            if item["Category"] == expenses_total[i]["Category"]:
                expenses_total[i]["Amount"] = round(expenses_total[i]["Amount"] + item["Amount"], 2)
                break
        else:
            expenses_total.append({"Category": item["Category"], "Amount": item["Amount"]})

    if len(expenses_total) > 0:
        for i in range(len(expenses_total)):
            print(f"{i + 1}. {expenses_total[i]["Category"]} - {expenses_total[i]["Amount"]}")
    else:
        print("There are no expenses")

def save_data():
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(expenses_list, f, ensure_ascii=False, indent = 2)

def load_data():
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise TypeError
        
        for item in data:
            if not isinstance(item, dict) or not isinstance(item["Category"], str) or not isinstance(item["Comment"], str):
                raise TypeError
            if not {"Category", "Amount", "Comment"} <= item.keys():
                raise ValueError
            if not isinstance(item["Amount"], (int, float)) or not math.isfinite(item["Amount"]) or isinstance(item["Amount"], bool):
                raise ValueError
                    
        expenses_list.clear()
        expenses_list.extend(data)

    except FileNotFoundError:
        save_data()
    except TypeError:
        error_handler()
    except ValueError:
        error_handler()

def error_handler():
    count = 0
    while True:
        if os.path.isfile(f"{file_path}.corrupted") and count == 0:
            count = 1
        elif os.path.isfile(f"{file_path}.corrupted{count}"):
            count += 1
        else:
            os.replace(file_path, f"{file_path}.corrupted{count}")
            break
    print("File was corrupted, but it will be saved")

    save_data()

def main():
    load_data()
    
    while True:
        print('''===Main menu===
        0. Exit
        1. Show all expenses
        2. Add expenses
        3. Total expenses''')

        while True:
            user_choice = input("Your choice:").strip()

            match user_choice:
                case "0":
                    save_data()
                    sys.exit()
                case "1":
                    expenses_show()
                    break
                case "2":
                    expenses_add()
                    break
                case "3":
                    expenses_total()
                    break
                case _:
                    print("Invalid input")
                    continue

if __name__ == "__main__":
    main()