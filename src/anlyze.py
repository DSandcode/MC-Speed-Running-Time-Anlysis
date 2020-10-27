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


def convert_to_units(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Real time"] = pd.to_timedelta(df["Real time"])
    df["In-game time"] = pd.to_timedelta(df["In-game time"])


def avg_STD_for_version(df, group):
    df["RTime"] = df["Real time"].values.astype(np.int64)
    df["IGTime"] = df["In-game time"].values.astype(np.int64)
    r_df1 = df.groupby(group).mean()
    r_df1["RTime"] = pd.to_timedelta(r_df1["RTime"])
    r_df1["IGTime"] = pd.to_timedelta(r_df1["IGTime"])
    r_df2 = df.groupby(group).std()
    r_df2["RTime"] = pd.to_timedelta(r_df2["RTime"])
    r_df2["IGTime"] = pd.to_timedelta(r_df2["IGTime"])
    return r_df1, r_df2


def plot_mean(df, ax, df_name="Mean"):
    mean_df, std_df = avg_STD_for_version(df, "Version")
    mean_df = mean_df.sort_values(by="RTime")
    ax.bar(
        list(range(len(mean_df["RTime"]))),
        mean_df["RTime"] / 60000000000,
        tick_label=mean_df.index,
    )
    ax.set_xlabel("Minecraft Version")
    ax.set_ylabel("Average Time (Min)")
    ax.set_title(df_name)
    plt.xticks(rotation="vertical")


convert_to_units(JMCSR_AnyGl_RS)
convert_to_units(JMCSR_AnyGl_SS)
convert_to_units(JMCSR_Any_RS)
convert_to_units(JMCSR_Any_SS)
for df, name in zip(
    [JMCSR_AnyGl_RS, JMCSR_AnyGl_SS, JMCSR_Any_RS, JMCSR_Any_SS],
    ["JMCSR_AnyGl_RS", "JMCSR_AnyGl_SS", "JMCSR_Any_RS", "JMCSR_Any_SS"],
):
    fig, ax_mean = plt.subplots()
    plot_mean(df, ax_mean, name)
    plt.savefig("./images/version_means/{}".format(name))
plt.show()
