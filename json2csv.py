import argparse
import csv
import json

parser = argparse.ArgumentParser(description="JSON to CSV converter")
parser.add_argument("-i", "--infile", dest="infile", help="Path to the JSON file with tweets.",
                    required=True)
parser.add_argument("-o", "--outfile", dest="outfile", required=True,
                    help="Path to the CSV file.")
args = parser.parse_args()

fields = ['id', 'created_at', 'user', 'text', 'favorite_count', 'retweet_count', 'lang', 'place']

tweets = []
with open(args.infile) as infile:
    for line in infile:
        tweet = json.loads(line)
        information = []
        for field in fields:
            if field not in tweet:
                information.append('')
            elif field == 'user':
                information.append(tweet['user']['name'])
            elif field == 'place' and tweet['place'] != None:
                information.append(tweet['place']['name'])
            else:
                information.append(tweet[field])
        tweets.append(information)

with open("args.outfile", "w") as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(fields) # write the field names as header
    csvwriter.writerows(tweets)
