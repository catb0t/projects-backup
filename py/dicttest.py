
class Obj(object):

	def __init__(self):
		self.val = 0

	def increment(self, amt):
		self.val += amt

	def decrement(self, amt):
		self.val -= amt

	def default(self):
		self.val = -9999999999999999999999999999999999999999

obj = Obj()

while True:
	func, args = {
		'a': (obj.increment, (1,)),
		'b': (obj.decrement, (1,)),
	}.get(input(), (obj.default, (1,)))

	func(*args)

	print(obj.val)
