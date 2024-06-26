# 1280 x 720
# Game created by Sebastian Bartuzi
# For cheat: add 10 points click Control Left
# For boss key click Shift Left
# Images sources:
# excel.png: https://www.klipfolio.com/blog/top-excel-alternatives
# pause.png: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3
# /Ic_pause_circle_outline_48px.svg/1024px-Ic_pause_circle_outline_48px.svg.png
# rocket.png: https://www.stickpng.com/img/transport/spacecraft/rounded
# -rocket-emoji
# tick.png: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5
# /Green_tick_pointed.svg/480px-Green_tick_pointed.svg.png


from tkinter import Tk, PhotoImage, Button, Entry, Label, Canvas
from random import randint as rand
import re


# Exiting game
def quitGame():
    global window, canva
    createStars()
    canva.create_text(wwidth/2, wheight/2, fill="white",
                      font=("Tahoma", 80, 'bold'), text="Thanks for playing!")
    window.after(1500, lambda: window.destroy())


# Changing settings - mouse or keyboard
def option(button1, button2, i):
    global opt1, opt2
    button1.configure(image=tick)
    button2.configure(image=notick)
    if (i == 1):
        opt1 = 1
        opt2 = 0
    else:
        opt1 = 0
        opt2 = 1


# Changing settings - Left/Right or a/d
def changeKeys(leftKey, rightKey):
    global opt2_1, opt2_2
    if opt2_1:
        opt2_1 = 0
        opt2_2 = 1
        leftKey.configure(text="Move Left: <a>")
        rightKey.configure(text="Move Right: <d>")
    elif opt2_2:
        opt2_1 = 1
        opt2_2 = 0
        leftKey.configure(text="Move Left: <Left>")
        rightKey.configure(text="Move Right: <Right>")


# Saving control settings to the file settings.txt
def saveControls():
    file = open("settings.txt", "w")
    file.write(str(int(opt1)) + "\n")
    file.write(str(int(opt2)) + "\n")
    file.write(str(int(opt2_1)) + "\n")
    file.write(str(int(opt2_2)))
    file.close()
    setMainMenu()


# Creating controls configuration design
def configureControls():
    global wwidth, canva
    createStars()

    # Creating heading
    canva.create_text(wwidth/2, 105, fill="white", font=("Tahoma", 60, 'bold'),
                      text="Configure Controls")
    canva.create_text(wwidth/2, 185, fill="white", font=("Tahoma", 20, 'bold'),
                      text="Here you can configure controls used in the game.")

    # Creating rectangle for option to control with mouse
    canva.create_rectangle(wwidth/2 - 410, 235, wwidth/2 - 10, 480,
                           fill="#101455", outline="white")
    opt1button = Button(window, bg="white", image=tick, command=lambda:
                        option(opt1button, opt2button, 1))
    opt1button_window = canva.create_window(wwidth/2 - 395, 250, anchor="nw",
                                            window=opt1button)
    canva.create_text(wwidth/2 - 355, 250, fill="white", font=("Tahoma", 20,
                      'bold'), text="Press the mouse and\nmove the rocket",
                      anchor="nw")

    # Creating rectangle for option to control with keyboard
    canva.create_rectangle(wwidth/2 + 10, 235, wwidth/2 + 410, 480,
                           fill="#101455", outline="white")
    opt2button = Button(window, bg="white", image=notick, command=lambda:
                        option(opt2button, opt1button, 2))
    opt2button_window = canva.create_window(wwidth/2 + 25, 250, anchor="nw",
                                            window=opt2button)
    # If control with keyboard is chosen, change position of tick
    if opt2:
        opt1button.configure(image=notick)
        opt2button.configure(image=tick)
    canva.create_text(wwidth/2 + 65, 250, fill="white", font=("Tahoma", 20,
                      'bold'), text="Control with keyboard", anchor="nw")
    temp_height = 340
    # Create buttons for Left or a
    if opt2_1:
        text = "Move Left: <Left>"
    if opt2_2:
        text = "Move Left: <a>"
    leftKey = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                     text=text, width=18, height=2, bg="#03051E")
    leftKey_window = canva.create_window(wwidth/2 + 210, temp_height,
                                         anchor="c", window=leftKey)
    # Create buttons for Right and d
    temp_height += 86
    if opt2_1:
        text = "Move Right: <Right>"
    if opt2_2:
        text = "Move Right: <d>"
    rightKey = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                      text=text, width=18, height=2, bg="#03051E",
                      command=lambda: changeKeys(leftKey, rightKey))
    rightKey_window = canva.create_window(wwidth/2 + 210, temp_height,
                                          anchor="c", window=rightKey)
    # Because we define right key after left, we must configure leftKey to
    # add changeKeys command
    leftKey.configure(command=lambda: changeKeys(leftKey, rightKey))

    # Creating button for returning to main menu
    mainMenu = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                      text="Save and Go Back to Menu", width=23, height=2,
                      bg="#03051E", command=lambda: saveControls())
    mainMenu_window = canva.create_window(wwidth/2, 560, anchor="c",
                                          window=mainMenu)
    canva.pack()


