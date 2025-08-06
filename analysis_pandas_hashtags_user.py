import pandas as pd
import re
from collections import Counter

# read the previous created CSV
df = pd.read_csv("C:/Users/Sebastian/PDA/original_tweets.csv")

print(df.head())

# most active user count
mostactive_user = df["author_id"].value_counts().head(10)

print("Top 10 User:")
print(mostactive_user)

# extraction of hashtags
all_text = df["text"].dropna().tolist()

hashtags = []
for text in all_text:
    hashtags += re.findall(r"#\w+", text.lower())

# top 5 hashtags
top_hashtags = Counter(hashtags).most_common(5)

print("Top 5 Hashtags:")
for tag, count in top_hashtags:
    print(f"{tag}: {count}")
