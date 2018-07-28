# Determine the most frequently occuring hash tag in all the tweets 

# Initialize dictionary of hash tags and their counts
# Go through all tweet data - to find hash tags do not parse text field, they are extracted by twitter 
# Identify list of hash tags for that tweet
# For each hash tag 
# if exists in dictionary increment the count by 1
# if not then add to dictionary with count of one 


# print out each hash tag and its occurences count


import sys
import json 
import operator 


tweet_file = open(sys.argv[1])


def get_popular_hashtags(tf):
	popular_hashtags = {}
	for line in tf:
		tweet = json.loads(line)
		try:
			hashtags = tweet["entities"]["hashtags"]
			# print "anything"
			if len(hashtags) > 0:
				for h in hashtags:
					text = h["text"]
					try:
						popular_hashtags[text] += 1
					except KeyError:
						popular_hashtags[text] = 1
		except KeyError:
			continue
	return popular_hashtags 

def print_result(t):
	for item in t:
		print item[0], item[1]
	return	

def get_sorted_tuples(dic):
	ordered_list = sorted(dic.items(), key=operator.itemgetter(1))
	# print_result(ordered_list)
	# return
	top_ten = ordered_list[:10]
	return top_ten


hashtags = get_popular_hashtags(tweet_file)
top_ten = get_sorted_tuples(hashtags)

print_result(top_ten)

