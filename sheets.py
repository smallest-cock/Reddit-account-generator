import json
import time
def add_account(account_dict):
    with open("accounts.json") as f:
        data = json.load(f)
    data['workers'][account_dict['username']] = {
        'password': account_dict['password'],
        'start_coords': [0, 0],
        'email': account_dict['email']
    }
    with open("accounts.json", 'w') as f:
        json.dump(data, f, indent=4)
    
    # Log time + account info
    named_tuple = time.localtime() # get struct_time
    print(time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple))
    print(f'Added new account credentials to accounts.json...')
    print(f"Email: {account_dict['email']}")
    print(f"Username: {account_dict['username']}")
    print(f"Password: {account_dict['password']}")