# Fake-News-Identification-System

![fake news image](images/pexels-markus-winkler-4072688.jpg)

### Business Case

Fake News has been on the rise this past decade.

The spread of fake news has been having clear negative effects. From denying the results of the 2020 presidential election to spreading misinformation about the COVID vaccine, fake news is causing real damage to our society.

One of the main sources of fake news is social media, such as Facebook and Twitter.

I set out to produce a fake news identification system that can be used by social media companies to filter out minsinformation.

### The Repo

All of the data cleaning, exploratory analysis and modeling can be found in the 'Capstone-Final-Version' notebook. Each section of the notebook is labelled.

### The Data

For this project, I used the 'Fake and Real News Dataset' from Kaggle.

The dataset contained 21,417 real articles from Reuters and 23,481 fake articles from various sources.

These articles spanned a period of time from January 2017 to december 2017

### Data Cleaning

The model is only looking at the text of the articles, not the titles, subject or date.

The only cleaning step required was to remove the names of the news outlet and city of origin from the real articles.

No cleaning was required with the fake articles.

### Data Preparation

I used SpaCy to tokenize the text of the articles and remove stop words, upper case letters and punctuation as well as to lemmatize the words in the articles.

### Exploratory Data Analysis

In addition to SpaCy, I used NLTK to perform my exploratory data analysis.

I used word clouds and frequency distribution tables to analyze the text from the real and fake articles.

Real Articles
![real news wordcloud](images/true_wordcloud.png)

Fake Articles
![fake news wordcloud](images/fake_wordcloud.png)

The frequency distribution tables looked at unigrams, bi-grams and tri-grams.

Real Article Unigrams
![real article unigrams](images/true_unigram.png)

Real Article Bigrams
![real article bigrams](images/true_bigram.png)

Real Article Trigrams
![real article trigrams](images/true_trigram.png)

Fake Article Unigrams
![fake article unigrams](images/fake_unigram.png)

Fake Article Bigrams
![fake article bigrams](images/fake_bigram.png)

Fake Article Trigrams
![fake article trigrams](images/fake_trigram.png)

Former President trump was at the top of the list int he frequency distribution tables for both the real and fake articles.

However, the real articles tended to have more of a focus on international events, international leaders and US government officials, while the fake articles had more of a focus on domestic events and individuals such as Hillary Clinton, former President Barack Obama as well as right wing talking points such as the New York Times, fake news and Black Lives Matters.

### Modeling

I used Logistic Regression, Multinomial Naive Bayes, a Random Forest Classifier and a Voting Classifier. 

For Logistic Regression and Multinomial Naive Bayes, I used both simple pipelines and pipelines combined with gridsearch to generate the best results.

I achieved my best results with Logistic Regression combined with Gridsearch. This model had very low variance but the bias appears to be high, indicating that perhaps the model needs to be trained on a wider variety of articles, spanning a longer period of time.

![pinochio fake news boy](images/ey-boy-holding-newspaper.jpg)