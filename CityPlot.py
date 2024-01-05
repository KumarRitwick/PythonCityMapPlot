import pandas as pd
import matplotlib.pyplot as plt

#This function will load the data from csv file
def loadData(file_path):
    return pd.read_csv(file_path)

#This function will filter the data based on requirement
#i.e. mentioned in the documnet
def filterLocation(location, long_range, lat_range):
    return location[
        (location['Longitude'].between(*long_range)) &
        (location['Latitude'].between(*lat_range))
    ]

#This function plots the Grow Data Set
#And produces an image for the results
def plotGrowDataSet(location, map_path, output_path):
    long_range = [50.681, 57.985]
    lat_range = [-10.592, 1.6848]

    filtered_location = filterLocation(location, long_range, lat_range)

    map_image = plt.imread(map_path)

    fig, ax = plt.subplots()
    ax.set_title("Plotting Grow Data")
    ax.imshow(map_image, extent=[lat_range[0], lat_range[1], long_range[0], long_range[1]])
    ax.plot(filtered_location['Latitude'], filtered_location['Longitude'], 'bo')

    plt.savefig(output_path)

def main():
    grow_location = loadData("GrowLocations.csv")
    map_path = "map7.png"
    output_path = "plots.png"

    plotGrowDataSet(grow_location, map_path, output_path)

if __name__ == '__main__':
    main()



#Reference Used:
    #https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac
