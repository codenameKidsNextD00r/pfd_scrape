import pdfplumber
import re

def extract_payment_data(path):
    extracted_data = []
    date_pattern = re.compile(r'^\d{1,2}$')
    month_pattern = re.compile(r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)$')
    # monetary_pattern = re.compile(r'\d+,\d+\.\d+\w?')
    # target_columns = ['Date', 'Description', 'Amount', 'Balance', 'Bank']

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.splitlines() 

            for line in lines:
                columns = line.split()
                if date_pattern.match(columns[0]) and month_pattern.match(columns[1]): #all tx lines in this particular statement start like this
                    # columns = line.split() 
                    # extracted_data.append(columns)
                    # print(columns)
                    # print('**************************************************************************************')

                    date = columns[0] + " " + columns[1]
                    description = " ".join(columns[2:-2])
                    amount = columns[-2]
                    balance = columns[-1]
         
                    # Check if amount ends with "Cr"
                    if "Cr" in amount:
                        if "Cr" in amount and "Cr" in balance:
                            extracted_data.append({
                                "date": date,
                                "description": description,
                                "amount": amount,
                                "balance": balance
                            })
    
    return extracted_data

path = "/home/roze/Downloads/GOLD_BUSINESS_ACCOUNT_105.pdf"
payments = extract_payment_data(path)
for payment in payments:
    print(payment)
