import pandas as pd
import matplotlib.pyplot as plt

#This function will load the data from csv file
def load_data(file_path):
    return pd.read_csv(file_path)

def main():
    grow_location = load_data("GrowLocations.csv")


if __name__ == '__main__':
    main()