# Read leaderboard.txt and save data to player and score arrays
def getLeaderboard():
    file = open("leaderboard.txt", "r")
    player = []
    score = []
    i = 0
    for line in file:
        j = 0
        for x in line.split():
            if j == 0:
                player.append(x)
                j += 1
            else:
                score.append(x)
            i += 1
    file.close()
    return player, score


# Creating leaderboard
def createLeaderboard(player, score):
    w = wwidth/2 - 300
    temp_height = 235
    tableRow = []*5

    # Creating row for leaderboard
    for i in range(5):
        canva.create_rectangle(w, temp_height, w+600, temp_height+60,
                               fill="#101455", outline="white")
        canva.create_text(w+10, temp_height+30, fill="white", font=("Tahoma",
                          20, 'bold'), text=player[i], anchor="w")
        canva.create_text(w+590, temp_height+30, fill="white", font=("Tahoma",
                          20, 'bold'), text=score[i], anchor="e")
        temp_height += 65

    # Creating button for returning to main menu
    mainMenu = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                      text="Back to Menu", width=15, height=2, bg="#03051E",
                      command=lambda: setMainMenu())
    mainMenu_window = canva.create_window(wwidth/2, temp_height+80, anchor="c",
                                          window=mainMenu)


# Creating leaderboard design
def leaderboard():
    global wwidth, canva
    createStars()

    # Creating heading
    canva.create_text(wwidth/2, 105, fill="white", font=("Tahoma", 60, 'bold'),
                      text="Leaderboard")
    canva.create_text(wwidth/2, 185, fill="white", font=("Tahoma", 20, 'bold'),
                      text="Here are 5 players with the highest scores in" +
                      " history!")

    # Save leaderboard data and create leaderboard
    player, score = getLeaderboard()
    createLeaderboard(player, score)
    canva.pack()


# Creating how to play design
def howToPlay():
    global wwidth, canva
    createStars()

    # Creating heading
    canva.create_text(wwidth/2, 105, fill="white", font=("Tahoma", 60, 'bold'),
                      text="How To Play")

    # Creating game instructions
    canva.create_rectangle(50, 185, wwidth - 50, 451, fill="#101455",
                           outline="white")
    temp_height = 218
    canva.create_text(wwidth/2, temp_height, fill="white", font=("Tahoma", 20,
                      'bold'), text="You will be travelling through space" +
                      " with 2 rockets. They move exactly")
    temp_height += 40
    canva.create_text(wwidth/2, temp_height, fill="white", font=("Tahoma", 20,
                      'bold'), text="the same way - when the left one moves" +
                      " 3 centimeters to left, the right one")
    temp_height += 40
    canva.create_text(wwidth/2, temp_height, fill="white", font=("Tahoma", 20,
                      'bold'), text="will do the same. You control the left" +
                      " rocket and you do it with your mouse")
    temp_height += 40
    canva.create_text(wwidth/2, temp_height, fill="white", font=("Tahoma", 20,
                      'bold'), text="(you can change it and use the keyboard" +
                      " controls, if you wish).")
    temp_height += 40
    canva.create_text(wwidth/2, temp_height, fill="white", font=("Tahoma", 20,
                      'bold'), text="The aim of the game is to survive as" +
                      " long as possible - avoid collision with")
    temp_height += 40
    canva.create_text(wwidth/2, temp_height, fill="white", font=("Tahoma", 20,
                      'bold'), text="the obstacles. Good luck!")

    # Creating button for returning to main menu
    mainMenu = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                      text="Back to Menu", width=15, height=2, bg="#03051E",
                      command=lambda: setMainMenu())
    mainMenu_window = canva.create_window(wwidth/2, 531, anchor="c",
                                          window=mainMenu)
    canva.pack()


