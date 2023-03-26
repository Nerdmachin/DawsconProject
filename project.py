#My imports
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd

#Source files for the graphs
lithiumGraphSrc = pd.read_csv(".\\lithium-production.csv")
CanadianImportsSrc = pd.read_csv(".\\imports.csv")
WaterContaminationSrc=pd.read_csv(".\\number-without-safe-drinking-water.csv")

#Plot for the lithium Consumption
lithium_plot = lithiumGraphSrc[
    (lithiumGraphSrc["Entity"] == "Chile")
    &
    (lithiumGraphSrc["Year"] >= 2009)]
#Plot for Water Contamination
noSafeWaterPlot = WaterContaminationSrc[
    (WaterContaminationSrc["Entity"] == "Chile")
    &
    (WaterContaminationSrc["Year"] >= 2009)]


#Create the 1st graph + the left side Y Axis (Water Consumption)
plt.style.use("dark_background")
mpl.rcParams["axes.facecolor"] = "#271a0c"
fig, axs = plt.subplots(figsize=(11.7, 8.27))

# Add second y-axis for Lithium Production data
ax2 = axs.twinx()
lithiumGraph2 = sns.lineplot(
    data=lithium_plot,
    x="Year",
    y="Lithium Production-Reserves",
    # hue="Entity",
    ax=ax2,
    color='#cca300',
    linestyle='--')
lithiumGraph2.set(
    ylabel="Lithium Production (tons)"
)

waterGraph = sns.lineplot(
    data=noSafeWaterPlot,
    x="Year",
    y="wat_sm_number_without",
    color='#d9d9d9',
    ax=axs,
    legend=False)
waterGraph.set(
    ylabel="Amount of people without water"
)

# Add legend and titles
axs.legend(
    ["Water accesibility","Lithium Production"],
    loc="upper left")  # Add legend for Lithium Production data
waterGraph.set(title="Chile's lack of access to clean water over the years")
axs.get_legend().legend_handles[0].set_color('#d9d9d9')
# axs.get_legend().legend_handles[1].set_linestyle('--')
axs.get_legend().legend_handles[1].set_color('#cca300')

# Display plot
plt.show()

#Transform the dates into Strings
CanadianImportsSrc["REF_DATE"]=CanadianImportsSrc["REF_DATE"].astype(str)
#Splits the now String with the help of the '-' and keep only the year
CanadianImportsSrc["REF_DATE"] = CanadianImportsSrc["REF_DATE"].apply({lambda x : x.split('-')[0] })
#Changes the transformed String into a int
CanadianImportsSrc["REF_DATE"] = pd.to_numeric(CanadianImportsSrc["REF_DATE"], downcast='integer')

#Takes the values($$) of each seperate date that we seperated above and combines them into one
canImports_yearly = CanadianImportsSrc.groupby("REF_DATE").sum("VALUE")

plt.style.use("seaborn-v0_8")
fig, axs = plt.subplots()
importgraph = sns.lineplot(
    data = canImports_yearly,
    x="REF_DATE",
    y="VALUE",
)
importgraph.set(
    xlabel='Year',
    ylabel='Imports in Candian dollars ($)',
    title='Canadian imports by the years'
)
plt.show()