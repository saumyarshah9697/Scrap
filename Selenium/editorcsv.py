from tqdm import tqdm
import random

str="Mittie,Owen,39\n"
fd=open("abc2.csv","r").readlines()
for x in tqdm(range(len(fd))):
    if random.random()<=0.01:
        fd[x]=str
        



