#!/usr/bin/env python3
# OPS435 Assignment 1
# check_apache_log_ckhna.py
# Author: Melanie Chu
import sys 

#Prints all filename that would be loaded
def load_logs(file_list):
    for filename in file_list:
        print(f"Loading {filename}")

#Display title with matching equal signs
def display_title(title):
    print(title)
    print("=" * len(title))

#Display main menu and proper navigation 
def main_menu():
    while True:
        display_title("Apache Log Analyser - Main Menu")
        print("1) Successful Requests")
        print("2) Failed Requests")
        print("q) Quit")
        choice = input("What would you like to do? ").strip().lower()
        if choice == "1":
            successful_request_menu()
        elif choice == "2":
            failed_request_menu()
        elif choice == "q":
            break
        else: 
            print("Invalid option. Please try again")

#Display successful request menu and proper navigation
def successful_request_menu():
    while True:
        display_title("Apache Log Analyser - Successful Requests Menu")
        print("1) How many total requests (Code 200)")
        print("2) How many requests from Seneca (IPs starting with 142.204)")
        print("3) How many requests for OPS435_Lab")
        print("q) Return to Main Menu")
        choice = input("What would you like to do? ").strip().lower()
        if choice == "1":
            total_requests_200()
        elif choice == "2":
            requests_seneca()
        elif choice == "3":
            requests_ops435()
        elif choice == "q":
            break
        else:
            print("Invalid option. Please try again") 


#Display failed request menu and proper navigation
def failed_request_menu():
    while True:
        display_title("Apache Log Analyser - Failed Requests Menu")
        print("1) How many total \"Not Found\" requests (Code 404)")
        print("2) How many 404 requests contained \"hidebots\" in the URL")
        print("3) Print all IP addresses that caused a 404 response")
        print("q) Return to Main Menu")
        choice = input("What would you like to do? ").strip().lower()    # strip() removes stray spaces, lower() lets Q and q both work

        if choice == "1":
            total_requests_404()
        elif choice == "2":
            requests_with_hidebots()
        elif choice =="3":
            ip_addresses_404()
        elif choice == "q":
            break #returns to the previous menu
        else:
            print("Invalid option. Please try again") 

#Print "Not implemented yet" for all 1,2,3 choices

#Option 1 - Successful requests menu
def total_requests_200():
    print("Not implemented yet")
#Option 2 - Successful requests menu
def requests_seneca():
    print("Not implemented yet")
#Option 3 - Successful requests menu
def requests_ops435():
    print("Not implemented yet")
#Option 1 - Failed requests menu
def total_requests_404():
    print("Not implemented yet")
#Option 2 - Failed requests menu
def requests_with_hidebots():
    print("Not implemented yet")
#Option 3 - Failed requests menu
def ip_addresses_404():
    print("Not implemented yet")

# Entry point: read the arguments, load the log files
if __name__ == '__main__':
    arg = sys.argv[1:]
#Condition 1: No argument
    if not arg:
        print("Invalid argument")
        sys.exit(1)
    elif arg[0] in ["-d", "--default"]:
#Condition 2: With -d or --default but no filenames provided after
        if len(arg) < 2:
            print("Error: No filenames provided.")
            sys.exit(1)
#Condition 3: With -d or --default with filenames provided after
#Print all filenames and execute the "How many total requests (Code200)".
        load_logs(arg[1:])
        total_requests_200()
#Condition 4: Filenames provided, print all filenames and main menu
    else:
        load_logs(arg)
        main_menu()


