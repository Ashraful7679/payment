import requests
from bs4 import BeautifulSoup

original_centers = {


"Al-Madina Medical Services": "A01",
"Green Crescent Health Services": "A02",
"Gulshan Medicare - Dhaka": "A03",
"Saudi Bangladesh Services Company": "A04",
"Arabian Medical Center": "A05",
"Saimon Medical Centre": "A06",
"Ibn Sina Medical Check Up Unit": "A07",
"Al-Humyra Health Centre Ltd": "A08",
"Al-Riyadh Medical Check up": "A09",
"Chandshi Medical Center": "A10",
"Fairways Medical Center": "A11",
"Gulf Medical Center": "A12",
"Health Care Center": "A13",
"Life Diagnostic Center": "A14",
"Muscat Medical Center": "A15",
"Makkha Medical Center": "A16",
"Medinova Medical Services Ltd": "A17",
"National Medical Center Limited": "A18",
"Nova Medical Center": "A19",
"Pulse Medical Center": "A20",
"Pushpo Clinic": "A21",
"International Health Center": "A22",
"Al Hayatt Medical Centre": "A23",
"Ishtiyaq Medical Center": "A24",
"Al-Nahda Medical Centre": "A25",
"The Classic Medical Centre Ltd": "A26",
"Allied Diagnostics Ltd": "A27",
"Paradyne Medical Centre": "A28",
"Ibn Rushd Medical Center": "A29",
"Unique Medical Centre": "A30",
"Standard Medical Centre": "A31",
"Leading Health Check up": "A32",
"SKN Health Services": "A33",
"Transworld Medical Center": "A34",
"Dhaka Crown Medical Centre": "A35",
"Al Mubasher Medical Diagnostic Services": "A36",
"Mohaimid Medical Center": "A37",
"Orbitals Medical Centre Limited": "A38",
"Bashundhara Medical Center": "A39",
"Crystal Diagnostic": "A40",
"Rx Medical Centre": "A41",
"Tulip Medical Center": "A42",
"Al Jami Diagnostic Centre": "A43",
"LAB QUEST LIMITED": "A44",
"NAFA MEDICAL CENTRE": "A45",
"Confidence Medical Centre": "A46",
"STAR MEDICAL AND DIAGNOSTIC CENTER": "A47",
"ADVANCE HEALTH CARE": "A48",
"Kent Medical Services Ltd.": "A49",
"Malancha Medical Services Ltd.": "A50",
"Perlov Medical Services Ltd.": "A51",
"The Eureka Diagnostic & Medical Services": "A52",
"DAWA MEDICAL CENTRE": "A53",
"IBN OMAR MEDICAL AND DIAGNOSTIC CENTER": "A54",
"Moon Check-up OPC": "A55",
"Saadiq Medical Services Ltd": "A56",
"Zain Medical Limited": "A57",
"INDEX DIAGNOSTIC CENTER": "A58",
"ALIF-LAM-MIM HEALTH SERVICES LTD": "A59",
"Overseas Health Checkup Ltd": "A60",
"Smart Medical Centre": "A61",
"Safa Diagnostic Center": "A62",
"Al Arouba Medical Services P.Ltd": "A63",
"WORLD HORIZON MEDICAL SERVICES LTD": "A64",
"Sahara Medical Center": "A65",
"Khoulud Medical Check-up": "A66",
"AMIR JAHAN MEDICAL CENTER": "A67",
"Nazrul Islam Diagnostic": "A68",
"Mostafa Health Care": "A69",
"ALTASHKHIS MARKAZ LIMITED": "A70",
"PACIFIC MEDICAL & DIAGNOSTIC CENTER": "A71",
"PHOENIX MEDICAL CENTER": "A72",
"Evergreen Medical Center": "A73",
"YADAN MEDICAL": "A74",
"Paramount Medical Centre": "A75",
"Saam Health Checkup Ltd": "A76",
"Quest Medical Centre": "A77",
"ANAS MEDICAL CENTER": "A78",
"Namirah Medical Center": "A79",
"Praava Health": "A80",
"SARVOSHRESTHA MEDICAL CENTER": "A81",
"Mohammdi Healthcare Systems Pvt. Ltd.": "A82",
"AL-BAHA MEDICAL CENTER": "A83",
"SARA MEDICAL CENTER": "A84",
"MediTest Medical Services": "A85",
"RELYON MEDICARE": "A86",
"Healthcare Diagnostic Center Ltd": "A87",
"Albustan Medical Center": "A88",
"Global Medicare Diagnostics Ltd.": "A89",
"Mediquest Diagnostics Ltd": "A90",
"MEDILINE HEALTH MANAGEMENT LTD": "A91",
"M. RAHMAN MEDICAL & DIAGNOSTIC CENTER": "A92",
"Vita Health Medical Center": "A93",
"KGN Medicare Limited": "A94",
"Precision Diagnostics Ltd": "A95",
"SR Medical & Diagnostic Center": "A96",
"HASAN MEDICAL SERVICE LTD.": "A97",
"Indigo Healthcare Ltd.": "A98",
"NEW KARAMA MEDICAL SERVICES": "A99",
"MODERN MEDICAL CENTER": "A100",
"ICON MEDICAL CENTRE": "A101",
"Lotus Medical Centre": "A102",
"City Medical Centre": "A103",
"Fortune Medical Centre": "A104",
"Lifeline Medical Centre": "A105",
"Prime Medical Centre": "A106",
"AL-BARAKAH MEDICAL CENTRE LIMITED": "A107",
"AOC Medical Center": "A108",
"Medison Medical Services Limited": "A109",
"CARBON MEDICAL CENTER": "A110",
"Medifly Health Services": "A111",
"ZAM ZAM MEDICAL CENTER": "A112",
"Islamia Diagnostic Center": "A113",
"FUTURE MEDICAL": "A114",
"Zara Health Care": "A115",
"Greenland Medical Center Limited": "A116",
"City Lab": "A117",
"Union Health Center": "A118",
"Al Maktoum Health Care": "A119",
"Al Qassimi Health Care": "A120",

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
                transition_to_120 = 120 - total
                total = number
                results.append(transition_to_120 + number)
            last_number = number

    return results


def main_menu():
    while True:
        print("\n -----For Dhaka Center Process-----")
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
