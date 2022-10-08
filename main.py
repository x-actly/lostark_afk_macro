import keyboard, pyautogui, random, time, os


def simple_afk_script():

    ability_list = ['q','w','e','r','s','d','f']
    item_list = []

    for x in ability_list:

        break_time = random.uniform(1, 3)

        pyautogui.press(x)
        time.sleep(break_time)
        print("random time between inputs in seconds: ", break_time,"\n")

    return




print("press space... switch back into game\n")

if keyboard.read_key() == "space":

    loop_counter = 0
    time.sleep(5)

    while True:

        loop_counter = loop_counter + 1
        print("loop counter: ", loop_counter, "\n")
        simple_afk_script()

        """
        if loop_counter == 500:
            os.system("shutdown /s /t 1")
            break
        """

else:
    print("wrong key...")
