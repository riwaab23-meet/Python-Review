
def create_youtube_video():
	title =input("enter a title :")
	description=input("enter a des:")
	dict= {"title":title,"description":description,"like":0,"dislikes":0,"comment":{},"hashtag":[]}
	return dict

##key = dict["like"]
##wee= dict["dislikes"]
def like(dict):
	##if key in dict:
	dict["like"] = dict["like"]+1
	return dict


def dislike(dict):
	dict["dislikes"] = dict["dislikes"]+1
	return dict

def add_comment(dict,username,comment_text):
	dict["comment"][username]=comment_text
	return dict

def add_hashtag():
	while True:
        hashtag.append(int(input()))
	return dict

new_video = create_youtube_video()
like(new_video)
dislike(new_video)
add_comment(new_video,'Ahmad',"hello im riwa")
print(new_video)


	
