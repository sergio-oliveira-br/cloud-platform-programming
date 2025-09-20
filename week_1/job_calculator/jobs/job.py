# week_1/job_calculator/jobs/job.py


class Job:
    """A base class to represent the jobs."""

    def __init__(self, job_name, basic_pay_rate, basic_hours, overtime_hours):
        """Constructor to initialise a new job."""
        self.job_name = job_name
        self.basic_pay_rate = basic_pay_rate
        self.basic_hours = basic_hours
        self.overtime_hours = overtime_hours

    def calculator(self):
        """Calculates the job's income."""

        if self.basic_pay_rate < 0 or self.basic_hours < 0:
            raise ValueError("'Basic pay rate' and 'basic hours' must be greater than zero.")

        total_basic_pay = self.basic_pay_rate * self.basic_hours

        return total_basic_pay

