import re


class SR(object):
	
	def __init__(self,response_string,id):
		self._response_string = response_string
		self._id = id
		pass


class Collection(object):

	def __init__(self, array):
		self._itemArray = array


sr = Collection([
	SR("abc",1),
	SR("bca",2),
	SR("bba",3),
	SR("baa",4),
	SR("cdc",5),
	SR("acc",6)
	])

for (i, i_sr) in enumerate(sr._itemArray):
	if i == 0:
		print "I = 0"
		p = re.compile('a+c')
		continue
	if p.match(i_sr._response_string):
		print "Mathced "+str(i_sr._id)
	