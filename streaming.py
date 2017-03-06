from twarc import Twarc
import logging
import json
import datetime
import requests


logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# put your consumer key here
consumer_key = ''

# put your consumer secret here
consumer_secret = ''

# put your access token here
access_token = ''

# put your access secret here
access_secret = ''

# the keywords you want to search
keywords = "melatonin, magnesium, theophylline, #Butler, #SundayFunday"


t = Twarc(consumer_key, consumer_secret, access_token, access_secret)

now = datetime.datetime.now
time_format = "%Y-%m-%d"


def collect():

    total = 0
    tweets = []
    time = now().strftime(time_format)
    try:
        for tweet in t.filter(track=keywords):
            tweets.append(tweet)
            total += 1
            if total % 1000 == 0:
                logging.info(time + "\n" + str(total) +
                             "tweets are collected.")
            if not now().strftime(time_format) == time:
                file_name = time + ".json"
                with open(file_name, 'w') as f:
                    json.dump(tweets, f)
                tweets = []
                time = now().strftime(time_format)

    except requests.exceptions.HTTPError as err:
        print(err)
    except KeyboardInterrupt:
        pass
    return tweets, time, total


def main():
    tweets, time, total = collect()
    if tweets:
        file_name = time + ".json"
        with open(file_name, 'w') as f:
            json.dump(tweets, f)
    print("")
    print(str(total) + " tweets are collected")


if __name__ == '__main__':
    main()
