import gspread
import pyfiglet
from colorama import Fore, Style, init

# This line is vital for Windows users to make the colors actually show up
init(autoreset=True)

# 1. CONNECT
gc = gspread.service_account(filename='credentials.json')
# Use your specific Sheet ID from the URL
sh = gc.open_by_key("10j6fMk5HsNXDyhbqJT66-zm67JDhgyJcMB1Wz05DBzU")

# 2. THE "UNIVERSAL" LOADER
# This dictionary will hold everything. 
# Example structure: { "Monsters": [data], "Weapons": [data], "Utility": [data] }
game_library = {} 

print("Loading data from Google Sheets...")

# sh.worksheets() gets a list of every tab (Monsters, Weapons, etc.)
for tab in sh.worksheets():
    print(f"  - Siphoning data from: {tab.title}...")
    
    # We grab raw values (lists) instead of records (dictionaries) to avoid the crash
    raw_rows = tab.get_all_values()
    
    # If a sheet is empty, skip it
    if not raw_rows:
        continue
        
    headers = raw_rows[0] # The first row is always headers
    tab_data = [] # This will store the clean data for this specific tab

    # Loop through the rest of the rows (skipping the header row)
    for row in raw_rows[1:]:
        entry = {}
        # We zip headers and row data together manually
        for header, value in zip(headers, row):
            # THE FIX: Only save data if the header has a name. 
            # This ignores those empty "" columns that crashed your code earlier.
            if header.strip() != "":
                entry[header] = value
        
        tab_data.append(entry)

    # Store this clean list into our main library using the tab name as the key
    game_library[tab.title] = tab_data

print("Download Complete!\n")

# ==========================================
# SEARCH ENGINE INTERFACE
# ==========================================

def search_in_category(category_name, data_list):
    print(f'Searching {category_name}')

    target = input(f"What {category_name} are you looking for?").lower().strip()

    found_match = False

    for row in data_list:
        name_in_sheet = row.get("Name", "Unknown")

        if target in name_in_sheet.lower():
            found_match = True
            print(f"\nFOUND: {name_in_sheet.upper()}")
            print('-' * 30)


            for key, value in row.items():
                if key != "Name":
                    print(f"  • {key}: {value}")

            print('-' * 30)

    if not found_match:
            print('Could not find anything matching {target} in {category_name}')

while True:


    ascii_banner = pyfiglet.figlet_format("R.E.P.O.  SEARCH", font="doom")
    print(Fore.CYAN + ascii_banner)


    print(Fore.GREEN + '\n\n===MainMenu===')

    categories = list(game_library.keys())

    for i, cat in enumerate(categories):
        print(f"{i + 1}. {cat}")
    print("q. Quit")

    selector = input('\nSelect category to search: ')

    if selector.lower() == 'q':
        print('Exiting...')
        break

    try:
        choice_index = int(selector) - 1

        if 0 <= choice_index < len(categories):
            selected_cat_name = categories[choice_index]
            selected_data_list = game_library[selected_cat_name]
            search_in_category(selected_cat_name, selected_data_list)
        else:
            print('invalid option')

    except ValueError:
        print("Please enter a valid number (or 'q' to quit).")
