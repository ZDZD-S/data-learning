import csv
import os

class Job:
    job_counter = 0
    headers = ['id', 'title', 'description']  # Define column titles

    def __init__(self, title, description):
        Job.job_counter += 1
        self.id = Job.job_counter
        self.title = title
        self.description = description
    
    def save(self):
        file_exists = os.path.isfile('jobs.csv')  # Check if the file already exists
        with open('jobs.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            if not file_exists:
                writer.writeheader()  # Write column titles if the file does not exist
            writer.writerow({'id': self.id, 'title': self.title, 'description': self.description})
