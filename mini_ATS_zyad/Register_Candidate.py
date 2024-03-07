import csv
import os

class Candidate:
    Candidate_counter = 0
    headers = ['id', 'name', 'phone number', 'email']  # Define column names

    def __init__(self, name, phonenumber, email):
        Candidate.Candidate_counter += 1
        self.id = Candidate.Candidate_counter
        self.name = name
        self.email = email
        self.phonenumber = phonenumber
    def save(self):
        file_exists = os.path.isfile('candidate.csv')  # Check if the file already exists
        with open('candidate.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            if not file_exists:
                writer.writeheader()  # Write column names if the file does not exist
            writer.writerow({'id': self.id, 'name': self.name,'phone number': self.phonenumber, 'email': self.email})