# Create leaderboard after finishing the game
def showStatistics(finalScore):
    global alreadyBossKey, canva
    createStars()

    # Save leaderboard data
    player, score = getLeaderboard()

    # If the result was higher than result of last player in leaderboard, add
    # new player to leaderboard and create updated leaderboard
    if (finalScore > int(score[4])):

        # Create heading
        canva.create_text(wwidth/2, 105, fill="white", font=("Tahoma", 60,
                          'bold'), text="Congratulations!")
        canva.create_text(wwidth/2, 185, fill="white", font=("Tahoma", 20,
                          'bold'), text="You made it to the TOP5 of history!" +
                          " Please type in your name.")
        canva.create_text(wwidth/2, 225, fill="white", font=("Tahoma", 20,
                          'bold'), text="Your name can consist only from" +
                          " letters and numbers. It must at most")
        canva.create_text(wwidth/2, 265, fill="white", font=("Tahoma", 20,
                          'bold'), text="20 characters. You will not be able" +
                          " to send it until it is inputted correctly.")

        # Create name input space
        enterName = Entry(window, bg="#101455", fg="white", font=("Tahoma", 20,
                          'bold'))
        enterName_window = canva.create_window(wwidth/2, 325, window=enterName)

        # Define which position should the player be placed into
        if (finalScore > int(score[0])):
            position = 0
        elif (finalScore > int(score[1]) and finalScore <= int(score[0])):
            position = 1
        elif (finalScore > int(score[2]) and finalScore <= int(score[1])):
            position = 2
        elif (finalScore > int(score[3]) and finalScore <= int(score[2])):
            position = 3
        else:
            position = 4

        # Add player to leaderboard
        def addToLeaderboard():
            # Create regex - word conists only from letters and numbers, at
            # most 20 characters
            regex = "^([A-Z]|[a-z]|[0-9]){1,20}$"
            # Get name from the input
            name = enterName.get()

            # If the name was inputted correctly, add data to player and score
            # arrays
            if(re.search(regex, name)):
                i = 4
                while (i >= 0):
                    # Write data to lower row
                    if (i > position):
                        player[i] = player[i - 1]
                        score[i] = score[i - 1]
                    # Put user data to appropriate row
                    if (i == position):
                        player[i] = name
                        score[i] = finalScore
                    i -= 1

                # Write data from player and score arrays to leaderboard.txt
                file = open("leaderboard.txt", "w")
                for i in range(5):
                    file.write(player[i] + " " + str(int(score[i])) + "\n")
                file.close()

                # Create leaderboard with updated data
                createStars()
                # Create heading
                canva.create_text(wwidth/2, 105, fill="white", font=("Tahoma",
                                  60, 'bold'), text="Congratulations!")
                canva.create_text(wwidth/2, 185, fill="white", font=("Tahoma",
                                  20, 'bold'), text="What about beating your" +
                                  " highscore?")
                # Create leaderboard
                createLeaderboard(player, score)

        # Create button to define addToLeaderboard function
        addName = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                         text="Enter Name", width=15, height=2, bg="#03051E",
                         command=lambda: addToLeaderboard())
        addName_window = canva.create_window(wwidth/2, 415, window=addName)

    # If the result was not higher than result of last player in leaderboard,
    # create regular leaderboard
    else:
        # Create heading
        canva.create_text(wwidth/2, 105, fill="white", font=("Tahoma", 60,
                          'bold'), text="Your score: " + str(finalScore))
        canva.create_text(wwidth/2, 185, fill="white", font=("Tahoma", 20,
                          'bold'), text="Here are 5 players with the highest" +
                          " scores in the history!")
        # Create leaderboard
        createLeaderboard(player, score)

    # The function showStatistics is called 3 seconds after the game is over.
    # If user calls bossKey during displaying "Game Over!", the screen will
    # update with statistics window, replacing the excel image. The if
    # statement below was provided to prevent from this situation.
    if alreadyBossKey:
        bossKey(0)
    canva.pack()


