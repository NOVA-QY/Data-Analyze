import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago , New York , or Washington?\n")
    while(city != "Chicago" and city != "New York" and city != "Washington"):
        print("Your input is invalid,please enter your choice again\n")
        city = input("Would you like to see data for Chicago , New York , or Washington?\n")
    # TO DO: get user input for month (all, january, february, ... , june)
    judge = input("Would you like to filter the data by month , day , or not at all? Type \"none\" for no time filter.\n")
    if(judge=="both"):
        month = input("Which month? January,February,March,April,May,or June?\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day? Please type your response as an integer(e.g.,1=Sunday).\n")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
#     print(df['month'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January','February','March','April','May','June']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
#         print(df['month'])
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    print(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()
    print(df['month'].mode())
    print('Most Frequent Start Month:',popular_month)
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()
    print('Most Frequent Start Day:',popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()
    print('Most Frequent Start Hour:',popular_hour) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user

    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
#         station_stats(df)
#         trip_duration_stats(df)
#         user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
