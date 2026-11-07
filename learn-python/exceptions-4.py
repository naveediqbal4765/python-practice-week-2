# 1. Checking emails. Write clean_email(email). It strips the spaces and returns the email in lowercase, 
# but raises a ValueError if the email is blank or doesn't contain @. Loop over this list, 
# catch each error and print it:

def clean_email(email):
    email = email.lower().strip()
    
    if "@" not in email:
        raise ValueError(f"skipping {email}: doesnt contain @")
    if not email:
        raise ValueError(f"skipping {email}: email cannot be blank")
    return email

emails = [" AMNA@noorfoods.pk ", "   ", "bilal.traders"]

for email in emails:
    try:
        (clean_email(email))
    except ValueError as error:
        print(error)