import csv

def write_to_file(data):
    with open('database/database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database/database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter =',', quotechar='"',quoting=csv.QUOTE_NONE)

        csv_writer.writerow([email,subject,message])