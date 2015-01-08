import time
name = raw_input ("What is your name?")
print ("Hello, %s.") % name
age = raw_input ("What is your age?")
print ("Let's do this!")
print ("Hello, %s.") % (name)
print ("Today we are going to play Truth or Dare. If you choose truth type in 't' if you choose dare, type in 'd'.")
truth_or_dare = raw_input ("What do you choose?")
while True:
    if truth_or_dare == "t":
        print ("Tell me a secret of yours.")
        truth = raw_input ("What is your secret?")
        print ("Thank you, this is being posted on Facebook right now.")
        time.sleep(2)
        break
    elif truth_or_dare == "d":
        print ("I dare you to kill yourself")
        print ("Goodbye")
        time.sleep(2)
        break
    else:
        print ("Since you didn't choose truth or dare, this game has finished.")
        break
