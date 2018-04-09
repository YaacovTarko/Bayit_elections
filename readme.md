Instant runoff voting methods for the 2018 Bayit resident elections!

Usage:
python instant_runoff.py <input_filename> <number_of_residents_to_accept>

python heuristic.py <input_filename> <number_of_residents_to_accept>

ex: python instant_runoff.py sample_input.csv 3

instant_runoff.py implements a single-transferable-vote Instant-runoff system, to prevent the multiple runoff elections we had in previous years. It relies on a heuristic to break elimination orders. That heuristic can also be used to rank candidates, as implemented in heuristic.py. 

I banged this out the morning before the election, so it's pretty messy. Please audit this code and let me know if you find any errors.