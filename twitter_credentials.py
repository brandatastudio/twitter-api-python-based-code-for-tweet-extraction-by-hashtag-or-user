## here we also have to add our user credentials to access the twitter api, 
# just like in the json document. From here we will autorize our app
# to add the information of our credentials, in all our calls to the json file
# making the credentials secret to other people that read our code if there were

import json
import

#this are the variables that contain the user credential to access
#the twitter api we should write the credentials inside the ' ' 

Twitter_credentials = { 'ACCESS_TOKEN':'add access token here', 
'ACCESS_TOKEN_SECRET': 'add access token secret here',
'CONSUMER_KEY': 'add consumer key here ',
'CONSUMER_SECRET': 'add consumer secret here ' } 



with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(Twitter_credentials, secret_info, indent=4, sort_keys=True)
