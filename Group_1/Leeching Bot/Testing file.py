
def Main_Ting():
    import instaloader
    from instaloader import Post
    import pandas as pd
    import csv

    L = instaloader.Instaloader()
    USER = "socialrupt"
    PASSWORD = "I am the best123_Instagram"
    L.login(USER, PASSWORD)

    #---------------------------
    Number_Of_Engagment = 0
    DX_Number = pd.read_csv("../Group1_Settings.csv")["DxNum"].iloc[0]
    Posts_Checked = 0
    All_Posts_Leached = 0
    Num_Of_Lines_Parsed = 0

    #---------------------------

    df1 = pd.read_csv("Links_That_Need_To_Give_Engagment.csv")
    df2 = pd.read_csv("Links_That_Need_To_Get_Engagment.csv")
    df3 = pd.read_csv("../Group1_Premium.csv")
    #----------------------

    for Account_From_File_That_Need_To_Give_Engagment in reversed(df1["Links"].dropna()):
        for Loop_Over_Chat_IDs in reversed(df1["Link_Chat_Id"]):
            for Loop_Over_Message_IDs in reversed(df1["Link_Message_Id"]):
                for Loop_Over_UserID in reversed(df1["Link_User_Id"]):
                    for Loop_Over_UserNames in reversed(df1["User_Name"]):
                        for Loop_Over_Premium_Usernames in reversed(df3["UserNames"]):
                            Num_Of_Lines_Parsed += 1
                            if Num_Of_Lines_Parsed == len(df3) or str(Loop_Over_Premium_Usernames).lower()[1:] == str(Loop_Over_UserNames).lower():#Allowed to enter the if statment if it has checked ALL the usernames in premium csv file or if a premium username matches the sender's username
                                if str(Loop_Over_Premium_Usernames).lower()[1:] != str(Loop_Over_UserNames).lower():#Runs if they are not a premium user
                                    print("You are not a premium user.")
                                    Identify_Post_That_Need_To_Give_Engagment = Post.from_shortcode(L.context, Account_From_File_That_Need_To_Give_Engagment)

                                    Username_Of_Post_That_Need_To_Give_Engagment = Identify_Post_That_Need_To_Give_Engagment.owner_profile

                        #------------------------------------------------------------

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
                                        


                                        if All_Likes_With_Username != []:#This runs if the posts have Likes
                            #-------------------------------------------------
                                            print("There are likes.", Each_Post_From_File_That_Need_To_Get_Engagment)
                                            for Loop_Over_Usernames in All_Likes_With_Username:
                                                Number_Likes_Checked += 1
                                                if Loop_Over_Usernames == Username_Of_Post_That_Need_To_Give_Engagment:
                                                    Number_Likes_Matched += 1

                                                    print("There is a like that matches there profile.", Each_Post_From_File_That_Need_To_Get_Engagment)
                                                    Number_Of_Engagment += 1

                                                    if Number_Of_Engagment == DX_Number:#runs if they have engaged 100%
                                                        print("They have engaged 100%", Each_Post_From_File_That_Need_To_Get_Engagment)

                                                        with open("Links_That_Need_To_Get_Engagment.csv", "a+", encoding='UTF-8') as f:
                                                            writer = csv.writer(f, delimiter=",", lineterminator="\n")
                                                            writer.writerow([Account_From_File_That_Need_To_Give_Engagment])

                                #-----------------------------------------------------------------------------------------------
                                                            Links_Dropped_By_User = Account_From_File_That_Need_To_Give_Engagment
                                                            Links_Dropped_By_User_Chat_Id = Loop_Over_Chat_IDs
                                                            Links_Dropped_By_User_Message_Id = Loop_Over_Message_IDs

                                                            d = {'Links': [Links_Dropped_By_User], 'Link_Chat_Id': [Links_Dropped_By_User_Chat_Id],
                                                                 'Link_Message_Id': [Links_Dropped_By_User_Message_Id]}

                                                            df = pd.DataFrame(data=d, )

                                                            df.to_csv("Links_That_Need_To_Be_Sent_To_Group.csv", index=False)


                                                            import Send_Checked_Link_To_Group
                                                            Send_Checked_Link_To_Group.Main_ting()
                                                            break

                                                    elif Posts_Checked == DX_Number and Number_Of_Engagment < DX_Number and All_Posts_Leached == 0:  #runs when all the links have been checked and warns the leacher one time
                                                        print("We checked all the posts and they haven't fully enagaged", Each_Post_From_File_That_Need_To_Get_Engagment)
                                                        All_Posts_Leached += 1

                                                        with open("Leached_Posts.csv", "a+",
                                                                  encoding='UTF-8') as f: #adds the leached link to a file
                                                            writer = csv.writer(f, delimiter=",",
                                                                                lineterminator="\n")
                                                            writer.writerow(
                                                                [Each_Post_From_File_That_Need_To_Get_Engagment])

                                                        import Warning_System
                                                        Warning_System.Main_Ting()

                                                    elif Posts_Checked == DX_Number and Number_Of_Engagment < DX_Number:
                                                        print("We have checked all the posts and they have not enagaged.", Each_Post_From_File_That_Need_To_Get_Engagment)
                                                        with open("Leached_Posts.csv", "a+",
                                                                  encoding='UTF-8') as f: #adds the leached link to a file
                                                            writer = csv.writer(f, delimiter=",",
                                                                                lineterminator="\n")
                                                            writer.writerow(
                                                                [Each_Post_From_File_That_Need_To_Get_Engagment])

                                                    else:#This run cuz we havnt checked all the posts yet OR All posts leached isn't equal to 0
                                                        print("This run cuz we havnt checked all the posts yet OR All posts leached isn't equal to 0", Each_Post_From_File_That_Need_To_Get_Engagment)


                                                else:#This else clause runs when the comment isnt the users comment
                                                    print("This isn't there likes.", Each_Post_From_File_That_Need_To_Get_Engagment)

                                                    if Number_Of_Engagment != DX_Number - 1 and Posts_Checked == DX_Number and All_Posts_Leached == 0:# warns the leecher when the num of engagment is less than dxnum when all the postes checked is dxnum and olny warns once.
                                                        print("They havn't engaged!!!", Each_Post_From_File_That_Need_To_Get_Engagment)
                                                        All_Posts_Leached += 1