# Display "Game Over!"
def gameOver(currentScore):

    # If the game is over, there is no need to make game paused and save its
    # data
    global doPauseGame, doSave
    doPauseGame, doSave = 0, 0

    # Write to save.txt that no game is saved
    file = open("save.txt", "w")
    file.write("0")
    file.close()
    createStars()
    gameOver = canva.create_text(wwidth/2, wheight/2, font=("Tahoma", 120,
                                 'bold'), fill="white", text="Game Over!")

    # After 3 seconds, call showStatistics
    window.after(3000, lambda: showStatistics(currentScore))
    canva.pack()


# Write to save.txt that no game was saved
def dontSave():
    file = open("save.txt", "w")
    file.write("0\n")
    file.close()


# Start the game
def startGame():
    global currentScore, speed, wwidth, wheight, paused, metObstacle, canva
    # When game starts, define that it is not paused and rocket did not hit
    # any obstacle
    paused, metObstacle = 0, 0
    # Check if a game was saved and loaded
    file = open("save.txt", "r")
    data = file.readlines()
    # If a game was saved and loaded, call its score and left rocket position
    if data[0] == "1\n":
        currentScore = int(data[1].rstrip())
        if len(data[2]) > 3:
            x = int(data[2][:-3])
        else:
            x = int(data[2])
        speed = int(data[3].rstrip())
    # If a game was not saved and loaded, define score as 0 and left rocket
    # position to the middle
    else:
        currentScore = 0
        x = (wwidth/2 - 8)/2
        speed = 25
    file.close()

    # Make the left rocket follow the mouse and right rocket to follow moves
    def moveRocketWithMouse(event):
        x = event.x
        if (x >= 20 and x <= wwidth/2 - 28):
            canva.coords(rocketLeft, x, y)
            canva.coords(rocketRight, x+((wwidth/2)+8), y)

    # Move rockets to left if the appropriate key was pressed
    def moveRocketLeft(event):
        coords = canva.coords(rocketLeft)
        if coords[0] >= 28:
            canva.move(rocketLeft, -8, 0)
            canva.move(rocketRight, -8, 0)

    # Move rockets to right if the appropriate key was pressed
    def moveRocketRight(event):
        coords = canva.coords(rocketLeft)
        if coords[0] <= wwidth/2 - 36:
            canva.move(rocketLeft, 8, 0)
            canva.move(rocketRight, 8, 0)

    # Create game design
    createStars()
    y = wheight - 50
    # Create line which seperates rockets area
    canva.create_rectangle(wwidth/2 - 8, 0, wwidth/2 + 8, 720, fill="#1E1106")
    # Create rockets
    rocketLeft = canva.create_image(x, y, image=rocketImage, anchor="s")
    rocketRight = canva.create_image(x + wwidth/2 + 8, y, image=rocketImage,
                                     anchor="s")
    # Create current score display
    displayCurrentScore = canva.create_text(wwidth-10, 10, font=("Tahoma", 30,
                                            'bold'), fill="white", anchor="ne",
                                            text=str(currentScore))

    # Define what program should do if the game was paused
    def pauseGame():
        global doSave

        # Go back to main menu and write to save.txt that no game was saved
        def menuWithoutSaving():
            dontSave()
            setMainMenu()

        # Quit the game and write to save.txt that no game was saved
        def quitWithoutSaving():
            dontSave()
            quitGame()

        # If the game was paused or boss key pressed, write data to save.txt
        if doSave:
            file = open("save.txt", "w")
            file.write("1\n")
            file.write(str(currentScore) + "\n")
            coords = canva.coords(rocketLeft)
            file.write(str(coords[0]) + "\n")
            file.write(str(speed) + "\n")
            file.close()
            # Set doSave to 0, saving game more than once may cause errors
            doSave = 0

        # Create pause design
        createStars()
        # Create heading
        canva.create_text(wwidth/2, 105, fill="white", font=("Tahoma", 60,
                          'bold'), text="Paused")
        # Create buttons of action
        temp_height = 215
        goBack = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                        text="Resume", width=26, height=2, bg="#03051E",
                        command=lambda: startGame())
        goBack_window = canva.create_window(wwidth/2, temp_height,
                                            window=goBack)
        temp_height += 76
        saveAndMenu = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                             text="Save And Go To Main Menu", width=26,
                             height=2, bg="#101455", command=lambda:
                             setMainMenu())
        saveAndMenu_window = canva.create_window(wwidth/2, temp_height,
                                                 window=saveAndMenu)
        temp_height += 76
        menuWithoutSave = Button(window, font=("Tahoma", 20, 'bold'),
                                 fg="white", text="Go To Main Menu Without" +
                                 " Saving", width=26, height=2, bg="#101455",
                                 command=lambda: menuWithoutSaving())
        menuWithoutSave_window = canva.create_window(wwidth/2, temp_height,
                                                     window=menuWithoutSave)
        temp_height += 76
        saveAndQuit = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                             text="Save And Quit Game", width=26, height=2,
                             bg="#101455", command=lambda: quitGame())
        saveAndQuit_window = canva.create_window(wwidth/2, temp_height,
                                                 window=saveAndQuit)
        temp_height += 76
        quitWithoutSave = Button(window, font=("Tahoma", 20, 'bold'),
                                 fg="white", text="Quit Without Saving",
                                 width=26, height=2, bg="#AE070C",
                                 command=lambda: quitWithoutSaving())
        quitWithoutSave_window = canva.create_window(wwidth/2, temp_height,
                                                     window=quitWithoutSave)

    # Start countdown after game started/was resumed
    def countdown(count):
        global alreadyBossKey, doPauseGame, paused

        # If the game is during countdown or during action, when bossKey is
        # called, the game must be paused
        doPauseGame = 1

        # When bossKey is called during game, include option to make pause
        def bossKeyAfterStart(event):
            if doPauseGame:
                pauseGame()
            bossKey(0)

        # If bossKeyAfterStart was called, there is no need to call it again
        if alreadyBossKey == 0:
            # Call bossKeyAfterStart when Shift Left pressed
            window.bind("<Shift_L>", bossKeyAfterStart)

        # If the countdown has not finished and game was not paused, continue
        # the countdown
        if count >= 0 and paused == 0:
            # If the countdown has finished, set text to "Start!" and play game
            if count == 0:
                countText = "Start!"
                playGame()
            # If the countdown has not finished, set text to count
            else:
                countText = str(count)
            # Display text
            countdownText = canva.create_text(wwidth/2, wheight/2,
                                              fill="white", text=countText,
                                              font=("Tahoma", 120, 'bold'))
            # Prepare for next countdown
            count -= 1
            window.after(1000, lambda: canva.delete(countdownText))
            window.after(1000, lambda: countdown(count))

    # Count from 3 to 0
    countdown(3)

    # Play the game
    def playGame():
        global doSave

        # Game started, so if it is paused, the data must be saved. Set doSave
        # to 1
        doSave = 1

        # Create the pause button
        pauseButton = Button(window, bg="white", image=pause,
                             command=lambda: pauseGame())
        pauseButton_window = canva.create_window(10, 10, anchor="nw",
                                                 window=pauseButton)

        # Move rocket, depending on chosen controls
        if opt1:  # moving with mouse was set
            canva.bind("<B1-Motion>", moveRocketWithMouse)
        if (opt2 and opt2_1):  # moving with keyboard and Left/Right was set
            window.bind("<Left>", moveRocketLeft)
            window.bind("<Right>", moveRocketRight)
        if (opt2 and opt2_2):  # moving with keyboard and a/d was set
            window.bind("<a>", moveRocketLeft)
            window.bind("<d>", moveRocketRight)

        # Add 10 to currentScore and update it
        def addPoints(event):
            global currentScore
            currentScore += 10
            canva.itemconfigure(displayCurrentScore, text=str(currentScore))

        # If the cheat was activated, call addPoints
        window.bind("<Control_L>", addPoints)

        # Define the set of obstacles colours
        set = ["#F015DA", "#6414A2", "#2917CE", "#21F0F7", "#15C727",
               "#81D217", "#F3FA1F", "#FF8000", "#E50D0D", "#351406"]

        # Create obstacles
        def createObstacles():

            # The first square can be created at x=0, all squares have width 79
            startPos = 0
            squareWidth = 79
            squares = []

            # One block per area must be free to make rocket able to go
            freeBlock = rand(0, 7)

            # Create (or not) obstacles
            for i in range(16):
                if i != freeBlock and i != freeBlock + 8:
                    # Probability of creating obstacle is 50%
                    doCreate = rand(0, 1)
                    if doCreate:
                        # Define colours and coords
                        colour = rand(0, 9)
                        xy = (startPos, -80, startPos + squareWidth, -1)
                        # Create square and add it to array of squares
                        square = canva.create_rectangle(xy, outline="white",
                                                        fill=set[colour])
                        squares.append(square)
                # Move to next square
                startPos += squareWidth
                if i == 7:
                    # If the seperation line is next, include its width
                    startPos += 16

            # Start moving obstacles
            def moveObstacles():
                global currentScore, paused, metObstacle, speed

                # Check if square collides with a rocket
                def checkCoords(coordsSquare, coordsRocket):
                    if (coordsSquare[0] < (coordsRocket[0] + 20) and
                       coordsSquare[2] > (coordsRocket[0] - 20) and
                       coordsSquare[1] < coordsRocket[1] and
                       coordsSquare[3] > (coordsRocket[1] - 144)):

                        window.after(1000, gameOver(currentScore))
                        metObstacle = 1
                        return metObstacle

                # Check if squares are able to touch rockets
                coords = canva.coords(squares[0])
                if coords[3] >= wheight - 194 and coords[1] <= wheight - 50:
                    # If squares are able to touch rockets, check, if they
                    # really do
                    coordsRocketLeft = canva.coords(rocketLeft)
                    coordsRocketRight = canva.coords(rocketRight)
                    for i in range(len(squares)):
                        # Check if a square is on a left or right area and
                        # then compare coords with appropriate rocket
                        coordsSquare = canva.coords(squares[i])
                        if coordsSquare[0] < wwidth/2:
                            checkCoords(coordsSquare, coordsRocketLeft)
                        else:
                            checkCoords(coordsSquare, coordsRocketRight)
                # Move all squares
                for square in squares:
                    canva.move(square, 0, 5)
                # If rocket did not hit obstacles and they are out of screen,
                # prepare for new row of obstacles
                if coords[1] > wheight:
                    # Check and update speed of squares
                    if currentScore >= 0 and currentScore < 50:
                        speed = 25
                    if currentScore >= 50 and currentScore < 100:
                        speed = 20
                    if currentScore >= 100 and currentScore < 250:
                        speed = 15
                    if currentScore >= 250 and currentScore < 500:
                        speed = 12
                    if currentScore >= 500 and currentScore < 1000:
                        speed = 10
                    if currentScore >= 1000:
                        speed = 8
                    # Update points
                    addPoints(0)
                    # Delete squares when they go out of screen
                    for square in squares:
                        canva.delete(square)
                    squares.clear()
                    # Create new obstacles
                    createObstacles()
                # If rocket did not hit squares and they are not out of screen
                # move them again after time of speed
                if coords[1] <= wheight and paused == 0 and metObstacle == 0:
                    window.after(speed, moveObstacles)

            # Start moving obstacles
            moveObstacles()
        # Start creating obstacles
        createObstacles()
    canva.pack()


