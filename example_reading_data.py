import pandas
import numpy as np

columns = [
    "Particle ID",
    "org-idx",
    "mass",
    "radius",
    "x",
    "y",
    "z",
    "vx",
    "vy",
    "vz",
    "sx",
    "sy",
    "sz",
    "colour",
]

# we do not need all of these columns

data = pandas.read_csv("sample_data.bt", sep=" ", names=columns)

print(data.head())

# now you can do whatever you want with the data.

# manipulate using pandas syntax.

X = data["x"]
Y = data["y"]

print(np.std(X))
