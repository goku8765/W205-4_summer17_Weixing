import tweepy

consumer_key = "xzPVyAATjCl17appNWv43dA0v";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "lA6mseIPGCP82P3qy7S5qnIYUDYfvhlBOYrMhZYXbtcKspiXMf";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "893553502135386113-LAEY7AD4aThwya4mFX1zrSFVhNfh5RO";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "9JxWfUjbQmEfZFAAXXP7LKNemjQCY072UkBeZdHS1OcFe";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



