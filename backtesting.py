
#%%
import matplotlib.pyplot as plt

plt.style.use("dark_background")

#%%
from vnpy_ctastrategy.backtesting import BacktestingEngine, OptimizationSetting
from datetime import datetime
from my_ma_strategy import MyMaStrategy
from pathlib import Path

#%%
Path.cwd()
engine = BacktestingEngine()
engine.set_parameters(
    vt_symbol="000001.SSE",
    interval="d",
    start=datetime(2009, 1, 1),
    end=datetime(2019, 7, 1),
    rate=3 / 10000,
    slippage=1,
    size=10,
    pricetick=1,
    capital=1_000_000,
)
#%%
engine.add_strategy(MyMaStrategy, {})

# #%%
engine.load_data()
engine.run_backtesting()
df = engine.calculate_result()
engine.calculate_statistics()
engine.show_chart()

# setting = OptimizationSetting()
# setting.set_target("sharpe_ratio")
# setting.add_parameter("rsi_window", 5, 50, 2) # 14
# setting.add_parameter("rsi_level", 5, 50, 2) # 20
# setting.add_parameter("cci_window", 5, 50, 2) # 30
# setting.add_parameter("cci_level", 5, 50, 2) # 10

# engine.run_ga_optimization(setting)