#-----------------------------------------------------------------------------------------
                                                        with open("Leached_Posts.csv", "a",
                                                                  encoding='UTF-8') as f:
                                                            writer = csv.writer(f, delimiter=",",
                                                                                lineterminator="\n")
                                                            writer.writerow(
                                                                [Each_Post_From_File_That_Need_To_Get_Engagment])
# -----------------------------------------------------------------------------------------
                                                        import Warning_System
                                                        Warning_System.Main_Ting()

                                                    elif Number_Of_Engagment != DX_Number - 1 and Number_Likes_Checked == len(All_Likes_With_Username) and Number_Likes_Matched == 0:
                                                        print("WTF EVEN IS ITHIS!!!")
                                                        with open("Leached_Posts.csv", "a",
                                                                  encoding='UTF-8') as f:
                                                            writer = csv.writer(f, delimiter=",",
                                                                                lineterminator="\n")
                                                            writer.writerow(
                                                                [Each_Post_From_File_That_Need_To_Get_Engagment])

                                                    else:#This runs if we havnt checked all the post or if they have already been warned.
                                                        print("You have already been warnt or we havnt checked all the posts yet.", Each_Post_From_File_That_Need_To_Get_Engagment, Number_Likes_Checked)

                                        elif All_Likes_With_Username == [] and All_Posts_Leached == 0:#warns the leecher if the post has no comments at all
                                            print("There are no Likes.", Each_Post_From_File_That_Need_To_Get_Engagment)
                                            All_Posts_Leached += 1

                                            with open("Leached_Posts.csv", "a",
                                                      encoding='UTF-8') as f:
                                                writer = csv.writer(f, delimiter=",",
                                                                    lineterminator="\n")
                                                writer.writerow(
                                                    [Each_Post_From_File_That_Need_To_Get_Engagment])

                                            import Warning_System
                                            Warning_System.Main_Ting()

                                        elif All_Likes_With_Username == []:
                                            print("The post has NO Likes!!!", Each_Post_From_File_That_Need_To_Get_Engagment)
                                            with open("Leached_Posts.csv", "a",
                                                      encoding='UTF-8') as f:
                                                writer = csv.writer(f, delimiter=",",
                                                                    lineterminator="\n")
                                                writer.writerow(
                                                    [Each_Post_From_File_That_Need_To_Get_Engagment])

                                        else:#This runns if the post has no Likes and if we havn't checked all the links yet or you may have already been warned.
                                            print("The post has no Likes and we havn't checked all the posts yet or you hve already been warned", Each_Post_From_File_That_Need_To_Get_Engagment)



                                else:#for preium users
                                    print("Premium vip running..", Account_From_File_That_Need_To_Give_Engagment)
                                    with open("Links_That_Need_To_Get_Engagment.csv", "a+", encoding='UTF-8') as f:
                                        writer = csv.writer(f, delimiter=",", lineterminator="\n")
                                        writer.writerow([Account_From_File_That_Need_To_Give_Engagment])

                                        # -----------------------------------------------------------------------------------------------
                                        Links_Dropped_By_User = Account_From_File_That_Need_To_Give_Engagment
                                        Links_Dropped_By_User_Chat_Id = Loop_Over_Chat_IDs
                                        Links_Dropped_By_User_Message_Id = Loop_Over_Message_IDs

                                        d = {'Links': [Links_Dropped_By_User],
                                             'Link_Chat_Id': [Links_Dropped_By_User_Chat_Id],
                                             'Link_Message_Id': [Links_Dropped_By_User_Message_Id]}

                                        df = pd.DataFrame(data=d, )

                                        df.to_csv("Links_That_Need_To_Be_Sent_To_Group.csv", index=False)

                                        import Send_Checked_Link_To_Group
                                        Send_Checked_Link_To_Group.Main_ting()
                                        break
                            else:#Runs when it hasn't loop over all the links or when the sender's username dosnt match a premium user's username.
                                print("Havn't checked the whole premium csv file yet.")

Main_Ting()