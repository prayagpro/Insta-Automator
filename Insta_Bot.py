from instabot import Bot

# Create an instance of the bot
bot = Bot()

# Log in with your Instagram credentials
bot.login(username="your_username", password="your_password")

# Follow a specific user
bot.follow("username_to_follow")

Optionally, you can add more actions like:
bot.unfollow("username_to_unfollow")
bot.upload_photo("path_to_your_photo.jpg", caption="Your caption here")