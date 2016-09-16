
import pandas

# by default the read_csv function will read a comma separated file,
# our gapminder data set is separated by a tab
# we can use the sep parameter and indicate a tab with \t
df = pandas.read_csv('../data/gapminder.tsv', sep='\t')
# we use the head function so Python only shows us the first 5 rows
print(df.head())

# can also 'nickname' pandas as 'pd' so we don't have to keep typing 'pandas'
import pandas as pd
df = pd.read_csv('../data/gapminder.tsv', sep='\t')
print(df.head())

print(type(df))

print(df.shape)

# this will error
print(df.shape())

# get column names

print(df.columns)

print(df.dtypes)

print(df.info())

# just get the country column and save it to its own variable
country_df = df['country']

# show the first 5 observations
print(country_df.head())

# show the last 5 observations
print(country_df.tail())

country_df_dot = df.country
print(country_df_dot.head())

# Looking at country, continent, and year
subset = df[['country', 'continent', 'year']]
print(subset.head())

print(subset.tail())

# try to get the first column by passing the integer 1
subset = df[[1]]
# we really end up getting the second column
print(subset.head())

# get the first column (index 0) and last column
subset = df[[0, -1]]
print(subset.head())

# create a range of integers from 0 - 4 inclusive
small_range = list(range(5))
# subset the dataframe with the range
subset = df[small_range]
print(subset.head())

# create a range from 3 - 5 inclusive
small_range = list(range(3, 6))
subset = df[small_range]
print(subset.head())

# create a range form 0 - 5 inclusive, every other integer
small_range = list(range(0, 6, 2))
subset = df[small_range]
print(subset.head())

print(df.head())

# get the first row
print(df.loc[0])

# get the 100th row
# recall that values start with 0
print(df.loc[99])

# get the last row
print(df.loc[-1])

# get the last row (correctly)
# use the first value given from shape to get the total number of rows
number_of_rows = df.shape[0]
# subtract 1 from the value since we want the last index value
last_row_index = number_of_rows - 1
# finally do the subset using the index of the last row
print(df.loc[last_row_index])

# there are many ways of doing what you want
print(df.tail(n=1))

subset_loc = df.loc[0]
subset_head = df.head(n=1)
print(type(subset_loc))

print(type(subset_head))

# select the first, 100th, and 1000th row
# note the double square brackets similar to the syntax used to
# subset multiple columns
print(df.loc[[0, 99, 999]])

# get the first row
print(df.iloc[0])

## get the 100th row
print(df.iloc[99])

## get the first, 100th, and 1000th row
print(df.iloc[[0, 99, 999]])

# get the first row
print(df.ix[0])

# get the 100th row
print(df.ix[99])

# get the first, 100th, and 1000th row
print(df.ix[[0, 99, 999]])

# get the 43rd country in our data
print(df.ix[42, 'country'])

print(df.loc[42, 'country'])

print(df.iloc[42, 0])

print(df.loc[42, 0])

# compare this ix code with the one above.
# instead of 'country' I used the index 0
print(df.ix[42, 0])

# get the first, 100th, and 1000th rows from the first, 4th, and 5th column
# note the columns we are hoping to get are: country, lifeExp, and gdpPercap
print(df.ix[[0, 99, 999], [0, 3, 5]])

# if we use the column names directly, it makes the code a bit easier to read
print(df.ix[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

print(df.head(n=10))

# For each year in our data, what was the average life expectancy?
# To answer this question, we need to split our data into parts by year
# then we get the 'lifeExp' column and calculate the mean
print(df.groupby('year')['lifeExp'].mean())

grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print(grouped_year_df)

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))
print(grouped_year_df_lifeExp)

mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

print(df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean())

# use the nunique (number unique) to calculate the number of unique values in a series
print(df.groupby('continent')['country'].nunique())

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

global_yearly_life_expectancy.plot()
