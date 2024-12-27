import pdfplumber
import re 

def extract_trip_data(path):
    extracted_data = []
    trip_summary = re.compile(r'^(Trip)')

    print('hello')

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.splitlines() 

            for line in lines:
                columns = line.split()
                if trip_summary.match(columns[0]) and columns[-1] == 'km':
                    distance = float(columns[-2])

                    if distance > 0:
                        trip = columns[0] + " " + columns[1] + " " + columns[2]

                        extracted_data.append({
                            "trip": trip,
                            "distance" : distance
                        })
                
                        # print(columns)
                        # print('************************************************************************')
    return extracted_data


path = "/home/roze/Downloads/TripReport(Detail)-01December2024-07December2024.pdf"
trips = extract_trip_data(path)
for trip in trips:
    print(trips)