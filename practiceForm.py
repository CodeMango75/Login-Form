import random

RegID = random.randint(5000, 10000)

# Create a Log In Form for Gravity Mart.

print("Welcome to Gravity Mart, User! If you are new to this platform, you will be taken to the Registration Form which is completely Free. We hope you will enjoy your journey. Happy Shopping!")

UserValidation = input("Are you new to this platform: ").lower()

# Check if the user is a new user. If a new user, then take the registration form. If not, ask the user to sign in.

if UserValidation == "yes":
    UserName = input("Please Enter Your Full Legal Name: ")
    # If the user enters a name which is less than the length of 6
    if len(UserName) < 6:
        print("Username Too Short! Username must be at least 6 Characters")
        exit()  # Exit the program once the username is too short
    UserAge = int(input("Enter Your Age: "))
    if UserAge < 21 or UserAge > 70:
        print("We are Sorry, You are not at the legal age for sign up. Legal age is between 21 to 70 years of age")
        exit()
    Candidate_Email = input(f"Dear {UserName}, please Enter Your Email ID: ")
    # Check if Email ID is valid.
    if "@" not in Candidate_Email or "." not in Candidate_Email:
        print("Invalid Email Address Provided!")
        exit()  # Exit the Program once this error is encountered
    TermsAndConditions = input("Do You Agree to the Terms and Conditions: ").lower()
    # Terminate the program if the user does not agree to the Terms and Conditions
    if TermsAndConditions == "no":
        print("You must agree to the Terms and Conditions!")
        exit()
    elif TermsAndConditions == "yes":
        print(f"Congratulations {UserName}. You Have Successfully Registered and your Registration ID is: {RegID}")
    else:
        print("Invalid Selection! Please Select Either from Yes or No")
        exit()
elif UserValidation == "no":
    print("Please return to the Sign-In Page")
else:
    print("Invalid Answer. Please select from Yes or No")
