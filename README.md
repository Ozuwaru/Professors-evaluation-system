<img alt="Static Badge" src="https://img.shields.io/badge/Powered_by-MySQL-blue" style="display:inline-block;"> <img alt="Static Badge" src="https://img.shields.io/badge/written_in-Python-orange" style="display:inline-block;">
# Professors-evaluation-system

## Description
Hi there! This is a Desktop application writen in **Python** that allows the directors or higher ups in an institution to see the performance of all teachers based on the info given by the students that are on those teachers classes. This project allows the user to send surveys to the students automatically via email, change the questions of the survey automatically and get the info answered from the students all via Google Cloud Services.
<br>
This app was made by Victor Rojas, Frank Diaz and myself Oswald Torrealba, i was in charge of the database management, creation, **google cloud services api**, a script that automatically creates google form surveys based on the database,etc.

## Instructions
<ol>
  <li>
    Since this a early version, to run the project you'll need the python modules witch are the following:
    
      'pip install mysql-connector'
      'pip install pyqt6'
  </li>
  <li>
        At this point you'll need to connect to your MySQL connection, so change the 'env.py' file and update to your             username and password:
    
      dbuser =  YourUsername
      dbpassword  = YourPassword
  </li>
  <li>
    Once you have installed all of the modules required, you'll need to start the database, so in the file 'BD.py' run the        following funtions:
    
        createDatabase()
        createTables()
  </li>
  <li>
    Now you should have both the database and tables, but no info inside of them, so you'll need to insert it, you can do it easily with [[this function has not been written yet]]
  </li>
</ol>
