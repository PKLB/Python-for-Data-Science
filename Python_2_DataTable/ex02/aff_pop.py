from matplotlib import pyplot as plt
from load_csv import load

def main(path: str):
    """calls the load function from the previous exercise, loads the file
life_expectancy_years.csv, and displays the country information of your campus"""
    try:
        df = load(path)
        X = df.loc[df["country"] == "France"]
        Y = df.loc[df["country"] == "Belgium"]
        X = X.iloc[:, 1:252]
        Y = Y.iloc[:, 1:252]
        Y_pop = Y.applymap(lambda x: float(x.strip("M")))
        X_pop = X.applymap(lambda x: float(x.strip("M")))
        years = X.columns.values.astype(int)
        mask = (years >= 1800) & (years <= 2050)
        ax = plt.subplot()
        ax.set_xlabel("OoOooOoh Year")
        ax.set_ylabel("Population")
        ax.plot(years[mask], Y_pop.values[0][mask], label = "France")
        ax.plot(years[mask], X_pop.values[0][mask], label = "Belgium")
        ax.set_xticks(range(1800,2041,40))
        ax.set_yticks([20,40,60])
        ax.set_yticklabels(["20M","40M","60M"])
        plt.title("Population Projections")
        plt.show()

    except (FileNotFoundError, AssertionError, IsADirectoryError,
            OSError, PermissionError, ValueError) as bref:
        print(bref)
        return

if __name__ == "__main__":
    main("population_total.csv")
    
    
# Create a program that calls the load function from the previous exercise, loads the file
# life_expectancy_years.csv, and displays the country information of your campus. Your
# graph must have a title and a legend for each axis.