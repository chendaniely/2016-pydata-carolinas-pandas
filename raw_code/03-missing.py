# Just import the numpy missing values ## TODO SEE APPENDIX
from numpy import NaN, NAN, nan

print(NaN == True)

print(NaN == False)

print(NaN == 0)

print(NaN == '')

print(NaN == NaN)

print(NaN == nan)

print(NaN == NAN)

print(nan == NAN)

import pandas as pd

print(pd.isnull(NaN))

print(pd.isnull(nan))

print(pd.isnull(NAN))

print(pd.notnull(NaN))

print(pd.notnull(42))

print(pd.notnull('missing'))

# set the location for data
visited_file = '../data/survey_visited.csv'

# load data with default values
print(pd.read_csv(visited_file))

# load data without default missing values
print(pd.read_csv(visited_file,
                  keep_default_na=False))

# manually specify missing values
print(pd.read_csv(visited_file,
                  na_values=[''],
                  keep_default_na=False))

visited = pd.read_csv('../data/survey_visited.csv')
survey = pd.read_csv('../data/survey_survey.csv')

print(visited)

print(survey)

vs = visited.merge(survey, left_on='ident', right_on='taken')
print(vs)

# missing value in a series
num_legs = pd.Series({'goat': 4, 'amoeba': nan})
print(num_legs)

# missing value in a dataframe
scientists = pd.DataFrame({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'missing': [NaN, nan]})
print(scientists)

# create a new dataframe
scientists = pd.DataFrame({
    'Name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation': ['Chemist', 'Statistician'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16']})

# assign a columns of missing values
scientists['missing'] = nan

print(scientists)
