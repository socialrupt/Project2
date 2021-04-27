import instaloader
from datetime import datetime as DT

Get_Posts_Miniutes_Ago = 10

L = instaloader.Instaloader()

while True:
    Target_UserName = "@python1937"#The profile username which needs to contain an @

    posts = instaloader.Profile.from_username(L.context, Target_UserName[1:]).get_posts()

    for post in posts:
        break

    print(post)
    print(post.date)#the date is wrong by 1 hour
    print(DT.now())
