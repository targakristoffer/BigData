from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import json


ckey="9dTrk09s8pR2qoEmgqulWeULV"
csecret="0CmbfXpvWGrpk9sqsolyj5gzj6y0yIiKOo92l3vZGFHQdnlK8c"
atoken="985614332590424065-5la3nVJVxT9KaKeHlfds0FvsZi7YpdE"
asecret="4Plal7AhC48BOckIQ9VTcasrZd1cUWt5UzLoPaBAe1RXz"




class TwitterHelper():

    def __init__(self):
        super().__init__()
        
        self.auth = OAuthHandler(ckey, csecret)
        self.auth.set_access_token(atoken, asecret)



    def get_tweet(self, keyword):

        numberOfLines = 50
        tweetConn = TwitterConn(numberOfLines)

        twitterStream = Stream(self.auth, tweetConn)
        try:
            twitterStream.filter(track=[keyword], async=True)
        except ReadTimeoutError:
            TwitterConn.disconnect()
            print('[+] READTIMEOUTERROR')
        except a >= self.file_len("twitter-out.text"):
            TwitterConn.disconnect()
            print('[+]other exception ')
        

    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1



class TwitterConn(StreamListener):
    def __init__(self, numberOfLines):
        super().__init__()
        self.numberOfLines = numberOfLines
        
       

    def on_data(self, data):

        

        try:

            all_data = json.loads(data)
            tweet = all_data["text"]

            output = open("twitter-out.txt", "a")
            output.write(tweet)
            output.write('/n')
            output.close()

            return True

    
            
            
    
        except:
            if self.numberOfLines <= TwitterHelper.file_len("twitter-out.txt"):
                print('[+] other exception')    
                return False

            print(TwitterHelper.file_len("twitter-out.txt"))
            return True
        



    def on_error(self, status):
        output.close()
        print(status)
        if(status == 420):
            return False

    def on_status(self, status):
        print(status.text)

    



