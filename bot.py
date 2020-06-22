import os
from config import getApi

api=getApi()

image = 'imagename'

def postStatus(update):
    status = api.PostUpdate(update)
    print(status)


def postWithImage(update):
    print(api.PostUpdate(update, media=image))
    os.remove(image) #this remove the image from your folder, if you dont want this remove it



# PostStatus("example")
# PostWithImage(example)  