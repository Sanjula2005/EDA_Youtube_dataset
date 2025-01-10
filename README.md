## YouTube Analytics Project

Welcome to the **YouTube Channel Analytics** project! This repository contains data-driven insights and visualizations based on various aspects of YouTube channels. By analyzing a wide range of attributes, from subscribers to earnings, this project reveals intriguing patterns and relationships that shape the world of YouTube content creators.

## 🚀 Overview

In this project, we explore the YouTube ecosystem by examining data such as:

- YouTuber statistics (subscribers, video views, uploads)
- Channel categories and their performance metrics
- Geographic and demographic trends
- Earnings analysis and trends
- Educational and employment factors that influence YouTube channel growth

The goal is to uncover insights that can be valuable for YouTube content creators, marketers, and researchers who are interested in understanding the dynamics of the YouTube platform.


## 🧩 Project Features

### Key Insights:
1. **Top 10 YouTube Channels by Subscribers**:
   - Identify the most influential YouTubers by their subscriber count.
   
2. **Category Analysis**:
   - Find the category with the highest average subscribers.
   - Calculate the average number of videos uploaded by YouTubers across different categories.
   
3. **Geographic Insights**:
   - Determine the countries with the highest number of YouTube channels.
   - Analyze the relationship between YouTube channels and education or employment statistics by country.

4. **Earnings Insights**:
   - Compare monthly earnings across various categories of YouTube channels.
   - Identify outliers in yearly earnings to discover exceptional creators.

5. **Subscriber Growth**:
   - Track the trend in subscribers gained in the last 30 days.
   - Analyze the correlation between subscribers and video views.

6. **Data Visualizations**:
   - **Distribution of Channel Types Across Categories**: Gain insights into the type of channels that dominate each category.
   - **Subscribers vs. Video Views**: Visualize the relationship between subscribers and total video views.

7. **Geographic Trends**:
   - Explore how the distribution of YouTube channels relates to latitude and longitude.
   - Study the correlation between population size and the number of subscribers.

8. **Other Patterns**:
   - Examine the correlation between subscribers gained in the last 30 days and unemployment rates.
   - Investigate urban population percentages and their connection to YouTube channel creation.


## 📊 Visualizations & Insights

- **Correlation Analysis**: Understand the key relationships, like the connection between subscribers and video views, or between education enrollment and YouTube channels.
- **Geographic Distribution**: Track the growth of YouTube channels across various countries, correlating it with social and economic factors such as population and unemployment rates.
- **Category Performance**: Discover the performance of different YouTube categories with respect to average subscribers, earnings, and uploads.


## 📥 Requirements

Before running the project, make sure to install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```


## 📂 File Structure

- **`Youtube.csv`**: This is the dataset containing all the information about YouTube channels, including attributes like `subscribers`, `uploads`, `category`, `Country`, and more.
- **`main.py`**: The main Python script that loads the data, performs analysis, and generates visualizations.

  
## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/Sanjula2005/EDA_Youtube_dataset.git
```

2. Navigate to the project folder:

```bash
cd youtube-channel-analytics
```

3. Run the main script:

```bash
python main.py
```


## 🎨 Results & Examples

- The **Top 10 Channels** by subscribers showcases the most influential creators.
- **Category performance** analysis shows how different niches are performing in terms of average subscribers and video uploads.
- A **scatter plot** of `Subscribers` vs. `Video Views` reveals how these two factors are interrelated.
- The **Earnings Analysis** uncovers the variation in monthly and yearly earnings across categories.


## 📈 Future Improvements

- **Real-Time Data**: Integrate real-time data from the YouTube API for up-to-date analytics.
- **Advanced Predictive Models**: Use machine learning to predict subscriber growth, earnings, and video views based on historical data.
- **More Advanced Visualizations**: Enhance the visualizations with interactive charts and graphs using libraries like Plotly or Dash.


Enjoy exploring the world of YouTube channels with this project, and let’s uncover the hidden trends and patterns together! 📊🎬

