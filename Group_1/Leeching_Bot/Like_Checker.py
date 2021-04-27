def Main_Ting():
    import instaloader
    from instaloader import Post
    import pandas as pd
    import csv
    L = instaloader.Instaloader()

    USER = str(pd.read_csv("Instagram_accounts.csv")["Leeching_Bot_Username"].iloc[0])
    PASSWORD = str(pd.read_csv("Instagram_accounts.csv")["Leeching_Bot_Password"].iloc[0])
    L.login(USER, PASSWORD)

    # ---------------------------
    Number_Of_Engagment = 0
    DX_Number = pd.read_csv("Group_1/Group1_Settings.csv")["DxNum"].iloc[0]
    Posts_Checked = 0
    All_Posts_Leached = 0
    Num_Of_Lines_Parsed = 0

    # ---------------------------

    df1 = pd.read_csv("Group_1/Leeching_Bot/Links_That_Need_To_Give_Engagment.csv")
    df2 = pd.read_csv("Group_1/Leeching_Bot/Links_That_Need_To_Get_Engagment.csv")
    df3 = pd.read_csv("Group_1/Group1_Premium.csv")
    # ----------------------

    for Account_From_File_That_Need_To_Give_Engagment in reversed(df1["Links"].dropna()):
        for Loop_Over_Chat_IDs in reversed(df1["Link_Chat_Id"]):
            for Loop_Over_Message_IDs in reversed(df1["Link_Message_Id"]):
                for Loop_Over_UserID in reversed(df1["Link_User_Id"]):
                    for Loop_Over_UserNames in reversed(df1["User_Name"]):
                        for Loop_Over_Premium_Usernames in reversed(df3["UserNames"]):
                            Num_Of_Lines_Parsed += 1
                            if Num_Of_Lines_Parsed == len(df3) or str(Loop_Over_Premium_Usernames).lower()[1:] == str(
                                    Loop_Over_UserNames).lower():  # Allowed to enter the if statment if it has checked ALL the usernames in premium csv file or if a premium username matches the sender's username
                                if str(Loop_Over_Premium_Usernames).lower()[1:] != str(
                                        Loop_Over_UserNames).lower():  # Runs if they are not a premium user
                                    print("You are not a premium user.")
                                    Identify_Post_That_Need_To_Give_Engagment = Post.from_shortcode(L.context,
                                                                                                    Account_From_File_That_Need_To_Give_Engagment)

                                    Username_Of_Post_That_Need_To_Give_Engagment = Identify_Post_That_Need_To_Give_Engagment.owner_profile

                                    # ------------------------------------------------------------

                                    for Each_Post_From_File_That_Need_To_Get_Engagment in df2["Links"].tail(DX_Number):
                                        Posts_Checked += 1
                                        Number_Likes_Checked = 0
                                        Number_Likes_Matched = 0

                                        Identify_Post_That_Need_Engagment = Post.from_shortcode(L.context,
                                                                                                Each_Post_From_File_That_Need_To_Get_Engagment)

                                        Likes_From_Post_That_Need_Engagment = Identify_Post_That_Need_Engagment.get_likes()

                                        All_Likes_With_Username = []

                                        for Like in Likes_From_Post_That_Need_Engagment:
                                            All_Likes_With_Username.append(Like)

                                        if All_Likes_With_Username != []:#This runs if the post has likes.
                                            print("This post has likes", Each_Post_From_File_That_Need_To_Get_Engagment)

                                            for Loop_Over_Usernames in All_Likes_With_Username:
                                                Number_Likes_Checked += 1

                                                if Loop_Over_Usernames == Username_Of_Post_That_Need_To_Give_Engagment:

                                                    Number_Likes_Matched += 1
                                                    Number_Of_Engagment += 1#Do i need this???

                                                    print("There is a comment that matches there profile.",
                                                          Each_Post_From_File_That_Need_To_Get_Engagment)

                                                elif Number_Likes_Checked == len(All_Likes_With_Username) and Number_Likes_Matched == 0:
                                                    print("We have checked all the likes and not even one matched.",
                                                          Each_Post_From_File_That_Need_To_Get_Engagment)
                                                    df1 = pd.read_csv("Group_1/Leeching_Bot/Leached_Posts.csv")
                                                    df1.loc[len(
                                                        df1), "Leached_Likes"] = Each_Post_From_File_That_Need_To_Get_Engagment
                                                    df1.to_csv("Group_1/Leeching_Bot/Leached_Posts.csv", index=False)

                                                else:  # This else clause runs when the like isnt the users like
                                                    print("This isn't there like.",
                                                      Each_Post_From_File_That_Need_To_Get_Engagment)





                                        elif All_Likes_With_Username == []:#This runs if the post dosn't have likes.
                                            print("This post don't have likes", Each_Post_From_File_That_Need_To_Get_Engagment)

                                            df1 = pd.read_csv("Group_1/Leeching_Bot/Leached_Posts.csv")
                                            df1.loc[len(df1), "Leached_Likes"] = Each_Post_From_File_That_Need_To_Get_Engagment
                                            df1.to_csv("Group_1/Leeching_Bot/Leached_Posts.csv", index=False)

                                        else:#I don't know why this is running???
                                            pass
                            else:  # Runs when it hasn't loop over all the links or when the sender's username dosnt match a premium user's username.
                                pass

