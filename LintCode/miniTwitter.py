#!/usr/bin/python
import sys

'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''


class MiniTwitter:
    def __init__(self):
        # do intialization if necessary
        self.order = 0
        self.news_feed = {}
        self.friends = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """

    def postTweet(self, user_id, tweet_text):
        # write your code here
        tweet = Tweet.create(user_id, tweet_text)
        self.order += 1
        if user_id not in self.news_feed:
            self.news_feed[user_id] = [(self.order, tweet)]
        else:
            self.news_feed[user_id].insert(0, (self.order, tweet))
        return tweet

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """

    def getNewsFeed(self, user_id):
        # write your code here
        feeds = []
        if user_id in self.news_feed:
            feeds = self.news_feed[user_id][:10]
        if user_id in self.friends:
            for f in self.friends[user_id]:
                if f in self.news_feed:
                    feeds.extend(self.news_feed[f][:10])
        feeds.sort(cmp=lambda x, y: cmp(x[0], y[0]), reverse=True)
        return [i[1] for i in feeds[:10]]

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """

    def getTimeline(self, user_id):
        # write your code here
        if user_id in self.news_feed:
            return [i[1] for i in self.news_feed[user_id][:10]]
        else:
            return []

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def follow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id not in self.friends:
            self.friends[from_user_id] = {to_user_id}
        else:
            self.friends[from_user_id].add(to_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id not in self.friends:
            return
        self.friends[from_user_id].remove(to_user_id)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())