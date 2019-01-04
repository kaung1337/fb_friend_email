#-*- coding: utf-8 -*-
import json
from facepy import GraphAPI

# kaung htet zaw


api = "" # enter your token


graph = GraphAPI(api)
r = graph.get('me/friends?fields=email')

for hee in r['data']:
        if 'email' not in hee:
            continue
        mail =str(hee['id'])+" "+"==="+str(hee['email'])
        print(mail)
  
 

     
 
   
 
    
