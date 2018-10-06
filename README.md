# Team26 Use case 1: Politic

## Description from notification
The first group project is: using this knowledge from this Thursday's and the previous werkcollege,
make an analysis on saved twitter data from the 2016 US election.
The deadline for this first project is midnight two weeks from Sunday (so 07/10/18, 23:59:59).
The details of the project are both in my next two lectures and in the notebook.

## Description

"Your assignment is to perform an analysis on a dataset of tweets provided in the course.
The analysis should contain topic modelling and sentiment analysis.
Use different splits of the data you have to perform your analysis, compare, correlate and visualize.”

### Purpose
The main purpose of this assignment is for us to see you are able to understand and use the material from Marcel's and my lectures and practicals. Some ideas for research questions to think about:
 

1. Were you able to load and parse the twitter data into a useful format for comparison with other data (e.g. state locations, demographics)? Were you able to show that you could do this clearly/visually?
2. Are you able to get insights into the data before using sentiment or topic analysis? If yes, what could you show? If not, why not? 
3. Did sentiment analyses help identify supporters of each candidate? How did sentiment correlate with other information like demographics? That is to say - where is each candidate popular, and who are they popular with?  Were you able to show this information clearly/visually? If you could not use sentiment analysis, why not? 
4. Were you able to combine sentiment knowledge with a topic analysis?  That is, were you able to show what supporters who were positive/negative towards each candidate talked about? Could you show this clearly/visually? If you could not use topic analysis, why not? 
5. Could you relate your results to the actual state-voting patterns in the election? What are you able to show, and how confident are you in your findings?

Please take these as loose guidelines, not a check list. If you find you can write interesting material about only a couple of these points, or something else entirely that takes your interest in the data, then great, please write about that instead. We ask that you at least try to use both sentiment and topic analyses, but if you can't use one and can explain why it is not useful for your analysis then this is also okay.

## Dataset metadata
Tweets were collected via Twitter's Streaming API in the period 12.08-12.09, 2016. The monitored hashtags and accounts were:
 

'@HillaryClinton', '#maga', '#trumppence16', '#hillaryclinton', '#hillary', '#crookedhillary', '#donaldtrump', '#dumptrump', '@realDonaldTrump', '#nevertrump', '#imwithher', '#neverhillary', '#trump'
 

Total number of tweets in the original dataset was: 26,687,737 . After selecting only those tweets with a geolocation, the number was reduced to: 657.307


## Initial priority
Based on the 'fail fast' philosophy of Google.

We do everything on 10% of the data,
only run final analyses on total dataset.
+ Parse data
+ Mongo connection
+ Initial insights
+ Go through tools mentioned in labs, apply
+ sentiment/topic analyses


## Links
+ [Team26](https://canvas.uva.nl/groups/12408)
+ [Assignment](https://canvas.uva.nl/courses/2046/assignments/24966)

