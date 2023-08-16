import pandas as pd
import time

data = [["hoge.rst",18,"google.com",200], 
        ["fuga.rst",23,"duckduckgo.com",200], 
        ["foo.rst",30,"mikamika.io",404]]

df = pd.DataFrame(data)
df.columns = ["rst fime name", "line", "URL", "http status"]

print(df)

print("Do you want to save this list? y/n")
if(input()=="y"):
    name = time.strftime('%Y%m%d_%H%M%S')
    df.to_csv(name+".csv")