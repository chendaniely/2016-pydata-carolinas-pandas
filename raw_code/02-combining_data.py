
import pandas as pd

df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')

print(df1)

print(df2)

print(df3)

row_concat = pd.concat([df1, df2, df3])
print(row_concat)

# subset the 4th row of the concatenated dataframe
print(row_concat.iloc[3, ])

# create a new row of data
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(new_row_series)

# attempt to add the new row to a dataframe
print(pd.concat([df1, new_row_series]))

                        # note the double brackets
new_row_df = pd.DataFrame([['n1', 'n2', 'n3', 'n4']],
                   columns=['A', 'B', 'C', 'D'])
print(new_row_df)

print(pd.concat([df1, new_row_df]))

print(df1.append(df2))

print(df1.append(new_row_df))

data_dict = {'A': 'n1',
             'B': 'n2',
             'C': 'n3',
             'D': 'n4'}

print(df1.append(data_dict, ignore_index=True))

row_concat_i = pd.concat([df1, df2, df3], ignore_index=True)
print(row_concat_i)

col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat)

print(col_concat['A'])

col_concat['new_col_list'] = ['n1', 'n2', 'n3', 'n4']
print(col_concat)

col_concat = pd.concat([df1, df2, df3], axis=1)

col_concat['new_col_series'] = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(col_concat)

print(pd.concat([df1, df2, df3], axis=1, ignore_index=True))

df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

print(df1)

print(df2)

print(df3)

row_concat = pd.concat([df1, df2, df3])
print(row_concat)

print(pd.concat([df1, df2, df3], join='inner'))

print(pd.concat([df1,df3], ignore_index=False, join='inner'))

df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]

print(df1)

print(df2)

print(df3)

col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat)

print(pd.concat([df1, df3], axis=1, join='inner'))

person = pd.read_csv('../data/survey_person.csv')
site = pd.read_csv('../data/survey_site.csv')
survey = pd.read_csv('../data/survey_survey.csv')
visited = pd.read_csv('../data/survey_visited.csv')

print(person)

print(site)

print(visited)

print(survey)

visited_subset = visited.ix[[0, 2, 6], ]

# internal check of data
assert visited_subset['site'].nunique() == 3

# the default value for 'how' is 'inner'
# so it doesn't need to be specified
o2o_merge = site.merge(visited_subset,
                       left_on='name', right_on='site')
print(o2o_merge)

m2o_merge = site.merge(visited, left_on='name', right_on='site')
print(m2o_merge)

ps = person.merge(survey, left_on='ident', right_on='person')
vs = visited.merge(survey, left_on='ident', right_on='taken')

print(ps)

print(vs)

ps_vs = ps.merge(vs,
                 left_on=['ident', 'taken', 'quant', 'reading'],
                 right_on=['person', 'ident', 'quant', 'reading'])

print(ps_vs.ix[0, ])
