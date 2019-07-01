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
    print('Hi! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ["chicago", "new york city", "washington"]
    city = input("Enter name of city [chicago, new york city or washington] : ").lower()
    while city not in city_list:
        city = input("ReEnter name of city [chicago, new york city or washington] : ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "may", "june"]
    month = input("Enter months [all, january, february, ... , june] : ").lower()
    while month not in months:
        month = input("ReEnter months [all, january, february, ... , june] : ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = input("Enter day of week [all, monday, tuesday, ... sunday] : ").lower()
    while day not in days:
        day = input("ReEnter day of week [all, monday, tuesday, ... sunday] : ").lower()

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
    global CITY_DATA
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1;
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day_of_week"] == day.title()]

    ans = input("Would you like to display the first 5 rows of DataFrame ? yes or no \n")
    i = 0
    i = ask(df, i)
    while ans != "no":


        ans = input("Would you like to display the next 5 rows of DataFrame ? yes or no \n ")
        if ans != "no":
            i = ask(df, i+1)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    popular_month = df["month"].mode()[0]
    print("MOST comon month : >_ ", popular_month)

    # TO DO: display the most common day of week
    df["day"] = df["Start Time"].dt.weekday_name
    popular_day = df["day_of_week"].mode()[0]
    print("MOST comon day of week  : >_ ", popular_day)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popular_hour = df["hour"].mode()[0]
    print("MOST comon hour : >_ ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df["Start Station"].mode()[0]
    print("MOST common Start Station : >_ ", popular_start)

    # TO DO: display most commonly used end station
    popular_end = df["End Station"].mode()[0]
    print("MOST common End Station : >_ ", popular_end)


    # TO DO: display most frequent combination of start station and end station trip

    result = df[["Start Station", "End Station"]].mode()
    start, end = result["Start Station"][0], result["End Station"][0]

    print("MOST frequent combinaison of Start Station and End Station trip : >_ {}, {} ".format(start, end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    popular_total = df["Trip Duration"].sum()
    print("TOTAL travel time : >_ ", popular_total)

    # TO DO: display mean travel time
    popular_mean = df["Trip Duration"].mean()
    print("MEAN travel time : >_ ", popular_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if "User Type" in df.columns:
        popular_user = df["User Type"].shape[0]
        print("USER types : >_ ", popular_user)
    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        popular_gender = df["Gender"].shape[0]
        print("GENDER total : >_ ", popular_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        popular_most = df["Birth Year"].min()
        popular_recent = df["Birth Year"].max()
        popular_com = df["Birth Year"].mode()[0]
        print("EARLIEST year of birth : >_ ", popular_most)
        print("RECENT year of birth : >_ ", popular_recent)
        print("MOST frequent year of birth : >_ ", popular_com)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def ask(df, indice):
    i = indice
    end = i + 5
    while i < end:
        print(df.iloc[i])
        i += 1
    return end

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
