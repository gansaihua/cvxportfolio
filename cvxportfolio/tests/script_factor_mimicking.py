import os
import numpy as np
import pandas as pd
import cvxportfolio as cp


os.chdir(r'D:\develop\cvxportfolio\cvxportfolio\tests')

scores = pd.read_csv('f_scores.csv', index_col=0, parse_dates=True)
scores['cash'] = np.nan

sectors = pd.read_csv('f_sectors.csv', index_col=0, parse_dates=True)
sectors['cash'] = np.nan

returns = pd.read_csv('f_returns.csv', index_col=0, parse_dates=True)
returns['cash'] = 0

benchmark = pd.read_csv('f_benchmark.csv', index_col=0, parse_dates=True)
benchmark = benchmark.reindex(columns=returns.columns, fill_value=0)
benchmark['cash'] = 1 - benchmark.sum(axis=1)
benchmark.index += pd.Timedelta(days=1)

#############
# Part One
#############
h0 = cp.time_locator(benchmark, '2019-4-30')
policy = cp.FactorMimicking(scores, sectors, benchmark)
trades = policy.get_trades(h0, '2019-4-30')

#############
# Part Two
#############
# simulator = cp.MarketSimulator(returns, [])
# policy = cp.FactorMimicking(scores, sectors, benchmark)
# result = simulator.run_backtest(benchmark.iloc[0], '2019-4-30', '2019-5-31', policy)

# policy2 = cp.Hold()
# result2 = simulator.run_backtest(benchmark.iloc[0], '2019-4-30', '2019-5-31', policy2)
