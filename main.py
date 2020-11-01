import random

pv = 2000
time_horizon = 30 # Years
additions = 200

pv_list = []
aggregate_returns = []
def monte_carlo(pv, time_horizon, additions):
    """
    Calculates expected returns for investment on variable interest rates.

    :param pv: Present value of investment.
    :param time_horizon: Time horizon of investment.
    :param additions: Marginal investment made by year.
    :return: Ending pv for the year.
    """
    yearly_returns = []# List of all investment returns for the time horizon
    for year in range(time_horizon):
        i = random.uniform(0.05, 0.12)
        pv = pv*(1+i) + additions # Investment return per year, with additions.
        yearly_returns.append(pv) # Adds value of investment return per year to list.
    horizon_return = yearly_returns[-1] # Final investment return at the end of the time horizion.
    return horizon_return

num_of_iter = 5000
for k in range(num_of_iter):
    horizon_return = monte_carlo(pv, time_horizon, additions)
    aggregate_returns.append(horizon_return)
avg_expected_return = sum(aggregate_returns)/num_of_iter
print(f"Your average return for the next {time_horizon} years is ${avg_expected_return}")

