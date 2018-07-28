import sys
import json 
import operator 


sentiment_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])


# Takes sentiment file and tweet file as input 
# Returns the name of the happiest state as a string

# Go through tweet file - for each tweet (object with text ):
# Determine the sentiment score and the state 

# for each state from above sum up all sentiment scores for all matching tweets
# which one is the highest 


#First lets take a look at all the tweet objects and what is there for state

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}





# when passed a location string
# if valid state, pass back state abbreviation, otherwise pass false 
def state_evaluate(location):
	words = location.split()
	for word in words:
		clean = word.strip(',')
		upper = clean.upper()
		try:
			state = states[upper]
			# print upper
			return upper
		except KeyError:
			return 0

# takes the sent file as input and returns list of known word scores 
def get_known_scores(sent_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	return scores


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


# Go through the tweet file return a dic of states and their sentiment scores 

def get_tweets(tf, ks):
	state_scores = {}
	for line in tf:
		tweet = json.loads(line)
		try:
			text = tweet["text"]
			location = tweet["user"]["location"]
			score = get_score(text, ks )
			if isinstance(location, basestring):
				state = state_evaluate(location.encode('utf-8'))
			else: 
				state = 0
		except KeyError:
			state = 0
		if state:
			try:
				state_scores[state] += score
			except KeyError:
				state_scores[state] = score
	return state_scores

def print_dic(dic):
	for word, score in dic.iteritems():
		print word, score 
	return	

def print_key_of_highest_value(stats):
	print max(stats.iteritems(), key=operator.itemgetter(1))[0]



known_scores = get_known_scores(sentiment_file)

state_scores = get_tweets(tweet_file, known_scores)

# print_dic(state_scores)
print_key_of_highest_value(state_scores)