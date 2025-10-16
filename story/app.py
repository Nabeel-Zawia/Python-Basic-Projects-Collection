import time

print(" ____________________________________________________________________")
print("/ \\-----     ---------  -----------     -------------- ------    ----\\")
print("\\_/__________________________________________________________________/")
print("|~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|")
print("|  _   ~~ ~~ __,---'_       \"         `. ~~~ _,--.  ~~~~ __,---.  ~~|")
print("| | \\___ ~~ /      ( )   \"          \"   `-.,' (') \\~~ ~ (  / _\\ \\~~ |")
print("|  \\    \\__/_   __(( _)_      (    \"   \"     (_\\_) \\___~ `-.___,'  ~|")
print("|~~ \\     (  )_(__)_|( ))  \"   ))          \"   |    \"  \\ ~~ ~~~ _ ~~|")
print("|  ~ \\__ (( _( (  ))  ) _)    ((     \\\\//    \" |   \"    \\_____,' | ~|")
print("|~~ ~   \\  ( ))(_)(_)_)|  \"    ))    //\\\\ \" __,---._  \"  \"   \"  /~~~|")
print("|    ~~~ |(_ _)| | |   |   \"  (   \"      ,-'~~~ ~~~ `-.   ___  /~ ~ |")
print("| ~~     |  |  |   |   _,--- ,--. _  \"  (~~  ~~~~  ~~~ ) /___\\ \\~~ ~|")
print("|  ~ ~~ /   |      _,----._,'`--'\\.`-._  `._~~_~__~_,-'  |H__|  \\ ~~|")
print("|~~    / \"     _,-' / `\\ ,' / _'  \\`.---.._          __        \" \\~ |")
print("| ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   \" \" \\~|")
print("|  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \\ \\_   \" |~|")
print("| ~ | | -- _    /~/  `-_- _  _,' '  \\ \\_`-._,-'  / --   \\  - \\_   / |")
print("|~~ | \\ -      /~~| \"     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|")
print("| ~~\\  \\_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|")
print("|~   \\      ,'~~|  \" (o o)   \"         \" \" |~~~ \\_,-' ~ `.     ,'~~ |")
print("| ~~ ~|__,-'~~~~~\\    \\\"/      \"  \"   \"    /~ ~~   O ~ ~~`-.__/~ ~~~|")
print("|~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|")
print("|____~jrei~__~_______~~_~____~~_____~~___~_~~___~\\_|_/ ~_____~___~__|")
print("/ \\----- ----- ------------  ------- ----- -------  --------  -------\\")
print("\\_/__________________________________________________________________/")

print("welcome to treasure island. /n your mission is to find the treasure.")
wayToHead = input("which way would you like top go left, right , straight or backward : ")
swimWait=""
house = 0
if wayToHead == "right":
    print("GameOver better luck next time, Fall into a hole")
elif wayToHead =="left":
    print("Oh no, there is a lake here what are you going to do??: ")
    time.sleep(3)
    swimWait = input("would you like to swim or wait for a boat ")
    if swimWait == "wait":
      house=  int(input("you are close to the treasure yet you are hungry and you need some supplemnts , how lucky you are you found a village with three houses , which door will you knock 1, 2 or 3: "))
      if house == 1:
        print("GameOver better luck next time, the villager burnt you ! 🫢") 
      elif house ==2:
         print("You found the supplements and the villager will give you the key for the treasure if you helpt him in part two \n you won the game for now")
      elif house ==3 :
         print("Game over better luck next time , you have been eaten by a beast 👹 !")
      else:
         print("Game over better luck next time, you died because of lack of supplements")
         

    else:
        print("GameOver better luck next time , Attacked by trout.")    

else:
    print("Gameover better luck next time , died with an air strike!")