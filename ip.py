from urllib import urlopen

IP_LOOKUP_URL = "http://myip.xname.org/"

def ip_lookup():
	return urlopen(IP_LOOKUP_URL).read().strip()
