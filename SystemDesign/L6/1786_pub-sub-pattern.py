# Description
# Pub/Sub pattern is a wide used pattern in system design. In this problem, you need to implement a pub/sub pattern to
# support user subscribes on a specific channel and get notification messages from subscribed channels.
#
# There are 3 methods you need to implement:
#
# subscribe(channel, user_id): Subscribe the given user to the given channel.
# unsubscribe(channel, user_id): Unsubscribe the given user from the given channel.
# publish(channel, message): You need to publish the message to the channel so that everyone subscribed on the
# channel will receive this message. Call PushNotification.notify(user_id, message) to push the message to the user.
# Have you met this question in a real interview?
# Example
# subscribe("group1",  1)
# publish("group1", "hello")
# >> user 1 received "Hello"
# subscribe("group1", 2)
# publish("group1", "thank you")
# >> user 1 received "thank you"
# >> user 2 received "thank you"
# unsubscribe("group2", 3)
# >> user 3 is not in group2, do nothing
# unsubscribe("group1", 1)
# publish("group1", "thank you very much")
# >> user 2 received "thank you very much"
# publish("group2", "are you ok?")
# >> # you don't need to push this message to anyone
# If there are more than 1 user subscribed on the same channel, it doesn't matter the order of time users
# receiving the message. It's ok if you push the message to user 2 before user 1.

'''
Definition of PushNotification
class PushNotification:
    @classmethod
    def notify(user_id, message):
'''


class PubSubPattern:
    channel_id = {}

    def __init__(self):
        pass

    # do intialization if necessary

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def subscribe(self, channel, user_id):
        # write your code here
        if channel not in self.channel_id:
            self.channel_id[channel] = set()
        self.channel_id[channel].add(user_id)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def unsubscribe(self, channel, user_id):
        # write your code here
        if channel in self.channel_id and user_id in self.channel_id[channel]:
            self.channel_id[channel].remove(user_id)

    """
    @param: channel: a channel name
    @param: message: need send message
    @return: nothing
    """

    def publish(self, channel, message):
        # write your code here
        if channel in self.channel_id and len(self.channel_id[channel]) != 0:
            for id in self.channel_id[channel]:
                PushNotification.notify(id, message)