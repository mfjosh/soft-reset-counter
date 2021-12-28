# soft-reset-counter
I am creating this script as a test of how much I can learn in Python. So far, I have made a working counter in console and in GUI. I am tweaking the GUI and functions constantly.

So far, the counter-gui.py is the actively updated script. I have cleaned up the GUI as far as I can with the limited knowledge I have in Python / Ktinker but this will be ever evolving.

1. when launching the program, a validation checker is ran that searches for counter.txt in the directory of the python script. If one is not found, one is generated with the value of 0. This is how we keep track of the counter, I prefer this method as you can easily utilize it as a save feature /  OBS feature to export the current count value which is updated immediately when the UI is.

2. I have not yet quite found a way to customize the hotkeys for user input so I have created default system hotkeys for adding(+) subtracting(-) and resetting counter value(*). Once I find an efficient way to record multiple keypress, I will implement this. For now, they are hard coded and will work even with the program not in focus.

3. I have added a switch to enable automation. This utilizes the reference.png file as its control and will increase the counter value while its running as long as the reference is detected on the screen. replace the reference.png with a screenshot of the game you are playing that you can rely on as a counter. (eg. Pokemon BDSP, the copyright screen only shows on game load so it is a perfect reference). You can also use the Switch home screen however the counter may increase anytime you press home prior to closing the game.
