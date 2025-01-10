import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\HP\Desktop\Youtube.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Use appropriate encoding
print(df.head())

# Top 10 YouTube Channels by Subscribers
top_10_channels = df.nlargest(10, 'subscribers')[['Youtuber', 'subscribers']]
print(top_10_channels)


# Category with the Highest Average Subscribers
category_avg_subs = df.groupby('category')['subscribers'].mean().sort_values(ascending=False)
highest_avg_category = category_avg_subs.idxmax()
print(f"Category with highest average subscribers: {highest_avg_category}")


# Average Videos Uploaded by Category
avg_videos_per_category = df.groupby('category')['uploads'].mean()
print(avg_videos_per_category)


# Top 5 Countries with the Highest Number of YouTube Channels
top_countries = df['Country'].value_counts().head(5)
print(top_countries)


# Distribution of Channel Types Across Categories
sns.countplot(y='category', hue='channel_type', data=df)
plt.title('Distribution of Channel Types Across Categories')
plt.show()


# Correlation Between Subscribers and Total Video Views
correlation = df['subscribers'].corr(df['video views'])
print(f"Correlation between subscribers and video views: {correlation}")
sns.scatterplot(x='subscribers', y='video views', data=df)
plt.title('Subscribers vs. Video Views')
plt.show()


# Monthly Earnings Variation Across Categories
monthly_earnings = df.groupby('category')[['lowest_monthly_earnings', 'highest_monthly_earnings']].mean()
print(monthly_earnings)
monthly_earnings.plot(kind='bar')
plt.title('Monthly Earnings Variation Across Categories')
plt.show()


# Trend in Subscribers Gained in the Last 30 Days
trend = df['subscribers_for_last_30_days'].sum()
print(f"Total subscribers gained in the last 30 days: {trend}")


# Outliers in Yearly Earnings
plt.boxplot(df['highest_yearly_earnings'].dropna())
plt.title('Outliers in Yearly Earnings')
plt.show()


# Distribution of Channel Creation Dates
df['created_year'] = pd.to_datetime(df['created_year'], errors='coerce').dt.year
sns.histplot(df['created_year'], bins=20, kde=True)
plt.title('Distribution of Channel Creation Dates')
plt.show()


# Relationship Between Education Enrollment and YouTube Channels
education_vs_channels = df.groupby('Country')['Gross tertiary education enrollment (%)'].mean()
print(education_vs_channels)


# Unemployment Rate in Top 10 Countries
top_10_unemployment = df.groupby('Country')['Unemployment rate'].mean().nlargest(10)
print(top_10_unemployment)


# Average Urban Population Percentage
avg_urban_population = df['Urban_population'].mean()
print(f"Average urban population percentage: {avg_urban_population}")


# Patterns in Latitude and Longitude
plt.scatter(df['Latitude'], df['Longitude'], alpha=0.5)
plt.title('Distribution of YouTube Channels by Latitude and Longitude')
plt.show()


# Correlation Between Subscribers and Population
correlation_subs_population = df['subscribers'].corr(df['Population'])
print(f"Correlation between subscribers and population: {correlation_subs_population}")


# Population in Top 10 Countries with Most YouTube Channels
top_10_countries_population = df.groupby('Country')['Population'].sum().nlargest(10)
print(top_10_countries_population)


# Correlation Between Subscribers Gained and Unemployment
correlation_subs_unemployment = df['subscribers_for_last_30_days'].corr(df['Unemployment rate'])
print(f"Correlation: {correlation_subs_unemployment}")


# Distribution of Video Views in Last 30 Days by Channel Type
sns.boxplot(x='channel_type', y='video_views_for_the_last_30_days', data=df)
plt.title('Video Views in Last 30 Days by Channel Type')
plt.show()


# Average Subscribers Gained Per Month
df['months_since_creation'] = ((pd.to_datetime('now') - pd.to_datetime(df['created_year'], errors='coerce')).dt.days / 30)
df['avg_subs_per_month'] = df['subscribers'] / df['months_since_creation']
avg_subs_per_month = df['avg_subs_per_month'].mean()
print(f"Average subscribers gained per month: {avg_subs_per_month}")
