# 1. Library Book Tracker
def add_book(library):
    print("\n----- Add Book -----")
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    while True:
        try:
            pages = int(input("Enter the number of pages: "))
            if pages > 0:
                break
            else:
                print("Number of pages must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer for the number of pages.")

    book = {
        "title": title,
        "author": author,
        "pages": pages
    }
    library.append(book)
    print(f"\nBook '{title}' by {author} added successfully.")
    return library


def find_book(library):
    print("\n--- Find Book ---")
    title_to_find = input("Enter the title of the book to find: ")
    found = False

    for book in library:
        if book["title"].lower() == title_to_find.lower():
            print("\nBook found!")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Pages: {book['pages']}")
            found = True
            break

    if not found:
        print(f"\nBook with title '{title_to_find}' not found.")


def show_books(library):
    print("\n--- Show Books ---")
    if not library:
        print("The library is empty.")
    else:
        for book in library:
            print(f"\n- Title: {book['title']}")
            print(f"  Author: {book['author']}")
            print(f"  Pages: {book['pages']}")


# 2. Student Grade Manager

grades={}
def add_student(name:str):
    grades[name]=[]
    
def add_grade(name:str,grade:float):
    grades[name].append(grade)
    

def get_average(name:str):
    average= sum(grades[name])/len(grades[name])
    return (average)



# 3. Restaurant menu editor
menu = []

def add_dish():
    name = input("Dish name: ").strip()
    try:
        price = float(input("Price: "))
        available = input("Is it available? (yes/no): ").strip().lower() == "yes"
        menu.append({"name": name, "price": price, "available": available})
        print("Dish added.")
    except ValueError:
        print("Invalid price.")

def update_availability():
    name = input("Dish name: ").strip().lower()
    for dish in menu:
        if dish["name"].lower() == name:
            dish["available"] = not dish["available"]
            print("Availability updated.")
            return
    print("Dish not found.")

def count_available_dishes():
    count = sum(1 for dish in menu if dish["available"])
    print(f"Total available dishes: {count}")

def restaurant_menu():
    while True:
        print("\n--- RESTAURANT MENU EDITOR ---")
        print("1. Add dish")
        print("2. Toggle availability")
        print("3. Count available dishes")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_dish()
        elif choice == "2":
            update_availability()
        elif choice == "3":
            count_available_dishes()
        elif choice == "0":
            break
        else:
            print("Invalid option.")
restaurant_menu()

# 4. Warehouse Box Counter
warehouse={}
def add_box(name:str,quantity:int):
    warehouse[name]=[]
    warehouse[name].append(quantity)

def update_quantity(name:str,quantity:int):
    warehouse[name]=[quantity]

def has_enough(name:str,quantity:int):
    if warehouse[name][0] <= quantity:
        return True
    else:
        return False 
    
    
