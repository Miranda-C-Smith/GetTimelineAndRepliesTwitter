#PARAMETERS
#ConservativeOutfile LiberalOutfile MaleOutfile FemaleOutfile
#ConservativePHV, LiberalPHV, MalePHV, and FemalePHV


import twitter
import sys
import replies
import json

if __name__ == "__main__":
    
    #CONSERVATIVE 
    ACCESS_TOKEN1 = ''
    ACCESS_SECRET1 = ''
    CONSUMER_KEY1 = ''
    CONSUMER_SECRET1 = ''

    #LIBERAL 
    ACCESS_TOKEN2 = ''
    ACCESS_SECRET2 = ''
    CONSUMER_KEY2 = ''
    CONSUMER_SECRET2 = ''

    #MALE 
    ACCESS_TOKEN3 = ''
    ACCESS_SECRET3 = ''
    CONSUMER_KEY3 = ''
    CONSUMER_SECRET3 = ''

    #FEMALE 
    ACCESS_TOKEN4 = ''
    ACCESS_SECRET4 = ''
    CONSUMER_KEY4 = ''
    CONSUMER_SECRET4 = ''

    apiC = twitter.Api(consumer_key=CONSUMER_KEY1,
                      consumer_secret=CONSUMER_SECRET1,
                      access_token_key=ACCESS_TOKEN1,
                      access_token_secret=ACCESS_SECRET1,
                      sleep_on_rate_limit=True)
    apiL = twitter.Api(consumer_key=CONSUMER_KEY2,
                      consumer_secret=CONSUMER_SECRET2,
                      access_token_key=ACCESS_TOKEN2,
                      access_token_secret=ACCESS_SECRET2,
                      sleep_on_rate_limit=True)
    apiM = twitter.Api(consumer_key=CONSUMER_KEY3,
                      consumer_secret=CONSUMER_SECRET3,
                      access_token_key=ACCESS_TOKEN3,
                      access_token_secret=ACCESS_SECRET3,
                      sleep_on_rate_limit=True)
    apiF = twitter.Api(consumer_key=CONSUMER_KEY4,
                      consumer_secret=CONSUMER_SECRET4,
                      access_token_key=ACCESS_TOKEN4,
                      access_token_secret=ACCESS_SECRET4,
                      sleep_on_rate_limit=True)

    

    stdout_= sys.stdout

    Files=[("ConservativeTimeline.txt","ConservativeReplies.txt", apiC), ("LiberalTimeline.txt", "LiberalReplies.txt", apiL), ("MaleTimeline.txt","MaleReplies.txt", apiM),( "FemaleTimeline.txt", "FemaleReplies.txt", apiF)]

    for timelineFile, replyFile, api in Files:
        with open(timelineFile, "w") as tFile:

            tweets = api.GetHomeTimeline(count=10)
            for tweet in tweets:
                tFile.write(json.dumps(tweet._json) + "\n")
                
            #call replies module and rerout standard out
            sys.stdout = open(replyFile, 'w')
            replies.main(timelineFile)
            
    sys.stdout = stdout_
