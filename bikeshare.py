# Please note that I have used code which was provided in the solution file for the practice problems to help complete the project
# Loading Bikeshare project on Git as part of the Version control project on October 24, 2018
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input('\nPlease provide the name of the city to analyze, Enter either chicago, new york city or washington:')

while True:

        city = input('\nPlease provide the name of the city to analyze, Enter either chicago, new york city or washington:').lower()
        if city  in ('chicago','new york city','washington'):
                   next_entry = input('Please enter if you want to filter data by month, day,both or none: ')
                   break
    while next_entry not in ('month','day','both','none'):
             next_entry = input('Please enter if you want to filter data by month, day,both or none: ')
             if next_entry in ('month','day','both','none'):
                             break

    if next_entry == 'none':
                       month = 'all'
                       weekday = 'all'
    elif next_entry == 'month':
                      month = input('\nPlease enter a month from January to June to filter the data:').lower()
                      weekday = 'all'
                      while month not in ('january','february','march','april','may','june'):
                         month = input('\nPlease enter a month from January to June to filter the data:').lower()
                         if month in ('january','february','march','april','may','june'):
                             break
    elif next_entry == 'day':
                      weekday = input('\nPlease enter the day of the week to filter the data: ').lower()
                      month = 'all'
                      while weekday not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
                         weekday = input('\nPlease enter the day of the week to filter the data:').lower()
                         if weekday in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
                             break
    elif next_entry == 'both':
           month = input('\nPlease enter a month from January to June to filter the data:')
           weekday = input('\nPlease enter the day of the week to filter the data: ')

    print('-'*40)
    return city, month, weekday


def load_data(city, month, weekday):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name

    #This is the section of the code which I have used from the solution file for the Practice problems to help complete the project
    if month != 'all':
      # filter by month to create the new dataframe
      # use the index of the months list to get the corresponding index number
     months = ('january','february','march','april','may','june')
     month = months.index(month) + 1
     df = df[df['month'] == month]

    if weekday != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['weekday'] == weekday.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print('The most common month of travel is:',common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['weekday'].mode()[0]
    print('The most common day of the week for travel is:',common_day_of_week)

    df['Start hour'] = df['Start Time'].dt.hour
    common_hour = df['Start hour'].mode()[0]
    print('The most common start hour of travel is:',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    popular_start_station =df['Start Station'].mode()[0]
    print('The most commonly used start station :',popular_start_station)


    popular_end_station =df['End Station'].mode()[0
    print('The most commonly used end station :',popular_end_station)


    combined_station = df['Start Station'] + df['End Station']
    df['combined station'] = combined_station
    most_frequent =  df['combined station'].mode()[0]
    print('The most frequent combination of start and end staton trip : ',most_frequent)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    print('The total trip duration',total_duration)


    Average_travel = df['Trip Duration'].mean()/360
    print('The average travel time',Average_travel, 'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type = df['User Type'].value_counts()
    print('The total count of users',user_type)


    try:
        gender = df['Gender'].value_counts()
        print('\nThe count of people by gender is\n',gender)
    except:
        print('There is no gender data in this file\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    youngest = df['Birth Year'].max()
    oldest = df['Birth Year'].min()
    popular_year = df['Birth Year'].mode()[0]

    print('\nThe most common year of birth:',popular_year,'\n','The most recent year of birth:',youngest,'\n','The earliest year of birth:',oldest,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
