over view 
my project is a simple log file analyzer that i wrote in pythone, this was done for my mini project. the goal of the project was to show my understanding and development of the topics from workshop 7 to 11, for example regex, testing, filehandeling, oop and using liberies 
the core og the program is that it read from a sample server log and extracts the nersary info and print the info in to a summery 

what the project does 
when the project is run it loads a lof file,then it counts the requests from each URL and how many times each ip the requests came from. then it identifies each error entry and how many error of each type occurd.and prints the whole thing in to a summery that can be seen by the user 

how this projeect meets the assisnments requirements 
regular expressions i used pythons re module to pull the info out of each log line which i used regex to extract it does this for the ip, urls status codes and error entries.

testing 
i used pytest to write a set of tests, the tests i used arew;loading logentries, counting by ip, counting url, getting error entries, and counting error codes 

libraies
the liberies in the project are pythones builtin re also its buitin datetime, a custome utils.py and a proper package structer log_analyzer_project

file i/o
the anaylezer ready from a .log file and stores it in a logs/ folder. it can processe the file line by line and use the data for the analyzes 

object-orientated programming 
the progect includes two classes 
loganalyzer and errorloganlyzer

for the above and beyond section
i made a run.py file for a fast and simple start for the program i also formatted the summery and added adate and time for when the anlyzer starts and a relistic samplelog 

comments 
i added comments to the code to try and help explaine the code

this is the structer for my folders and files for this project 
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

what i strugled with the hardest part for this project was to get pythone to be able to find my files, import erors where the biggest setback i found this was due to folder names and case sencitivity and ghost files, regex was also a case of trial and error after a bit of research and the trial and error i maneged to debugg my code. also i had issues with my memory of the correct wording and phrasing to pythone to work alsmost as difficult as trying to learn a new languade 

final notes 
this progect should demonstrate every thing required for the project and the extra fetures added to make it feel more complete
