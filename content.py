class Content(object):
	""" Content is the object for the news itself """
	def __init__(self, param_dictionary):
		self.title = param_dictionary['title']
		self.body = param_dictionary['body']
		self.url = param_dictionary['url']

		# TODO:
		# self.url_recommendations = []	