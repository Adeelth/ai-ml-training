
## Projects
### [Data Reader](DataReader/main.py)

Datareader is class the can read any type of file and proceess it based of pre decided rules
- The dataset first downloaded using `requests` and then unziped using `Zipfile` packages
- To read extremely large files and not run itn "out of memory erros" we uitlise the `yield` keyword 
- For each type of file .txt, .json or .csv there is a seperate class catering to each type and a `Factory Method` is used decide which class to call upon reading a file
- As a data set folder can have many files processing them one by one may take a alot of time to counter this mulitprocessing is used to process each file in parallel, the `multiprocessing` package is able over python's GIL lock by creating subprocesses 



## Scripts

### [Yield Key Word demo](yeild_demo.py)

Created a weather man demo to demonstrate the use of a the yeild keyword, the yeild key word is able to create a generator that can generate over a 1 million rows without using any memory and and acting as a continuous stream of data

### [Python Peepholing](peepholing.ipynb)

### [Linear Regression](regression.ipynb)


