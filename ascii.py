import random
import os
i = random.randrange(9) + 1 
website="https://raw.githubusercontent.com/rakeshappycodes/ubuntu-terminal-splash/master/art"+ str(i) + ".txt"
os.system("curl " +  website)