# Start new game, but first write to save.txt that new game has started
def startNewGame():
    dontSave()
    startGame()


# Create main menu design
def setMainMenu():
    global wwidth, wheight, canva
    createStars()
    # Create heading
    canva.create_text(wwidth/2, 105, fill="white", font=("Tahoma", 60, 'bold'),
                      text="Space Traveller")
    canva.create_text(wwidth/2, 185, fill="white", font=("Tahoma", 20, 'bold'),
                      text="Welcome!")
    temp_height = 275
    # Check in save.txt if any game is saved
    file = open("save.txt", "r")
    data = file.readlines()
    # If a game is saved, create buttons for loading and starting new game
    if data[0] == "1\n":
        loadGame = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                          text="Load Game", width=15, height=2, bg="#03051E",
                          command=lambda: startGame())
        loadGame_window = canva.create_window(wwidth/2, temp_height,
                                              anchor="c", window=loadGame)
        temp_height += 76
        newGame = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                         text="Start New Game", width=15, height=2,
                         bg="#101455", command=lambda: startNewGame())
        newGame_window = canva.create_window(wwidth/2, temp_height, anchor="c",
                                             window=newGame)
    # If a game is not saved, create button for starting game
    else:
        start = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                       text="Start Game", width=15, height=2, bg="#03051E",
                       command=lambda: startGame())
        start_window = canva.create_window(wwidth/2, temp_height, anchor="c",
                                           window=start)
    # Create other buttons
    temp_height += 76
    htp = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                 text="How To Play", width=15, height=2, bg="#101455",
                 command=lambda: howToPlay())
    htp_window = canva.create_window(wwidth/2, temp_height, anchor="c",
                                     window=htp)
    temp_height += 76
    ldrbrd = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                    text="Leaderboard", width=15, height=2, bg="#101455",
                    command=lambda: leaderboard())
    ldrbrd_window = canva.create_window(wwidth/2, temp_height, anchor="c",
                                        window=ldrbrd)
    temp_height += 76
    configure = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                       text="Configure Controls", width=15, height=2,
                       bg="#101455", command=lambda: configureControls())
    configure_window = canva.create_window(wwidth/2, temp_height, anchor="c",
                                           window=configure)
    temp_height += 76
    quit = Button(window, font=("Tahoma", 20, 'bold'), fg="white",
                  text="Quit Game", width=15, height=2, bg="#AE070C",
                  command=lambda: quitGame())
    quit_window = canva.create_window(wwidth/2, temp_height, anchor="c",
                                      window=quit)
    canva.pack()


