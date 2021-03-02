
def Main_Ting():
    import instaloader
    from instaloader import Post
    import pandas as pd
    import csv

    L = instaloader.Instaloader()
    USER = "socialrupt"
    PASSWORD = "I am the best123_Instagram"
    L.login(USER, PASSWORD)
    #L.load_session_from_file(USER)
    #---------------------------
    Number_Of_Engagment = 0
    DX_Number = pd.read_csv("../Group1_Settings.csv")["DxNum"].iloc[0]
    Posts_Checked = 0
    All_Posts_Leached = 0
    Num_Of_Lines_Parsed = 0
    Num_Sent_To_User = 0# Numbeer of times we have sent the list of leached posts to the user.
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

                                    for Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment in df2["Links"].tail(DX_Number):
                                        Posts_Checked += 1
                                        Number_Comments_Checked = 0
                                        Number_Comments_Matched = 0

                                        if Posts_Checked == DX_Number and All_Posts_Leached >= 1 and Num_Sent_To_User == 0:
                                            Num_Sent_To_User += 1
                                            import Warning_System
                                            Warning_System.Main_Ting()

                                        else:
                                            pass

                                        Identify_Post_That_Need_Engagment = Post.from_shortcode(L.context, Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)

                                        Comments_From_Post_That_Need_Engagment = Identify_Post_That_Need_Engagment.get_comments()

                                        All_Comments_With_Username = []

                                        for Comment in Comments_From_Post_That_Need_Engagment:
                                            All_Comments_With_Username.append(Comment.owner)
                                        print(len(All_Comments_With_Username), "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")


                                        if All_Comments_With_Username != []:#This runs if the posts have comments
                            #-------------------------------------------------
                                            print("There are comments.", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)
                                            for Loop_Over_Usernames in All_Comments_With_Username:
                                                Number_Comments_Checked += 1
                                                if Loop_Over_Usernames == Username_Of_Post_That_Need_To_Give_Engagment:
                                                    Number_Comments_Matched += 1

                                                    print("There is a comment that matches there profile.", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)
                                                    Number_Of_Engagment += 1

                                                    if Number_Of_Engagment == DX_Number:#runs if they have engaged 100%
                                                        print("They have engaged 100%", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)

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
                                                        print("We checked all the posts and they haven't fully enagaged", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)
                                                        All_Posts_Leached += 1

                                                        with open("Leached_Posts.csv", "a+",
                                                                  encoding='UTF-8') as f: #adds the leached link to a file
                                                            writer = csv.writer(f, delimiter=",",
                                                                                lineterminator="\n")
                                                            writer.writerow(
                                                                [Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment])



                                                    elif Posts_Checked == DX_Number and Number_Of_Engagment < DX_Number:
                                                        print("We have checked all the posts and they have not enagaged.", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)
                                                        with open("Leached_Posts.csv", "a+",
                                                                  encoding='UTF-8') as f: #adds the leached link to a file
                                                            writer = csv.writer(f, delimiter=",",
                                                                                lineterminator="\n")
                                                            writer.writerow(
                                                                [Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment])

                                                    else:#This run cuz we havnt checked all the posts yet OR All posts leached isn't equal to 0
                                                        print("This run cuz we havnt checked all the posts yet OR All posts leached isn't equal to 0", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)


                                                else:#This else clause runs when the comment isnt the users comment
                                                    print("This isn't there comment.", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)

                                                    if Number_Of_Engagment != DX_Number - 1 and Posts_Checked == DX_Number and All_Posts_Leached == 0:# warns the leecher when the num of engagment is less than dxnum when all the postes checked is dxnum and olny warns once.
                                                        print("They havn't engaged!!!", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)
                                                        All_Posts_Leached += 1
#-----------------------------------------------------------------------------------------
                                                        with open("Leached_Posts.csv", "a",
                                                                  encoding='UTF-8') as f:
                                                            writer = csv.writer(f, delimiter=",",
                                                                                lineterminator="\n")
                                                            writer.writerow(
                                                                [Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment])
# -----------------------------------------------------------------------------------------


                                                    elif Number_Of_Engagment != DX_Number - 1 and Number_Comments_Checked == len(All_Comments_With_Username) and Number_Comments_Matched == 0:
                                                        print("WTF EVEN IS ITHIS!!!")
                                                        with open("Leached_Posts.csv", "a",
                                                                  encoding='UTF-8') as f:
                                                            writer = csv.writer(f, delimiter=",",
                                                                                lineterminator="\n")
                                                            writer.writerow(
                                                                [Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment])

                                                    else:#This runs if we havnt checked all the post or if they have already been warned.
                                                        print("You have already been warnt or we havnt checked all the posts yet.", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment, Number_Comments_Checked)

                                        elif All_Comments_With_Username == [] and All_Posts_Leached == 0:#warns the leecher if the post has no comments at all
                                            print("There are no comments.", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)
                                            All_Posts_Leached += 1

                                            with open("Leached_Posts.csv", "a",
                                                      encoding='UTF-8') as f:
                                                writer = csv.writer(f, delimiter=",",
                                                                    lineterminator="\n")
                                                writer.writerow(
                                                    [Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment])



                                        elif All_Comments_With_Username == []:
                                            print("The post has NO comments!!!", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)
                                            with open("Leached_Posts.csv", "a",
                                                      encoding='UTF-8') as f:
                                                writer = csv.writer(f, delimiter=",",
                                                                    lineterminator="\n")
                                                writer.writerow(
                                                    [Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment])

                                        else:#This runns if the post has no comments and if we havn't checked all the links yet or you may have already been warned.
                                            print("The post has no comments and we havn't checked all the posts yet or you hve already been warned", Each_Comment_From_Post_From_File_That_Need_To_Get_Engagment)



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

