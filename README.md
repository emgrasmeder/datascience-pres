# datascience-pres
An Introduction to Data Science Tools with Python

### Table of Contents:
1. [Packages to install](https://github.com/emmagras/datascience-pres/tree/master#packages-to-install)
2. [Books to read](https://github.com/emmagras/datascience-pres/blob/master/README.md#things-to-read)
1. [Pandas](https://github.com/emmagras/datascience-pres/tree/master#pandas): Your gateway to an Excel-free life
1. [NLTK](https://github.com/emmagras/datascience-pres/tree/master#nltk): Natural language processing
1. [Sci-Kit Learn](https://github.com/emmagras/datascience-pres/tree/master#sklearn): Machine learning, classification
2. [IPython Notebook](ipython-notebook): Visuals and code sharing made easy
1. [Matplotlib](https://github.com/emmagras/datascience-pres/tree/master#matplotlib): Data visualizations

## Packages to install
### Links to websites explaining how to download
- [Anaconda](http://continuum.io/downloads#py34)
- [NLTK](http://www.nltk.org/install.html)
  - [also see: NLTK extras](https://github.com/emmagras/datascience-pres/blob/master/README.md#nltk-extras)

You can also skip the `Anaconda` install and install these packages separately:
(please raise an issue or submit a pull request here if you found dependencies you needed to install in addition to these)
- `pip install sklearn`
- `pip install pandas`
- `pip install "ipython[notebook]"`
- `pip install matplotlib`
- `pip install numpy`

## Things to read 
-  [Natural Language Processing with Python](http://www.nltk.org/book/ch01.html)
-  [This Pandas tutorial](http://pandas.pydata.org/pandas-docs/stable/10min.html)
-  [Beautiful Visualizations - pdf download](http://deca.cuc.edu.cn/Community/cfs-filesystemfile.ashx/__key/CommunityServer.Components.PostAttachments/00.00.00.11.38/Beautiful.Visualization.pdf)

## Pandas
### Your gateway to an Excel-free life

[Pandas](http://pandas.pydata.org/) is a robust Data Science package with a powerful data structure known as a DataFrame. Pandas documentation is excellent and provides a thorough variety of tutorials and examples. I recommend their [10 Minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html) tutorial.

## NLTK
### Powerful Natural Language Processing with Python

I strongly recommend using the Natural Language ToolKit during your introductory steps into Natural Language Processing. The Toolkit has an [enjoyable to read book](http://www.nltk.org/book/) which simultaneously teaching natural language processing and the Python language with tangible, nontrivial examples in both regards. 
The NLTK creators have also added a [list of resources to wiki](https://github.com/nltk/nltk/wiki), including a *project ideas* page. 
####  NLTK Extras

The Natural Language Toolkit comes with a lot of features built into it, and still many others that you're probably never going to use (for example, a multitude of languages, or a series of tagged texts including parts of the Torah, Jane Austen's Emma, and an online chatroom in the 90s. Many of these packages have uses, for example training classifiers for a given topic, but they need to be downloaded using the [NLTK Downloader, which you can use through the command line while in interactive python mode.](http://www.nltk.org/data.html)

## Sklearn
### Machine learning with Python

The Sklearn package is exciting and deep. You can use it for almost any machine learning tasks you might be interested in. If you don't know what you're interested in, check out this [chart](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) to maybe get an idea of the possibilities and learn what vocabulary you might need to learn before/while moving forward. The [Sklearn Documentation](http://scikit-learn.org/stable/user_guide.html) requires and bestows a deep level of statistical knowledge. I usually mention Naive Bayes classification when talking Intro to Data Science. Did you catch it? Do you know what it is? If you haven't heard of it before, go read the [Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html) docs and get your Google engines warmed up, you're about to research a lot of new vocabulary. I've lost count of the number of times I've read the documentation for certain algorithms. I always learn something new, and can always put that to use in my work. As you decide on what you want to accomplish, you will then search through what Sklearn has to offer until you find the right set of tools to use. 

## IPython Notebook
### Sharing code and visualizing data elegantly

The easiest way to get started with Data Science is to [download this Anaconda distribution.](http://continuum.io/downloads#py34). In doing so, you will get the most popular science packages, including IPython Notebook. Alternatively, you can install IPython on your own, following [these simple directions](http://ipython.org/install.html). IPython allows you to share your code more easily, and has become a popular way for hard-copy authors of coding books to share their code snippets as supplementat material for their books. 

## Matplotlib
### Data Visualizations!

Visualizations are memorable, shareable, and, when done right, make data more understandable. Most PytData folks recommend using Matplotlib in conjunction with IPython Notebook to create your graphs on the fly. [Matplotlib's website](http://matplotlib.org/) also has a ton of [examples](http://matplotlib.org/examples/index.html) for anything you want to plot. 

As you practice making visualizations with Matplotlib, I recommend you pair your efforts with [Beautiful Visualization](http://deca.cuc.edu.cn/Community/cfs-filesystemfile.ashx/__key/CommunityServer.Components.PostAttachments/00.00.00.11.38/Beautiful.Visualization.pdf), which will teach you things about the ethics, philosophy, and efficacy of various visualization types. Did you know that humans over estimate how much larger a circle needs to be to double in volume? If your visualization compares population sizes using circle size, you will probably downplay the difference in size because of how humans reason spatially. 
