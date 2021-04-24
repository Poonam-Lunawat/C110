import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import plotly_express as px 
import pandas as pd 
import csv 
import statistics
import random

df = pd.read_csv("data.csv")
#print(df.head())

# calculating mean of dataframe
mean1 = df.mean()
print("mean by : ",+mean1)
data=df["temp"].tolist()
#mean= statistics.mean(data)
#print("mean by statistics : ",+mean)

# calculating standard deviation of dataframe
stddev= df.std()
print("Std dev : ",+stddev)
#ff.create_distplot([data],["temperature"],show_hist=False).show()

def random_set_of_mean(count):
    dataset=[]
    value=0
    for i in range (0,count): 
        random_index= random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    sample_mean = statistics.mean(dataset)
    sample_stddev= statistics.stdev(dataset)
    #print (" sample mean : ", +sample_mean ,"\n", " sample stddev : ",+sample_stddev)
    return sample_mean

def show_fig(mean_list):
    df= mean_list
    mean1= statistics.mean(mean_list)
   # fig=ff.create_distplot([df],["temperature"],show_hist=False)
    #fig.add_trace(go.Scatter(x=[mean1,mean1], y=[0,1], mode="lines", name = "MEAN"))
    #fig.show()
    stddev1 =  statistics.stdev(mean_list)
    print("mean of sample : " ,+mean1)
    print("standard deviation of samples : ",+stddev1)

def main(): 
    mean_list=[]
    for j in range(0,100): 
        set_of_means = random_set_of_mean(1000)
        mean_list.append(set_of_means)
    show_fig(mean_list)

main()


