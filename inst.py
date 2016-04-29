from instagram import client, subscriptions


def save(t):
	f = open('media.txt', 'a+')
	f.write(t + '\n')
	f.close()

#import inspect

user_id = '249608318' #ricardoabrasil
followers = []


api = client.InstagramAPI(access_token=access_token, client_secret=client_secret)

#print(inspect.getmembers(api, lambda a:not(inspect.isroutine(a))))
#print(dir(api))
#print(api.user_recent_media())
#print(api.user_follows('ricardoabrasil'))

#user_follows, next = api.user_follows(user_id, as_generator=True)
recent_media, next_ = api.user_recent_media()
photos = []
for media in recent_media:
	t = '<img src="%s"/>' % media.images['thumbnail'].url
	save(t)


	
follows, next_ = api.user_follows()
while next_:
	more_follows, next_ = api.user_follows(with_next_url=next_)
	follows.extend(more_follows)
	print(follows)

			
#recent_media, next_ = api.user_recent_media(user_id="ricardoabrasil", count=10)
#for media in recent_media:
#   print (media.caption.text)
