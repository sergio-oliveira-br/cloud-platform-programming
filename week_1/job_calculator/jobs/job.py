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

