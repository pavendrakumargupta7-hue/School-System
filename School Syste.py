import json
import os
from datetime import datetime, timedelta

DB = "students.json"

def load():
    if not os.path.exists(DB):
        return []
    with open(DB, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save(data):
    with open(DB, "w") as f:
        json.dump(data, f, indent=2)

def visit_school():
    print("""
        Welcome to Example Public School!
        - Classrooms
        - Labs
        - Sports Ground
        - Library
        Timing: 10 AM to 4 PM (Lunch 12–1 PM)
    """)
    ch = input("Interested in admission? (yes/no): ").lower()
    if ch == "yes":
        admission()
    else:
        print("You can leave now. Thanks for visiting.")

def admission():
    print("\n--- Admission Form ---")
    name = input("Name: ")
    parent = input("Father/Mother Name: ")
    dob = input("DOB (YYYY-MM-DD): ")
    age = input("Age: ")
    aadhar = input("Aadhar: ")
    birth = input("Birth Certificate No: ")
    photo = input("Photo filename: ")
    contact = input("Contact: ")
    address = input("Address: ")

    data = load()
    adm_id = str(len(data) + 1)

    data.append({
        "id": adm_id,
        "name": name,
        "parent": parent,
        "dob": dob,
        "age": age,
        "aadhar": aadhar,
        "birth": birth,
        "photo": photo,
        "contact": contact,
        "address": address
    })

    save(data)
    print(f"Admission Successful! Admission ID: {adm_id}")

def remove_admission():
    data = load()
    if not data:
        print("No records found.")
        return

    key = input("Enter Admission ID to remove: ")

    new_data = [d for d in data if d["id"] != key]

    if len(new_data) == len(data):
        print("No such admission found.")
    else:
        save(new_data)
        print("Admission removed successfully.")

def schedule():
    print("\n--- Class Time Schedule ---")
    start = datetime.strptime("10:00", "%H:%M")
    end = datetime.strptime("16:00", "%H:%M")
    lunch_start = datetime.strptime("12:00", "%H:%M")
    lunch_end = datetime.strptime("13:00", "%H:%M")

    subjects = input("Enter subjects (comma separated): ").split(",")
    subjects = [s.strip() for s in subjects if s.strip()]

    curr = start
    i = 0

    while curr < end and i < len(subjects):
        next_time = curr + timedelta(minutes=45)

        if curr < lunch_start and next_time > lunch_start:
            print(f"{subjects[i]} (Part 1): {curr.time()} to {lunch_start.time()}")
            print(f"{subjects[i]} (Part 2): {lunch_end.time()} to {(lunch_end + (next_time - lunch_start)).time()}")
            curr = lunch_end + (next_time - lunch_start)
            i += 1
        elif curr >= lunch_start and curr < lunch_end:
            curr = lunch_end
        else:
            if next_time <= end:
                print(f"{subjects[i]}: {curr.time()} to {next_time.time()}")
            curr = next_time
            i += 1

def menu():
    while True:
        print("""
======== School System ========
1. Visit School
2. Admission
3. Remove Admission
4. Class Time Schedule
5. Exit
""")
        choice = input("Choose: ")

        if choice == "1": visit_school()
        elif choice == "2": admission()
        elif choice == "3": remove_admission()
        elif choice == "4": schedule()
        elif choice == "5":
            print("Thank you. Exiting...")
            break
        else:
            print("Invalid choice.")
            
menu()