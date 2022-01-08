import csv
import pandas as pd 
import statistics

df = pd.read_csv("data.csv")
heightlist = df["height"].to_list()
weightlist = df["weight"].to_list()

heightmean = statistics.mean(heightlist)
weightmean = statistics.mean(weightlist)

heightmedian = statistics.median(heightlist)
weightmeadian = statistics.median(weightlist)

heightmode = statistics.mode(heightlist)
weightmode = statistics.mode(weightlist)

heightstd = statistics.stdev(heightlist)
weightstd = statistics.stdev(weightlist)

#print(" The height mean is "heightmean,"The height median is " heightmedian, "The height mode is " heightmode, "The height std is " heightstd)

h1stdevs, h1stdeve = heightmean - heightstd, heightmean + heightstd
h2stdevs, h2stdeve = heightmean - (2*heightstd), heightmean + (2*heightstd)

w1stdevs, w1stdeve = weightmean - weightstd, weightmean + weightstd
w2stdevs, w2stdeve = weightmean - (2*weightstd), weightmean + (2*weightstd)

hldi1std = [result for result in heightlist if result>h1stdevs and result<h1stdeve]
print("Percentage of data lies between two std is ", len(heightlist)*100.0/len(heightlist))

hldi2std = [result for result in heightlist if result>h2stdevs and result<h2stdeve]
print("Percentage of data lies between two std is ", len(heightlist)*100.0/len(heightlist))

wldi1std = [result for result in weightlist if result>w1stdevs and result<w1stdeve]
print("Percentage of data lies between one std is ", len(weightlist)*100.0/len(weightlist))

wldi2std = [result for result in weightlist if result>w2stdevs and result<w2stdeve]
print("Percentage of data lies between two std is ", len(weightlist)*100.0/len(weightlist))
