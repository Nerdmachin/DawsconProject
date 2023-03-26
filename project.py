#My imports
import matplotlib.pyplot as plt
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
plt.style.use("seaborn-v0_8-bright")
fig, axs = plt.subplots()
lithiumGraph = sns.lineplot(
    data=lithium_plot,
    x="Year",
    y="Lithium Production-Reserves",
    hue="Entity",
    ax=axs,
    color='white')
lithiumGraph.set(
    title="Graph representing lithium production and water contamination over the years",
    ylabel="Amount of people without access to water")

# Add second y-axis for Lithium Production data
ax2 = axs.twinx()
lithiumGraph2 = sns.lineplot(
    data=lithium_plot,
    x="Year",
    y="Lithium Production-Reserves",
    # hue="Entity",
    ax=ax2,
    color='green',
    linestyle='--')
lithiumGraph2.set(
    ylabel="Lithium Production (tons)"
)

waterGraph = sns.lineplot(
    data=noSafeWaterPlot,
    x="Year",
    y="wat_sm_number_without",
    color='red',
    ax=axs,
    legend=False)

# Add legend and titles
axs.legend(
    ["Water accesibility","Lithium Production"],
    loc="upper left")  # Add legend for Lithium Production data
waterGraph.set(title="Chile's lack of access to clean water over the years")
axs.get_legend().legend_handles[0].set_color('red')
axs.get_legend().legend_handles[1].set_linestyle('--')
axs.get_legend().legend_handles[1].set_color('green')

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