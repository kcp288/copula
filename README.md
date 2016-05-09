# AAE final project
### Copula presence/absence counter
African American English (Spring 2016), Professor Renée Blake

Implemented in python using the nltk library

Hosted as a Flask app on heroku at https://copula-calculator.herokuapp.com

### Background
Copula absence is a grammatical feature of African American English, denoted by absence of 'is' or 'are'. This feature is systematic and rule-governed: some copula forms can not be left out, and the absences that do occur are distributed in frequencies that are context-dependent.

### Copula deletion features

**Absence**
- Forms 'are' and 'is' ("We (are) inside.")
  - Absence of 'are' is more common than 'is'
- Absence can occur after
  - Pronoun ("he", "she", "they", "we")
  - Noun ("Daniel", "people")
  - Absence after Pronoun is more common than after Noun
- Absence can occur before
  - **Most common absence** occurs before present progressive of 'to go': 'gonna', 'going to', 'gon' ("She (is) gonna be here soon.")
  - Adjective ("People (are) crazy.")
  - Noun ("She (is) a writer.")
  - Gerund: verb ending in -ing ("He (is) walking.")
  - Locative: any preposition ("They (are) in the store.")
  - Frequency is as follows (most to least likely): 'Gonna' > verb + ing > Adjective/Locative > Noun


**Obligatory Presence**
- First person singular 'am' ("I _am_ walking.")
- Past tense 'was' and 'were' ("She _was_ inside.")
- Sentence-final ("I know that she _is_.")
- Emphasized ("He _IS_ a teacher.")
- Contracted 's ("She_'s_ happy.")
- Contracted form ain't ("He _ain't_ allowed.")
- Infinitive be ("She can _be_ a famous.")


Based on *Rickford & Rickford, Chapter 7 (2000)*.

### Local installation
- Install xcode (development tools from Apple) and download Python from https://www.python.org/downloads/
- Open Terminal app
- Click "Download ZIP" in this repo
- Use `cd` (to change directory) and `ls` (list contents of directory) to navigate into the "Copula" download Directory
- Run the following commands in the Terminal
```
$ sudo easy_install pip
$ sudo pip install -r requirements.txt
```
- This means you've installed the requirements, and you should be ready to go! Type `python hello.py` in the terminal. You should see this
```
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
- Now, go to your browser and type 'http://0.0.0.0:5000/' into the navigation bar. You should see the Copula Calculator!

### Show me!

![Screenshot](/images/1.png?raw=true "Screenshot")
<img src="/images/2.png?raw=true" width="518">
<img src="/images/3.png?raw=true" width="518">
<img src="/images/4.png?raw=true" width="518">
