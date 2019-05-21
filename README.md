#Description:

This code notifies the user (via gmail) if there is a change in the number of seats on One.uf for course registration. The current code is designed to search for the inputed course during Fall 2019 (see notes below on how to edit) however, it is not course section specific. 
Inspiration largely from (https://github.com/Rolstenhouse/uf_api) UF's unofficial API.

# Environment settings:

1) Use https://chromedriver.storage.googleapis.com/index.html?path=2.35/ to get the most recent chromedriver, add it to your path AND to the same directory as the program files
2) Turn on access to less secure apps https://myaccount.google.com/lesssecureapps
3) pip install (Python 3.7)
	a. `pip install selenium `
	b. `pip install tkinter`


#Notes: 

1) I tried to compile this into an exe using py2exe but was unsuccessful, sorry.
2) Changing semester search: 
	Within checkSeat.py line 53 and 60 contain the values "2198" that correspond with 2019 Fall semester.
	The first 3 digits indicate the year, with the 0 removed, and the last digits indicates the semester.
	
	Last digits key:

	Spring: 1
	Summer: 5
	Fall: 8	

	Examples: 

	Fall 2019 (from https://github.com/Rolstenhouse/uf_api)
	2198 = Year (with 0 removed) + Semester number + optional Summer Semester (A,B,C)

	Spring 2019 : 2191 
	Summer 2019 : 2195 
	Summer A 2018 : 2195A 
	Fall 2018 : 2198

	To find courses for semester A, append A. The same holds for semester B and C
3) Refresh Rate:
	Refresh rate set to 10 seconds on line 80 of checkSeat.py, change if necessary
4) Incorrect Gmail Information
	If gmail information is incorrect, you will not be notified. This edge case is not tested for at the moment so enter your information corrrectly.




