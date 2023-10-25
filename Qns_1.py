# Prompt the user to enter their Fasting Blood Sugar (FBS) test result
user_fbs = float(input("Enter your Fasting Blood Sugar (FBS) in mg/dl: "))

# Define the upper limit of the normal FBS range
normal_range_max = 99  # mg/dl

# Check if the user's FBS is within the normal range
if user_fbs <= normal_range_max:
    # If the FBS is within the normal range, print a message
    print("Your Fasting Blood Sugar (FBS) is within the normal range.")
else:
    # If the FBS is higher than the normal range, print a message and advise consulting a healthcare professional
    print("Your Fasting Blood Sugar (FBS) is higher than the normal range. Please consult a healthcare professional.")
