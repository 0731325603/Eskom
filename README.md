## Group5_Analyse_Predict
![Heading](https://www.afriforum.co.za/wp-content/uploads/2019/12/Eskom.jpg)

# Python library containing seven functions that will be used to analyse ESKOM data:

* <b> Dictionary_of_metrics </b> <br/>
Returns a dictionary with keys 'mean', 'median', 'std', 'var', 'min', and 'max', corresponding to the mean, median, standard deviation, variance, minimum and maximum of the input list, respectively. <br/>
The standard deviation and variance values are unbiased. <br/>
All values are rounded to 2 decimal places.

* <b> Five_num_summary </b> <br/>
Takes in a list of integers and returns a dictionary of the five number summary. <br/>
All values are rounded to 2 decimal places. 

* <b> Date_parser </b> <br/>
Takes a list of datetime strings as an input, the string contains the date in 'yyyy-mm-dd' format, as well as the time in hh:mm:ss formamt and returns only the date in 'yyyy-mm-dd' format.

* <b> Extract_municipality_hashtags </b> <br/>
Takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet.

* <b> Number_of_tweets_per_day </b> <br/>
 Calculates the number of tweets that were posted per day.

* <b> Word_splitter </b> <br/>
Splits the sentences in a dataframe's column into a list of the separate words. The created lists are placed in a column named 'Split Tweets' in the original dataframe

* <b> Stop_words_remover </b> <br/>
Removes english stop words from a tweet.

## How to install this package
To remotely installation from github:<br/>
```pip install --upgrade git+https://github.com/IvenoCarolus/Group5_Analyse_Predict.git```<br/><br/>
To perform a local Installation after cloning or downloading package run this following command (Please make sure you direct yourself into /dist):<br/>
```pip install predicttools-0.1.tar```
## Links to data used 
<b> EBP data: </b> 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv' <br/>

<b>Twitter data: </b> 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'

## List of contributors:
* Iveno Carolus
* Nicole Meinie
* Mandla Hadebe
* Noah KaeKae

<b> If you would like to contribute to our repository contact bubblesortguru@gmail.com </b>

