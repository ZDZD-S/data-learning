from add_job import Job
from Register_Candidate import Candidate

def main():
    while True:
        print("\nSimple ATS")
        print("1. Add Job")
        print("2. Register Candidate")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            job = Job(title, description)  # Create a Jobt
            job.save()  # Save the job in CSV
        elif choice == "2":
            name = input("Name: ") 
            phonenumber = input("Phone Number: ")
            email = input("Email: ")
            candidate = Candidate(name, phonenumber, email)  # Create a Candidate
            candidate.save()  # Save the Candidate in CSV

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == '__main__':
    main()
