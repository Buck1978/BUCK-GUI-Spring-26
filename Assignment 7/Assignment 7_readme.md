Assignment 7 - Measurement Converter GUI

Student: Richard Buckholz

Development Tools/Versions
    - Python: 3.12.8
    - PySide6: 
    - IDE: Visual Studio Code

How to Run
    1.	Ensure Python 3 and PySide6 are installed
    2.	Place all project files, including the image, in the same directory.
    3.	Run the application.
    4.	The GUI window will open.
        a.	Enter a numeric value (Letters, blanks, and negative numbers will not  work)
        b.	Select a conversion direction (inches to meters or meters to inches)
        c.	Click Convert

Issues Encountered
    I was having an issue showing the image on the GUI. I learned how to create an absolute path to the image because of this issue. Turns out that PySide6 doesn’t like ‘ in the directory name.