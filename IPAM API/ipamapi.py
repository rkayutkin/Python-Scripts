#!/usr/bin/env python

import requests, urllib3, collections, re, json
from requests.auth import HTTPBasicAuth
from datetime import datetime
from pprint import pprint

log_datetime = str(datetime.now().strftime('%Y%m%d-%H%M%S'))

"""
Following Script will make API call to IPAM
"""

class PHPIPam(object):
    def __init__(self, url, user, passwd, verifySSL=True):
        self.url=url
        self.user=user
        self.passwd=passwd
        self.verifySSL=verifySSL

        if not self.verifySSL:
            # Suppress unverifies SSL cert warnign
            from requests.packages.urllib3.exceptions import InsecureRequestWarning
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        r = requests.post(url+'/user/', auth=HTTPBasicAuth(user, passwd), verify=self.verifySSL)
        self.token = r.json()["data"]["token"]

    def get_token_value(self):
        #print self.token
        return self.token

    def ipam_getIP(self, address):
        desc = ''
        host = ''
        port = ''
        response = requests.get(self.url + '/addresses/search/' + address + '/',
                                headers={'token': self.token})

        parsedjson = json.loads(response.text)

        #pprint(parsedjson)

        if 'data' in parsedjson:
            ip = response.json()["data"]
            desc = ip[0]['description']
            host = ip[0]['hostname']
            port = ip[0]['port']

            return desc, host, port
            #return(ip)
        return False

    # def variable_def(variable):
    #     """
    #     Global List of variables
    #     """
    #     global log_datetime
    #     variable_dict = {
    #         'log_file': 'ipam_' + log_datetime + '.log',
    #         'ipam_host': 'ipam.bamtech.co'
    #     }
    #     return variable_dict[variable]
