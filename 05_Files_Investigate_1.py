# filename: 05_Files_Investigate_1.py
"""
Activity: Investigate the Code

1.  Run this program **once**. A file named `log.txt` will be created.
    Open `log.txt` in your file explorer to see its content. It should say "First entry."

2.  Now, run this program a **second time**. Check the content of `log.txt` again.

3.  Change the mode in the `open()` function from "w" to "a".

4.  Run the program a **third time**. Check `log.txt`.

5.  Run the program a **fourth time**. Check `log.txt`.

6.  Answer the questions below in comments.

Questions:
1. What happened to the content of `log.txt` when you ran the program the second time (while in 'w' mode)?
   # the file was overwritten and first entry was replaced with "new entry./n"

2. What happened to the content of `log.txt` when you ran the program the third and fourth times (while in 'a' mode)?
   # i got 2 "new entry" outputs on the third run and 3 "new entry" outputs on the fourth run. This happens because the content was appended

3. What is the key difference between 'w' (write) mode and 'a' (append) mode?
   # The difference is that write mode truncates the file therefor erasing all the existing content. Wheres append preserves what was there and adds onto it.
"""

# Change the mode below from "w" to "a" after the second run
file = open("log.txt", "w")

file.write("New entry.\n")

file.close()

print("Wrote a new entry to log.txt")
