#! /usr/bin/python

import requests, simplejson, uuid
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth



my_device="Hub"
my_uuid=uuid.uuid4()
my_nick="Alex"
data={
        "method" : "actRegister",
        "id":8,
        "version":"1.0",
        "params" : [
            {
                "clientid" : my_device + ':' + str(my_uuid),
                "nickname" : my_nick + ' (' + my_device + ')',
                "level" : "private"
            },
            [
                {
                    "value" : "yes",
                    "function" : "WOL"
                }
            ]
        ]
    }

# print simplejson.dumps(data, indent=4)

host="http://192.168.1.80:80"
url=host + "/sony/accessControl"
#print url

# class PizzaAuth(AuthBase):
#     """Attaches HTTP Pizza Authentication to the given Request object."""
#     def __init__(self, username):
#         # setup any auth-related data here
#         self.username = username
#
#     def __call__(self, r):
#         # modify and return the request
#         r.headers['X-Pizza'] = self.username
#         return r

def auth(r, *args, **kwargs):
    print(r.url)
    code = raw_input('Okay, now enter the 4-digit code shown on the TV: ')
    print requests.auth.b64encode(code)
    rr= requests.get(r.url, auth=HTTPBasicAuth('', code))
#    a = requests.auth.HTTPBasicAuth("",code)
    print rr.text
    r.auth(a)
    print r.headers
    # auth = HTTPBasicAuth
    # tv_auth_header="Authorization: Basic $(echo -n ":$tv_challenge" | base64)"
    # requests.

    print code
    # request.
#    Bravia.prototype.auth = function(callback) {

#    var that = this;

#    if(!this.hasCookie()) {
#     if(true):
#
#         this.makeAuthRequest();
#
#         var rl = readline.createInterface({
#             input: process.stdin,
#             output: process.stdout
#         });
#
#         rl.question('Please enter the 4-digit code shown on your TV: ', function(challenge) {
#
#             that.makeAuthRequest(function(response) {
#                 callback();
#             }, {
#                 Authorization: 'Basic ' + new Buffer(':' + challenge).toString('base64')
#             });
#
#             rl.close();
#         });
#     } else {
#         if(callback !== undefined) {
#             callback();
#         }
#     }

#    };


r=requests.post(url, json=data, cookies={'auth': 'bb84ebaacda3c025286deab70a6444437c1cc1c7f96ca6f7a99d3ffa01ea5e49'})
print r.text
code = raw_input('Now enter the 4-digit code shown on the TV: ')
rr= requests.post(url, json=data, auth=HTTPBasicAuth('', code))
print rr.text
print rr.cookies.get('auth')

#r=requests.post(url, json=data, stream=True, hooks=dict(response=auth))
#r=requests.post(url, json=data, auth=PizzaAuth('kenneth'))
#print r.headers
#print r.cookies['auth']
# params='--trace-ascii curl.trace --include --header "$tv_auth_header"'
# cookie=$(curl $params -POST $url -d $d_str)
# | grep -o -E 'auth=([a-z0-9]+)')

# #data='{' +
# #        '"method":"actRegister",' +
#
# d_str+='"params":['
# d_str+='{"clientid":"'$my_device':'$my_uuid'",'
# d_str+='"nickname":"'$my_nick'('$my_device')",'
# d_str+='"level":"private"},'
# d_str+='[{"value":"yes","function":"WOL"}]'
# d_str+='],"id":8,"version":"1.0"'
# d_str+='}'
# echo $d_str
# #d_str=$(echo $d_str | python -m json.tool)
# echo hello5

# url="http://$tv_ip/sony/accessControl"
# params='--trace-ascii curl.trace --include --header "$tv_auth_header"'
# cookie=$(curl $params -POST $url -d $d_str)
# | grep -o -E 'auth=([a-z0-9]+)')

# requests.get()

#def makeAuthRequest(headers):
    # print(r.url)

# Bravia.prototype.makeAuthRequest = function(callback, headers) {
#
#   this.request({
#     path: '/sony/accessControl',
#     json: {
#       method: 'actRegister',
#       id: 8,
#       version: '1.0',
#       params: [
#         {
#           clientid: this.device + ':' + this.uuid,
#           nickname: this.nickname + ' (' + this.device + ')',
#           level: 'private'
#         },
#         [{
#           value: 'yes',
#           function: 'WOL'
#         }]
#       ]
#     },
#     headers: headers
#   }, function(response) {
#     if(callback !== undefined) {
#       callback(response);
#     }
#   });
#
# };
