import sys

input_filename = sys.argv[1]
num_to_accept = int(sys.argv[2])

import csv

data = []
with open(input_filename) as inputfile:
	for line in inputfile:
		data.append(line.rstrip())



candidates = []
candidate_parser = csv.reader(data[0], skipinitialspace=True)

for i in candidate_parser:
	candidates.append(i)

#print candidates
for i in range(0, len(candidates)):
	if i<len(candidates) and candidates[i] == ['', '']:
		candidates = candidates[:i] + candidates[i+1:]
candidates = candidates[1:]
for i in range(0, len(candidates)):
	candidates[i] = candidates[i][0]

vote_counts = {}
for i in range(0, len(candidates)):
	vote_counts[candidates[i]]= 0

ballots = []

for i in range(1, len(data)):
	ballot = []
	vote_parser = csv.reader(data[i], skipinitialspace=True)
	for i in vote_parser:
		if i != ['', '']:
			ballot.append(i)
	ballots.append(ballot)

for i in range(0, len(ballots)):
	for j in range(0, len(ballots[i])):
		ballots[i][j]= ballots[i][j][0]
	ballots[i] = ballots[i][1:]
#print ballots

#count the number of #1 scores
#also, keep track of which candidate each ballot's vote is assigned to. For now, each one is assigned to their #1 vote
ballot_vote_assignments = []
for i in range(0, len(ballots)):
	for score_location in range(0, len(ballots[i])):
		if ballots[i][score_location] == "1":
			vote_counts[candidates[score_location]] += 1
			ballot_vote_assignments.append(candidates[score_location])
print "Initially, vote totals are: "
print vote_counts

#only eliminate one person per round, based on this heuristic
def tiebreaker_heuristic(candidates_rankings):
	score=0
	for rank in candidates_rankings:
		score += (len(candidates)-int(rank))
	return score


#print(len(candidates), num_to_accept)

#now start eliminating canddiates and redistributing their votes
num_iterations = 0
while len(candidates) > num_to_accept:
	#first choose who to eliminate
	min_score_candidates = []
	min_score = vote_counts[candidates[0]]
	for i in candidates:
		if vote_counts[i] == min_score:
			min_score_candidates.append(i)
		elif vote_counts[i] < min_score:
			min_score = vote_counts[i]
			min_score_candidates = [i]
	print "After " + str(num_iterations) + " iterations, candidates: ", min_score_candidates, " each have " + str(min_score) + " votes." 
	
	min_heuristic_result = len(candidates)**2
	min_heuristic_candidate = ""
	min_heuristic_candidate_loc = -1
	for candidate in min_score_candidates:
		loc = -1
		scores_for_this_candidate = []
		for i in range(0, len(candidates)):
			if candidates[i] == candidate: #possible bug here-- check
				loc = i

		for i in range(0, len(ballots)):
			scores_for_this_candidate.append(ballots[i][loc])
		score = tiebreaker_heuristic(scores_for_this_candidate)
		if score < min_heuristic_result:
			min_heuristic_result = score
			min_heuristic_candidate = candidate
			min_heuristic_candidate_loc = loc
	print "Candidate " + min_heuristic_candidate + " has the lowest heuristic score, so they are eliminated."
	if vote_counts[min_heuristic_candidate] != 0:
		print "Reassigning " + str(vote_counts[min_heuristic_candidate]) + " votes." 
		for i in range(0, len(ballot_vote_assignments)):
			if ballot_vote_assignments[i] == min_heuristic_candidate:
				#reassign: assign this ballot's vote to the highest-ranked candidate who is still in the running
				next_candidate = "none"
				max_rank = 1
				while (not next_candidate in candidates) or  (next_candidate == min_heuristic_candidate):
					#print next_candidate, candidates
					for j in range(0, len(ballots[i])):
						rank = ballots[i][j]
						if int(rank) == max_rank:
							next_candidate = candidates[j]
					max_rank += 1 
				print "Assigning one vote to: ", next_candidate
				ballot_vote_assignments[i] = next_candidate
				vote_counts[next_candidate] += 1

	#clear candidate and ballots
	del vote_counts[min_heuristic_candidate]
	candidates = candidates[0:min_heuristic_candidate_loc] + candidates[min_heuristic_candidate_loc+1:]
	for i in range(0, len(ballots)):
		ballots[i] = ballots[i][0:min_heuristic_candidate_loc] + ballots[i][min_heuristic_candidate_loc+1:]
	print "After this iteration, vote totals are:" 
	print vote_counts
	print "\n"

	num_iterations += 1
	
print "The final results are:"
print vote_counts
#while len(vote_counts) > num_to_accept:
