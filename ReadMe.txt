Dataset
--------------------------
 The dataset has dimensions 1000 x 4
 The dataset contains information about 6 different cow breeds along with their milk yeild ,skin color and calving period.
 Can be used for Classification and recommendation systems.

 Languages to be cleaned:
	Kanada       ಕನ್ನಡ್'
	Arabic       عرب    
	Bengali      বাংলা
	Tamil        தமிழ்
	Bulgarian    български

Languages remaining after cleaning:
	Hindi   हिंदी
 	English English

----------------------------------
Helper files
---------------------------------

Create_dataset.py :- Creates a dummy multilingual dataset.
		     Some places in column are randomly filled with "NA" values.
		     similary some rows in column1 are filled with other language.

Cleaner.py :- Performs Cleaning.
	      Replaces "NA" values by using classsize,frequency count and average.
	      Makes the dataset  bilingual(Hindi and english) removing rows containg multilingual info.

Views.py :- Since CSV can only save , but cannot represent the unicode chracters properly.
	    Hence a helper file to see diffetent stages of dataset cleaning.
            To use Run and enter the .csv filename

data.csv and out.csv : -To store intermediate data and show stages of cleaning.

-------------------
Result files
-------------------

out1.csv :- file cleaned and dataset converted t bilingual
outclean :- Replaced all "NA" values with above mentioned processes. 
---------------------------------------------------------------------------------------------

Software:-
--------------------------------------------------------------
Python 3.7.x
libraries :- codecs,random,pandas

---------------------------------------------------------
Project by:-

	SHIVAM
	