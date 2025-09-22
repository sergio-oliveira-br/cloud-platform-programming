# week_1/job_calculator/menu/menu_options.py

from week_1.job_calculator.jobs.job import Job


def display_menu():

    user_input = int(input("\n    -- Menu --"
          "\n 1. Create new job"
          "\n 2. Compare the earnings from jobs"
          "\n 3. Exit \n"))

    return user_input


def create_new_job():

    # Get the job's name
    job_name = input("Let's calculates your income together. "
                       "\nTo start, please informe the name of the first job:\n")

    # basic pay rate
    basic_pay_rate = int(input("\nPlease informe your basic pay rate: "))

    # hours
    basic_hours = int(input("\nFor this '" + str(job_name) + " €" + str(basic_pay_rate) + "\h', how many hours did you work this week? "))

    # overtime
    overtime_hours = int(input("\nHow many additional hours did you spend working overtime? "))

    # create a new object
    job = Job( job_name, basic_pay_rate, basic_hours, overtime_hours)

    return job