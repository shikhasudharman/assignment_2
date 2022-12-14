# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:55:46 2022

@author: USER
"""
#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#giving the function to read the file
def read_file(filename):
    """
    

    Parameters
    ----------
    filename : csv file

    Returns
    -------
    df : dataframe with years as columns
    dftrans : dataframe with countries as columns

    """
    df = pd.read_csv(filename)
    print("standard deviation",np.std(df))
#transposing and returning the data
    dftrans= df.set_index('Country Name').transpose()
    return df, dftrans
#creating two list of countries. One for plotting the line graph and other for bar graph
Countries1 = ['Albania','Bangladesh','Canada','Germany','Sri Lanka']
Countries2 = ['Africa Western and Central','Bangladesh','Botswana','Senegal','El Salvador']
#in order to plot the bar graph, creating the function to filter the data
def filter_bar_data(df):
    df = df[['Country Name','Indicator Name','1990','1997','2000','2007','2015']]
    df = df[(df["Country Name"]=="Albania")|
            (df["Country Name"]=="Bangladesh")|
            (df["Country Name"]=="Canada")|
            (df["Country Name"]=="Germany")|
            (df["Country Name"]=="Sri Lanka")]
    return df
#in order to plot line graph, creating the function to filter the data
def filter_line_plot(df):
    df = df[['Country Name','Indicator Name','1995','2000','2005','2010','2016']]
    df = df[(df["Country Name"]==("Africa Western and Central"))|
            (df["Country Name"]==("Bangladesh"))|
            (df["Country Name"]==("Botswana"))|
            (df["Country Name"]==("Senegal"))|
            (df["Country Name"]==("El Salvador"))]
    return df
#creating the function to plot bar graph
def barplot(df,lab1,lab2):
    plt.figure(figsize=(30,20))
    dx = plt.subplot(1,1,1)
    x = np.arange(5)
    width = 0.1
    
    bar1 = dx.bar(x, df["1990"], width, label=1990)
    bar2 = dx.bar(x+width, df["1997"], width, label=1997)
    bar3 = dx.bar(x+width*2, df["2000"], width, label=2000)
    bar4 = dx.bar(x+width*3, df["2007"], width, label=2007)
    bar5 = dx.bar(x+width*4, df["2015"], width, label=2015) 
    dx.set_xlabel("Country", fontsize=30)
    dx.set_ylabel(lab1, fontsize=30)
    dx.set_title(lab2, fontsize=30)
    dx.legend(fontsize=20)
    dx.bar_label(bar1, padding=2, rotation=90, fontsize=18)
    dx.bar_label(bar2, padding=2, rotation=90, fontsize=18)
    dx.bar_label(bar3, padding=2, rotation=90, fontsize=18)
    dx.bar_label(bar4, padding=2, rotation=90, fontsize=18)
    dx.bar_label(bar5, padding=2, rotation=90, fontsize=18)
    plt.savefig("barplot.png")
    plt.show()
#creating the function to plot the line chart
def line_plot(df,lab1,lab2):
        plt.figure(figsize=(18,12))
        ss=df.set_index('Country Name')
        trans=ss.transpose()
        trans=trans.drop(index=['Indicator Name'])
        
        for i in range(len(Countries2)):
            plt.plot(trans.index,trans[Countries2[i]],label=Countries2[i])
            
        plt.title(lab2,size=25)
        plt.xlabel("Years",size=25)
        plt.ylabel(lab1,size=25)
        plt.xticks(rotation=90)
        plt.legend(fontsize=20)
        plt.savefig("lineplot.png")
        plt.show()
        
        df1,df2 = read_file("API_EG.ELC.FOSL.ZS_DS2_en_excel_v2_4687507-_1__1.csv")
        
        data = df1.set_index('Country Name')
        transpose = data.transpose()
        
        transpose = transpose.drop(index='Indicator Name')
        mean = transpose[["Albania","Bangladesh","Canada","Germany","Sri Lanka"]].mean()
        return mean
    
#bringing the csv file by displaying the path of the data with the help of functions
renew_data1,renew_data2 = read_file("API_EG.FEC.RNEW.ZS_DS2_en_excel_v2_4701085.csv")
renew_data1=filter_bar_data(renew_data1)

Electricity_data1,Electricity_data2 =read_file("API_EG.ELC.FOSL.ZS_DS2_en_excel_v2_4687507-_1__1.csv")
Electricity_data1 =filter_bar_data(Electricity_data1)

Urban_data1,Urban_data2 = read_file("API_EG.ELC.ACCS.UR.ZS_DS2_en_excel_v2_4524494 (1).csv")
Urban_data1 = filter_line_plot(Urban_data1)
Rural_data1,Rural_data2 = read_file("API_EG.ELC.ACCS.RU.ZS_DS2_en_excel_v2_4690135 (1).csv")
Rural_data1 = filter_line_plot(Rural_data1)

barplot(renew_data1,"Renewable Energy Consumption (% of total final energy consumption)","Renewable energy consumption")
barplot(Electricity_data1,"Electricity production from oil,gas and coal sources(%of total)","Electricity production from natural resources")

line_plot(Urban_data1,"Access to electricity,urban(% of urban population)","Access to electricity in urban area")
line_plot(Rural_data1,"Access to electricity,rural(% of rural population)","Access to electricity in rural area")