#!/usr/bin/env python2.7
from ipamapi import PHPIPam
import requests, base64, urllib3, collections, re, json, sys, csv, os, re, argparse, itertools
import ConfigParser as configparser
from requests.auth import HTTPBasicAuth
from pprint import pprint
from datetime import datetime

# from openpyxl import Workbook
log_datetime = str(datetime.now().strftime('%Y%m%d-%H%M%S'))
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

os.system('clear')

def variable_def(variable):
    """
    Global List of variables
    :param variable:
    :return:
    """
    global log_datetime
    variable_dict = {
        'log_file': 'ipam_' + log_datetime + '.log',
        'ipam_host': 'xxxx',
        'ipam_api_name': 'netadmin'
    }

    return variable_dict[variable]

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', help='provide CSV file', type=str)
    parser.add_argument('--action', help='reserve or delete', choices=['reserve','delete'],type=str, required=True)
    #parser.add_argument('--ip', help='ip', type=str)
    #parser.add_argument('--debug', help='enable debug', action='store_true')

    args = parser.parse_args()

    if args.action:
        action = args.action
    # if args.debug:
    #     debug = args.debug
    # else:
    #     debug = False

    if action == 'reserve':
        if args.inputfile:
            csv_file = args.inputfile
            updateFile = csv_file[:-4] + "_Update.csv"
            #open(updateFile, 'a').close()
            #print updateFile
            if not os.path.isfile(csv_file):
                print('ERROR: File was not found: ' + csv_file)
                sys.exit(1)
        else:
            print('--inputfile is REQUIRED with action=reserve')
            sys.exit(1)

    # if action == 'delete':
    #     if args.ip:
    #         ip_to_delete = args.ip
    #     else:
    #         print('--ip is REQUIRED when using action=delete')
    #         sys.exit(1)

    # Setting up Env.
    # export CRED=~/.cred OR
    # env CRED=~/.cred
    cred_file = os.environ.get('CRED')

    if not cred_file:
        print('ERROR: Please Set CRED EX: env CRED=~/cred')
        sys.exit(1)

    if not os.path.isfile(cred_file):
        print('ERROR: File Not Found. Check CRED env var path')
        sys.exit(1)

    # pull in cred variables
    config = configparser.RawConfigParser()

    config.read(cred_file)

    username = config.get("ipamauth","user")
    password = config.get("ipamauth","pass")

    ipam_url = 'https://' + variable_def('ipam_host') + '/api/' + variable_def('ipam_api_name')
    ipam = PHPIPam(ipam_url, username, password, verifySSL=False)

    token = ipam.get_token_value()
    #filename = "MD3_NAT_Update.csv"

    if action == 'reserve':
        print ("Making an API call to Python and gathering data!!!\n")

        # Find list of VLANs need to find subnets
        cwd = os.getcwd()
        data = csv.DictReader(open(cwd + "/" + csv_file, 'r'))
        data2 = []
        for i in data:
            #print "IP: " + i['Internal_IP']
            check = ipam.ipam_getIP(i['Internal_IP'])
            #write_file = csv.writer(open(filename, 'w'),lineterminator='\n')
            if check:
                desc, host, port = ipam.ipam_getIP(i['Internal_IP'])
                i['Description'] = desc
                i['Hostname'] = host
                i['Port'] = port
                data2.append(i)

#print data2
print ("Generating the updated file with gathered data!!!\n")

keys = data2[0].keys()

with open(updateFile, 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data2)

print ("The CSV 'Update' file was generated!!!\n")
