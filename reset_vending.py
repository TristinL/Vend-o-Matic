# This is to be used to reset the vending.json file.
# Imagine the machine gets refilled by a vendor, and they run this to reset the machine's inventory

import json
DATA = {
  "0": 5, "1": 5, "2": 5
}
USERNAME = "valleycoffeecakelionpie"
PASSWORD = "30df3556d16fabda5481d88899945e1c970972d2ed092305696d965385051e92"

#demand a username and password for security purposes
def reset_vending():
    user_credentials = input("please enter your username: ")
    pass_credentials = input("please enter your password: ")
    if user_credentials != USERNAME or pass_credentials != PASSWORD:
        print("username or password is incorrect. Please try again")

    else:
        with open("vending.json", "w") as write_file:
            json.dump(DATA, write_file)
        write_file.close()

#set to run when called in CLI
if __name__ == "__main__":
    reset_vending()