#!/usr/bin/env python

__author__ = "Rustam Mehmandarov"
__copyright__ = "Copyright 2016, The Quizzr Project"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Rustam Mehmandarov, https://github.com/mehmandarov"
__status__ = "Production"


import hashlib

"""
Returns digest of a string s.

>>> hashlib.sha1('Nobody inspects the spammish repetition').hexdigest()
531b07a0f5b66477a21742d2827176264f4bbfe2
"""
def encrypt(s):
	return hashlib.sha1(s).hexdigest()


"""
Returns True if the digest of a string s is equal to the provided digest d. Otherwise False.

>>> verify_string("Nobody inspects the spammish repetition", "531b07a0f5b66477a21742d2827176264f4bbfe2")
True
"""
def verify_string(s, d):
	if hashlib.sha1(s).hexdigest() == d:
		return True
	return False




# Examples:
digest = encrypt("Nobody inspects the spammish repetition")
print verify_string("Nobody inspects the spammish repetition", "531b07a0f5b66477a21742d2827176264f4bbfe2")
print verify_string("Test", "640ab2bae07bedc4c163f679a746f7ab7fb5d1fa")