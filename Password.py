from dotenv import load_dotenv
import os
import random
import string

def generate_otp(length=6):
    """Generate a random OTP."""
    return ''.join(random.choices(string.digits, k=length))

def authenticate():
    load_dotenv()

    # Retrieve stored security questions and answers
    security_questions = os.getenv("SECURITY_QUESTIONS").split("|")
    security_answers = os.getenv("SECURITY_ANSWERS").split("|")

    # Get username and password
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Verify username and password
    stored_username = os.getenv("USERNAME1").strip()
    stored_password = os.getenv("PASSWORD1").strip()

    if username != stored_username or password != stored_password:
        return False

    # Randomly select one security question
    index = random.randint(0, len(security_questions) - 1)
    question = security_questions[index]
    correct_answer = security_answers[index]

    # Prompt user for the selected security question
    answer = input(question + " ").strip()

    # Verify the user's answer
    if answer != correct_answer.strip():
        return False

    # Generate and display OTP
    otp = generate_otp()
    print(f"Your OTP is: {otp}")

    # Prompt user to enter OTP
    entered_otp = input("Enter OTP: ").strip()

    # Verify OTP
    if entered_otp != otp:
        return False

    return True

def main():
    if authenticate():
        print("Authentication successful.")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
