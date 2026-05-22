#!/usr/bin/python3

print('\n')
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

full_name = f"{first_name} {last_name}"

message = f"\nHello, {full_name.title()}!\n\nSince our last letter to you the market has  moved\nsignificantly in line with our predictions.\n\nNow is the perfect time to subscribe and stay ahead of the\ncompetition in the money race to crypto millionaire status.\n\nSincerely your's\nJon Maccabee"
print(message)

print('\n')
print("-" * 64, '\n')

message = f"""
Hello, {full_name.title()}!

Since our last letter to you the market has  moved
significantly in line with our predictions.

Now is the perfect time to subscribe and stay ahead of the
competition in the money race to crypto millionaire status.

Sincerely yours
Jon Maccabee
"""
print(message)