"""Bitmap Message, by Al Swigart and reproduced by Will Morgan
Displays a text message according to the provided bitmap image.
This code is avilable at Al's website
Tags: tiny, beginner, artistic"""

import sys

#  (!) Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from 
# https://inventwithpython.com/bitmapworld.txt)
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Message, by Al Sweigart and reproduced by Will Morgan.')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since theres a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print() # print a new line

# Exploring the program
# What happens if the player enters a blank string for the message?
    # the program exits.

# Does it matter what the nonspace characters are in the bitmap variable’s string?
    # No. The program only looks for ' '. Any other character will
    # be replaced with one from the message variable. 

# What does the i variable created on line 45 represent?
    # Each character (or ' ') in the bitmap variable. 

# What bug happens if you delete or comment out print() on line 52?
    # It prints everything on one line. 