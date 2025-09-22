# week_1/job_calculator/main.py

from week_1.job_calculator.user_interface.menu_options import display_menu
from week_1.job_calculator.user_interface.menu_options import create_new_job
from week_1.job_calculator.jobs.job import Job


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

    # local variables
    jobs_list = []

    print("*** Problem 4 - Job Calculator ***")

    while True:
        menu_user_input = display_menu()

        if menu_user_input == 1 :
            jobs_list.append(create_new_job())

        if menu_user_input == 2 :
            for job in jobs_list:
                print(job)
                print("Basic payment: ", Job.basic_pay_calculator(job), "€")
                print("Overtime payment: ", Job.overtime_pay_calculator(job), "€")
                print("Total payment: ", Job.total_pay_calculator(job), "€")


        elif menu_user_input == 3 :
            print("Thank you for using this program.")
            break

if __name__ == '__main__':
    main()
