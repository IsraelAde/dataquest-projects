# Working with Data Downloads

This folder contains files created/used for the 'Working with Data Downloads' project at [www.dataquest.io](https://www.dataquest.io/). This readme contain my solutions done on the command line.

List the contents of the current directory with the ls command, and take note of the archive file crdc201314csv.zip.

    ls -l

Extract the files in crdc201314csv.zip using the unzip command.

    unzip crdc201314csv.zip
    
Delete crdc201314csv.zip.

rm crdc201314csv.zip
•	Activate the python3 virtual environment.

source /dataquest/system/env/python3/bin/activate
•	Run pip freeze to verify that pandas is installed and available.

pip freeze
•	Edit read.py so that it will run from the command line.

nano read.py
•	Run read.py from the terminal, and verify that it worked properly.

python read.py
•	Create a new file called exploration.py that you can run from the command line.

nano exploration.py
•	Execute exploration.py.

python exploration.py
•	Execute exploration.py.

python exploration.py
•	Create a text file called findings.txt that summarizes any interesting patterns you observe.

nano findings.txt







The folder you unzipped contains two files:

CRDC2013_14.csv: the actual subset of the data we'll explore
CRDC2013_14content.csv: an explanatory file that describes each of the columns in CRDC2013_14.csv



We'll have to run our Python script using a virtual environment that has a pandas installation on it. The virtual environment we need to activate is in the /dataquest/system/env/python3 folder. 




Now that you've read in the files and found some interesting columns, you can dig in and analyze the data more. There are quite a few interesting angles you could explore:

Review expulsions (which refers to when students are kicked out of school permanently). Columns like SCH_DISCWODIS_EXPWOE_HI_M and TOT_DISCWODIS_EXPZT_F contain information on expulsions.
Explore gender and race differences in SAT scores. Columns like SCH_SATACT_HI_M contain this information.
Figure out the racial and gender breakdowns for different types of schools, such as magnet schools.
Determine how many students are in gifted and talented programs, or advanced placement classes.
Investigate how racial differences in enrollment change from preschool to high school.
Explore school bullying. The SCH_HBDISCIPLINED_DIS_HI_M column contains some of this information.
We recommend that you download these files and work on your own machine. We also recommend that you download the full data set from data.gov. If you find anything interesting while exploring the data, please let us know!
