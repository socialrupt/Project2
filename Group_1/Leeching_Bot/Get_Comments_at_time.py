"""
This is not compltete.
You still need to get the time at which your bot sends the links


This program get the time at which the links where sent to the user and gets all the comments at a certain time frame to avoid
ppl trying to leach cuz they havew engaged on a post before acouple days ago.
"""



def Main_Ting():
    import instaloader
    from instaloader import Post
    import pandas as pd
    import csv
    import datetime

    L = instaloader.Instaloader()
    USER = "socialrupt_autodrop"
    PASSWORD = "I am the best123_Instagram"
    L.login(USER, PASSWORD)


    Identify_Post_That_Need_Engagment = Post.from_shortcode(L.context, "CJymaIQpdhw")

    Comments_From_Post_That_Need_Engagment = Identify_Post_That_Need_Engagment.get_comments()


    All_Comments_With_Date = []#Year/Month/Day

    for Comment in Comments_From_Post_That_Need_Engagment:
        All_Comments_With_Date.append(Comment.created_at_utc)#0:10 and 11:

    Since = datetime.datetime(2021, 1, 8, 16, 51, 00)  # smaller/youngee #date and time the links where sent
    Untill = datetime.datetime(2021, 1, 9, 9, 5)  # bigger/older and current date

    for Loop_Over_CommentsDates in All_Comments_With_Date:
        if Loop_Over_CommentsDates > Since:
            if Loop_Over_CommentsDates <= Untill:
                print(Loop_Over_CommentsDates)



Main_Ting()