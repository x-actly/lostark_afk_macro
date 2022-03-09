import time, pyautogui, random


def simple_afk_script():

    # ability variables for randomize the time.sleep function

    q_ability = random.uniform(0, 3)
    w_ability = random.uniform(0, 3)
    e_ability = random.uniform(0, 3)
    r_ability = random.uniform(0, 3)
    a_ability = random.uniform(0, 3)
    s_ability = random.uniform(0, 3)
    d_ability = random.uniform(0, 3)
    f_ability = random.uniform(0, 3)

    # hotkey variables for healing potion and hp percent potion

    one_battle_hotkey = random.uniform(0, 3)
    five_item_hotkey = random.uniform(0, 3)

    # input, time and print functions for a better overview

    pyautogui.press('q')
    time.sleep(q_ability)
    print("key 'q' float in seconds", q_ability)

    pyautogui.press('w')
    time.sleep(w_ability)
    print("key 'w' float in seconds", w_ability)

    pyautogui.press('e')
    time.sleep(e_ability)
    print("key 'q' float in seconds", e_ability)

    pyautogui.press('r')
    time.sleep(r_ability)
    print("key 'r' float in seconds", r_ability)

    pyautogui.press('a')
    time.sleep(a_ability)
    print("key 'a' float in seconds", a_ability)

    pyautogui.press('s')
    time.sleep(s_ability)
    print("key 's' float in seconds", s_ability)

    pyautogui.press('d')
    time.sleep(d_ability)
    print("key 'd' float in seconds", d_ability)

    pyautogui.press('f')
    time.sleep(f_ability)
    print("key 'f' float in seconds", f_ability)

    pyautogui.press('1')
    time.sleep(one_battle_hotkey)
    print("key '1' float in seconds", one_battle_hotkey)

    pyautogui.press('5')
    time.sleep(five_item_hotkey)
    print("key '5' float in seconds", five_item_hotkey)
    
    print("\n")

    return