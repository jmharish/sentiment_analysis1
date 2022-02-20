from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from sentiment_mod import sentiment  as s 





#consumer key, consumer secret, access token, access secret.
ckey="2xVImCDWf7lSkkJSyXvouNRjl"
csecret="m1Til56RiHbtlj7bD5EmFSOusAUvhWzrTlmxl7m4Js2trCilQ5"
atoken="4170856812-OrLIZsuqPByjhhbnoYdtBJMsyDMECjqBn7usJ21"
asecret="ETM30l58tROFbtKBOmhnxTb9m59jRvhmkBMOXLFXJImCt"

tweet_save = open ('twitter_res.txt' , 'w' )
tweet_save.truncate(0)
tweet_save.close


class listener(StreamListener):
    
    def on_data(self, data):
        all_data = json.loads(data)#loads the tweets 

        tweet = all_data["text"]
        (a,b) = s(tweet)# we are using the function written for sentiment analysis 'a' is the class predicted 'b' is the % confidence in prediction
        print("TWEET:",tweet)
        print("RESULT:",a)
        print("CONFIDENCE:",b*100)

            
        tweet_save = open ('twitter_res.txt' , 'a' )
        tweet_save.write(a)# saves the pos/neg class for each tweet in a file, that is read while graph is plotted
        tweet_save.write('\n')
        tweet_save.close()

            
        return True

    def on_error(self, status):
            print (status)

auth = OAuthHandler(ckey, csecret)# to stream live tweets 
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

def func(n =0):
    while(n<100):
        try:
            twitterStream.filter(track=["india"])# filters all the tweets that contain india
        except :
            print ('error')
            func(n+1)# calls upto 100 errors 
    return(True)
func()
    

    
'''
acc token 4170856812-OrLIZsuqPByjhhbnoYdtBJMsyDMECjqBn7usJ21
acc token secret ETM30l58tROFbtKBOmhnxTb9m59jRvhmkBMOXLFXJImCt
'''
