import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

JMCSR_AnyGl_RS, JMCSR_AnyGl_SS, JMCSR_Any_RS, JMCSR_Any_SS = (
    pd.read_csv("./data/combined/JMCSR_AnyGl_RS.csv"),
    pd.read_csv("./data/combined/JMCSR_AnyGl_SS.csv"),
    pd.read_csv("./data/combined/JMCSR_Any_RS.csv"),
    pd.read_csv("./data/combined/JMCSR_Any_SS.csv"),
)


def group_by_mean(df, group):
    return df.groupby(group)["Real time"].mean()


print(JMCSR_AnyGl_RS.info())
# print(group_by_mean(JMCSR_AnyGl_RS, "Version"))

