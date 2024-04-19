print("Welcome to the jungle.")
print("You have been left here after your tour guide decided to leave you.")
print("Now it's up to you to escape.")
print("   ")
print("You come across a roaring river.")
word = input("Do you want to walk along or swim? ")
if word == "walk":
    print("You find a camp.")
elif word != "swim":
    print("You can't do this. Stop breaking the game.")
else:
    print("You drowned because the water was too fast and rough. Game over.")
print("   ")
funny = input("Unfortunately, they are cannibals and want to eat you. But they also have a treasure map. Do you run or sneak to get the map? ")
if funny == "run":
    print("The cannibals heard and saw you, making chase. They were faster and caught up. Game over.")
elif funny != "sneak":
    print("The cannibals saw you instantly, and ran up to you. Game over.")
else:
    print("You managed to sneak around and steal the map.")
print("   ")
meme = input("You stealthly walk out of the camp and follow the map. After a few hours, you find the place marked 'x'. Do you dig with your hands or try make a tool? ")
if meme == "dig":
    print("You got a cut and died from infections. Game over.")
elif meme != "tool":
    print("You died from starvation.")
else:
    print("You managed to make a tool that could dig without any injuries. You dig up the treasure, but there wasn't any in the hole. The only thing in the area marked 'x' was a bomb. By digging, you have activated the bomb and you blew up. The end.")
print("   ")
print("...")
print("   ")
print("Just kidding. Miraculously, you have survived your dilemma and found the real treasure map in the hole. However, you are currently running from the cannibals as they managed to hear the explosion.")
print("   ")
harhar = input("There are a bunch of bushes to your left, and a clearing to your right. Do you go left to hide or right and try to run? ")
if harhar == "left":
    print("You hid in the bushes and the cannibals ran past you. After some time has passed, they walked back to their camp.")
elif harhar != "right":
    print("You took too long deciding between left or right, as going straight would make you hit a wall of trees. The cannibals caught up and they ate you for dinner. The end")
else:
    print("You almost got caught by the cannibals, but a wolf suddenly appeared with it's pack and scare them off, while chasing them. Good thing you were always skinny.")
print("  ")
print("Deciding you did not want to stay any longer so you could live, you head to a river you heard far away. You find 2 boats.")
lel = input("Which boat do you pick? (first or second) ")
if lel == "first":
    print("Both boats were the same. You found a GPS on a boat and rowed home. The end.")
elif lel != "second":
    print("Both boats were the same. You found a GPS on a boat and rowed home. The end.")
else:
    print("Pick one, you ain't getting out otherwise.")
