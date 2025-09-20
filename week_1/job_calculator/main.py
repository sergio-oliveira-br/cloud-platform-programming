# week_1/job_calculator/main.py

# Problem 4: Having just started college, Bob has been busy
# looking for a part-time job to fund his new college social life
# and after only two weeks of looking he has managed to get
# two job offers! Each job comes with different hours, basic rates
# of pay and over-time rates so he needs to work out which
# would get him the most money. Develop an application that
# would allow Bob to enter his basic pay rate, his number of
# regular hours work per week and his number of overtime
# hours per week. The application should then calculate and
# display Bob’s total basic pay for the week, his overtime pay for
# the week and his total pay including overtime. Note: The
# overtime rate is 1.5 times the basic rate of pay.


def main():

    print("*** Problem 4 - Job Calculator ***")

    # Get the job's name
    job_name_1 = input("Hi Bob, let's calculates your income together. "
                       "\nTo start, please informe the name of the first job:\n")

    job_name_2 = input("Now, please enter the name of the second job:\n")

    # basic pay rate
    basic_pay_rate = input("Hi Bob, please informe your basic pay rate: ")

    # hours
    basic_hours = input("For this " + basic_pay_rate + " how many hours did you work this week? ")

    # overtime
    overtime_hours = input("Did you make any overtime? \n-> Please informe your overtime hours? ")


    



if __name__ == '__main__':
    main()
