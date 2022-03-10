import keyboard
import functions


# example script to loop the afk macro

print("press space... and switch back into game\n")

if keyboard.read_key() == "space":

    loop_counter = 0

    while True:

        loop_counter = loop_counter + 1
        print("loop counter: ", loop_counter,"\n")

        functions.simple_afk_script()



else:
    print("wrong key...")
