from bs4 import BeautifulSoup
import requests
import json
import re
from multiprocessing import Pool
from datetime import datetime


def process_payment(input_pay_link, selected_card):
    session = requests.Session()

    # Fetch the HTML content from the payment link
    response = session.get(input_pay_link)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    data = {}

    # Extracting hidden input fields
    input_fields = ["merchant_reference", "language", "signature", "return_url"]
    for field in input_fields:
        input_element = soup.find("input", {"name": field})
        if input_element:
            data[field] = input_element["value"]

    # Payment URL
    url = "https://checkout.payfort.com/FortAPI/paymentPage"

    # Payment request data
    datas = {
        "expiry_date": selected_card["expiry_date"],
        "service_command": "TOKENIZATION",
        "access_code": "QbRIlPcveY8j3Hv7CxNO",
        "merchant_identifier": "abKSBKKe",
        "merchant_reference": data["merchant_reference"],
        "language": "en",
        "signature": data["signature"],
        "return_url": data["return_url"],
        "card_holder_name": selected_card["name"],
        "card_number": selected_card["number"],
        "card_security_code": selected_card["code"]
    }

    # Send the payment request
    response = session.post(url, data=datas)
    payment_response = BeautifulSoup(response.content, 'html.parser')

    # Extract the script content
    script_content = payment_response.find('script', string=re.compile('var returnUrlParams')).string

    # Extract the JSON object from the script
    match = re.search(r'var returnUrlParams = (.*?);', script_content)
    if match:
        json_str = match.group(1)
        return_url_params = json.loads(json_str)
        # Send the final request
        response = session.post(input_pay_link, data=return_url_params)
        return input_pay_link, response.url
    else:
        print("returnUrlParams not found!")
        return input_pay_link, None


def process_link(link, selected_card):
    try:
        response_url = process_payment(link, selected_card)
        if response_url and response_url[1]:
            output_line = f"{response_url[0]}\t{response_url[1]}\n"  # Add a newline character
            print(output_line, end='')  # end='' to avoid double new lines when printing
            with open("payment_info.txt", "a") as f:
                f.write(output_line)
        else:
            print(f"Failed to process {link}")
    except Exception as e:
        print(f"Error processing {link}: {e}")


if __name__ == "__main__":
    while True:
        user_input = input('Do you want to begin? yes/no : ')
        if user_input.lower() == 'yes':
            # Sample card data

            cards = [
                            {
                    "name": "MD NAZRUL ISLAM ",
                    "number": "4199501301746202",
                    "code": "246",
                    "expiry_date": "2404",
                    "remarks": "One Bank"
                },
                {
                    "name": "AYESHA BEGUM",
                    "number": "5439830410614200",
                    "code": "762",
                    "expiry_date": "2612",
                    "remarks": "Southeast "
                },
                {
                    "name": "MOHAMMAD MINHAJ UDDIN",
                    "number": "5439830331920678",
                    "code": "632",
                    "expiry_date": "2612",
                    "remarks": "Southeast"
                },
                {
                    "name": "MD MINHAJ UDDIN",
                    "number": "4520172401557913",
                    "code": "145",
                    "expiry_date": "2608",
                    "remarks": "EBL CARD"
                },
                
                {
                    "name": "ARMANUL HOQUE MAROF",
                    "number": "5439835416880358",
                    "code": "575",
                    "expiry_date": "2504",
                    "remarks": "SOUTHEAST"
                },
                {
                    "name": "PARVEZ",
                    "number": "5439835728893065",
                    "code": "935",
                    "expiry_date": "2612",
                    "remarks": "SOUTHEAST"
                },

                {
                    "name": "TAPHIM MARWAH",
                    "number": "5439830348194309",
                    "code": "775",
                    "expiry_date": "2612",
                    "remarks": "SOUTHEAST"
                },
                {
                    "name": "MOHAMMAD FORKAN",
                    "number": "4520174672457005",
                    "code": "270",
                    "expiry_date": "2501",
                    "remarks": "EBL"
                },
                    {
                    "name": "MD RAIHAN UDDIN ",
                    "number": "5439835435961940",
                    "code": "317",
                    "expiry_date": "2504",
                    "remarks": "SOUTHEST Bank"
                },


                            {
                    "name": "Minhaj ",
                    "number": "4937280037105556",
                    "code": "998",
                    "expiry_date": "2705",
                    "remarks": "Redotpay "
                },
                
                    
                                    {
                    "name": "Shanewaz sultana",
                    "number": "4937280082413301",
                    "code": "158",
                    "expiry_date": "2706",
                    "remarks": "PPPPPP"
                },
                                {
                    "name": "JAHED HOSSAIN ",
                    "number": "5439832381490321",
                    "code": "308",
                    "expiry_date": "2612",
                    "remarks": "SEBL "
                },
                            {
                    "name": "MOHAMMAD ABRAR FYSAL CHY",
                    "number": "4937280016304444",
                    "code": "168",
                    "expiry_date": "2707",
                    "remarks": "Redot Rakin"
                },
                
                        {
                    "name": "MOHAMMAD MINHAJ UDDIN",
                    "number": "4937280082396498",
                    "code": "868",
                    "expiry_date": "2711",
                    "remarks": "Redot MINHAJ 2"
                },
                        {
                    "name": "MOHAMMAD MINHAJ UDDIN",
                    "number": "4238000001440722",
                    "code": "614",
                    "expiry_date": "2906",
                    "remarks": "EBL CREDIT MINHAJ"
                },

    {
        "name": "SHAHID MONSHI",
        "number": "5439831906822406",
        "code": "169",
        "expiry_date": "2612",
        "remarks": "Sohid Southest"
    },


                   {
        "name": "JAMALA UDDIN",
        "number": "5439832401481656",
        "code": "062",
        "expiry_date": "2612",
        "remarks": "SEBL"
    },

            ]
            

            # Function to display cards and get user choice
            def choose_card(cards):
                print("Available Cards:")
                for index, card in enumerate(cards):
                    print(f"{index + 1}. {card['name']} - {card['remarks']}")
                choice = int(input("Select a card (by number): ")) - 1
                return cards[choice]

            # User selects a card
            selected_card = choose_card(cards)

            # Collect payment links from the user
            payment_links = []
            while True:
                link = input("Enter the Link (or type 'done' to finish): ").strip()
                if link.lower() == 'done' or link == '':
                    break
                payment_links.append(link)

            # Process links using multiprocessing
            with Pool(processes=4) as pool:  # Adjust the number of processes as needed
                pool.starmap(process_link, [(link, selected_card) for link in payment_links])

            # Log completion time
            now = datetime.now()
            formatted_now = now.strftime("%Y-%m-%d %I:%M:%S %p")
            completion_message = f"Done time: {formatted_now}\n\n\n"
            print(completion_message)
            with open("payment_info.txt", "a") as f:
                f.write(completion_message)

        elif user_input.lower() == 'no':
            break
        else:
            print('Type yes/no')
