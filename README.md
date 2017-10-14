# ES 96 Software Engineering for Outpatient Wearable
# Team: Mikhail Grushko, Olga Romanova, Shelby Yuan & Ethan Wong

## Instructions for Using this Repository

1. This is an open source project, so anyone can see the source code of the project. Feel free to browse or download the files in this repo. In order to get contributor priviliges, please talk to one of the team members.
    If you want to copy this repository to your machine, execute execute the following command inside the folder (where you want to store your repository) in your terminal: 

        git clone https://github.com/grushkom/es96wearable.git
    
    You should be all set to start contributing!

2. Before starting work, execute the following command inside the es96wearable folder in your terminal:

         git pull

    This will make the repository on your computer up-to-date.

3. To work on any of the files, use any sort of text editor or IDE you might 
prefer. I suggest using Sublime Text 3, available to download for free [here](https://www.sublimetext.com/3). 

    Some of the code here is developed through specialized development environments: please see next sections for more details.

4. In order to save progress into your **local** (on your machine) git repo, execute the following command inside the es96wearable folder in your terminal: 

         git commit -am "THE COMMIT'S NAME GOES HERE"

    please make sure commit messages are informative, so that is easier to track the versions.
    In order to update the repository stored online with your new updates, execute: 
    
         git push
         
## Instructions for Setting Up the Software
### Anaconda

[Anaconda](https://www.anaconda.com) is the software that provides a variety of tools for work with Python 3. The installation process is really straightforward: just click the download button [here](https://www.anaconda.com/download/#macos). **Please Make Sure You Download The 3.6 Version**. 

To make sure you have the correct version (3.6) of python on your machine, run in your terminal:

        python -V
        
It should yield something like the following:

        Python 3.6.X :: Anaconda 4.4.0 (x86_64)
        
Where X is whatever the current version of Python 3.6 is. At this point you're all set with Anaconda!

### Arduino

For programming the wearable's hardware, we're using the [Arduino](https://www.arduino.cc) software. It lets you program hardware directly using the C language. To install Arduino software, [follow this link](https://www.arduino.cc/en/Main/Software).

### DB Browser for SQLite

[DB Browser for SQLite](http://sqlitebrowser.org) is used for this project for database visualization. In order to install it on your machine, simply download it [here](http://sqlitebrowser.org)

### HTML/CSS/Javascript Editors

There are many web development platoforms, all of which are fine to use. My suggestion would be the [Brackets](http://brackets.io), which is free, elegant, and easy to use.

For a more comprehensive and professional web development experience, I recommend [Adobe Dreamweaver](http://www.adobe.com/products/dreamweaver.html). It is a paid application; however, it is worth it if you're looking for extra web development tools.

### SQLite 3

[SQLite 3](http://sqlite.org/index.html) is used for working with SQL databases in the project. Please follow the following instructions for its installation.

1. Go to the [SQLite Downloads page](http://sqlite.org/download.html)
2. Download the file called *sqlite-autoconf-3200100.tar*
3. Next, starting at your root directory (**~** or **/**), execute the following set of commands in your terminal:

        cd downloads
        tar -xf sqlite-autoconf-3200100.tar
        cd sqlite-autoconf-3200100
        ./configure --prefix=/usr/local
        make
        make install
    
    if second command doesn't work, try instead:
    
        tar -xf sqlite-autoconf-3200100.tar.gz
    if make install gives a permission error, run:
    
        sudo make install

4. To make sure your SQLite 3 is installed normally, run the following command in your terminal:

        sqlite3
    
    You should be able to see the following command line prompt:
    
        SQLite version 3.13.0 2016-05-18 10:57:30
        Enter ".help" for usage hints.
        Connected to a transient in-memory database.
        Use ".open FILENAME" to reopen on a persistent database.
        
5. To exit SQLite, press **control+D**. You should be all set!

## Instructions for Running code

Code development in progress: please check back soon! :P