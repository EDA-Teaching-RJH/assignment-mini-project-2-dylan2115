overview 
my project is a simple log file analyser that I wrote in python, this was done for my mini project. the goal of the project was to show my understanding and development of the topics from workshop 7 to 11, for example regex, testing, file handling, oop and using libraries 
the core of the program is that it read from a sample server log and extracts the important info and print the info in to a summery 

what the project does 
when the project is run it loads a log file, then it counts the requests from each URL and how many times each Ip the requests came from. then it identifies each error entry and how many errors of each type that occurs .and prints the whole thing into a summery that can be seen by the user 

how this project meets the assignment requirements 
regular expressions I used pythons re module to pull the info out of each log line which I used regex to extract it does this for the Ip, URLs status codes and error entries.

testing 
I used pytest to write a set of tests, the tests I used are loading log entries, counting by Ip, counting URL, getting error entries, and counting error codes 

libraries
the libraries in the project are pythons built-in re also its built in datetime, a custom utils.py and a proper package structure log_analyzer_project

file I/o
the analyser ready from a .log file and stores it in a logs/ folder. it can process the file line by line and use the data for the analyses 

object-orientated programming 
the project includes two classes 
loganalyzer and errorloganlyzer

for the above and beyond section
I made a run.py file for a fast and simple start for the program I also formatted the summery and added a date and time for when the analyser starts and a realistic sample log 

comments 
I added comments to the code to try and help explain the code

this is the structure for my folders and files for this project 
log_analyzer_project/
│
├── analyzer.py
├── utils.py
├── main.py
│
├── logs/
│   └── sample.log
│
├── tests/
│   └── test_analyzer.py
│
run.py
README.md
coversheet.md

how to run the project 
in the terminal write pythone3 run.py 
for the test 
in the terminal write pytest

what I struggled with the hardest part for this project was to get python to be able to find my files, import errors where the biggest setback I found this was due to folder names and case sensitivity and ghost files, regex was also a case of trial and error after a bit of research and the trial and error I managed to debug my code. also, I had issues with my memory of the correct wording and phrasing to python to work almost as difficult as trying to learn a new language 

final notes 
this project should demonstrate everything required for the project and the extra features added to make it feel more complete