# 5. Movie rating system
movies = []
# Add a new movie to the list
def add_movie():
    title = input("Enter the movie title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    for movie in movies:
        if movie['title'].lower() == title.lower():
            print("This movie already exists.")
            return
    movies.append({'title': title, 'ratings': []})
    print(f"Movie '{title}' added successfully.")
    
    
# 6. Online Course Tracker
def register_course(courses):
    print("\n--- Register Course ---")
    title = input("Enter the course title: ")
    duration = input("Enter the course duration: ")
    while True:
        try:
            enrolled = int(input("Enter the number of enrolled students: "))
            if enrolled >= 0:
                break
            else:
                print("The number of enrolled students must be a non-negative integer.")
        except ValueError:
            print("Invalid number. Please enter an integer.")

    course = {
        "title": title,
        "duration": duration,
        "enrolled": enrolled
    }
    courses.append(course)
    print(f"\nCourse '{title}' registered successfully.")
    return courses


def update_enrollment(courses):
    print("\n--- Update Enrollment ---")
    title = input("Enter the title of the course to update enrollment: ")
    while True:
        try:
            change = int(input("Enter the number to add (positive) or remove (negative) from enrollment: "))
            break
        except ValueError:
            print("Invalid number. Please enter an integer.")

    for course in courses:
        if course["title"].lower() == title.lower():
            course["enrolled"] += change
            print(f"\nNumber of enrolled students in '{course['title']}' updated. New total: {course['enrolled']}")
            return courses

    print(f"\nNo course found with title '{title}'.")
    return courses


def filter_by_duration(courses):
    print("\n--- Filter by Duration ---")
    max_duration = input("Enter the maximum duration to filter (e.g., '10 weeks', '3 months'): ")

    print(f"\nCourses with a maximum duration of {max_duration}:")
    for course in courses:
        if course["duration"] <= max_duration:
            print(f"- {course['title']} ({course['duration']})")
            
            
# 7. To do list organizer
tasks = []

def add_task():
    desc = input("Task description: ").strip()
    priority = input("Priority (low/medium/high): ").lower()
    tasks.append({'desc': desc, 'priority': priority, 'done': False})
    print("Task added.")

def mark_done():
    desc = input("Task to mark as done: ").strip()
    for task in tasks:
        if task['desc'].lower() == desc.lower():
            task['done'] = True
            print("Marked as completed.")
            return
    print("Task not found.")

def filter_tasks():
    print("1. Filter by priority")
    print("2. Filter by status")
    opt = input("Choose: ")
    if opt == "1":
        level = input("Priority level: ").lower()
        for task in tasks:
            if task['priority'] == level:
                print(task)
    elif opt == "2":
        status = input("Status (done/pending): ").lower()
        for task in tasks:
            if (status == "done" and task['done']) or (status == "pending" and not task['done']):
                print(task)

def todo_menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Mark as Done")
        print("3. Filter Tasks")
        print("4. Exit")
        opt = input("Choose: ")
        if opt == "1":
            add_task()
        elif opt == "2":
            mark_done()
        elif opt == "3":
            filter_tasks()
        elif opt == "4":
            break
todo_menu()


# 8. Digital Wallet
expenses = []

def add_expense():
    category = input("Enter category (e.g. food, transport, etc.): ").strip()
    try:
        amount = float(input("Enter amount: "))
        expenses.append({"category": category, "amount": amount})
        print("Expense added.\n")
    except ValueError:
        print("Invalid amount.\n")

def total_spent():
    total = sum(e["amount"] for e in expenses)
    print(f"Total spent: ${total:.2f}\n")

def expense_percentages():
    total = sum(e["amount"] for e in expenses)
    if total == 0:
        print("No expenses recorded.\n")
        return

    category_totals = {}
    for e in expenses:
        category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]

    for category, amount in category_totals.items():
        percent = (amount / total) * 100
        print(f"{category}: {percent:.2f}%")
    print()

# Menu
def menu():
    while True:
        print("1. Add Expense")
        print("2. Total Spent")
        print("3. Expense Percentages")
        print("4. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            add_expense()
        elif option == "2":
            total_spent()
        elif option == "3":
            expense_percentages()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu()


# 9. Pet Adoption Center
pets = []

def add_pet():
    name = input("Name: ").strip()
    species = input("Species: ").strip()
    try:
        age = int(input("Age: "))
        if age < 0:
            raise ValueError
        pets.append({'name': name, 'species': species, 'age': age})
        print("Pet added.")
    except ValueError:
        print("Invalid age.")

def search_species():
    specie = input("Species to search: ").strip()
    for pet in pets:
        if pet['species'].lower() == specie.lower():
            print(pet)

def filter_by_age():
    try:
        max_age = int(input("Max age: "))
        for pet in pets:
            if pet['age'] <= max_age:
                print(pet)
    except ValueError:
        print("Invalid age.")

def pet_menu():
    while True:
        print("\n--- Pet Adoption Center ---")
        print("1. Add Pet")
        print("2. Search by Species")
        print("3. Filter by Age")
        print("4. Exit")
        opt = input("Choose: ")
        if opt == "1":
            add_pet()
        elif opt == "2":
            search_species()
        elif opt == "3":
            filter_by_age()
        elif opt == "4":
            break
pet_menu()


# 10. Gym Membership System
def register_member(members):
    print("\n--- Register Member ---")
    name = input("Enter the member's name: ")
    plan = input("Enter the membership plan (e.g., 'monthly', 'annual'): ")
    member = {
        "name": name,
        "plan": plan,
        "payment_due": True
    }
    members.append(member)
    print(f"\nMember '{name}' registered with plan '{plan}'.")
    return members


def change_plan(members):
    print("\n--- Change Membership Plan ---")
    name = input("Enter the name of the member whose plan you want to change: ")
    new_plan = input("Enter the new membership plan: ")

    for member in members:
        if member["name"].lower() == name.lower():
            member["plan"] = new_plan
            print(f"\nMembership plan of '{member['name']}' changed to '{new_plan}'.")
            return members

    print(f"\nNo member found with name '{name}'.")
    return members


def unpaid_members(members):
    print("\n--- Show Unpaid Members ---")
    print("\nMembers with unpaid dues:")
    for member in members:
        if not member["payment_due"]:
            print(f"- {member['name']} ({member['plan']})")