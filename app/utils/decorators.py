from flask import session, redirect, url_for, request, flash
from functools import wraps

def errorhandle(route):
	"""Returns a 500 JSON upon any error"""	

	@wraps(route)
	def wrapper(*args, **kwargs):
		try:
			route(*args, **kwargs)
		except:
			return {"status":500}
	return wrapper
