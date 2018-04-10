import sys

input_filename = sys.argv[1]
num_to_accept = -1
if len(sys.argv) > 2:
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

for i in range(0, len(candidates)):
	if i<len(candidates) and candidates[i] == ['', '']:
		candidates = candidates[:i] + candidates[i+1:]
for i in range(0, len(candidates)):
	candidates[i] = candidates[i][0]
candidates = candidates[1:]
vote_counts = {}
for i in range(0, len(candidates)):
	vote_counts[candidates[i]]= []

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

def counting_heuristic(candidates_rankings):
	score=0
	for rank in candidates_rankings:
		score += (len(candidates)-int(rank))
	return score

def heuristic_compare(candidate1, candidate2):
	return counting_heuristic(vote_counts[candidate1]) - counting_heuristic(vote_counts[candidate2])

for ballot in ballots:
	for i in range(0, len(ballot)):
		vote_counts[candidates[i]].append(ballot[i])

candidates.sort(cmp=heuristic_compare)

if num_to_accept > 0:
	for candidate in candidates[-num_to_accept:]:
		print candidate, counting_heuristic(vote_counts[candidate])
else:
	for candidate in candidates:
		print candidate, counting_heuristic(vote_counts[candidate])
