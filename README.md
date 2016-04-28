/** 
* Name: Kai Huang
* Course Name: Natural Language Processing
* CS6320, Final Project
* Due Date: Wed, April 27th, 2016 16:30:00 PM CDT 
* NetID   : kxh132430
*/

I. Purpose

Design and implement an unsupervised web page clustering system backed-up by two unsupervised clustering algorithm, K-mean and Ward algorithms. In this system, web pages were crawled from www.dmoz.org directory in six categories (business, entertainment, health, politics, sports and technology), then processed by the web page clustering system. Finally, the clustering result can be viewed in a web browser.

II. File List
The submission contains two files:

kxh132430_final_project.zip --- A zip file containing the source code and data files for the program.

README.txt --- A description of the file in the unzipped folders.

After you unzip the kxh132430_hw4.zip file, you will see three directories:
   -- src/                     The source code for the clustering system.
      --- cluster              
                               The driver python script for the program.
      --- document_clustering  
                               A python package that implements K-means and Ward clustering algorithm.
      --- setup.py             
                               The setup scripts to build and install the document_clustering package.
      --- requirement.txt      
                               The dependencies that you need to install for the document_clustering package.
   
   -- input/                   Web documents in six topics in json format.
      --- business.json
      --- entertainment.json
      --- health.json
      --- politics.json
      --- sports.json
      --- technology.json

   -- output/                  The default output directory of the program.
      --- kmeans.html 
                               A sample html page of the clustering result by the kmeans algorithm.
      --- kmeans.png 
                               A sample png file of the clustering result by the kmeans algorithm.  
      --- ward.html 
                               A sample png file of the clustering result by the ward algorithm.    


III. How to Run the Program

Prerequisites:
To run the program, you need Python 2.7.x installed on your PC. 

1. Before running the program, you will need to install a number of python packages in your system. Go to the src/ folder, you will find a dependency file named requirements.txt, type in the following command in the console:
    $ pip install -r requirement.txt

The pip tool will automatically install all the dependencies for you.

2. Download the nltk corpus, which contains the stopwords list.
Type  in "python " to enter Python Interpreter interactive mode. In this mode, type in:
>>> import nltk
>>> nltk.download()

nltk will automatically download the corpus data(stopwords) and install on your system.

3. Build and install the python package to your system.
Go to the src/ folder, you will find a setup.py script under this folder. Type in the following commands:

    $ python setup.py build install

The built-in setuputils of python will automatically install the package to your system.


How to Run:
Go to the root directory of the project where you can find the input/ and output/ folders under it, open a terminal here and type in:

    $ cluster -h

The program will automatically print the help message of how to cluster the web documents from each topics. If you see the help message below, then that means you've successfully installed the document_clustering package to your system!

usage: cluster [-h] [-t TOPICS [TOPICS ...]] [-a {kmm,hac}] [-s SIZE]
               [-i INPUT] [-o OUTPUT] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -t TOPICS [TOPICS ...], --topics TOPICS [TOPICS ...]
                        topics of the news
  -a {kmm,hac}, --algorithm {kmm,hac}
                        the document clustering algorithm
  -s SIZE, --size SIZE  the size of the sample from each topic [1-100]
  -i INPUT, --input INPUT
                        default input folder
  -o OUTPUT, --output OUTPUT
                        default output folder
  -v, --verbose         verbose mode

Here I will provide some examples:

(a) Take 5 documents each from the topics "business" and "entertainment", cluster the 10 documents by K-means algorithm and plot the clusters:

    $ cluster -s 5 -a kmm -t business entertainment

(b) Take 5 documents each from all 6 topics, cluster the 30 documents by K-means algorithm, print the 6 most frequent words in each cluster(verbose mode), and plot the clusters:

    $ cluster -s 5 -v

    You don't need to provide -a argument here, since the program by default will choose K-means as the underlying clustering algorithm.

    You don't need to provide -t argument here, since the program by default will select all 6 topics (business, entertainment, health, politics, sports and technology).

(c) Take 5 documents each from the topics "business" and "entertainment", cluster the 10 documents by Ward algorithm and plot the clusters:

    $ cluster -s 5 -a hac -t business entertainment

    If you want to use ward algorithm to cluster the documents, you will have to explicitly specify "hac" as the clustering algorithm. 

(d) Take 5 documents each from all 6 topics, cluster the 30 documents by K-means algorithm and plot the clusters:
    $ cluster -s 5

    You don't need to provide -t argument here, since the program by default will select all 6 topics (business, entertainment, health, politics, sports and technology).





 
