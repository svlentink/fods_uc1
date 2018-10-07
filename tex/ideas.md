
## raw snipets for paper

This paper show a first presentation of the provided data set.
Based on these findings,
further questions can be formulated.
The provided approach allows one to easily change
the variables to retrieve other outcomes.


## Characteristics

Volume
multivariate
atomic (no, very high overview with country_code)
cleaned, current values: see code
clear, understandable labels
segmented: location based on country
known pedigree: twitter datadump provided by UvA

## my steps

lecture3 stages of maturity
+ step01 aquire: data aggregation (bulk splitting)
+ step02 prepare: reduce set, to db
+ step03 analyze

## report todos
FDS_Report_Guidelines.pdf

Only real restriction – must try both sentiment and topic analysis

lecture3
sacha2014 data model based on visualization
[Sacha2014] D. Sacha, A. Stoffel, F. Stoffel, B. C. Kwon, G. Ellis
and D. A. Keim Knowledge Generation Model for Visual Analytics.
IEEE TVCG 2014

lecture6
supervised:
+ qualitative (classification) IMPORTANT! algorithm model
+ quantitative (regression)

Naïve Bayes classifiers

### questions afterward:
+ What problem are we trying to solve? Articulate the answer as a
sentence, especially when communicating with the end user. Make sure
that it sounds like an answer. For example, “Given a fixed amount of
human capital, deploying people with these priorities will generate the
best return on their time.”
+ Does the approach make sense? Write out your analytic plan.
Embrace the discipline of writing, as I brings structure to your thinking.
Back of the envelop calculations are an existence proof of your
approach. Without this kind of preparation, computers are power tools
that can produce lots of bad answers really fast.
+ Does the answer make sense? Can you explain the answer?
Computers, unlike children, do what they are told. Make sure you spoke
to it clearly by validating that the instructions you provided are the ones
you intended. Document your assumption and make sure they have not
introduced bias in your work.
+ Is it a finding or a mistake? Be skeptical of surprise findings.
Experience says that it if seems wrong, it probably is wrong. Before
you accept that conclusion, however, make sure you understand
and can clearly explain why it is wrong.
+ Does the analysis address the original intent? Make sure that
you are not aligning the answer with the expectations of the client.
Always speak the truth, but remember that answers of “your baby
is ugly” require more, not less, analysis.
+ Is the story complete? The goal of your analysis is to tell an
actionable story. You cannot rely on the audience to stitch the
pieces together. Identify potential holes in your story and fill them to
avoid surprises. Grammar, spelling and graphics matter your
audience will lose confidence in your analysis if your results look
sloppy.
+ Where would we head next? No analysis is ever finished, you just
run out of resources. Understand and explain what additional
measures could be taken if more resources are found.


lecture2 forms of insight


### motivation unsupervised
economics (lack of time), less human interaction

## TODO
### lecture5
+ regex on data
+ twitterdata visualization (plotting)
+ to pandas
+ tokenize

### lec6
#### classification
first get list of words,
sort by occurence

nltk training data

#### clustering
Unsupervised learning: Topic analysis