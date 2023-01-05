import pandas as pd
import numpy as np

df = pd.read_csv("quechua_unimorph.tsv", header=None, sep="\t", names=["root", "word", "morphs"])
print(df)
df["suffix"] = df["word"]
df["suffix"] = df.apply(lambda x: x["suffix"].replace(x["root"], ""), axis=1)
df["suffix"] = df.apply(lambda x: " ".join(list(x["suffix"])), axis=1)
df = df.drop(columns=["morphs"], axis=1)
df = df[["word", "root", "suffix"]]
print(df)
#df.to_csv('quechua_morphemes_char.txt', header=None, index=None, sep=' ', mode='a')