# Create new design, starting with stars in background
def createStars():
    global wwidth, wheight, star, canva
    # Delete previous design
    canva.delete("all")
    # Clear star array
    star.clear()
    # Define set of possible star colours
    set = ["white", "#fefefe", "#dfdfdf"]
    # Create 1200 stars
    for i in range(1200):
        x = rand(1, wwidth)
        y = rand(1, wheight)
        size = rand(2, 5)
        f = rand(0, 2)
        xy = (x, y, x+size, y+size)
        # Create shape of star and add shape to star array
        temp_star = canva.create_oval(xy, fill=set[f])
        star.append(temp_star)


# Boss key
def bossKey(event):
    global alreadyBossKey, doPauseGame, paused, canva
    # Set alreadyBossKey and paused (if the game is not on, this variable will
    # not be necessary anywhere) to 1
    alreadyBossKey, paused = 1, 1
    # Create excel image
    excelImage = Label(window, image=excel)
    excelImage_window = canva.create_window(0, 0, anchor="nw",
                                            window=excelImage)

    # Function which comes after bossKey, this is for removing excel image
    def bossKeyRelease(event):
        global alreadyBossKey
        # Set alreadyBossKey to 0 - that will make bossKey able to be called
        # again
        alreadyBossKey = 0
        # Delete excel image
        canva.delete(excelImage_window)
        # Call bossKey when Shift Left pressed
        window.bind("<Shift_L>", bossKey)
    # Call bossKeyRelease  when Shift Left pressed
    window.bind("<Shift_L>", bossKeyRelease)


