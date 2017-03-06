## Tweets Collector Based on TWARC

### Quick Start:
1. Install [TWARC](https://github.com/DocNow/twarc) first if you have not already installed.
2. Edit streaming.py, put your twitter API keys in there. (e.g. consumer_key...)
3. Edit the keywords varibale in the code, put the key words you'd like to search there.
4. run python streaming.py

### Description:
1. This code using Twitter Streaming API to search the keywords provided by us.
2. Unless you stop the code, it will keep running and put everything collected each day in a separat json file named by the date of collecting it. 
