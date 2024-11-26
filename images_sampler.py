"""
We must sample a reasonable ammount of images from training. 10 000 will be good.
"""

import random
import os
import csv
import pandas as pd
import time

random.seed(22)

print("Starting images.py")

start = time.time()

# We must assert that ./galaxies is empty and csv does not exists
os.system("rm ./galaxies/*")
os.system("rm random_galaxies.csv")

# First we need to read from all the training set
df = pd.read_csv("./training_solutions.csv")
galaxies = df.to_dict(orient = "records")
print(f"Read {len(galaxies)} galaxies from training_solutions.csv")

# Select 10 000 random entries from the dictionary
num_galaxies = 10000
print(f"We are going to select {num_galaxies} random galaxies")
random_galaxies = random.sample(list(galaxies), num_galaxies)

# For each galaxy we copy its image in the galaxies directory
for galaxy in random_galaxies:
    id = galaxy['GalaxyID']
    # print(f"Copying {id}")
    os.system(f"cp ./images_training_rev1/{id}.jpg ./galaxies/{id}.jpg")

# We can now save the random_galaxies object
with open('random_galaxies.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, random_galaxies[0].keys())
    writer.writeheader()
    writer.writerows(random_galaxies)

end = time.time()

print(f"Sample done in {end - start:.2f} seconds")
print(f"Saved {len(random_galaxies)} images")
print("Sample finished")
