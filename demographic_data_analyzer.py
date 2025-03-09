#%%
import pandas as pd
import numpy as np

#%%
def calculate_demographic_data(print_data=True):
    # Read data from file
    #%%
    df = pd.read_csv('adult.data.csv')

    #%%
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # %%
    # What is the average age of men?
    df_males = df.loc[df['sex'] == 'Male']
    
    average_age_men = df_males['age'].mean().round(1)

    # %%
    # What is the percentage of people who have a Bachelor's degree?
    df_bachelors = df.loc[df['education'] == 'Bachelors']

    percentage_bachelors = np.round(df_bachelors.shape[0] / df.shape[0] * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # %%
    df_advanced_ed = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]

    df_higher_education_rich = df_advanced_ed.loc[df_advanced_ed['salary'] == '>50K']

    higher_education_rich = np.round(df_higher_education_rich.shape[0] / df_advanced_ed.shape[0] * 100, 1)

    # %%
    # What percentage of people without advanced education make more than 50K?

    df_no_advanced_ed = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    
    df_no_advanced_ed_rich = df_no_advanced_ed.loc[df_no_advanced_ed['salary'] == '>50K']
    
    lower_education_rich = np.round(df_no_advanced_ed_rich.shape[0] / df_no_advanced_ed.shape[0] * 100, 1)

    #%%
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df_advanced_ed.shape[0] / df.shape[0] * 100

    lower_education = df_no_advanced_ed.shape[0] / df.shape[0] * 100

    # %%
    # percentage with salary >50K

    # %%
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # %%
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    df_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    df_min_workers_rich = df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]
    
    rich_percentage = df_min_workers_rich.shape[0] / df_min_workers.shape[0] * 100
    
    #%
    # What country has the highest percentage of people that earn >50K?
    df_total_per_country = df['native-country'].value_counts()

    df_richs_per_country = df.loc[df['salary'] == '>50K']['native-country'].value_counts()

    riches_percentages_per_country = df_richs_per_country / df_total_per_country * 100

    highest_earning_country = riches_percentages_per_country.idxmax()
    highest_earning_country_percentage = np.round(riches_percentages_per_country.max(), 1)

    # %%
    # Identify the most popular occupation for those who earn >50K in India.
    df_riches_india = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India')]

    riches_india_occupations = df_riches_india['occupation'].value_counts()
    
    top_IN_occupation = riches_india_occupations.idxmax()
    # %%
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# %%

