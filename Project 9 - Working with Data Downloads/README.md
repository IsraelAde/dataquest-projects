# Working with Data Downloads

In this project, we'll be working with an education data set in ZIP format. The data set we'll work with is the Civil Rights Data Collection. It contains information on educational achievement and opportunities in the U.S. broken down by race and school. Each row represents a school, while each column records an indicator of academic achievement.

This folder contains files created/used for the 'Working with Data Downloads' project at [www.dataquest.io](https://www.dataquest.io/). This readme contain my solutions done on the command line.


List the contents of the current directory with the ls command, and note the file crdc201314csv.zip.

    ls -l

Extract the files in crdc201314csv.zip using the unzip command.

    unzip crdc201314csv.zip
    
Delete crdc201314csv.zip using the rm command.

    rm crdc201314csv.zip
    
Activate the python3 virtual environment.

    source /dataquest/system/env/python3/bin/activate
    
Run pip freeze to verify that pandas is installed and available.

    pip freeze
    
Edit read.py so that it will run from the command line.

    nano read.py
    
    In order to run a script from the terminal, we need to add the following scaffolding to the code.
    if __name__ == "__main__":
    ## Add code here
    
Run read.py from the terminal, and verify that it worked properly.

    python read.py
    
Create a new file called enrollment.py that we can run from the command line.

    nano enrollment.py

Execute enrollment.py.

    python exploration.py

Create a new file called exploration.py that we can run from the command line.

    nano exploration.py

Execute exploration.py.

    python exploration.py

Create a text file called findings.txt that summarizes any interesting patterns observed.

    nano findings.txt
