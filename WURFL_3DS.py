# WURFL for BOS and SLG (both 1.0 and 2.0)
# another code is needed for RSAC (COLO) - needs to run at the same week with BOS
# Running time - every Sunday at 05:30 IL time

import os
import urllib.request
import datetime


# ask mart how to get the file from the internet to the 3DS env
def get_wurfl_file():
    week_num = datetime.date.today().isocalendar().week

    if week_num % 2 == 1:  # BOS - smaller environments
        url = "https://data.scientiamobile.com/ahfyw/wurfl.zip"
        date = datetime.date.today()
        file_name = "{}_wurfl.zip".format(date)
        print(file_name)
        urllib.request.urlretrieve(url, file_name)
        return file_name

    else:  # SLG - major environments
        # get the last WURFL file from the folder
        return "hi"


# file_path = get_wurfl_file()  # maybe when download change the name to WURFL latest
file_path = "/tmp/files"  # delete
date = datetime.date.today()
file_name = "{}_wurfl.zip".format(date)
# os.chmod(file_path, 0o777)
file_dest = "/cype_home/central_config/mobile/" + file_name
print(file_dest)
# os.replace(file_path, file_dest)
comm = '/cype_home/runtime/commn/bin/WurflXmlTester -zip_path /cype_home/central_config/mobile/' + file_name + ' wurfl.xml'
output = os.popen(comm)
if 'ERROR' in output:
    print('Error')
    # send email to mart

