#!/usr/bin/env python3
import requests,json
from sys import*

def m(a, *b):
	t, *o = argv[1:]
	j = {
	    "title":    t,
	    "options":  o,
	    "dupcheck": False,
	}
	j = json.dumps(j)
	p = requests.post("https://strawpoll.me/api/v2/polls", data=j, headers={"Content-Type":"application/json"})
	return p