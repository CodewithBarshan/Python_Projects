from instabot import Bot
bot=Bot()
bot.login(username="barshan_mukherjee",password="Physics&math")
bot.follow("wscubetechindia")
bot.upload("C:/Users/Barshan Mukherjee/Downloads/python.jpeg",caption="I love Python")
bot.send_message("I love Python",["ria.ghoshal","wscubetechindia"])
followers=bot.get_user_followers("barshan_mukherjee")
for follower in followers:
    print(bot.get_user_info(follower))
#in the same  way i can fetch datas of following