# Analyzing Art Theater data

## Organization Name
The Art Theater

## Overview
The Art Theater is a one-screen Art House theater that programs its films for a combination of fulfilling its mission and keeping the business operating through ticket and concessions sales.  

## Problem Statement
Choosing films is a difficult process;  theaters must select movies well in advance – so strategy is necessary to choose the right films.  The good news is that the Theater gets a new chance each week.

The Art Theater is looking for help to make its data more meaningful.  Some ways this could happen:

1. The Concessions sales are by day and time, but not by movie.  Surely, there should be a way to infer the associated film from the Ticket datasets...

2. The movie data in "ticket_sales_by_showing" is in a vacuum.  We would very much like to be able to combine this information with existing databases to answer qusetions based on factors such as: genre, critic & audience ratings scores, MPAA ratings, etc.   Of note... there are open APIs with IMDB-like data (https://rapidapi.com/imdb/api/movie-database-imdb-alternative) 

3. Of even more value would be to compare the performance of films at the Art Theater with the performance of the same film at other theaters, AT THE SAME TIME.  This would allow the Art to understand what films might do better (or worse) with our audience.  This information is available on sites like Box Office Mojo: https://www.boxofficemojo.com/movies/?page=daily&view=chart&id=rbg.htm  

Other data sets are included that contain the use of reloadable Smart Cards, to mine that information for possible trends - or to detect abuse of the cards.  (We don't suspect any, but just in case.) 

## Evaluation criteria

We are looking for tools that can be used on an ongoing basis, so a sustainable project that can be reloaded with fresh data for new analysis is an important aspect.

Otherwise, meaningful insights and improved decision-making are what we seek!

The team with the best project using our data will win $20 gift cards for each member!

## Data Details

There are five datasets:

- ticket_sales_by_showing.csv - this sumarizes the count of tickets by type (Adult, Student, etc.) by movie, date, and time.

- gross_revenue_by_event.csv - summarizes all tickets and concessions by event/film

- ConcessionsSales_Anonymized.csv - lists transactions of food & drink by date & time (but not by event!)

- gift_card_transactions.csv - lists the amounts added and removed from gift cards

- merchandise_sales.csv - lists the sales of merch, which is generally special event passes
