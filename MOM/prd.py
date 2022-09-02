import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt



url = '/home/dev/Sun/akatsuki_product_file.prd'

#with open(url, "rb") as f:
#    while (byte := f.read(1)):
#    	print(byte)

#file = open(url, "rb")
#binary_data = file. read()

# Open the binary file for reading

file_handler = open(url, "rb")

# Read the first three bytes from the binary file

data_byte = file_handler.read(7)

print("Print three characters in each iteration:")

# Iterate the loop to read the remaining part of the file

while data_byte:

    print(data_byte)

    data_byte = file_handler.read(7)


# Read the entire file as a single byte string

#with open('string.bin', 'rb') as fh:

#    content = fh.read()

#print("Print the full content of the binary file:")

#print(content)
