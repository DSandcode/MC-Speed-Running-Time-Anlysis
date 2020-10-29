import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

JMCSR_AnyGl_RS, JMCSR_AnyGl_SS, JMCSR_Any_RS, JMCSR_Any_SS, JMCSR_all = (
    pd.read_csv("./data/combined/JMCSR_AnyGl_RS.csv"),
    pd.read_csv("./data/combined/JMCSR_AnyGl_SS.csv"),
    pd.read_csv("./data/combined/JMCSR_Any_RS.csv"),
    pd.read_csv("./data/combined/JMCSR_Any_SS.csv"),
    pd.read_csv("./data/combined/JMCSR_all.csv"),
)

# Once the data is gotten the columns are not in the right data type so this changes them to it
def convert_to_units(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Real time"] = pd.to_timedelta(df["Real time"])
    df["In-game time"] = pd.to_timedelta(df["In-game time"])


# Make a bunch of sample data. Boolean testing and plot the means


# Test wether the difference is significant
