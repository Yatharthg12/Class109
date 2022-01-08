import random
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

diceresult = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1+dice2)

mean = sum(diceresult)/len(diceresult)
std = statistics.stdev(diceresult)
median = statistics.median(diceresult)
mode = statistics.mode(diceresult)
print(mean,std,median,mode)

firststd_start, firststd_end = mean-std, mean+std
secondstd_start, secondstd_end = mean-(2*std), mean+(2*std)

list_ofdata_inonestd = [result for result in diceresult if result > firststd_start and result < firststd_end]
print("Percentage of data lies between one std is ", len(list_ofdata_inonestd)*100.0/len(diceresult))

list_ofdata_intwostd = [result for result in diceresult if result > secondstd_start and result < secondstd_end]
print("Percentage of data lies between two std is ", len(list_ofdata_intwostd)*100.0/len(diceresult))

fig = ff.create_distplot([diceresult], ["result"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0, 0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [firststd_start,firststd_start], y = [0, 0.17], mode = "lines", name = "std 1"))
fig.add_trace(go.Scatter(x = [firststd_end,firststd_end], y = [0, 0.17], mode = "lines", name = "std 1"))
fig.add_trace(go.Scatter(x = [secondstd_start,secondstd_start], y = [0, 0.17], mode = "lines", name = "std 2"))
fig.add_trace(go.Scatter(x = [secondstd_end,secondstd_end], y = [0, 0.17], mode = "lines", name = "std 2"))
fig.show()