import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Where are the best cocao beans grown?
Which countries produce the highest-rated bars?
What`s the relationship between cocao solids percentage and rating?
'''

# Creating a request and getting the content
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
webpage = webpage_response.content

# Creating a BeautifulSoup object
soup = BeautifulSoup(webpage, 'html.parser')
print(soup)

# Getting ratings
rating_tags = soup.find_all(attrs = {'class': 'Rating'})
ratings = []
for rating in rating_tags[1:]:
  ratings.append(float(rating.get_text()))

# Creating a histogram
plt.hist(ratings)
plt.show()

# Getting the companies` names
company_tags = soup.select('.Company')
companies = []
for company in company_tags[1:]:
  companies.append(company.get_text())


# Creating a dataframe with company names, ratings
d = {'Company': companies, 'Ratings': ratings}
cocoa_df = pd.DataFrame.from_dict(d)

# Finding the 10 most highly rated chocolatiers
mean_ratings = cocoa_df.groupby(['Company'])['Ratings'].mean()
ten_best = mean_ratings.nlargest(10)
print("Top 10 Highest Rated Chocolatiers:")
print(ten_best)

# Plot the table with a title
#fig, ax = plt.subplots()
#ax.axis('tight')
#ax.axis('off')
# Add the title
#ax.set_title("Top 10 Highest Rated Chocolatiers")
# Convert the series to a DataFrame for display
#table_data = ten_best.reset_index()
# Displaying the table
#ax.table(cellText=table_data.values, colLabels=table_data.columns, cellLoc='center', loc='center')
#plt.show()


# Getting cocoa percentages
cocoa_percent = soup.find_all(attrs = {'class': 'CocoaPercent'})
cocoa_percentages = []
for p in cocoa_percent[1:]:
  cocoa_percentages.append(float(p.get_text().strip('%')))

# Adding the new column 'CocoaPercentage' to the DataFrame
cocoa_df['CocoaPercentage'] = cocoa_percentages

# Getting the countries
country_tags = soup.select('.BroadBeanOrigin')
countries = []
for country in country_tags[1:]:
  countries.append(country.get_text())

# Adding the new column 'Broad Bean Origin' to the DataFrame
cocoa_df['Broad Bean Origin'] = countries

# Finding the best 10 bean origin
best_ratings_per_country = cocoa_df.groupby('Broad Bean Origin')['Ratings'].max()
sorted_best_ratings = best_ratings_per_country.sort_values(ascending=False)
top_10_countries = sorted_best_ratings.head(10)
print("Top 10 Best Bean Origin Countries Based on Ratings:")
print(top_10_countries)


# Making a scatterplot of ratings
plt.clf()
plt.scatter(cocoa_df['CocoaPercentage'], cocoa_df['Ratings'])

# Drawing a line of best-fit
z = np.polyfit(cocoa_df['CocoaPercentage'], cocoa_df['Ratings'], 1)
line_function = np.poly1d(z)
plt.plot(cocoa_df['CocoaPercentage'], line_function(cocoa_df['CocoaPercentage']), "r--")

# Labeling axes
plt.xlabel('Cocoa Percentage')
plt.ylabel('Ratings')

# Displaying the plot
plt.show()
