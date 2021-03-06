import pandas as pd 
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go 

df=pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print('population mean: ', population_mean)
print('standard deviation mean: ', std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean
#print('mean of sample: ', mean)
#print('standard deviation of sample: ', std_dev)

def show_fig(mean_list):
    df = mean_list
    mean=statistics.mean(mean_list)
    print('mean of sample distribution: ',mean)
    fig = ff.create_distplot([data],['reading_time'],show_hist=False)
    fig.add_trace(go.Scatter(x =[mean,mean],y=[0,1],mode='lines',name='MEAN'))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()

def std_deviation():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(10)
        mean_list.append(set_of_means)

    std_dev=statistics.stdev(mean_list)
    print('standard deviation of sample: ', std_dev)
std_deviation()

first_std_deviation_start, first_std_deviation_end=mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end=mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end=mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot([data],['reading score'],show_hist=False)
fig.add_trace(go.Scatter(x =[mean,mean],y=[0.17],mode='lines',name='MEAN'))

fig.add_trace(go.Scatter(x =[first_std_deviation_start,first_std_deviation_start],y=[0,0.20],mode='lines',name='STANDARD DEVIATION 1 START'))
fig.add_trace(go.Scatter(x =[first_std_deviation_end,first_std_deviation_end],y=[0,0.20],mode='lines',name='STANDARD DEVIATION 1 END'))
fig.add_trace(go.Scatter(x =[second_std_deviation_start,second_std_deviation_start],y=[0,0.20],mode='lines',name='STANDARD DEVIATION 2 START'))
fig.add_trace(go.Scatter(x =[second_std_deviation_end,second_std_deviation_end],y=[0,0.20],mode='lines',name='STANDARD DEVIATION 2 END'))
fig.show()
