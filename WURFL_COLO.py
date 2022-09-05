# WURFL for RSAC (COLO)
# Running time - every even week, Sunday at 05:30 IL time

import os

def get_wurfl_file():
    import urllib.request
    import datetime
    week_num = datetime.date.today().isocalendar().week

    if week_num % 2 == 1:  # BOS - smaller environments
        url = "https://data.scientiamobile.com/ahfyw/wurfl.zip"
        date = datetime.date.today()
        file_name = "{}_wurfl.zip".format(date)
        print(file_name)
        urllib.request.urlretrieve(url, file_name)
        return file_name

    else:  # SLG - major environments
        print()
        # get the last WURFL file from the folder
        return "hi"


file_path = get_wurfl_file()  # maybe when download change the name to WURFL latest

# change permissions
os.chmod(file_path, 0o777)


