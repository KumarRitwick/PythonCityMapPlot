import pandas as pd
import matplotlib.pyplot as plt

#This function will load the data from csv file
def load_data(file_path):
    return pd.read_csv(file_path)

#This function will filter the data based on requirement
#i.e. mentioned in the documnet
def filter_location(location, long_range, lat_range):
    return location[
        (location['Longitude'].between(*long_range)) &
        (location['Latitude'].between(*lat_range))
    ]

def plot_grow_data(location, map_path, output_path):
    long_range = [50.681, 57.985]
    lat_range = [-10.592, 1.6848]

    filtered_location = filter_location(location, long_range, lat_range)

def main():
    grow_location = load_data("GrowLocations.csv")
    map_path = "map7.png"
    output_path = "plots.png"

    plot_grow_data(grow_location, map_path, output_path)

if __name__ == '__main__':
    main()
