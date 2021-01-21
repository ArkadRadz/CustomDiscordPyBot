import os

starting_currency = 1000
user_dir = "users"


def read_user_data(user_id):
    user_string = "users/" + str(user_id)
    user_cash = str(starting_currency)

    try:
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        user_cash = open(user_string, "r").read()
    except IOError:
        print("User does not have a profile, creating new storage for user " + str(user_id))
        write_user_data(str(user_id), str(starting_currency))

    return user_cash


def write_user_data(user_id, new_value):
    user_string = "users/" + user_id
    f = open(user_string, "w")
    f.write(str(new_value))
    f.close()
