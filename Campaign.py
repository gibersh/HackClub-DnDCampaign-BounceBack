from pyscript import document

def handle_roll(event):
    global current_room
    event.preventDefault()  # Stops page reload
    
    roll_input = document.querySelector("#fname")
    output_div = document.querySelector("#output")
    
    try:
        roll = int(roll_input.value)
    except ValueError:
        output_div.innerText = "Please enter a valid number!"
        return

    # Room 2 Logic
    if current_room == 2:
        if roll < 1 or roll > 20:
            message = "Invalid roll! Enter a number between 1 and 20."
        elif roll == 20:
            message = "Natural 20! You smash the door open and enter Room 3!"
            current_room = 3
        elif roll >= 12:
            message = f"Rolled {roll}: Success! You pick the lock and enter Room 3."
            current_room = 3
        elif roll == 1:
            message = "Natural 1! Your lockpick snaps. You are still stuck in Room 2."
        else:
            message = f"Rolled {roll}: Failure! The door won't budge. Roll again."
    else:
        message = f"Rolled {roll} in Room {current_room}! (Add Room 3 logic next!)"

    # Update BOTH the webpage banner and the terminal log
    output_div.innerText = message
    print(f"> {message}")
    
    # Clear the input box for the next roll
    roll_input.value = ""


print("")
print("")
print("ROOM 1:")
print("")
print("DM: You're all in a cage. Bars surround you, making up the walls, floor and ceiling. The cage is suspended above an immeasurable fall, held up by a single chain. Enclosed with you in the 25ft. cube is a menacing druid, fast asleep in his bear form. Your cage is the only one in the room, an additional 25ft. from the walls and ceiling. In the dim lighting, you can barely make out the shape of an arch, beyond which is a magical darkness no eyes can pierce. You have been stripped of your memories and all you have is your starter gear, two 15ft. long iron poles, and two silver claspes.")
print("")
print("The bars on the ceiling and floor, the chain, and the claspes are all mithril, and as such are unbreakable. The poles themselves are usable weapons, with a to-hit bonus of +1+PB+Strength modifier, dealing 1d4+to-hit bonus Bludgeoning damage on a hit and forcing the target to make both Constitution and Dexterity saving throws, dealing an additional 4d4 blugeoning damage on two failed saves, half as much on split saves, or none on two succesful throws, with the target knocked prone if the Dexterity throw is failed. The bars that make up the walls are enchanted silver, and they break upon a 20+ srength check or an 11+ to hit roll with a mithril object. Over the course of the entire campaign, unless otherwise stated in the DM-only notes after the description of the room, the druid revives all characters ASAP. As DM, it is up to you how detailed the druid's stat block/character sheet  is, along with their pronouns, but please note that they have an unlimited ability to revive characters, except after three failed death saves, which is a scnario that will be explaind later. After the room is cleared, tell each player IN PRIVATE how many times they leveled up, but not why. They will update their character sheet in the break taken in between rooms during the short rest. Character's level should be calculated where the number of deaths required to level up is one more than the previous level, starting at one death to reach level two.")
print("")
print("The solution to escaping the first room is to shear one of the poles into a 5ft. and a 10ft. segment, then using one of the claspes to connect the 10ft. segment with the remaining 15ft. pole. All other solutions, no matter how creative, will cause them to any characters that 'reach the other side' to fall into the chasm. The druid now resurects them, and they are summoned back into the cage.")
print("")
print("Room 2:")
print("")
print("DM: The darkness in the room prevents everyone from seeing anything. Suddeny you all find yourselves scattered, and when the darkness clears, you each stnd in a room with a single desk, piece of paper, and a pencil. On the paper, one question and one question only is writen:")
print("Which is red and which is blue?")
print("A: \033[31mBlue\033[0m")
print("B: \033[34mRed\033[0m")
print("C: YOUR MOM")
print("D: All the above")
print("E: A&B")
print("Red:_")
print("Blue:_")
print("Each character MUST select ONE LETTER as their answer.")
print("")
print("Red is 'D' and Blue is 'E.' All other answers result in death and the druid will revive them in cage. BTW, he hasn't left the cage.")
print("")
print("")
print("If you fail, roll again. Each failure counts as a death as far as leveling up is concerned.")
