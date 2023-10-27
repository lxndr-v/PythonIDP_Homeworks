'''
pip  install requests, pwinput, beautifulsoup4
'''
import requests
import urllib3
import json
from pwinput import pwinput 
from bs4 import BeautifulSoup

urllib3.disable_warnings()

def gallery_auth(login, password):
    #POST to https://gallery.dev.local/api/authenticate
    headers = {'Content-Type' : "application/json"}
    url = "https://gallery.dev.local/api/authenticate"

    # Request payload
    payload = {
        "login": login,
        "password": password,
    }
    # Make the POST request
    request = requests.post(url, headers=headers, json=payload, verify=False)
    responce = request.json()
    
    # Print the response
    return responce['auth_token']

def find_employee(token, target_email):
    #GET all employees https://gallery.dev.local/api/Employees/

    employees_request = requests.get(
        url='https://gallery.dev.local/api/Employees/',
        headers={"authorization": 'Bearer '+str(token)}, 
        verify=False
    )
    employees = employees_request.json()

    # Find the JSON object with the target email
    matching_user = next((email for email in employees if email.get('Email') == target_email), None)

    # Print the result
    if matching_user:
        return matching_user
    else:
        return None
   

def quit_program():
    print("Exiting the program. Bye-bye!")
    exit()


if __name__ == "__main__":
    
    while True:
        input_type = input("How you want to provide credentials:\n\ta - from file\n\tb - from keyboard\n\tq - to quit\n>>").lower()
        
        if input_type == "a":
        #take credentials from file:
            with open("user_credentials.txt", 'r') as cred_file:
                credentials = json.load(cred_file)
            user_login = credentials['login']
            user_password = credentials['password'] 

        elif input_type == "b":
        #take credentials from keyboard: (mask for the password input)
            user_login = input("Enter your login: ")
            user_password = pwinput(prompt="Enter your password: ", mask='')
        elif input_type == "q":
            quit_program()

        email_to_search = input("Enter user email to search:\n>>")  

        token = gallery_auth(login=user_login, password=user_password)
        employee_info = find_employee(token=token, target_email=email_to_search)
        if employee_info:
            print("Found the JSON object with the target email:")

            #Cleaning JSON from HTML inside 
            profile_info_html = employee_info.get('ProfileInfo', '')
            soup = BeautifulSoup(profile_info_html, 'html.parser')
            formatted_profile_info = ' '.join(soup.stripped_strings)
            employee_info['ProfileInfo'] = formatted_profile_info
            # print(employee_info)
            print(json.dumps(employee_info, indent=2, ensure_ascii=False))

            quit_program()
        else:
            print("No JSON object found with the target email.")
            print("Try again, please...")


