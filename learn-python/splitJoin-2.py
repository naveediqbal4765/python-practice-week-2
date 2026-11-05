# Cleaning a tag list. Someone typed "rice, oil ,sugar " into a form. 
# Split it at the commas, strip each part and join them so it prints:

# Copy
# rice | oil | sugar

given = "rice, oil ,sugar "
splitted = given.strip().split(",")
splitted = "|".join(splitted)
print(splitted)