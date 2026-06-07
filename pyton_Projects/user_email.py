# Action Function
def user_log(message: str)-> None:
    """
        Store the user data in app.log file.
        Args:
            message (str): The message to be logged.
        Returns:
            None
    """
    with open(R"F:\DATA SCIENCE 2\PYTHON\app.log","a") as file:
        file.write(message + "\n")

# validation function
def is_valid_email(email: str)-> bool:
    """
        Check the valid email that user entered.
        Args:
            email (str): The email entered by user.
        Return:
            True Or False
    """
    return "@" in email and "." in email

# Transformation function
def clean_user_email(email: str)-> dict:
    """
        Clean the user email.
        Args:
            email (str): The email entered by user.
        Tranformation:
            1. Strip the email of leading and trailing whitespace.
            2. Convert the email to lowercase.
            3. Split the emaail into username and domain.
            
        Return:
            username (dict): split email and take user name from it.
            domain (dict): split email and take user domain from it.
    """
    clean_email = email.strip().lower()
    username, domain = clean_email.split("@") 
    return {"username":username, "domain":domain}

# ochestration Function
def user_email_validation(email):
    """
        The main function to validate the user emial and log the process.
        Args:
            email (str): The email entered by user.
        Return:
            None
    """
    user_log("App Start")
    if not is_valid_email(email):
        user_log(f"invalid Email: {email}")
    else:
        p_email = clean_user_email(email)
        user_log(f"processed Email: {p_email}")
    user_log("App Stoped")


email = input("Enter your email: ")
user_email_validation(email)






