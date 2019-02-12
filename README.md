# find-me-a-makeup
Recommender to extract text features of makeup description and find a similar product based on prior reviews

## Introduction

[Temptalia](https://www.temptalia.com/) is a well-known review blog and resource for makeup enthusiasts, recieving 1 million unique visitors each month. The site has a variety of tools for visitors, one of which is the ["Dupe List"](https://www.temptalia.com/makeup-dupe-list/), which helps a user find similar products to the input. The recommendations are hand-selected by the blog author, and thus reliant on her expertise. By scraping reviews from the site, my goal was to recreate this tool in Python by parsing out relevant language from the reviews, and building a reccomender

## Recommender

The newest iteration of the reccomender uses LSA for dimensionality reduction combined with a KNN model of count vectorized reviews. The input is a user generated text string, which can be copy pasted from elsewhere or typed. A flask app is coming very soon!


