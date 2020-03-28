'''General utilities for the main shark compiler.'''

matching_dict = {
	'(':')', '[':']', '{': '}', '"': '"', "'":"'"
}


def find_matching_close(code_string, position):
	'''Takes in a string and a position, intended
	to be the position of an opening quote or bracket,
	and returns the position of the matching closing one.'''

	char = code_string[position]

	# Checking to see if legit
	if char not in matching_dict.keys():
		raise RuntimeWarning(f'Warning: {char} is not an opening character.')

	# Narrowing down the possible code to search
	# Chops off everything before the given position
	reduced_string = code_string[position : len(code_string)]

	# The POSITIONS of all currently open brackets without a matching closing one
	current_open = []

	for i in range(0, len(reduced_string)):
		# The character we're checking (can't think of a better name)
		match = reduced_string[i]

		if match in matching_dict.keys():
			# Add it to the currently_open dict
			# EXCEPT if it's a quote, because then it might
			# also be a closing character
			if match not in ["'", '"']:
				current_open.append(i)
			else:
				# Add it to the open list if the currently open
				# position doesn't match, otherwise close off
				# the currently open one
				if reduced_string[current_open[-1]] == match:
					current_open.pop()
				else:
					# We can definitely clean this repeated code up a bit.
					current_open.append(i)
		elif match in matching_dict.values():
			# If it matches the closing one, close it - otherwise, raise all hell (or maybe just an error)
			expected = matching_dict[reduced_string[current_open[-1]]]
			if match == expected:
				# Again more repeated code. Someone may need to help.
				current_open.pop()
			else:
				# Another todo: don't check matches in strings. Please.
				raise RuntimeWarning(f'Warning: expected {expected}, got {match} instead.')

		# If there are no more open brackets, return this value
		if len(current_open) == 0:
			# BUT remember that i refers to a oclation in reduced_string, not in code_string
			return i + position

	# If nothing has been returned, raise an error because there are unclosed brackets.
	raise Exception(f'Invalid string: {len(current_open)} segments still unclosed.')

# Should (and does) output 3.
print(find_matching_close('()[]', 2))
