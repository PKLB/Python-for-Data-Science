from matplotlib import pyplot as plt
from load_csv import load

def main(path: str):
    """calls the load function from the previous exercise, loads the file
life_expectancy_years.csv, and displays the country information of your campus"""
    try:
        df = load(path)
        # print(data.iloc[58])
        X = df.loc[df["country"] == "France"]
        Y = X.iloc[:, 10:281]
        years = Y.columns.values.astype(int)
        mask = (years > 1800) & (years < 2080)
        plt.plot(years[mask], Y.values[0][mask])
        plt.xticks(range(1800,2081,40))
        plt.yticks(range(30,100,10))
        plt.title("France Life expectancy Projections")
        plt.xlabel("OoOooOoh Year")
        plt.ylabel("Life expectancy")
        plt.show()

    except (FileNotFoundError, AssertionError, IsADirectoryError,
            OSError, PermissionError, ValueError) as bref:
        print(bref)
        return

if __name__ == "__main__":
    main("life_expectancy_years.csv")
    
    
# Create a program that calls the load function from the previous exercise, loads the file
# life_expectancy_years.csv, and displays the country information of your campus. Your
# graph must have a title and a legend for each axis.