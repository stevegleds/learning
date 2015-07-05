def right_justify(s, p): # prints s right-justified to end at position p
	print s
	print (p - len(s)) * " " + s
right_justify('allen', 50)
