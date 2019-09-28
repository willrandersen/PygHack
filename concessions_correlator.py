import pandas as pd
from datetime import datetime, timedelta

def find_closest(date, date_list):
    closest_date = date_list[0]
    closest_delta = timedelta(weeks=1000000)
    for date_in_list in date_list:
        delta = abs(date - date_in_list)
        if delta < closest_delta:
            closest_delta = delta
            closest_date = date_in_list
    return closest_date

ticket_sales = pd.read_csv("ticket_sales_by_showing.csv")
concession_sales = pd.read_csv("ConcessionsSales_Anonymized.csv")

movie_dates = ticket_sales["EventDate"].unique().tolist()
for date in range(len(movie_dates)):
    movie_dates[date] = datetime.strptime(movie_dates[date], "%b %d, %Y %I:%M:%S %p")

for row in range(len(ticket_sales["EventDate"])):
    ticket_sales.at[row, "EventDate"] = datetime.strptime(ticket_sales.at[row, "EventDate"], "%b %d, %Y %I:%M:%S %p")

for row in range(len(concession_sales["Order Date"])):
    order_date = datetime.strptime(concession_sales.at[row, "Order Date"], "%m/%d/%Y %I:%M:%S %p")
    for x in range(len(ticket_sales)):
        if ticket_sales.at[x, "EventDate"] == order_date:
            concession_sales.at[x, "InternalEventName"] = ticket_sales.at[x, "InternalEventName"]


concession_sales.to_csv("test.csv")