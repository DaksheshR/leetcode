import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def bar_chart():
    data=[ 21 , 22 , 44 , 11 , 64 ]
    month=[ "jan" , "feb" , "march" , "april" , "may" ]
    colors=plt.cm.plasma(np.linspace(0,1,len(data)))
    plt.bar(month, data, color=colors)
    plt.xlabel("months")
    plt.ylabel("count")
    plt.title("comparing two discrete variables by bar chart")
    plt.show()

def histogram():
    data = np.random.randint(100, size=1000)
    plt.hist(data, bins=5, edgecolor='black')
    plt.show()

def box_plot():
    data=[87,66,78,66,44,78,56,199]
    plt.boxplot(data)
    plt.show()

def scatter_plot():
    xpoints=np.random.randint(100,size=50)
    ypoints=np.random.randint(100,size=50)
    plt.scatter(xpoints, ypoints)
    plt.show()

def pie_chart():
    month=[ "jan" , "feb" , "march" , "april" , "may" ]
    data=[ 21 , 22 , 44 , 11 , 64 ]
    plt.pie(data, labels=month, autopct='%1.1f%%')
    plt.show()
    
def sampling_dist():    
    # Simulate likes on 100 tweets
    tweets_likes = np.random.randint(0, 500, size=100)
    print("First 10 tweet likes:", tweets_likes[:10])

    # Population mean
    print("Population mean likes:", np.mean(tweets_likes))

    # Take 5 random samples of 10 tweets each and calculate sample means
    sample_means = []
    for i in range(5):
        sample = np.random.choice(tweets_likes, size=10, replace=True)
        mean = np.mean(sample)
        sample_means.append(mean)
        print(f"Sample {i+1} mean likes:", mean)

    # Mean of sample means
    print("Mean of sample means:", np.mean(sample_means))
