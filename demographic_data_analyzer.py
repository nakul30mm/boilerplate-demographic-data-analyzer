
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read the dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Number of people of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 4. Percentage of people with advanced education earning >50K
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    higher_education_rich = round(
        (df[higher_education]["salary"] == ">50K").mean() * 100, 1
    )

    # 5. Percentage of people without advanced education earning >50K
    lower_education_rich = round(
        (df[~higher_education]["salary"] == ">50K").mean() * 100, 1
    )

    # 6. Minimum number of hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of people working minimum hours who earn >50K
    num_min_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    rich_percentage = round(
        (num_min_workers["salary"] == ">50K").mean() * 100, 1
    )

    # 8. Country with the highest percentage of people earning >50K
    country_earning = (
        df[df["salary"] == ">50K"]["native-country"].value_counts()
        / df["native-country"].value_counts()
        * 100
    )

    highest_earning_country = country_earning.idxmax()

    highest_earning_country_percentage = round(
        country_earning.max(), 1
    )

    # 9. Most popular occupation among people earning >50K in India
    top_IN_occupation = df[
        (df["native-country"] == "India")
        & (df["salary"] == ">50K")
    ]["occupation"].value_counts().idxmax()

    # Print results
    if print_data:
        print("Number of people of each race:")
        print(race_count)
        print("\nAverage age of men:", average_age_men)
        print(
            "Percentage with Bachelor's degree:",
            percentage_bachelors
        )
        print(
            "Percentage with advanced education earning >50K:",
            higher_education_rich
        )
        print(
            "Percentage without advanced education earning >50K:",
            lower_education_rich
        )
        print("Minimum hours worked per week:", min_work_hours)
        print(
            "Percentage of minimum-hour workers earning >50K:",
            rich_percentage
        )
        print(
            "Country with highest percentage earning >50K:",
            highest_earning_country
        )
        print(
            "Percentage earning >50K in that country:",
            highest_earning_country_percentage
        )
        print("Most popular occupation in India earning >50K:")
        print(top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
