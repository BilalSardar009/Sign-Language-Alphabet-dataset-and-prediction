import os
  
labels = ["j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  
for items in labels:
    os.mkdir("Data/"+items.upper())
