import time, sys, random

indent = 0 # How many spaces to indent
indentIncresing = True # whether the indentation is increasing or not.

try:
        while True: # The main program loop
                        print(' ' * indent, end ='')
                        print('*********')
                        time.sleep(0.1) #Puse for 1/10 of a second

                        if indentIncresing:
                                indent = indent + 1
                              
                                if indent == 20:
                                        indentIncresing = False
                        else:
                                indent = indent - 2
                                
                                if indent == 0 :
                                        indentIncresing = True       

                       
except KeyboardInterrupt:
        sys.exit()