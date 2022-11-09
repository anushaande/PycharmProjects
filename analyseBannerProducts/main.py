import json
import pandas
import requests

# SHEETY_API = "https://api.sheety.co/3461b4c69feeced3d329745da58320cb/bannerModulesInfo"
SHEETY_API = "https://api.sheety.co/0637ed736914ef3d8b04f4074eced431/bannerModulesInfo"

with open("C:/PycharmProjects/analyseBannerProducts/data/versions.json", "r") as versions_file:
    data = json.load(versions_file)
banner_dict = pandas.DataFrame(data)
installed = []
not_installed = []

# ToDo : get the list of products that are installed. Get their IDs, names, versions and date installed
for (index, row) in banner_dict.iterrows():
    temp_dict = {}
    for module in row["products"]["modules"]:
        temp_dict["id"] = row["products"]["id"]
        if module['installed'] != "NA":
            temp_dict["module_name"] = module['name']
            temp_dict["installed"] = module['installed']
            temp_dict["version"] = module['version']
        installed.append(temp_dict)
# ToDO : insert the results to installed excel.
installed_end_point = f"{SHEETY_API}/installed/"
for module in installed:
    try:
        info = {"installed": {"id": module["id"],
                              "name": module['module_name'],
                              "installed": module["installed"],
                              "version": module["version"],
                              }
                }
        response = requests.post(url=installed_end_point, json=info)
        response.raise_for_status()
        result = response.json()
        print(result)
    except KeyError:
        pass

# TODo : get the list of products that are not installed. Get their Ids and names.
for (index, row) in banner_dict.iterrows():
    temp_dict = {}
    for module in row["products"]["modules"]:
        temp_dict["id"] = row["products"]["id"]
        if module['installed'] == "NA":
            temp_dict["module_name"] = module['name']
            temp_dict["installed"] = module['installed']
            temp_dict["version"] = module['version']
        not_installed.append(temp_dict)

# ToDO : insert the results to installed excel.
not_installed_end_point = f"{SHEETY_API}/notinstalled/"
for module in not_installed:
    try:
        info = {"notinstalled": {"id": module["id"],
                                 "name": module['module_name'],
                                 "installed": module["installed"],
                                 "version": module["version"],
                                 }
                }
        response = requests.post(url=not_installed_end_point, json=info)
        response.raise_for_status()
        result = response.json()
        print(result)
    except KeyError:
        pass
