import sys
import json
#The frequency of a term can be calculated as [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]

# Initialzie a dictionary that will contain all disctinct words in all tweets as well as the counter of all occurences of that word
# Initialize an integer that will count all occurences of all words in all tweets
# Go through each line of file
# For each tweet (defined as "text" properties of objects)
# Go through each word (defined as the text split by spaces)
# for every word - increment the counter for all words
# if the word is not in dictionary yet then add it with a count of one
# if it is in the dictionalry then increment the count by 1 

# Iterate through the resulting dictionary from above 
# print each word as well as the count of occurences of that word divided by counter from above (round to 3 decimals )




file = open(sys.argv[1])

def lines(fp):
    print str(len(fp.readlines()))

def get_tweet_word_counts(file):
	word_counts = {}
	total_word_occurences = 0
	for line in file:
		data = json.loads(line)
		try:
			words = data["text"].split()
		except KeyError:
			continue 
		for word in words:
			total_word_occurences += 1
			try:
				word_counts[word] += 1
			except KeyError:
				word_counts[word] = 1
	return word_counts, total_word_occurences


def print_frequency(word_counts, twc):
	for key, value in word_counts.iteritems():
		frequency = value / float(twc)
		# string = "{:.1f}".format(frequency)
		# print key, round(frequency, 4)
		print key, frequency
	



word_count_info = get_tweet_word_counts(file)
word_counts = word_count_info[0]
total_word_occurences = word_count_info[1]

print_frequency(word_counts, total_word_occurences)






