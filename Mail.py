from jinja2 import Template

class Mail:
	'''
	A class to represent a mail object
	'''
	def __init__(self,template, variables = {}, retryLimit = 3):
		'''
		Accepts the template string, the variables dictionary, and retryLimit
		'''
		self.template = template
		self.variables = variables
		self.retryLimit = retryLimit
	
		self.subject = variables["$$_SUBJECT_"] if "$$_SUBJECT_" in variables else ""
		self.receivers = variables["$$_RECEIVERS_"] if "$$_RECEIVERS_" in variables else ""
		
		self.generateContent()
	
	def generateContent(self):
		'''
		The function that mixes the templates and the variables
		'''
		template = Template(self.template)
		self.content = template.render(**self.variables)
		return self.content
	
	def preview(self):
		'''
		The function will be used to preview the mail in the browser
		'''
		pass
