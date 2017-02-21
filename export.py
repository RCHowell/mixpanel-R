#! /usr/bin/env python
#
# Modified Version of Mixpanel Python Client For Exporting Raw Data to a JSON Array by R.C. Howell
#
# Mixpanel, Inc. -- http://mixpanel.com/
#
# Python API client library to consume mixpanel.com analytics data.
#
# Copyright 2010-2013 Mixpanel, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import base64
import json
import urllib
import urllib2

class Mixpanel(object):

    ENDPOINT = 'https://data.mixpanel.com/api'
    VERSION = '2.0'

    def __init__(self, api_secret):
        self.api_secret = api_secret

    def request(self, methods, params, http_method='GET'):
        """
            methods - List of methods to be joined, e.g. ['events', 'properties', 'values']
                      will give us http://mixpanel.com/api/2.0/events/properties/values/
            params - Extra parameters associated with method
        """
        # params['format'] = format

        request_url = '/'.join([self.ENDPOINT, str(self.VERSION)] + methods)

        if http_method == 'GET':
            data = None
            request_url = request_url + '/?' + self.unicode_urlencode(params)
        else:
            data = self.unicode_urlencode(params)

        headers = {'Authorization': 'Basic {encoded_secret}'.format(encoded_secret=base64.b64encode(self.api_secret))}
        request = urllib2.Request(request_url, data, headers)
        response = urllib2.urlopen(request, timeout=120)
        return response.read()

    def unicode_urlencode(self, params):
        """
            Convert lists to JSON encoded strings, and correctly handle any
            unicode URL parameters.
        """
        if isinstance(params, dict):
            params = params.items()
        for i, param in enumerate(params):
            if isinstance(param[1], list):
                params[i] = (param[0], json.dumps(param[1]),)

        return urllib.urlencode(
            [(k, isinstance(v, unicode) and v.encode('utf-8') or v) for k, v in params]
        )

def printArr(data):
    # print json array
    print "["
    data = data.split("\n")
    data_i = len(data) - 1; # max non-null data index (element i-1 is null)
    for i in range(data_i):
        if i != 0:
            print ","
        print data[i]
    print "]"

def checkArgs():
    if len(sys.argv) != 4:
        sys.exit(
            "Usage: python ./export 'event1,event2,..' from_date to_date\n"
            "Date Format YYYY-MM-DD"
        ) #End program if improper usage

if __name__ == '__main__':
    secret = open('./secret.txt', 'r').readline()
    api = Mixpanel(api_secret=secret)
    checkArgs()
    data = api.request(['export'], {
        'event': sys.argv[1].split(","),
        'from_date': urllib2.quote(sys.argv[2]),
        'to_date': urllib2.quote(sys.argv[3])
    })
    printArr(data)


