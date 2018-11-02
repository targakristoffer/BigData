from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import json


ckey="2AvbG84msbL34BEHslMsWZTUR"
csecret="gzEENqmZoMl2hhHvDIdaWzIF9ShMSLO0o7gh8csZnfqKdK6Y9H"
atoken="14113114-1we8sJQs1z54dWfjWbUwZtDtkQYf3kDOrXLUMBFkZ"
asecret="6Sq95ezVVRNTuLw7grKzm4czA32VqmlM0QwvaLjWLNl5A"




class TwitterHelper():

    def __init__(self):
        super().__init__()
        
        self.auth = OAuthHandler(ckey, csecret)
        self.auth.set_access_token(atoken, asecret)



    def get_tweet(self, keyword): 

        numberOfLines = 50
        tweetConn = TwitterConn(numberOfLines)




        twitterStream = Stream(self.auth, tweetConn)
        twitterStream.filter(track=[keyword], async=True)
        

        

    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1



class TwitterConn(StreamListener):
    def __init__(self, numberOfLines):
        super().__init__()
        self.numberOfLines = numberOfLines
        self.count = 0
       

    def on_data(self, data):

        

        try:

            all_data = json.loads(data)
            tweet = all_data["text"]

            self.count = self.count + 1

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
            print(self.count)
            return True
        



    def on_error(self, status):
        
        print(status)
        if(status == 420):
            return False

    def on_status(self, status):
        print(status.text)

    



