Intelligent-Twitter-Favoriting-bot
==================================

The working of this code is simple. After Authenticating the user, the code reads the last 20 tweets of the user and favorites tweets by others on the same topic, using hashtags. 

I have kept the limit of favorities per hashtag as 5, per execution, because over-favoriting can lead to the app being blacklisted by Twitter. I dont know the exact limit, but it does put on a block after favoriting around 1000 tweets. So this can be executed like, every 1 or 2 hours using cronjobs. 

New commit feature:
Eliminating redundant hashtags to imporve efficiency.

TODO:
Proxy Authentication for the code to work behind a Proxy Server
