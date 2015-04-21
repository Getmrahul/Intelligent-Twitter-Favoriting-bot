Intelligent-Twitter-Favoriting-bot
==================================

Installation: 
pip install twitter

Run: python favhash.py

The working of this code is simple. After Authenticating the user, the code reads the hashtag you mention and favorites tweets by others on the same topic, using hashtags. 

I have kept the limit of favorities per hashtag as 5, per execution, because over-favoriting can lead to the app being blacklisted by Twitter. I dont know the exact limit, but it does put on a block after favoriting around 1000 tweets. So this can be executed like, every 1 or 2 hours using cronjobs. 
