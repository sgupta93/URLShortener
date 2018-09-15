
import redis
import base64
import hashlib
import config
import traceback

class UrlShortener:

	def __init__(self):
		self.redis = redis.StrictRedis(host=config.REDIS_HOST,
	                                   port=config.REDIS_PORT,
	                                   db=config.REDIS_DB)
	    
	def shortcode(self, url):
		try:
			encodedURL = base64.b64encode(bytes(hashlib.md5(url.encode()).hexdigest(), encoding="UTF-8"))
			return str(encodedURL.decode('UTF-8')).replace('=', '').replace('/', '_')
		except:
			traceback.print_exc()
			return None
	
	def shorten(self, url):
		code = self.shortcode(url)
		try:
			self.redis.set(config.REDIS_PREFIX + code, url)
			return {'success': True, 'url': url, 'code': code, 'shorturl': config.URL_PREFIX + code[:20]}
		except:
			traceback.print_exc()
			return {'success': False}
	
	def lookup(self, code):
		try:
			return self.redis.get(config.REDIS_PREFIX + code)
		except:
			traceback.print_exc()
			return None
