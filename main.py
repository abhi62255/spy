from steganography.steganography import Steganography   # Importing function form Steganography Library
from spy_details import spy, Spy, ChatMessage, friends ,user_spy_rating        # Importing Classes and Variables from  spy_details.py file
status_messages = []          # Declaring a list to Store Status from the User


def start_chat():   # Main Function
    choice = 1
    while choice != 3:
        print(" 1 Enter as a Guest \n 2 To Create New Account \n 3 To Exit Application")  # First Menu Options
        choice = int(raw_input("ENTER YOUR CHOICE :-"))
        if choice == 1:
            print("Welcome %s %s " % (spy.salutation,spy.name))
            menu()

        elif choice == 2:
            print "Add All The Details Carefully For Wrong Information Your Execution Will Be Terminated"
            print "Age limit to be a spy 12 - 50"
            spy.name = raw_input("Tell us your name : ")            # Taking Name as Input
            if len(spy.name) == 0 :
                print("You are not providing valid information")
            elif spy.name.isalpha() == 0:
                print("You are not providing valid information ")
            else:
                spy.age = raw_input("Enter your age : ")

                if len(spy.age) == 0:
                    print("You are not providing valid information \n")
                elif spy.age.isdigit() == 0:
                    print("You  are not providing valid information \n")
                else:
                    spy.age=int(spy.age)                # Converting age into an Integer value
                    if spy.age< 12 or spy.age > 50:
                            print("You are not eligible to be a spy \n")
                    else:
                        spy.salutation = raw_input("What should we call you (Mr or Ms) : ")
                        if len(spy.salutation) == 0 :
                            print("You are not providing valid Option")
                        elif spy.salutation.isalpha() == 0:
                            print("you are not providing valid information ")
                        else:
                            spy.name = spy.salutation+" "+spy.name
                            spy.rating = raw_input("Enter your rating : ")
                            if len(spy.rating) == 0:
                                print("You are not providing correct information \n")
                            else:
                                spy.rating = float(spy.rating)      # Converting Rating into an Floating value
                                if spy.rating > 4.0:
                                    print("--->>>You Can Be A Good Leader<<<---")
                                elif spy.rating < 4.0 and spy.rating > 3.0:
                                    print("-->>You Are Good To BE In A Team<<--")
                                else:
                                    print("->We Can Always Use An Helping Hand<-")
                                print (" Your account has been created \n Welcome %s .We are happy to have you here. \n Your age %s and Rating is %s" %(spy.name,spy.age,spy.rating))
                                menu()         # Calling of menu function which provide second menu options


def menu():             # Function for Second Menu options
    current_status_message=None
    choice2 = int(raw_input(" 1) To Add Status \n 2) To Add friend \n 3) Send A Secret Message \n 4) Read A Secret Message \n 5) Read chats history from a user \n 6) Go To Main Menu \n ENTER YOUR CHOICE  :- "))
    while True:
        if choice2 == 1:
            current_status_message=(status_update(current_status_message))          # Calling of status_update() function

        elif choice2 == 2:
            choice3 = 'Y'
            while choice3.upper() == 'Y':
                print(add_friend())         # Calling of add_friend() function
                choice3 = raw_input("want to add more friends (Y or N)\n")
        elif choice2 == 3:
            send_a_message()            # Calling of send_a_message() function
        elif choice2 == 4:
            read_a_message()            # Calling of read_a_message() function
        elif choice2 == 5:
            read_chat_history()             # Calling of read_chat() function
        elif choice2 == 6:
            break
        else:
            print "[[Select From Valid Options]]"
        choice2 = int(raw_input(" 1) To Add Status \n 2) To Add friend \n 3) Send A Secret Message \n 4) Read A Secret Message \n 5) Read chats history from a user \n 6) Go To Main Menu \n ENTER YOUR CHOICE  :- "))


def status_update(current_status_message):  # Function to add a status

    updated_status_message = None

    if(current_status_message!=None):
        print "Current Status is ''" + current_status_message+"''"

    else:
        print "Current Status is ''"+str(updated_status_message)+"''"

    choice = raw_input("Want to chose from old status (Y or N) : ")

    if choice.upper() == 'N':           # Add new status

        new_status_message = raw_input("Enter your status : ")

        if  len(new_status_message) == 0:
            print("You are not providing Valid Information \n")
        else:
            updated_status_message = new_status_message
            status_messages.append(new_status_message)

    elif choice.upper() == 'Y':         # Chose from old status
        counter=1
        for temp in status_messages:
            print(str(counter) + " " + temp)
            counter = counter + 1
        choice2 = int(raw_input("Choose the status  "))
        updated_status_message = status_messages[choice2 - 1]

    if(updated_status_message):
        print "  STATUS UPDATED -> "+updated_status_message

    return updated_status_message


