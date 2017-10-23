#PARAMETERS
#ConservativeOutfile LiberalOutfile MaleOutfile FemaleOutfile
#ConservativePHV, LiberalPHV, MalePHV, and FemalePHV


import twitter
import sys
import replies
import json

if __name__ == "__main__":
    
    #CONSERVATIVE 
    ACCESS_TOKEN1 = '910124707252523008-ZoEXhvNolzVDsrhm8xsKVvTHDcjynnU'
    ACCESS_SECRET1 = 'spViZjNY6oGGvRZYhY2io5NEXPOPIw0yrhlOppPs9OYdD'
    CONSUMER_KEY1 = 'Swo2Y5iZf0Y5fS99nb3fFoFT5'
    CONSUMER_SECRET1 = 'mLqE6lAHVUkSTdHXDGviJEuI1btZvRARB6vFnUua13ydNIBZIh'

    #LIBERAL 
    ACCESS_TOKEN2 = '910495310056755200-AGnfxoHF2C3fYIQ0xk8OVKOZrg3HFvI'
    ACCESS_SECRET2 = 'kOrCJeHzikxwusvUsHGaQl6HIXWUp3Ool6zUizwzEKo6z'
    CONSUMER_KEY2 = '9zUnXpeR6CSetlCartf0hDhst'
    CONSUMER_SECRET2 = 'zBf0mINbKxLVO1l4s7N2KgLQivZxRseVkXWPfxT3ilppcor6Y9'

    #MALE 
    ACCESS_TOKEN3 = '910497122071564289-LToIgQi0QRHi9HjyDVeLQDegh3i0q2L'
    ACCESS_SECRET3 = 'JdMxA8ejxyMQwq09opNP8Rk4fbDpxUxEu1KsKtFhnqjbe'
    CONSUMER_KEY3 = 'vuaBJOsVu3XVTcDXByqJ1dUiW'
    CONSUMER_SECRET3 = 'EZkxgCKYE4zgWiwUVCAaIssz21LGVv6ER80fIFSFakGrM0BcgA'

    #FEMALE 
    ACCESS_TOKEN4 = '910502511278198786-PjZd1YGqCu0WBBB7FIB8optxXxbK3jM'
    ACCESS_SECRET4 = 'vXFqdqaEG3TgGiYE50oUrwS7GvqM20ue0NWVnGyXFCFb9'
    CONSUMER_KEY4 = 'b31uOYoB9gti5AVZwz2owQSqv'
    CONSUMER_SECRET4 = 'Q1xVPixZOft2a8Bf3N2BVUcQHHul0TXnktyPFDs5tGNlxsnthj'

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
