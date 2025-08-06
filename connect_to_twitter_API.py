import contextlib
import csv
import os

import tweepy
import tweepy as tw

# Bearer Token for API v2
bearer_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# API v2 Client
client = tweepy.Client(bearer_token=bearer_token)

# Search query for my region
query = '(Frankfurt OR #Frankfurt OR "Frankfurt am Main") -is_retweet lang:de'

# Collect Tweets with date, author and text
response = client.search_recent_tweets(
    query=query,
    max_results=100,
    tweet_fields=["created_at", "author_id","text", "geo"])

tweets = response.data
# Output in Console for testing
#if tweets:
#   for tweet in tweets:
#       print(f"{tweet.created_at} | @{tweet.author_id}:\n{tweet.text}\n")
#   else:
#       print("No tweets found")

# Save Path for CSV
csv_path = "C:/Users/Sebastian/PDA/original_tweets.csv"

# Function to save data in CSV for Analysis with Pandas (also because of the data extraction cap from X)
def save_tweets_to_csv(tweets, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, mode='w', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "created_at", "author_id", "text", "geo"])
        writer.writeheader()

        for tweet in tweets:
            writer.writerow({
                "id": tweet.id,
                "created_at": tweet.created_at,
                "author_id": tweet.author_id,
                "text": tweet.text.replace("\n", " ").replace("\r", " "),
                "geo": tweet.geo
            })

    print(f"{len(tweets)} tweets saved to {save_path}")

# Just saving data if data is collected if none data is collected no file will be saved
if tweets:
    save_tweets_to_csv(tweets, csv_path)
else:
    print("No tweets saved")
