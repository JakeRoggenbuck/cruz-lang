# Utility tree for ASTs, etc.

class Tree:

	def __init__(self, content, children):
		self.content = content
		self.children = children

	# Output a list of all end-node children
	def ends(self):
		output = []
		for child in self.children:
			if len(child.children) == 0:
				output.append(child)
			else:
				output.extend(child.end())
		return output
