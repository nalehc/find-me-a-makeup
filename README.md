# find-me-a-makeup
Recommender to extract text features of makeup description and find a similar product based on prior reviews

## Introduction

[Temptalia](https://www.temptalia.com/) is a well-known review blog and resource for makeup enthusiasts, recieving 1 million unique visitors each month. The site has a variety of tools for visitors, one of which is the ["Dupe List"](https://www.temptalia.com/makeup-dupe-list/), which helps a user find similar products to the input. The recommendations are hand-selected by the blog author, and thus reliant on her expertise. By scraping reviews from the site, my goal was to recreate this tool in Python by parsing out relevant language from the reviews, and building a reccomender

## Recommender

I used TF-IDF vectorization from SkLearn and built a text reccomender which utilized a 
Non-negative matrix factorization technique to reccomend similar text. The input is a user generated text string, which can be copy pasted from elsewhere or typed. I do plan to build a web application to make this more user friendly at some point. The reccomender also relies on extracted descriptive words (adjectives) in the base text. With minimal modification, I'd imagine the recomender could be currated for the user's own makeup collection. 

## Additional Information Extracted

The type of product and price was extracted from the review body using a combination of regular expressions and SVM modeling. This enabled the recommender to fetch a result of the desired type and price range. 

## Tableau Dash

An overall view of the review information can be seen via a Tableau dashboard I've built [here](https://public.tableau.com/profile/chelan.patton#!/vizhome/MakeupData/Dashboard1). This fulfills a similar functionality to another tool on the blog, which lets the user browse products by texture, color, or score.

A demo for the dashboard can be seen below:

[link](https://drive.google.com/file/d/186F_A7hdddxBYqkhaTB1rqsfY8wWt7Ui/view?usp=sharing)
