scholarships = [
    {
        "name": "GKS-U (Global Korea Scholarship)",
        "country": "South Korea",
        "field": "Any",
        "min_percentage": 80,
        "funded": "Fully Funded",
        "deadline": "October 2026",
        "description": "Korean government scholarship for undergraduate degree in South Korea. Covers tuition, accommodation, airfare and monthly stipend."
    },
    {
        "name": "MEXT Scholarship",
        "country": "Japan",
        "field": "Any",
        "min_percentage": 75,
        "funded": "Fully Funded",
        "deadline": "June every year",
        "description": "Japanese government scholarship for undergraduate studies in Japan."
    },
    {
        "name": "Underwood International Scholarship",
        "country": "South Korea",
        "field": "Any",
        "min_percentage": 90,
        "funded": "Fully Funded",
        "deadline": "February every year",
        "description": "Prestigious scholarship at Yonsei University Korea for exceptional students."
    },
    {
        "name": "DAAD Scholarship",
        "country": "Germany",
        "field": "Any",
        "min_percentage": 75,
        "funded": "Fully Funded",
        "deadline": "October every year",
        "description": "German government scholarship for studies in Germany."
    }
]

def find_scholarships():
    print("\n=== SCHOLARSHIP FINDER ===")
    percentage = float(input("Enter your percentage: "))
    country = input("Preferred country (South Korea/Japan/Germany/Any): ")
    
    print("\n--- ELIGIBLE SCHOLARSHIPS ---")
    found = False
    
    for s in scholarships:
        if percentage >= s["min_percentage"]:
            if country.lower() == "any" or country.lower() == s["country"].lower():
                print(f"\n✅ {s['name']}")
                print(f"Country: {s['country']}")
                print(f"Funding: {s['funded']}")
                print(f"Deadline: {s['deadline']}")
                print(f"Details: {s['description']}")
                found = True
    
    if not found:
        print("No scholarships found for your profile.")

def save_search(percentage, country, results_count):
    with open("search_history.txt", "a") as f:
        f.write(f"Percentage:{percentage}, Country:{country}, Scholarships Found:{results_count}\n")

def view_history():
    try:
        with open("search_history.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No search history found!")
                return
            print("\n--- SEARCH HISTORY ---")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No search history found!")

def find_scholarships():
    print("\n=== SCHOLARSHIP FINDER ===")
    percentage = float(input("Enter your percentage: "))
    country = input("Preferred country (South Korea/Japan/Germany/Any): ")
    
    print("\n--- ELIGIBLE SCHOLARSHIPS ---")
    found = False
    count = 0
    
    for s in scholarships:
        if percentage >= s["min_percentage"]:
            if country.lower() == "any" or country.lower() == s["country"].lower():
                print(f"\n✅ {s['name']}")
                print(f"Country: {s['country']}")
                print(f"Funding: {s['funded']}")
                print(f"Deadline: {s['deadline']}")
                print(f"Details: {s['description']}")
                found = True
                count += 1
    
    if not found:
        print("No scholarships found for your profile.")
    
    save_search(percentage, country, count)

def menu():
    while True:
        print("\n=== SCHOLARSHIP FINDER ===")
        print("1. Find Scholarships")
        print("2. View All Scholarships")
        print("3. View Search History")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            find_scholarships()
        elif choice == "2":
            for s in scholarships:
                print(f"\n{s['name']} | {s['country']} | Min: {s['min_percentage']}%")
        elif choice == "3":
            view_history()
        elif choice == "4":
            print("Good luck with your applications!")
            break
        else:
            print("Invalid choice!")

menu()