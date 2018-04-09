Instant runoff voting methods for the 2018 Bayit resident elections!

Usage:
python instant_runoff.py <input_filename> <number_of_residents_to_accept>

python heuristic.py <input_filename> <number_of_residents_to_accept>

ex: python instant_runoff.py sample_input.csv 3

instant_runoff.py implements a single-transferable-vote system with instant runoffs, to prevent the multiple runoff elections we had in previous years. It relies on a heuristic to break ties in the elimination order. That heuristic can also be used to rank candidates, as implemented in heuristic.py. 

instant_runoff.py will provide the canonical results of the election, while heuristic.py is intended for a sanity check of the results.

Feel free to audit this code and let me know if you find any errors.