import sys
import json
import string
#Initialize an array to hold all tweets and their scores


# Returns the sentiment score of a tweet
# by summing the score of all knwon words
def get_score(tweet, ks):
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

# Takes tweet file as input and returns a list of tweets
def get_tweets(tf):
	t = []
	for line in tf:
		tweet = json.loads(line)
		try:
			t.append(tweet["text"])
		except KeyError:
			continue
	return t


# returns list of tuples of each tweet and its sentiment score
def get_tweet_scores(tweets, known_scores):
	t = []
	# print str(len(tf.readlines()))
	for tweet in tweets:
		number =  get_score(tweet, known_scores)
		record = (tweet , number)	
		# # print "check"
		t.append(record)
		# print t
	return t

# takes the sent file as input and returns list of known word scores 
def get_known_scores(sent_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	return scores

# Returns dictionary of unmatching words and their estimated scores
# estimation is based on sum of all the tweet sentiment scores that the word is found in 
def unknown_words(tweet_scores, known_scores):
	new_scored_words = {}
	# for each tweet score
	for tweet_score in tweet_scores:
		tweet = tweet_score[0]
		score = tweet_score[1]
		words = tweet.split()
		#initialie list of words to hold all words in this tweet that don't have known scores
		mystery_words = []
		# for each word in the tweet
		for word in words:
			# If the word is not in known scores 
			try:
				known_scores[word]
			except KeyError:
				# add to the mystery word list list 
				mystery_words.append(word)
		# For all of the mystery words
		for word in mystery_words:
			#If the word is in the new scored words dic already then increment the score by this tweet
			try:
				new_scored_words[word] += score
			# If it's not then add it to the dic matched with the score of this tweet 
			except KeyError:
				new_scored_words[word] = score 
	return new_scored_words


def print_dic(dic):
	for word, score in dic.iteritems():
		print word, score 
	return

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    known_scores = get_known_scores(sent_file)
    tweet_file = open(sys.argv[2])
    tweets = get_tweets(tweet_file)
    hw()
    # lines(sent_file)
    # lines(tweet_file)
    # initiatlize a variable with a list of tweets and their sentiment scores
    tweet_scores =  get_tweet_scores(tweets, known_scores)
    # print tweet_scores
    new_word_scores = unknown_words(tweet_scores, known_scores)
    print_dic(new_word_scores)
 

if __name__ == '__main__':
    main()