def send_a_message():           # Function to send a Message

    friend_choice = select_a_friend()           # Calling of select_a_friend() Function
    original_image = raw_input("What is the name of the image? ")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)
    print "Your secret message image is ready"


def read_a_message():           # Function to Read A Message

    sender = select_a_friend()          # Calling of select_a_friend() Function
    output_path = raw_input("What is the name of the file? ")
    try:
        length_chat = 0           # To store Maintain the average number of words spoken by a spy
        count = 1
        secret_text = Steganography.decode(output_path)

        length_chat = int(length_chat +len(secret_text.split()))
        length_chat=length_chat/count
        count=count+1

        new_chat = ChatMessage(secret_text,length_chat,False,)
        friends[sender].chats.append(new_chat)
        print "Your secret message has been saved \n Message is : %s" % (secret_text)

        if secret_text.upper() == 'SOS' or secret_text.upper() == 'SAVE ME' or secret_text.upper() == 'DANGER' or secret_text.upper() == 'SAVEME':
            print "**WARNING** \n  Spy %s ''NEED HELP IMMEDIATELY''" % (friends[sender].name)

        if len(secret_text.split()) > 100:
            print "Your Friend Spy  %s Is speaking too much." % (friends[sender].name)
            print "So, Cheif decided To Kick Spy Out of  The Application"
            del friends[sender]

    except:
        print("-->>You received an Empty Image<<-- \n -->> Or You are providing Wrong Image \n")


def read_chat_history():

    read_for = select_a_friend()            # Calling of select_a_friend() Function

    print '\n'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y  %I:%M %p"), 'You said:', chat.message)
        else:
            print '[%s] %s (You Received): %s' % (chat.time.strftime("%d %B %Y  %I:%M %p"), friends[read_for].name, chat.message)

            # read_chat history function ends


def select_a_friend():           # Function to show friend list
    counter = 1
    for temp in friends:
        print ("%d %s " % (counter,temp.name))
        counter = counter + 1

    friend_choice = int(raw_input("Chose the Friend To Communicate With\n"))
    friend_choice_position = friend_choice-1
    return(friend_choice_position)


def add_friend() :              # Function to add Friend
    new_friend = Spy('','',0,0.0)
    print("Number of Friends :"+str(len(friends)))
    new_friend.name = raw_input("Enter Name of Your Friend : ")
    if len(new_friend.name) == 0:
        print("You are not providing valid information")
    elif new_friend.name.isalpha() == 0:
        print("you are not providing valid information ")
    else:
        new_friend.age = raw_input("Enter your Friends Age : ")
        if len(new_friend.age) == 0:
            print("You are not providing valid information \n")
        elif new_friend.age.isdigit() == 0:
            print("You  are not providing valid information \n")
        else:
            new_friend.age=int(new_friend.age)            # Converting Age into Integer type
            if int(new_friend.age) < 12 or int(new_friend.age) > 50:
                print("Not eligible to be a friend in spy  application\n")
            else:
                new_friend.salutation = raw_input("What should we call you (Mr or Ms) : ")
                if len(new_friend.salutation) == 0:
                    print("You are not providing valid option")
                elif new_friend.salutation.isalpha() == 0:
                    print("You are not providing valid information ")
                else:
                    new_friend.name = new_friend.salutation + " " + new_friend.name
                    new_friend.rating = raw_input("Enter your friends rating : ")
                    if len(new_friend.rating) == 0:
                        print("You are not providing correct information \n")
                    elif float(new_friend.rating) < user_spy_rating :
                        print "Your Friends Rating is not Good to be a Spy on this Application"
                    else:
                        new_friend.rating = float(new_friend.rating)          # Converting Rating Into Floating Type
                        print ("Your Friend has been Added \n")
                        friends.append(new_friend)
                        return "Number of Friends :"+str(len(friends))



start_chat()               # Calling of main function start_chat()