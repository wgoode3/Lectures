# functions?

def name(paramet1, parameter2):
	print "hello world"

# name("a", 2)

# debugging?

# print everything!

# tuples and dictionaries and lists

a = [1,2,"abacus"]

b = {"name": "Example McExampleface", "email": "example@example.com"}

c = (1,2,3)

# c[3] = 4 # doesn't work

d = 1,2

e = {"thing1": a, "thing2": b, "thing3": (a,b,c)}

# print type(a)
# print type(a[1])
# print type(a[2])
# print type(b)
# print type(b["name"])
# print type(c)
# print type(d)
# print type(e)
# print type(e["thing1"])
# print type(e["thing1"][2])
# print type(e["thing2"])
# print type(e["thing3"])
# print type(e["thing3"][3])
# print type(e["thing3"][2])

import twitter
api = twitter.Api(consumer_key = 'LgPgWrpf0zyJimw1DSa4a9obx', 
	consumer_secret = 'RqazdCx73l8x2RRmvntVW08AYaFikh9lvYwc9iMdPTMICSgAmu', 
	access_token_key = '1564487502-FICCLO2KJOXTNW0BQmY3Hu7dxpm6psYcAsk8Bvw', 
	access_token_secret = 'GAQffclcmUeib1uPgsbGfM3RJnWDVDnxbnZzv7VcWNvJL', 
	sleep_on_rate_limit=True)

tweet = api.GetUserTimeline(screen_name='@elonmusk', count=1)

print tweet
print '*'*100
print type(tweet)
print '*'*100

print tweet[0].id
print tweet[0].created_at
print tweet[0].text
print tweet[0].retweeted_status



# for thing in tweets:
# 	print type(thing)


'''
for i in range(0, len(tweets)):
	print i
	print tweets[i]
	# for thing in tweet.iterkeys():
	# 	print thing
	print '*'*100
'''

'''

{"created_at": "Tue Jun 06 10:00:58 +0000 2017", 
"hashtags": [], 
"id": 872030545722482688, 
"id_str": "872030545722482688", 
"lang": "en", 
"retweet_count": 1837, 
"retweeted_status": 
	{"created_at": "Tue Jun 06 09:58:14 +0000 2017", 
	"favorite_count": 6208, 
	"hashtags": [], 
	"id": 872029857231843329, 
	"id_str": "872029857231843329", 
	"lang": "en", 
	"media": [
		{"display_url": "pic.twitter.com/yFbNVo2Den", 
		"expanded_url": "https://twitter.com/newscientist/status/872029857231843329/video/1", 
		"id": 872029755213725696, 
		"media_url": "http://pbs.twimg.com/ext_tw_video_thumb/872029755213725696/pu/img/kp4ca0dfmFaAX4tk.jpg", 
		"media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/872029755213725696/pu/img/kp4ca0dfmFaAX4tk.jpg", 
		"type": "video", 
		"url": "https://t.co/yFbNVo2Den"}], 
	"retweet_count": 1837, 
	"source": "<a href=\"http://www.hootsuite.com\" rel=\"nofollow\">Hootsuite</a>", 
	"text": "SpaceX is the first private company to send the same vehicle into orbit twice https://t.co/O0fUAhlF0g https://t.co/yFbNVo2Den", 
	"urls": [
		{"expanded_url": "http://ow.ly/xC8p30clU4S", 
		"url": "https://t.co/O0fUAhlF0g"}], 
	"user": 
		{"created_at": "Wed Jan 28 16:05:49 +0000 2009", 
		"description": "The best place to find out what\u2019s new in science \u2013 and why it matters. To subscribe go to: https://t.co/nsC9MjQzmh", 
		"favourites_count": 15974, 
		"followers_count": 2879832, 
		"friends_count": 73, 
		"geo_enabled": true, 
		"id": 19658826, 
		"lang": "en", 
		"listed_count": 33020, 
		"location": "Worldwide", 
		"name": "New Scientist", 
		"profile_background_color": "333333", 
		"profile_background_image_url": "http://pbs.twimg.com/profile_background_images/378800000152251610/2hsomJrk.png", 
		"profile_banner_url": "https://pbs.twimg.com/profile_banners/19658826/1399482279", 
		"profile_image_url": "http://pbs.twimg.com/profile_images/843789564074496001/m34mTHmg_normal.jpg", 
		"profile_link_color": "0084B4", 
		"profile_sidebar_fill_color": "FFFFFF", 
		"profile_text_color": "333333", 
		"screen_name": "newscientist", 
		"statuses_count": 39430, 
		"time_zone": "London", 
		"url": "http://t.co/6LpUpVcVZt", 
		"utc_offset": 3600, 
		"verified": true}, 
		"user_mentions": []}, 
	"source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>", 
	"text": "RT @newscientist: SpaceX is the first private company to send the same vehicle into orbit twice https://t.co/O0fUAhlF0g https://t.co/yFbNVo\u2026", 
	"urls": [
		{"expanded_url": "http://ow.ly/xC8p30clU4S", 
		"url": "https://t.co/O0fUAhlF0g"}], 
		"user": {
			"created_at": "Tue Jun 02 20:12:29 +0000 2009", 
			"description": "Tesla, SpaceX, OpenAI & Neuralink", 
			"favourites_count": 475, 
			"followers_count": 9117963, 
			"friends_count": 41, 
			"id": 44196397, 
			"lang": "en", 
			"listed_count": 35514, 
			"location": "Boring", 
			"name": "Elon Musk", 
			"profile_background_color": "C0DEED", 
			"profile_background_image_url": "http://pbs.twimg.com/profile_background_images/399721902/fusion.jpg", 
			"profile_banner_url": "https://pbs.twimg.com/profile_banners/44196397/1354486475", 
			"profile_image_url": "http://pbs.twimg.com/profile_images/782474226020200448/zDo-gAo0_normal.jpg", 
			"profile_link_color": "0084B4", 
			"profile_sidebar_fill_color": "DDEEF6", 
			"profile_text_color": "333333", 
			"screen_name": "elonmusk", 
			"statuses_count": 3022, 
			"time_zone": "Pacific Time (US & Canada)", 
			"utc_offset": -25200, 
			"verified": true}, 
		"user_mentions": [
			{"id": 19658826, 
			"name": "New Scientist", 
			"screen_name": "newscientist"}]}

'''