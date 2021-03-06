import asyncio
import aiohttp
import urllib.parse

class SetsObject(object):
	def __init__(self, _url, **kwargs):
		self.params = {'format': kwargs.get('format', 'json'), 'pretty': kwargs.get('pretty', '')}

		self.encodedParams = urllib.parse.urlencode(self.params)
		self._url = 'https://api.scryfall.com/' + _url + "&" + self.encodedParams #Find a fix for this later

		async def getRequest(client, url, **kwargs):
			async with client.get(url, **kwargs) as response:
				return await response.json()

		async def main(loop):
			async with aiohttp.ClientSession(loop=loop) as client:
				self.scryfallJson = await getRequest(client, self._url)

		loop = asyncio.get_event_loop()
		loop.run_until_complete(main(loop))

		if self.scryfallJson['object'] == 'error':
			raise Exception(self.scryfallJson['details'])

	def __checkForKey(self, key):
		try:
			return self.scryfallJson[key]
		except KeyError:
			return None

	def object(self):
		if self.__checkForKey('object') is None:
			raise KeyError('This object has no key \'object\'')

		return self.scryfallJson['object']

	def code(self):
		if self.__checkForKey('object') is None:
			raise KeyError('This object has no key \'code\'')

		return self.scryfallJson['code']

	def mtgo_code(self):
		if self.__checkForKey('mtgo_code') is None:
			raise KeyError('This object has no key \'mtgo_code\'')

		return self.scryfallJson['mtgo_code']

	def name(self):
		if self.__checkForKey('name') is None:
			raise KeyError('This object has no key \'name\'')

		return self.scryfallJson['name']

	def set_type(self):
		if self.__checkForKey('set_type') is None:
			raise KeyError('This object has no key \'set_type\'')

		return self.scryfallJson['set_type']

	def released_at(self):
		if self.__checkForKey('released_at') is None:
			raise KeyError('This object has no key \'released_at\'')

		return self.scryfallJson['released_at']

	def block_code(self):
		if self.__checkForKey('block_code') is None:
			raise KeyError('This object has no key \'block_code\'')

		return self.scryfallJson['block_code']

	def block(self):
		if self.__checkForKey('block') is None:
			raise KeyError('This object has no key \'block\'')

		return self.scryfallJson['block']

	def parent_set_code(self):
		if self.__checkForKey('parent_set_code') is None:
			raise KeyError('This object has no key \'parent_set_code\'')

		return self.scryfallJson['parent_set_code']

	def card_count(self):
		if self.__checkForKey('card_count') is None:
			raise KeyError('This object has no key \'card_count\'')

		return self.scryfallJson['card_count']

	def digital(self):
		if self.__checkForKey('digital') is None:
			raise KeyError('This object has no key \'digital\'')

		return self.scryfallJson['digital']

	def foil(self):
		if self.__checkForKey('foil') is None:
			raise KeyError('This object has no key \'foil\'')

		return self.scryfallJson['foil']

	def icon_svg_uri(self):
		if self.__checkForKey('icon_svg_uri') is None:
			raise KeyError('This object has no key \'icon_svg_uri\'')

		return self.scryfallJson['icon_svg_uri']

	def search_uri(self):
		if self.__checkForKey('search_uri') is None:
			raise KeyError('This object has no key \'search_uri\'')

		return self.scryfallJson['search_uri']
