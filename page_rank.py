
def calculate_page_rank(PR):
	time = 0
	lambdaJump = .15 # jump rate.

	I = [1.0/len(PR) for i in PR]
	R = [0 for i in PR]

	dampening = .0001

	iteration = 0

	while(True):

		iteration += 1

		R = [lambdaJump/len(PR) for i in PR]

		for pIndex, page in enumerate(PR):
			Q = [i for i, val in enumerate(page) if val > 0 ]

			if( len(Q) > 0):
				for qIndex in Q:
					R[qIndex] = R[qIndex] + (((1 - lambdaJump)*I[pIndex])/len(Q))

			else:
				for qIndex, qPage in enumerate(PR):
					R[qIndex] = R[qIndex] + (((1 - lambdaJump)*I[pIndex])/len(PR))


		if(iteration % 10 == 0):
			print "Iteration: ", iteration
			print "I :",I 
			print "R :",R

		total = 0
		for index, val in enumerate(I):
			total = total +  abs(R[index] - I[index])

		avgDelta = (float(total)) / len(I)
		if(avgDelta < dampening):
			break
		else:
			I = R


	print(iteration)
	return(R)


if __name__ == "__main__":

	# Example from Book
	# PR = [(0,1,1),(0,0,1),(1,0,0)]

	# 3a - A -> B -> C -> D
	# PR = [(0,1,0,0),(0,0,1,0),(0,0,0,1), (0,0,0,0)]

	# 3b A links to B and C, B links to D, and C links to D
	# PR = [(0,1,1,0), (0,0,0,1), (0,0,0,1), (0,0,0,0)]

	# 3c "A -> B -> C -> D -> A"
	PR = [(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,0,0)]
	print "Results: ", calculate_page_rank(PR)

