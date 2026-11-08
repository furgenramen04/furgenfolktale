# diagram of game where a person escapes the serial killer in a hotel.
#   [escape] <- [riddle room (reception)] <- [elevator with math puzzle] <- [bedroom] -> [laundry room] -> [hide in basket (death)]
#                                                                                 |
#                                                                                 v
#                                                                          [hide behind door]

room = "bedroom"
ekey = 0
bkey = 0
game_running = True

while game_running:
    if room == "bedroom":
        print("You wake up to the sound of the television in your hotel room. 'That's odd', you think, 'I didn't leave the TV on last night.' On it is the news. A serial killer has broken into a hotel. In fact, YOUR hotel. It is now up to you whether you survive. You jump out of bed and grab a flashlight, and you are met with two choices. Run to the elevator and try to leave the hotel, or hide in the laundry room.")
        print("")
        choice = input("Laundry or elevator? ").lower()

        if choice == "laundry":
            room = "laundry"
        elif choice == "laundry room":
            room = "laundry"
        elif choice == "elevator":
            room = "elevator"
        else:
            print("Where are you trying to go?")

    elif room == "laundry":
        print("You tiptoe into the laundry room and shut the door behind you. You hear heavy footsteps coming from the bedroom. You need to hide, and now.")
        print("")
        print("You see a full-size laundry basket that you could hide inside. Or, you could hide behind the door, hoping that the darkness of the room conceals you.")
        print("")

        hide_choice = input("Basket or door? ").lower()

        if hide_choice == "basket":
            print("A man walks into the room. You hear his slurred speech, 'It would be a pity if a victim of mine lay in this basket...'. Before you can do anything, you feel his machete penetrate through the clothes and you. You are dead.")
            game_running = False
        elif hide_choice == "door":
            print("A man walks into the room. You hear his slurred speech, 'It would be a pity if a victim of mine lay in this basket...'. You see his shadow stab his knife into the laundry basket. Annoyed, he slams the door and leaves. You are alive, for now." )
            print("")
            print("You can hear the man destroying things in the bedroom. His machete is buried in the basket. Do you confront him or run to the elevator?")
            print("")
            confront_choice = input("Confront or run: ").lower()

            if confront_choice == "confront":
                print("Even with a machete, you are no match for the serial killer. He snatches the machete away and quickly disposes of your head.")
                print("")
                print("You are dead.")
                game_running = False
            elif confront_choice == "run":
                room = 'elevator'

    elif room == 'elevator':
        print("You run out of your room and down the hallway, slamming the buttons of the elevator, which don't work.")
        print("")
        print("You look carefully at the buttons. Someone has swapped them with mathematical equations. You need to go to the 3rd floor, so you need to find where x = 3. ")
        print("")
        print("a. 3x+2 = 6")
        print("b. 4x+4 = 4")
        print("c. 3x > 3")
        print("d. 2x+6 = 12")
        print("")

        answer = input("What is your decision? ").lower()

        if answer == "d":
            print("You enter the elevator safely, and make it to the reception floor.")
            room = "reception"
        elif answer == "a" or answer == "c" or answer == "b":
            print("You enter the elevator. You watch as it misses room three, continuing to fall while gaining speed. You can only watch as the elevator smashes into the floor, erupting into flames around you.")
            print("")
            print("You are dead.")
            game_running = False
        else:
            print("Invalid response.")

    elif room == "reception":
        print("You enter the receptionist's room. As you step foot in the room, you see the elevator doors slam shut. The door to the exit is locked, with chains and a heavy iron padlock. Searching around the room, you find a paper note. It says 'Where the elephant lies is where you shall find their tail, but the key is within the brain.")
        print("")
        print("You remember that there is a plush elephant inside the merch shop. Maybe 'the brain' is referring to the CCTV room?")
        print("")

        choice_riddle = input("Do you go to the merch shop or try the CCTV? ").lower()

        if choice_riddle == "merch shop" or choice_riddle == "merch" or choice_riddle == "shop":
            print("You enter the dark merch shop. There are two claw machines, lit up at the back of the room. You see a grey plush elephant in one and a black one in the other. Which elephant do you try?")
            print("")
            elephant_choice = input("Black or grey? ").lower()

            if elephant_choice == "black":
                print("The machine acts weirdly at your every touch. Each movement of the joystick seems delayed, and it refuses to coordinate with you. You start hearing hisses from the back of it. You go around to find snakes coming out from under it. Before you can run, one of them sinks its teeth into your foot. ")
                print("")
                print("You are dead.")
                game_running = False
            elif elephant_choice == "grey":
                print("The machine feels easy and obedient to your commands. You painlessly remove the elephant from it. Within the elephant's behind is a bronze key. You return to the receptionist's room. Do you try to escape or try the CCTV door?")
                print("")
                bkey = 1

                cctv_choice = input("CCTV room or escape? ").lower()

                if cctv_choice == "cctv" or cctv_choice == "cctv room" or choice_riddle == "cctv":
                    if bkey == 1:
                        print("You enter the CCTV surveillance room. All screens are dark but one. You walk towards the screen, which shows points towards a drawer in the receptionist's room.")
                        print("")
                        print("You open the drawer to find another key.")
                        ekey = 1 

                        escape_choice = input("Do you try to escape using the key? ").lower()

                        if escape_choice == "yes":
                            print("You unlock the door and sprint out of the hotel, into the street. Somehow, there is no one there, even though the sun is up. ")
                            print("")
                            print("At last, you are free, you think as an anvil drops onto your head.")
                            print("")
                            print("You are dead.")
                            game_running = False

                        else:
                            print("It is too late. The serial killer runs into the room, stabbing you with his machete.")
                            print("")
                            print("You are dead.")
                            game_running = False

                    elif bkey == 0:
                        print("You try the lock on the door, but you cannot open it.")
                        room = "reception"

                elif cctv_choice == "escape":
                    if ekey == 0:
                        print("You try the lock, and it fails.")
                        room = "reception"
                    elif ekey == 1:
                        print("You unlock the door and sprint out of the hotel, into the street. Somehow, there is no one there, even though the sun is up. ")
                        print("")
                        print("At last, you are free, you think as an anvil drops onto your head.")
                        print("")
                        print("You are dead.")
                        game_running = False

        elif choice_riddle == "cctv":
            if bkey == 0:
                print("You try the lock on the door, but you cannot open it.")
                room = "reception"
            elif bkey == 1:
                print("You enter the CCTV surveillance room. All screens are dark but one. You walk towards the screen, which shows points towards a drawer in the receptionist's room.")
                print("")
                print("You open the drawer to find another key.")
                ekey = 1

                escape_choice = input("Do you try to escape using the key? ").lower()

                if escape_choice == "yes":
                    print("You unlock the door and sprint out of the hotel, into the street. Somehow, there is no one there, even though the sun is up. ")
                    print("")
                    print("At last, you are free, you think as an anvil drops onto your head.")
                    print("")
                    print("You are dead.")
                    game_running = False

                else:
                    print("It is too late. The serial killer runs into the room, stabbing you with his machete.")
                    print("")
                    print("You are dead.")
                    game_running = False

    print("")