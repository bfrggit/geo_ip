from urllib import urlopen

GEO_IP_LOOKUP_URL = "http://ip-api.com/json"

def geo_ip_lookup(ip_address = None):
	lookup_url = GEO_IP_LOOKUP_URL
	if ip_address is not None:
		if type(ip_address) != type("") and type(ip_address) != type(u""):
			raise TypeError
		lookup_url += "/" + ip_address
	return urlopen(lookup_url).read().strip()
	