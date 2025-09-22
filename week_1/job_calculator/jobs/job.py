# week_1/job_calculator/jobs/job.py


class Job:
    """A base class to represent the jobs."""

    # constructor
    def __init__(self, job_name, basic_pay_rate, basic_hours, overtime_hours):
        """Constructor to initialise a new job."""

        # The constructor checks the input data. If validation fails, it raises an exception immediately.
        # This ensures that no invalid objects are created.
        if job_name is None or job_name == "":
            raise ValueError("Job's name cannot be none or empty.")

        elif basic_pay_rate < 0:
            raise ValueError("'Basic pay rate' cannot be negative")

        elif basic_hours < 0 or overtime_hours < 0:
            raise ValueError("'Basic hours' and or 'overtime hours' cannot be negative")

        self.job_name = job_name
        self.basic_pay_rate = basic_pay_rate
        self.basic_hours = basic_hours
        self.overtime_hours = overtime_hours

    # toString
    def __str__(self):
        """Returns a string representation of the job."""

        job_name = str(self.job_name)
        basic_pay_rate = str(self.basic_pay_rate)
        basic_hours = str(self.basic_hours)
        overtime_hours = str(self.overtime_hours)

        return (f"*****\n"
                f"--> Job Name: {job_name} \n"
                f"  Basic Rate: {basic_pay_rate}\n"
                f"  Basic Hours: {basic_hours} \n"
                f"  Overtime Hours: {overtime_hours}\n"
                f"*****")

    # BUSINESS LOGIC
    # ... The application should then calculate and
    # display Bob’s total basic pay for the week, his overtime pay for
    # the week and his total pay including overtime. Note: The
    # overtime rate is 1.5 times the basic rate of pay.

    def basic_pay_calculator(self):
        """Calculates the job's income in basic rate."""
        return self.basic_pay_rate * self.basic_hours

    def overtime_pay_calculator(self):
        """Calculates the job's income in overtime rate."""
        return self.basic_pay_rate * self.overtime_hours * 1.5

    def total_pay_calculator(self):
        """Calculates the total job's income in total."""
        return self.basic_pay_calculator() + self.overtime_pay_calculator()