# Set dimensions of a window
def setWindowDimensions(w, h):
    window = Tk()
    window.title("Space Traveller")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # Put 1280 x 720 game screen at the middle of computer screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window

# Define empty star array
star = []

# Define deafult game options
currentScore = 0
speed = 25

# Define variables used for checking if some functions must be executed or not
metObstacle = 0
doPauseGame = 0
doSave = 0
paused = 0
alreadyBossKey = 0

# Read settings from settings.txt
settings = []
file = open("settings.txt", "r")
for line in file:
    for word in line.split():
        settings.append(word)
opt1 = bool(int(settings[0]))
opt2 = bool(int(settings[1]))
opt2_1 = bool(int(settings[2]))
opt2_2 = bool(int(settings[3]))
file.close()

# Set window dimensions
wwidth = 1280
wheight = 720
window = setWindowDimensions(wwidth, wheight)

# Define images used in game
rocketImage = PhotoImage(file="rocket.png")
pause = PhotoImage(file="pause.png")
tick = PhotoImage(file="tick.png")
notick = PhotoImage(file="none.png")
excel = PhotoImage(file="excel.png")

# Create canva
canva = Canvas(window, bg="black", width=wwidth, height=wheight)

# Set main menu when entering game
setMainMenu()

# Call bossKey when Shift Left pressed
window.bind("<Shift_L>", bossKey)

# Do main loop
window.mainloop()
