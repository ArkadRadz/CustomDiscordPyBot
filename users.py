import utils
from datetime import date
import json

starting_currency = 1000
user_dir = "users"


def read_user_data(user_id):
    user_string = user_dir + "/" + str(user_id)
    user_cash = str(starting_currency)
    user_data = {"cash": str(user_cash), "last_daily": str(date.today())}

    utils.check_if_dir_exists(user_dir)
    if utils.check_if_file_exists(user_string):
        with open(user_string) as json_file:
            user_data = json.load(json_file)
    else:
        print("User does not have a profile, creating new storage for user " + str(user_id))
        f = open(user_string, "w")
        f.write("temp")
        f.close()
        with open(user_string, "w") as json_file:
            json.dump(user_data, json_file)

    return user_data


def write_user_data(user_id, new_value):
    utils.check_if_dir_exists(user_dir)
    user_string = user_dir + "/" + user_id
    utils.check_if_dir_exists(user_dir)
    if utils.check_if_file_exists(user_string):
        with open(user_string, "r+") as json_file:
            final_data = {}
            user_data = json.load(json_file)
            json_file.seek(0)
            json_file.truncate(0)
            if "cash" in new_value:
                final_data["cash"] = new_value["cash"]
            else:
                final_data["cash"] = user_data["cash"]

            if "last_daily" in new_value and new_value["last_daily"] != user_data["last_daily"]:
                final_data["last_daily"] = new_value["last_daily"]
            else:
                final_data["last_daily"] = user_data["last_daily"]
            json.dump(final_data, json_file)
            json_file.close()
    #
    # f = open(user_string, "w")
    # f.write(str(new_value))
    # f.close()
