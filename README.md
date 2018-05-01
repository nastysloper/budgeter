next step is to follow this tutorial:
http://flask.pocoo.org/docs/1.0/tutorial/factory/

http://flask.pocoo.org/docs/1.0/tutorial/layout/

I've imported Bootstrap 4

I need to reorganize the application according to the flask tutorial.

Then I'm setting up a sqlite database.

The reason is to save sample data which I will display when the user clicks on
tabbed navigation.

Create a template to render the response from the database.
This will be the budget categories and values.

1. How to model the data?
Can I do this in a funcitonal way?
I just grab a map? Nah, cause each month owns it's own categories and values.
They can vary from month to month.

I need to carry over last month's balance.
I want to sum up each month's savings and spend, so a user can see how much
she's spent over the year as well as how much she's saved.
I also want to display amounts for different categories.



possible data model:
User
Budget 
Year
Month
Savings -> the carry over from last month (positive or negative)
Category (an entry in your budget)
Value (how much you budget for the month)

query -> give me the budget for 2018
fetch all the months
months fetch their categories (which have a name and a dollar value)

Can I auto-populate categories?
Yes, I definitely want to do this.
But then they will be user editable.
Plus, a user can add or remove categories in each month.


