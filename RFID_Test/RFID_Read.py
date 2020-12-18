#!/usr/bin/env python

import RPi.GPIO as GPIO
import MFRC522
import signal
import Msg_Publisher

card1 = ("34,103,107,52")
card2 = "233,16,216,86"
card3 = "217,83,102,194"
card4 = "57,154,26,43"

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
    
    
# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

#string rfidcard 
while continue_reading:
	# Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID
        rfidcard = "%s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
        #print "%s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
        print (rfidcard)
    if rfidcard == card1:
    	print ("i love you")	
    	Msg_Publisher.A1
    elif rfidcard == card2:
    	print ("i hate you")
    	Msg_Publisher.E4
    elif rfidcard == card3:
    	print ("i like you")
    	Msg_Publisher.C1
    elif rfidcard == card4:
    	print ("i kill you")
    	Msg_Publisher.B3    		    		
    else:
    	print ("this is new")
    	  
     
    
        
        
        
        
 
