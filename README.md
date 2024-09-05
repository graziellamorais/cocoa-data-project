# cocoa-data-project
Utilizing BeautifulSoup to scrape data from a website that contains more than 1700 reviews of various chocolate bars

Summary

Data Collection:

Scraping the Web: Used requests to fetch HTML content from a webpage containing information about chocolate bars.
Parsing HTML: Employed BeautifulSoup to parse the HTML and extract relevant data.
Data Extraction:

Ratings: Extracted ratings of chocolate bars from the HTML, converted them into floats and stored them in a list.
Companies: Retrieved names of companies that produce the chocolate bars and stored them in a list.
Cocoa Percentages: Extracted cocoa percentage data, stripped the '%' sign, and converted them into floats.
Countries: Gathered the broad bean origin (country of origin) for each chocolate bar and stored it in a list.
Data Preparation:

Creating DataFrame: Constructed a pandas DataFrame using company names and ratings.
Adding Columns: New columns were added to the DataFrame for cocoa percentages and broad bean origins.
Data Analysis:

Top 10 Highest-Rated Chocolatiers: Grouped data by company and calculated the mean ratings to find the top 10 highest-rated chocolatiers.
Top 10 Best Bean Origin Countries: Grouped data by bean origin and found the top 10 countries based on the highest maximum ratings (repeated values found). 

Visualization:

Histogram: Plotted a histogram of chocolate ratings to visualize the distribution.
Scatterplot with Line of Best Fit: Created a scatterplot to show the relationship between cocoa percentage and ratings, and added a line of best fit to the plot.
