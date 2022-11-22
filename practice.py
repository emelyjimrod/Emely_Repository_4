import pathlib
from pathlib import Path

csvpath = Path('whale_navs.csv')

import pandas as pd

df = pd.read_csv('whale_navs.csv')
print(df)

Use the whale_analysis.ipynb file to complete the following steps:

Import the required libraries and dependencies.

Use the read_csv function and the Path module to read the whale_navs.csv file into a Pandas DataFrame. Be sure to create a DateTimeIndex. Review the first five rows of the DataFrame by using the head function.

Use the Pandas pct_change function together with dropna to create the daily returns DataFrame. Base this DataFrame on the NAV prices of the four portfolios and on the closing price of the S&P 500 Index. Review the first five rows of the daily returns DataFrame. The following image shows how your daily returns DataFrame should appear:

A screenshot depicts the first five rows of the DataFrame.

Nice work—you’re ready to do your quantitative analysis!

The analysis has several components: performance, volatility, risk, risk-return profile, and portfolio diversification. You’ll analyze each component one at a time.

Analyze the Performance
Analyze the data to determine if any of the portfolios outperform the broader stock market, which the S&P 500 represents. To do so, complete the following steps:

Use the default Pandas plot function to visualize the daily return data of the four fund portfolios and the S&P 500. Be sure to include the title parameter, and adjust the figure size if necessary.

Use the Pandas cumprod function to calculate the cumulative returns for the four fund portfolios and the S&P 500. Review the last five rows of the cumulative returns DataFrame by using the Pandas tail function.

Use the default Pandas plot to visualize the cumulative return values for the four funds and the S&P 500 over time. Be sure to include the title parameter, and adjust the figure size if necessary.

Answer the following question: Based on the cumulative return data and the visualization, do any of the four fund portfolios outperform the S&P 500 Index?

Analyze the Volatility
Analyze the volatility of each of the four fund portfolios and of the S&P 500 Index by using box plots. To do so, complete the following steps:

Use the Pandas plot function and the kind="box" parameter to visualize the daily return data for each of the four portfolios and for the S&P 500 in a box plot. Be sure to include the title parameter, and adjust the figure size if necessary.

Use the Pandas drop function to create a new DataFrame that contains the data for just the four fund portfolios by dropping the S&P 500 column. Visualize the daily return data for just the four fund portfolios by using another box plot. Be sure to include the title parameter, and adjust the figure size if necessary.

HINT
Answer the following question: Based on the box plot visualization of just the four fund portfolios, which fund was the most volatile (with the greatest spread) and which was the least volatile (with the smallest spread)?

Analyze the Risk
Evaluate the risk profile of each portfolio by using the standard deviation and the beta. To do so, complete the following steps:

Use the Pandas std function to calculate the standard deviation for each of the four portfolios and for the S&P 500. Review the standard deviation calculations, sorted from smallest to largest.

Calculate the annualized standard deviation for each of the four portfolios and for the S&P 500. To do that, multiply the standard deviation by the square root of the number of trading days. Use 252 for that number.

Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of the four fund portfolios and of the S&P 500 index. Be sure to include the title parameter, and adjust the figure size if necessary.

Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of only the four fund portfolios. Be sure to include the title parameter, and adjust the figure size if necessary.

Answer the following three questions:

Based on the annualized standard deviation, which portfolios pose more risk than the S&P 500?

Based on the rolling metrics, does the risk of each portfolio increase at the same time that the risk of the S&P 500 increases?

Based on the rolling standard deviations of only the four fund portfolios, which portfolio poses the most risk? Does this change over time?

Analyze the Risk-Return Profile
To determine the overall risk of an asset or portfolio, quantitative analysts and investment managers consider not only its risk metrics but also its risk-return profile. After all, if you have two portfolios that each offer a 10% return but one has less risk, you’d probably invest in the smaller-risk portfolio. For this reason, you need to consider the Sharpe ratios for each portfolio. To do so, complete the following steps:

Use the daily return DataFrame to calculate the annualized average return data for the four fund portfolios and for the S&P 500. Use 252 for the number of trading days. Review the annualized average returns, sorted from lowest to highest.

Calculate the Sharpe ratios for the four fund portfolios and for the S&P 500. To do that, divide the annualized average return by the annualized standard deviation for each. Review the resulting Sharpe ratios, sorted from lowest to highest.

Visualize the Sharpe ratios for the four funds and for the S&P 500 in a bar chart. Be sure to include the title parameter, and adjust the figure size if necessary.

Answer the following question: Which of the four portfolios offers the best risk-return profile? Which offers the worst?

