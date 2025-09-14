from bs4 import BeautifulSoup
import requests
import json
import re

while True:
    user_input = input('Do you want to Begain? yes/no : ')
    if user_input.lower() == 'yes':

        # Sample card data
        cards = [
    {
        "name": "Rakin",
        "number": "5439833125282842",
        "code": "385",
        "expiry_date": "2612",
        "remarks": "SOUTHEST"
    },
    {
        "name": "ASHRAFUL",
        "number": "4937280013986086",
        "code": "543",
        "expiry_date": "2807",
        "remarks": "Redot"
    },
    {
        "name": "ALEYA AKTER PURNIMA",
        "number": "4937280076070273",
        "code": "527",
        "expiry_date": "2808",
        "remarks": "Redot"
    },
    {
        "name": "MD MINHAJ UDDIN",
        "number": "0",
        "code": "145",
        "expiry_date": "2608",
        "remarks": "EBL CARD"
    },
    {
        "name": "ARMANUL HOQUE MAROF",
        "number": "0",
        "code": "575",
        "expiry_date": "2504",
        "remarks": "SOUTHEAST"
    },
    {
        "name": "PARVEZ",
        "number": "0",
        "code": "935",
        "expiry_date": "2612",
        "remarks": "SOUTHEAST"
    },
    {
        "name": "TAPHIM MARWAH",
        "number": "0",
        "code": "775",
        "expiry_date": "2612",
        "remarks": "SOUTHEAST"
    },
    {
        "name": "MOHAMMAD FORKAN",
        "number": "0",
        "code": "270",
        "expiry_date": "2501",
        "remarks": "EBL"
    },
        {
        "name": "MD RAIHAN UDDIN ",
        "number": "0",
        "code": "317",
        "expiry_date": "2504",
        "remarks": "SOUTHEST Bank"
    },
    {
        "name": "Minhaj ",
        "number": "0",
        "code": "998",
        "expiry_date": "2705",
        "remarks": "Redotpay "
    },
    {
        "name": "Shanewaz sultana",
        "number": "0",
        "code": "158",
        "expiry_date": "2706",
        "remarks": "PPPPPP"
    },
    {
        "name": "JAHED HOSSAIN ",
        "number": "0",
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
        "name": "MOHAMMAD ABRAR FYSAL CHY",
        "number": "5341837604509390",
        "code": "198",
        "expiry_date": "2801",
        "remarks": "Bybit Rakin"
    },
    {
        "name": "Minhaj Uddin",
        "number": "0",
        "code": "614",
        "expiry_date": "2906",
        "remarks": "EBL MINHAJ"
    },
    {
        "name": "Mohammad abrar faysal chy",
        "number": "0",
        "code": "952",
        "expiry_date": "2802",
        "remarks": "Rakin Redot 2 "
    },

    {
        "name": "SHAHID MONSHI",
        "number": "0",
        "code": "169",
        "expiry_date": "2612",
        "remarks": "Sohid Southest"
    },
    {
        "name": "DR JASHIM UDDIN CHY ",
        "number": "0",
        "code": "546",
        "expiry_date": "2911",
        "remarks": "jASHIM oNE bANK"
    },

    {
        "name": "JAMALA UDDIN",
        "number": "0",
        "code": "062",
        "expiry_date": "2612",
        "remarks": "SEBL"
    },

    {
        "name": "Shanewaz sultana",
        "number": "0",
        "code": "299",
        "expiry_date": "2802",
        "remarks": "Redot 2..."
    },

    {
        "name": "MAHEDI HASAN MUSLIM",
        "number": "0",
        "code": "006",
        "expiry_date": "2802",
        "remarks": "Redot..."
    },
    
    {
        "name": "AYESHA BEGUM",
        "number": "0",
        "code": "067",
        "expiry_date": "2802",
        "remarks": "Redot..."
    },

    {
        "name": "JAHED HOSEN",
        "number": "0",
        "code": "736",
        "expiry_date": "2802",
        "remarks": "Redot..."
    },


    {
        "name": "SALMA SONIA",
        "number": "0",
        "code": "617",
        "expiry_date": "2802",
        "remarks": "Redot..."
    },



    {
        "name": "RIFAT",
        "number": "0",
        "code": "545",
        "expiry_date": "2802",
        "remarks": "Redot..."
    },


    {
        "name": "TAPHIM MARWA",
        "number": "0",
        "code": "879",
        "expiry_date": "2802",
        "remarks": "Redot..."
    },


    {
        "name": "Minhaj Uddin",
        "number": "0",
        "code": "308",
        "expiry_date": "2802",
        "remarks": "Tevau..."
    },


    {
        "name": "Minhaj Uddin",
        "number": "0",
        "code": "903",
        "expiry_date": "3003",
        "remarks": "Tevau...2"
    },
            # Add more cards as needed
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
                return response.url
            else:
                print("returnUrlParams not found!")
                return None


        # Collect payment links from the user
        payment_links = []
        while True:
            link = input("Enter the Link (or type 'done' to finish): ").strip()
            if link.lower() == 'done' or link == '':
                break
            payment_links.append(link)

        # Process each payment link
        for link in payment_links:
            try:
                response_url = process_payment(link, selected_card)
                if response_url:
                    #output_line = f"{link}\t{response_url}\n"  # Add a newline character
                    output_line = f"{response_url}\n"  # Add a newline character

                    print(output_line, end='')  # end='' to avoid double new lines when printing
                    with open("payment_info.txt", "a") as f:
                        f.write(output_line)
                else:
                    print(f"Failed to process {link}")
            except Exception as e:
                print(f"Error processing {link}: {e}")
                

        from datetime import datetime
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