#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import smtplib
import getpass

def generate_otp():
    """Generate a 6-digit OTP."""
    return ''.join(random.choices('0123456789', k=6))

def send_otp(email, otp):
    """Simulate sending the OTP to the user's email address."""
    print(f"Sending OTP {otp} to {email}...")

def prompt_otp():
    """Prompt the user to enter the OTP received in their email."""
    return input("Enter the OTP received in your email: ")

def verify_otp(otp, entered_otp):
    """Verify if the entered OTP matches the generated OTP."""
    return otp == entered_otp

def main():
    email = input("Enter your email address: ")
    
    # Generate OTP
    otp = generate_otp()
    # Simulate sending OTP
    send_otp(email, otp)
    
    # Prompt user to enter OTP
    entered_otp = prompt_otp()
    
    # Verify OTP
    if verify_otp(otp, entered_otp):
        print("Access granted!")
    else:
        print("Access denied. Incorrect OTP.")
        # Allow the user to retry OTP entry
        retry = input("Do you want to retry? (yes/no): ")
        if retry.lower() == 'yes':
            main()
        else:
            print("Thank you for using the OTP verification system.")

if __name__ == "__main__":
    main()


# In[ ]:




