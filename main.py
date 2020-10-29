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
    temp = []
    for year in range(time_horizon):
        i = random.uniform(0.05, 0.12)
        ending = pv*(1+i) + additions #10000 * 1.07 + 10000
        pv = ending
        temp.append(pv)
    horizon_return = temp[-1]
    return horizon_return

num_of_iter = 5000
for k in range(num_of_iter):
    horizon_return = monte_carlo(pv, time_horizon, additions)
    aggregate_returns.append(horizon_return)
avg_expected_return = sum(aggregate_returns)/num_of_iter
print(f"Your average return for the next {time_horizon} years is ${avg_expected_return}")

