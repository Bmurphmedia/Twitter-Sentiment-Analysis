import sys
import json


def sentiments(tf, ks):
	x = 0
	for line in tf:
		
		tweet = json.loads(line)
		
		try:
			# print tweet["text"]
			#call a function which gets the score of the tweet
			print score(tweet["text"], ks)
			x += 1
		except KeyError:
			continue

def get_known_scores(sent_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	return scores

def score(tweet, ks):
	# Initialize an interger to represent score
	s = 0
	# split tweet into list of words
	words = tweet.split()
	# Loop through these words
	for word in words:
		# Try to increment the score by any defined sentiment score if it exists
		try:
			s += ks[word]
		except KeyError:
			continue
	
	return s


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    known_scores = get_known_scores(sent_file)
    sentiments(tweet_file, known_scores)

if __name__ == '__main__':
    main()











