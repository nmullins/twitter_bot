#!/usr/bin/env python
import sys
from twython import Twython
from datetime import date

today = date.today();

t = today.timetuple();

day_of_week = today.strftime("%A");

# Send a different tweet depending on the day of the week
if day_of_week == 'Monday':
    tweetStr = "I hope everyone is having a great Monday! -- Nick via RaspPi Twitter Bot"
elif day_of_week == 'Tuesday':
    tweetStr = "Good afternoon everyone! -- Nick via RaspPi Twitter Bot"
elif day_of_week == 'Wednesday':
    tweetStr = "Happy Humpday! -- Nick via RaspPi Twitter Bot"
elif day_of_week == 'Thursday':
    tweetStr = "Friday is almost here! -- Nick via RaspPi Twitter Bot"
elif day_of_week == 'Friday':
    tweetStr = "I am ready for the weekend! -- Nick via RaspPi Twitter Bot"
elif day_of_week == 'Saturday':
    tweetStr = "Let's see what kind of trouble I can get into this weekend! -- Nick via RaspPi Twitter Bot"
else:
    tweetStr = "The end of another weekend.  Not ready to go back to work tomorrow! -- Nick via RaspPi Twitter Bot"

#tweetStr = "Test of TweetBot Twitter Webservice";

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
apiKey = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
apiSecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXXXX'
accessToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
accessTokenSecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
