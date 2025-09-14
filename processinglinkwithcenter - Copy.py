import requests
from bs4 import BeautifulSoup

original_centers = {
    
"Gulf Medical Centre": "A01",
"Al-Khaleej Diagnostic Centre": "A02",
"Gulshan Medicare - New Delhi": "A03",
"HEFCO, Medicare & Research Centre": "A04",
"Lama Medical Centre": "A05",
"Paramount Diagnostic Centre": "A06",
"Health Plus Diagnostic Centre": "A07",
"New Delhi Medical Centre": "A08",
"Medivisa Diagnostic Centre": "A09",
"DKH Diagnostics": "A10",
"Mayfair Diagnostic Clinic": "A11",
"Corporate Diagnostic Centre - New Delhi": "A12",
"ACE DIAGNOSTICS": "A13",
"DR SANGHI PATH LABS": "A14",
"SUMMITCARE MEDICAL CENTER": "A15",
"SYNERGY DIAGNOSTIC CENTER": "A16",
"EVERGREEN DIAGNOSTIC CENTER": "A17",
"Brand Diagnostics": "A18",
"MARKA MEDICAL CENTRE PRIVATE LIMITED": "A19",
"GULFSTAR MEDICAL CENTRE PRIVATE LIMITED": "A20",
"JP DIAGNOSTIC CENTRE": "A21",
"ATLANTIS DIAGNOSTIC CENTRE": "A22",
"PROHEALTH DIAGNOSTIC SERVICES": "A23",
"Sheetal Diagnostic Centre": "A24",
"HEFCORP DIAGNOSTIC CENTRE": "A25",
"RAKSA MEDICAL CENTER": "A26",
"PERFECT MEDICAL CENTER": "A27",
"PRIDE MEDICAL CENTER": "A28",

}


def process_payment(link):
    """
    Process the payment link and extract specific data.
    """
    try:
        response = requests.get(link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            merchant_reference = soup.find('input', {'id': 'id_merchant_reference'})
            if merchant_reference:
                return merchant_reference['value'].split('-')[1]
            else:
                return "Merchant reference not found"
        else:
            return "Failed to fetch the page"
    except Exception as e:
        return f"Error: {e}"


def generate_set_identifiers(center_names):
    """
    Generate set identifiers based on center names.
    """
    center_set_counts = {center: 0 for center in original_centers}
    output = []

    for center_name in center_names:
        if center_name in original_centers:
            center_set_counts[center_name] += 1
            set_letter = chr(64 + center_set_counts[center_name])
            set_identifier = f"{set_letter}{original_centers[center_name][1:]}"
            output.append((center_name, set_identifier))
        else:
            output.append((center_name, " "))
    return output


def process_data(data):
    """
    Process data to generate the required output.
    """
    sorted_data = sorted(data, key=lambda x: (x[0], int(x[1:])))
    results = []
    last_number = 0
    total = 0

    for index, item in enumerate(sorted_data):
        letter, number = item[0], int(item[1:])

        if index == 0:
            results.append(number)
            last_number = number
            total = number
        else:
            if letter == sorted_data[index - 1][0]:
                diff = number - last_number
                results.append(diff)
                total += diff
            else:
                transition_to_28 = 28 - total
                total = number
                results.append(transition_to_28 + number)
            last_number = number

    return results


def main_menu():
    while True:
        print("\n -----For Delhi-INDIA Center Process-----")
        print("\n1. Process Payment Links")
        print("2. Generate Set Identifiers")
        print("3. Process Data Set")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            payment_links = []
            while True:
                link = input("Enter the Link (or type 'done' to finish): ").strip()
                if link.lower() == 'done':
                    break
                payment_links.append(link)
            for link in payment_links:
                print(process_payment(link))

        elif choice == '2':
            center_names = []
            print("Enter center names (type 'done' to finish):")
            while True:
                center_name = input().strip()
                if center_name.lower() == 'done':
                    break
                center_names.append(center_name)
            identifiers = generate_set_identifiers(center_names)
            for center, identifier in identifiers:
                print(f"{identifier}")

        elif choice == '3':
            input_data = []
            print("Enter data (type 'done' to finish):")
            while True:
                data = input().strip()
                if data.lower() == 'done':
                    break
                input_data.append(data)
            output = process_data(input_data)
            for item in output:
                print(item)

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main_menu()
