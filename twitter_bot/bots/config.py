# tweepy-bots/bots/config.py
import tweepy
import logging

logger = logging.getLogger()

def create_api():
    ACCESS_KEY = "1282769687387013121-T9v1SfLtKJfdZEm6brJPreBdZVz3XF" 
    ACCESS_KEY_SECRET = "h7yiJvMK0ZloFKF9n3ws0rCHGHRZ1s2P4kkQj37gqwCA2"
    API_KEY = "1Uba1SRW2aVwjjy97ZB0F8Lba"
    API_KEY_SECRET = "qjLjpp3xTEk14XaqJFAUY5tGpDw0OyB40E76WFAuOYRfVxIF8C"

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_KEY_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api