Diversify the Portfolio
Your analysis is nearing completion. Now, you need to evaluate how the portfolios react relative to the broader market. Based on your analysis so far, choose two portfolios that you’re most likely to recommend as investment options. To start your analysis, complete the following step:

Use the Pandas var function to calculate the variance of the S&P 500 by using a 60-day rolling window. Visualize the last five rows of the variance of the S&P 500.
Next, for each of the two portfolios that you chose, complete the following steps:

Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.

Calculate the beta of the portfolio. To do that, divide the covariance of the portfolio by the variance of the S&P 500.

Use the Pandas mean function to calculate the average value of the 60-day rolling beta of the portfolio.

Plot the 60-day rolling beta. Be sure to include the title parameter, and adjust the figure size if necessary.

Answer the following two questions:

Which of the two portfolios seem more sensitive to movements in the S&P 500?

Which of the two portfolios do you recommend for inclusion in your firm’s suite of fund offerings?

Requirements
Imports (10 points)
To receive all points, you must:
Import all required libraries and dependencies. (3 points)

Use read_csv and Path to read whale_navs.csv into a Pandas DataFrame. (3 points)

Use pct_change and dropna to create the daily returns DataFrame. (4 points)

Analysis (10 points)
To receive all points, you must:
Use plot to visualize the daily return data of the four fund portfolios and the S&P 500. (2 points)

Use cumprod to calculate the cumulative return for the four fund portfolios and the S&P 500. (3 points)

Use plot to visualize the cumulative return values for the four funds and the S&P 500 over time. (2 points)

Answer the following question in the Jupyter notebook: Do any of the four fund portfolios outperform the S&P 500 index? (3 points)

Volatility (10 points)
To receive all points, you must:
Use plot with the kind="Box" parameter to visualize the daily return data for each of the four portfolios and the S&P 500. (2 points)

Use drop to create a new DataFrame containing data for the four fund portfolios, dropping the S&P 500 column, and then visualize it using a box plot. (5 points)

Answer the following question in the Jupyter notebook: Based on the box plot visualization of just the four fund portfolios, which fund was the most volatile (with the greatest spread) and which was the least volatile (with the smallest spread)? (3 points)

Risk (10 points)
To receive all points, you must:
Use std to calculate the standard deviation for each of the four portfolios and the S&P 500. (2 points)

Calculate annual standard deviation for each of the four portfolios and the S&P 500. (2 points)

Plot the rolling standard deviation for the four fund portfolios and the S&P 500, using the daily returns DataFrame and a 21-day rolling window. (2 points)

Plot the rolling standard deviation for ONLY the four fund portfolios, using the daily returns DataFrame and a 21-day rolling window. (2 points)

Answer the following three questions in the Jupyter notebook: (2 points)

Based on the annualized standard deviation, which portfolios pose more risk than the S&P 500?

Based on the rolling metrics, does the risk of each portfolio increase at the same time that the risk of the S&P 500 increases?

Based on the rolling standard deviations of only the four fund portfolios, which portfolio poses the most risk? Does this change over time?

Risk and Return (15 points)
To receive all points, you must:
Calculate the annualized average return data of the four fund portfolios and the S&P 500, using the daily returns DataFrame. (2 points)

Calculate the Sharpe ratios of the four fund portfolios and the S&P 500. (5 points)

Visualize the Sharpe ratios of the four fund portfolios and the S&P 500 in a bar chart. (5 points)

Answer the following question in a Jupyter notebook: Which of the four portfolios offers the best risk-return profile? Which offers the worst? (3 points)

Diversification (15 points)
To receive all points, you must:
Calculate the covariance, using a 60-day rolling window, daily return data, and S&P 500 returns. (3 points)

Calculate the beta of the portfolio. (3 points)

Calculate the average value of the 60-day rolling beta of the portfolio, using mean. (3 points)

Plot the 60-day rolling beta. (3 points)

Answer the following two questions in a Jupyter notebook: (3 points)

Which of the two portfolios seem more sensitive to movements in the S&P 500?

Which of the two portfolios do you recommend for inclusion in your firm’s suite of fund offerings?

Coding Conventions and Formatting (10 points)
To receive all points, your code must:
Place imports at the beginning of the file, just after any module comments and docstrings and before module globals and constants. (3 points)

Name functions and variables with lowercase characters and with words separated by underscores. (2 points)

Follow Don't Repeat Yourself (DRY) principles by creating maintainable and reusable code. (3 points)

Use concise logic and creative engineering where possible. (2 points)

