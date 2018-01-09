#!/usr/bin/python
import sys


class FriendshipService:
    def __init__(self):
        # do intialization if necessary
        self.followers = {}
        self.followings = {}

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """

    def getFollowers(self, user_id):
        # write your code here
        if user_id in self.followers:
            return sorted(self.followers[user_id])
        return []

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """

    def getFollowings(self, user_id):
        # write your code here
        if user_id in self.followings:
            return sorted(self.followings[user_id])
        return []

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def follow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id in self.followers:
            if to_user_id not in self.followers[from_user_id]:
                self.followers[from_user_id].append(to_user_id)
        else:
            self.followers[from_user_id] = [to_user_id]
        if to_user_id in self.followings:
            if from_user_id not in self.followings[to_user_id]:
                self.followings[to_user_id].append(from_user_id)
        else:
            self.followings[to_user_id] = [from_user_id]

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id in self.followers and to_user_id in self.followers[from_user_id]:
            self.followers[from_user_id].remove(to_user_id)
        if to_user_id in self.followings and from_user_id in self.followings[to_user_id]:
            self.followings[to_user_id].remove(from_user_id)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())