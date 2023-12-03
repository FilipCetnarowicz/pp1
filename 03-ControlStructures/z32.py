# Survey Questions
question1 = "Are you interested in computer science? (Y/N): "
question2 = "Do you like playing computer games? (Y/N): "
question3 = "Do you have an Instagram account? (Y/N): "

# Initialize variables to store survey responses as booleans
response1 = bool(input(question1).upper() == 'Y')
response2 = bool(input(question2).upper() == 'Y')
response3 = bool(input(question3).upper() == 'Y')

# Display Survey Results
print("\nSurvey Results:")
print(f"Interested in computer science: {'Yes' if response1 else 'No'}")
print(f"Playing computer games: {'Yes' if response2 else 'No'}")
print(f"Has an Instagram account: {'Yes' if response3 else 'No'}")
