import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Gets the data from the CSV
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


# This calculates the Mean and standard deviation and returns them as Dataframe
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


# Plots the mean in minutes
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
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)


def plot_data(dfs, names, axs):
    # Goes through the Dataframes and plots them
    for df, name, ax in zip(dfs, names, axs.flatten(),):
        # fig, z = plt.subplots()
        convert_to_units(df)
        plot_mean(df, ax, name)
        # plt.savefig("./images/version_means/{}.png".format(name))


# Makes the subplots
# fig, axs = plt.subplots(2, 2, sharey=True)

# plot_data(
#     [JMCSR_AnyGl_RS, JMCSR_AnyGl_SS, JMCSR_Any_RS, JMCSR_Any_SS],
#     ["JMCSR_AnyGl_RS", "JMCSR_AnyGl_SS", "JMCSR_Any_RS", "JMCSR_Any_SS"],
#     axs,
# )
fig, ax = plt.subplots()
convert_to_units(JMCSR_all)
plot_mean(JMCSR_all, ax, "JMCSR_all")
# Saves the images
plt.tight_layout()
plt.savefig("./images/version_means/speedrunVersionAVGall.png")
# plt.savefig("./images/version_means/speedrunAVGVersiontime.png")
# plt.show()
