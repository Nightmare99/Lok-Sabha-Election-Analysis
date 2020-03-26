from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib
matplotlib.use('Agg')
import numpy as np
import seaborn as sns
from pprint import pprint
from tabulate import tabulate
from hdfs import InsecureClient
import os.path
import collections

def Home(request):
    client = InsecureClient('http://localhost:50070', user='hduser')
    if not os.path.exists('1989.csv'):
        client.download('1989.csv', '1989.csv')
    if not os.path.exists('1991.csv'):
        client.download('1991.csv', '1991.csv')
    if not os.path.exists('1996.csv'):
        client.download('1996.csv', '1996.csv')
    if not os.path.exists('1998.csv'):
        client.download('1998.csv', '1998.csv')
    if not os.path.exists('1999.csv'):
        client.download('1999.csv', '1999.csv')
    if not os.path.exists('2004.csv'):
        client.download('2004.csv', '2004.csv')
    if not os.path.exists('2009.csv'):
        client.download('2009.csv', '2009.csv')
    if not os.path.exists('2014.csv'):
        client.download('2014.csv', '2014.csv')
    if not os.path.exists('Candidate.csv'):
        client.download('Candidate.csv', 'Candidate.csv')
    return render(request, 'election/home.html')

def TamilNadu(request):
    #1989
    context = dict()
    df=pd.read_csv('1989.csv')

    y1=df[df['TERRITORY']=='TAMIL NADU']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party89=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party89.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party89[j]=y1['PARTY'][i]

    #1991
    df=pd.read_csv('1991.csv')

    y1=df[df['TERRITORY']=='TAMIL NADU']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party91=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party91.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party91[j]=y1['PARTY'][i]

    #1996
    df=pd.read_csv('1996.csv')

    y1=df[df['TERRITORY']=='TAMIL NADU']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party96=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party96.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party96[j]=y1['PARTY'][i]

    #1998
    df=pd.read_csv('1998.csv')

    y1=df[df['TERRITORY']=='TAMIL NADU']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party98=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party98.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party98[j]=y1['PARTY'][i]

    #1999
    df=pd.read_csv('1999.csv')

    y1=df[df['TERRITORY']=='TAMIL NADU']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party99=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party99.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party99[j]=y1['PARTY'][i]

    #2004
    df=pd.read_csv('2004.csv')

    y1=df[df['TERRITORY']=='TAMIL NADU']
    y1=y1[['No', '% OF TOTAL VOTES', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party04=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['% OF TOTAL VOTES'][i])
            party04.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['% OF TOTAL VOTES'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party04[j]=y1['PARTY'][i]

    final=pd.DataFrame({'Constituency': check, '1989': party89, '1991': party91, '1996': party96, '1998': party98, '1999': party99, '2004': party04})
    #print(final, '\n')
    context["final"] = final
    years=list(final.columns)
    years.remove(years[0])
    parties=pd.unique(final[years].values.ravel())
    parties.sort()
    #ADK  ADMK  BJP  CPI  CPM  DMK  INC  IND  JP  MADMK  MDMK  PMK  TMC(M)

    columns=list(parties)
    columns.insert(0, 'Year')

    ins=[]
    for i in years:
        l=[0]*len(parties)
        k=list(final[i])
        for j in k:
            for m in range(len(parties)):
                if(j==parties[m]):
                    l[m]+=1
        l.insert(0, i)
        ins.append(l)
        
    df=pd.DataFrame(ins, columns=columns)
    #print(df)
    context["df"] = df
    df.set_index('Year', inplace=True)
    df.index.name=""

    sns.set(font_scale=1.2)
    ax = sns.heatmap(df, linewidths=0.3, cmap="Blues")
    ax.xaxis.tick_top()
    plt.xticks(rotation=90)
    plt.yticks(rotation=20)
    fig = ax.get_figure()
    fig.set_size_inches(8, 10)
    fig.savefig('election/static/election/TamilNadu.png')
    #context["fig"] = fig
    #fig.close()
    return render(request, 'election/TamilNadu.html', context)

def AndhraPradesh(request):
    context = dict()
    #1989
    df=pd.read_csv('1989.csv')

    y1=df[df['TERRITORY']=='ANDHRA PRADESH']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party89=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party89.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party89[j]=y1['PARTY'][i]

    #1991
    df=pd.read_csv('1991.csv')

    y1=df[df['TERRITORY']=='ANDHRA PRADESH']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party91=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party91.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party91[j]=y1['PARTY'][i]

    #1996
    df=pd.read_csv('1996.csv')

    y1=df[df['TERRITORY']=='ANDHRA PRADESH']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party96=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party96.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party96[j]=y1['PARTY'][i]

    #1998
    df=pd.read_csv('1998.csv')

    y1=df[df['TERRITORY']=='ANDHRA PRADESH']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party98=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party98.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party98[j]=y1['PARTY'][i]

    #1999
    df=pd.read_csv('1999.csv')

    y1=df[df['TERRITORY']=='ANDHRA PRADESH']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party99=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party99.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party99[j]=y1['PARTY'][i]

    #2004
    df=pd.read_csv('2004.csv')

    y1=df[df['TERRITORY']=='ANDHRA PRADESH']
    y1=y1[['No', '% OF TOTAL VOTES', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party04=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['% OF TOTAL VOTES'][i])
            party04.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['% OF TOTAL VOTES'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party04[j]=y1['PARTY'][i]

    final=pd.DataFrame({'Constituency': check, '1989': party89, '1991': party91, '1996': party96, '1998': party98, '1999': party99, '2004': party04})
    #print(final, '\n')
    context["final"] = final

    years=list(final.columns)
    years.remove(years[0])
    parties=pd.unique(final[years].values.ravel())
    parties.sort()

    columns=list(parties)
    columns.insert(0, 'Year')

    ins=[]
    for i in years:
        l=[0]*len(parties)
        k=list(final[i])
        for j in k:
            for m in range(len(parties)):
                if(j==parties[m]):
                    l[m]+=1
        l.insert(0, i)
        ins.append(l)
        
    df=pd.DataFrame(ins, columns=columns)
    #print(df)
    context["df"] = df
    df.set_index('Year', inplace=True)
    df.index.name=""

    sns.set(font_scale=1.2)
    ax = sns.heatmap(df, linewidths=0.3, cmap="Blues")
    ax.xaxis.tick_top()
    plt.xticks(rotation=90)
    plt.yticks(rotation=20)
    fig = ax.get_figure()
    fig.set_size_inches(8, 10)
    fig.savefig('election/static/election/AndhraPradesh.png')
    return render(request, 'election/AndhraPradesh.html', context)

def Kerala(request):
    context = dict()
    #1989
    df=pd.read_csv('1989.csv')

    y1=df[df['TERRITORY']=='KERALA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party89=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party89.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party89[j]=y1['PARTY'][i]

    #1991
    df=pd.read_csv('1991.csv')

    y1=df[df['TERRITORY']=='KERALA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party91=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party91.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party91[j]=y1['PARTY'][i]

    #1996
    df=pd.read_csv('1996.csv')

    y1=df[df['TERRITORY']=='KERALA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party96=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party96.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party96[j]=y1['PARTY'][i]

    #1998
    df=pd.read_csv('1998.csv')

    y1=df[df['TERRITORY']=='KERALA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party98=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party98.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party98[j]=y1['PARTY'][i]

    #1999
    df=pd.read_csv('1999.csv')

    y1=df[df['TERRITORY']=='KERALA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party99=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party99.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party99[j]=y1['PARTY'][i]

    #2004
    df=pd.read_csv('2004.csv')

    y1=df[df['TERRITORY']=='KERALA']
    y1=y1[['No', '% OF TOTAL VOTES', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party04=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['% OF TOTAL VOTES'][i])
            party04.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['% OF TOTAL VOTES'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party04[j]=y1['PARTY'][i]

    final=pd.DataFrame({'Constituency': check, '1989': party89, '1991': party91, '1996': party96, '1998': party98, '1999': party99, '2004': party04})
    #print(final, '\n')
    context["final"] = final

    years=list(final.columns)
    years.remove(years[0])
    parties=pd.unique(final[years].values.ravel())
    parties.sort()

    columns=list(parties)
    columns.insert(0, 'Year')

    ins=[]
    for i in years:
        l=[0]*len(parties)
        k=list(final[i])
        for j in k:
            for m in range(len(parties)):
                if(j==parties[m]):
                    l[m]+=1
        l.insert(0, i)
        ins.append(l)
        
    df=pd.DataFrame(ins, columns=columns)
    #print(df)
    context["df"] = df
    df.set_index('Year', inplace=True)
    df.index.name=""

    sns.set(font_scale=1.2)
    ax = sns.heatmap(df, linewidths=0.3, cmap="Blues")
    ax.xaxis.tick_top()
    plt.xticks(rotation=90)
    plt.yticks(rotation=20)
    fig = ax.get_figure()
    fig.set_size_inches(8, 10)
    fig.savefig('election/static/election/Kerala.png')
    return render(request, 'election/Kerala.html', context)

def Karnataka(request):
    context = dict()
    #1989
    df=pd.read_csv('1989.csv')

    y1=df[df['TERRITORY']=='KARNATAKA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party89=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party89.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party89[j]=y1['PARTY'][i]

    #1991
    df=pd.read_csv('1991.csv')

    y1=df[df['TERRITORY']=='KARNATAKA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party91=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party91.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party91[j]=y1['PARTY'][i]

    #1996
    df=pd.read_csv('1996.csv')

    y1=df[df['TERRITORY']=='KARNATAKA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party96=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party96.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party96[j]=y1['PARTY'][i]

    #1998
    df=pd.read_csv('1998.csv')

    y1=df[df['TERRITORY']=='KARNATAKA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party98=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party98.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party98[j]=y1['PARTY'][i]

    #1999
    df=pd.read_csv('1999.csv')

    y1=df[df['TERRITORY']=='KARNATAKA']
    y1=y1[['No.', '%', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party99=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['%'][i])
            party99.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['%'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party99[j]=y1['PARTY'][i]

    #2004
    df=pd.read_csv('2004.csv')

    y1=df[df['TERRITORY']=='KARNATAKA']
    y1=y1[['No', '% OF TOTAL VOTES', 'CONSTITUENCY', 'PARTY']]

    j=-1
    unique=list(y1.CONSTITUENCY.unique())
    check=[]
    votes_percent=[]
    party04=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            j+=1
            check.append(const)
            votes_percent.insert(j, y1['% OF TOTAL VOTES'][i])
            party04.insert(j, y1['PARTY'][i])
            
        if(const in unique and const in check):
            if(y1['% OF TOTAL VOTES'][i]>votes_percent[j]):
                votes_percent[j]=y1['%'][i]
                party04[j]=y1['PARTY'][i]

    final=pd.DataFrame({'Constituency': check, '1989': party89, '1991': party91, '1996': party96, '1998': party98, '1999': party99, '2004': party04})
    #print(final, '\n')
    context["final"] = final

    years=list(final.columns)
    years.remove(years[0])
    parties=pd.unique(final[years].values.ravel())
    parties.sort()

    columns=list(parties)
    columns.insert(0, 'Year')

    ins=[]
    for i in years:
        l=[0]*len(parties)
        k=list(final[i])
        for j in k:
            for m in range(len(parties)):
                if(j==parties[m]):
                    l[m]+=1
        l.insert(0, i)
        ins.append(l)
        
    df=pd.DataFrame(ins, columns=columns)
    #print(df)
    context["df"] = df
    df.set_index('Year', inplace=True)
    df.index.name=""

    sns.set(font_scale=1.2)
    ax = sns.heatmap(df, linewidths=0.3, cmap="Blues")
    ax.xaxis.tick_top()
    plt.xticks(rotation=90)
    plt.yticks(rotation=20)
    fig = ax.get_figure()
    fig.set_size_inches(8, 10)
    fig.savefig('election/static/election/Karnataka.png')
    return render(request, 'election/Karnataka.html', context)

def Independent(request):
    context = dict()
    ind=pd.DataFrame(columns=['CANDIDATE', '%', 'CONSTITUENCY', 'PARTY', 'STATE', 'YEAR'])
    #1989
    df=pd.read_csv('1989.csv')
    y1=df[['CANDIDATE', '%', 'CONSTITUENCY', 'PARTY', 'TERRITORY']]
    y1.sort_values(['%', 'CONSTITUENCY'], ascending=[False, True])

    unique=list(y1.CONSTITUENCY.unique())
    check=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            check.append(const)
            ind=ind.append({'CANDIDATE': y1['CANDIDATE'][i], '%': y1['%'][i], 'CONSTITUENCY': y1['CONSTITUENCY'][i], 'PARTY': y1['PARTY'][i], 'STATE': y1['TERRITORY'][i], 'YEAR': '1989'}, ignore_index=True)
            
        elif(const in unique and const in check):
            continue

    #1991        
    df=pd.read_csv('1991.csv')
    y1=df[['CANDIDATE', '%', 'CONSTITUENCY', 'PARTY', 'TERRITORY']]
    y1.sort_values(['%', 'CONSTITUENCY'], ascending=[False, True])

    unique=list(y1.CONSTITUENCY.unique())
    check=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            check.append(const)
            ind=ind.append({'CANDIDATE': y1['CANDIDATE'][i], '%': y1['%'][i], 'CONSTITUENCY': y1['CONSTITUENCY'][i], 'PARTY': y1['PARTY'][i], 'STATE': y1['TERRITORY'][i], 'YEAR': '1991'}, ignore_index=True)
            
        elif(const in unique and const in check):
            continue

    #1996
    df=pd.read_csv('1996.csv')
    y1=df[['CANDIDATE', '%', 'CONSTITUENCY', 'PARTY', 'TERRITORY']]
    y1.sort_values(['%', 'CONSTITUENCY'], ascending=[False, True])

    unique=list(y1.CONSTITUENCY.unique())
    check=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            check.append(const)
            ind=ind.append({'CANDIDATE': y1['CANDIDATE'][i], '%': y1['%'][i], 'CONSTITUENCY': y1['CONSTITUENCY'][i], 'PARTY': y1['PARTY'][i], 'STATE': y1['TERRITORY'][i], 'YEAR': '1996'}, ignore_index=True)
            
        elif(const in unique and const in check):
            continue

    #1998        
    df=pd.read_csv('1998.csv')
    y1=df[['CANDIDATE', '%', 'CONSTITUENCY', 'PARTY', 'TERRITORY']]
    y1.sort_values(['%', 'CONSTITUENCY'], ascending=[False, True])

    unique=list(y1.CONSTITUENCY.unique())
    check=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            check.append(const)
            ind=ind.append({'CANDIDATE': y1['CANDIDATE'][i], '%': y1['%'][i], 'CONSTITUENCY': y1['CONSTITUENCY'][i], 'PARTY': y1['PARTY'][i], 'STATE': y1['TERRITORY'][i], 'YEAR': '1998'}, ignore_index=True)
            
        elif(const in unique and const in check):
            continue

    #1999
    df=pd.read_csv('1999.csv')
    y1=df[['CANDIDATE', '%', 'CONSTITUENCY', 'PARTY', 'TERRITORY']]
    y1.sort_values(['%', 'CONSTITUENCY'], ascending=[False, True])

    unique=list(y1.CONSTITUENCY.unique())
    check=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            check.append(const)
            ind=ind.append({'CANDIDATE': y1['CANDIDATE'][i], '%': y1['%'][i], 'CONSTITUENCY': y1['CONSTITUENCY'][i], 'PARTY': y1['PARTY'][i], 'STATE': y1['TERRITORY'][i], 'YEAR': '1999'}, ignore_index=True)
            
        elif(const in unique and const in check):
            continue

    #2004        
    df=pd.read_csv('2004.csv')
    y1=df[['CANDIDATES', '% OF TOTAL VOTES', 'CONSTITUENCY', 'PARTY', 'TERRITORY']]
    y1.sort_values(['% OF TOTAL VOTES', 'CONSTITUENCY'], ascending=[False, True])

    unique=list(y1.CONSTITUENCY.unique())
    check=[]

    for i in y1.index:
        const=y1['CONSTITUENCY'][i]
        if(const in unique and const not in check):
            check.append(const)
            ind=ind.append({'CANDIDATE': y1['CANDIDATES'][i], '%': y1['% OF TOTAL VOTES'][i], 'CONSTITUENCY': y1['CONSTITUENCY'][i], 'PARTY': y1['PARTY'][i], 'STATE': y1['TERRITORY'][i], 'YEAR': '2004'}, ignore_index=True)
            
        elif(const in unique and const in check):
            continue

    ind=ind[ind['PARTY']=='IND']
    ind.reset_index(drop=True, inplace=True)
    #display(ind)
    context["ind"] = ind

    #SC reserved constituencies with independent candidates as winners
    sc = ind[ind['CONSTITUENCY'].str.contains("\(SC\)")]
    context["sc"] = sc

    #ST reserved constituencies with independent candidates as winners
    st = ind[ind['CONSTITUENCY'].str.contains("\(ST\)")]
    context["st"] = st

    #Overall Constituency-wise
    const = ind['CONSTITUENCY'].value_counts()
    constdf = pd.DataFrame(list(const.items()), columns=['Constituency', 'Count'])
    context["const"] = constdf

    plt.figure(figsize=(16,9))
    ind['CONSTITUENCY'].value_counts().sort_index().plot.bar()
    plt.title("Constituencies with the most number of Winning Independent candidates")
    plt.xlabel("Constituencies")
    plt.ylabel("No. of Winning Independent candidates")
    #fig = plt.get_figure()
    plt.savefig("election/static/election/Indep1.png")

    #Overall State-wise
    state = ind['STATE'].value_counts()
    statedf = pd.DataFrame(list(state.items()), columns=['State', 'Count'])
    context["state"] = statedf

    plt.figure(figsize=(16,9))
    ind['STATE'].value_counts().sort_index().plot.bar()
    plt.title("States with the most number of Winning Independent candidates")
    plt.xlabel("States")
    plt.ylabel("No. of Winning Independent candidates")
    #fig = plt.get_figure()
    plt.savefig("election/static/election/Indep2.png")

    #Overall year-wise
    year = ind['YEAR'].value_counts()
    yeardf = pd.DataFrame(list(year.items()), columns=['Year', 'Count'])
    context["year"] = yeardf

    plt.figure(figsize=(16,9))
    ind['YEAR'].value_counts().sort_index().plot.bar()
    plt.title("Year-wise most number of Winning Independent candidates")
    plt.xlabel("Years")
    plt.ylabel("No. of Winning Independent candidates")
    #fig = plt.get_figure()
    plt.savefig("election/static/election/Indep3.png")

    return render(request, "election/Independent.html", context)

def CandidateWise(request):
    context = dict()
    df=pd.read_csv('Candidate.csv')
    Candidate_Count={}

    cand=list(df['CANDIDATE'])
    const=list(df['CONSTITUENCY'])

    for name in cand:
        if name not in Candidate_Count:
            Candidate_Count[name]=1
        else:
            Candidate_Count[name]+=1

    k=list(Candidate_Count.keys())
    v=list(Candidate_Count.values())
    z=sorted(zip(k,v),key=lambda t:t[1],reverse=True)
    del (z[0])

    name=[]
    timescontested=[]

    for i in range(len(z)):
        name.append(z[i][0])
        timescontested.append(z[i][1])

    df=pd.DataFrame({"Contestant":name,"Times Contested":timescontested})
    #df=df.style.hide_index()
    #display(df)
    context["df"] = df
    
    df2=pd.read_csv('Candidate.csv')
    Candidate_ConstituencyList={}
    
    for index,row in df2.iterrows():
        candidate=row['CANDIDATE']
        if candidate in Candidate_ConstituencyList:
            if (row['YEAR'],row['CONSTITUENCY'].strip()) not in Candidate_ConstituencyList[candidate]:
                Candidate_ConstituencyList[candidate].append((row['YEAR'],row['CONSTITUENCY'].strip()))
        else:
            Candidate_ConstituencyList[candidate]=[(row['YEAR'],row['CONSTITUENCY'].strip())]

    CandidateHistory={}
    for key,value in Candidate_ConstituencyList.items():
        candi_year_const={}                                          
        for i in range(len(value)):
            year=value[i][0]
            constituency=value[i][1]
            if year not in candi_year_const:
                candi_year_const[year]=[constituency]
            else:
                candi_year_const[year].append(constituency)
        
        if (key.strip().lower()!='none of the above'):
            CandidateHistory[key.strip()]=candi_year_const

    k=CandidateHistory.keys()
    v=CandidateHistory.values()
    z=sorted(zip(k,v),key=lambda t:t[0])
    #print ("Candidates contesting in more than 5 seats in a year")
    c=[]
    ye=[]
    cons=[]
    for item in z:
        year=list(item[1].keys())
        for y in year:
            if len(item[1][y])>5:
                c.append(item[0])
                ye.append(y)
                cons.append(item[1][y])

    candCons=[]
    for i in range (len(cons)):
        for j in range (len(cons[i])):
            cons[i][j]=cons[i][j].upper()
        candCons.append(", ".join(cons[i]))

    df2 = pd.DataFrame({"Candidate":c,"Year":ye,"Constituencies":candCons})
    #df=df.style.hide_index()
    #display(df)
    context["df2"] = df2
    return render(request, "election/Candidates.html", context)

# Melon's part starts here

def f1(state,year,df):
    
    t1 = df.loc[df["TERRITORY"] == state]
    const = list(t1["CONSTITUENCY"].unique())
    
    won = 0
    tv = 0
    tvw = 0
    total_c = 0
    tp = 0
    
    for i in const:
        
        tc = df.loc[df["CONSTITUENCY"] == i]
        ti = list(tc.index)
        tv += tc["TOTAL VALID VOTES"][ti[0]]
        tf = tc.loc[tc["SEX"] == 'F']
        
        if tf.shape[0] !=0:
            total_c += 1

        for j in list(tf.index):
            
            if tf["No."][j] == 1:
                won+=1
            
            tvw += tf["VOTES"][j]
            tp += 1
    
    if(tv == 0):
        perc = 0
    else:
        perc = round(tvw/tv,2)*100
    temp = pd.DataFrame(data = [[year,won,total_c,tp,perc]] ,columns = ['year','won','contested','total_participation','% of votes'])
    return temp

def f2(state,year,df):
    
    t1 = df.loc[df["TERRITORY"] == state]
    const = list(t1["CONSTITUENCY"].unique())
    
    won = 0
    tv = 0
    tvw = 0
    total_c = 0
    tp = 0
    
    for i in const:
        
        tc = df.loc[df["CONSTITUENCY"] == i]
        ti = list(tc.index)
        tv += tc["TOTAL VOTES POLLED"][ti[0]]
        tf = tc.loc[tc["SEX"] == 'F']
        
        
        if tf.shape[0] !=0:
            total_c += 1

        for j in list(tf.index):
            
            if tf["No"][j] == 1:
                won+=1
            
            tvw += tf["TOTAL VOTES RECEIVED"][j]
            tp += 1
    
    if(tv == 0):
        perc = 0
    else:
        perc = round(tvw/tv,2)*100
    temp = pd.DataFrame(data = [[year,won,total_c,tp,perc]] ,columns = ['year','won','contested','total_participation','% of votes'])
    return temp

def func(state):
    
    df_1989 = pd.read_csv("1989.csv")
    df_1991 = pd.read_csv("1991.csv")
    df_1996 = pd.read_csv("1996.csv")
    df_1998 = pd.read_csv("1998.csv")
    df_1999 = pd.read_csv("1999.csv")
    df_2004 = pd.read_csv("2004.csv")
    df_2009 = pd.read_csv("2009.csv")
    df_2014 = pd.read_csv("2014.csv")

    temp = pd.DataFrame(columns = ['year','won','contested','total_participation','% of votes'])
    
    t1 = f1(state,1989,df_1989)
    t2 = f1(state,1991,df_1991)
    t3 = f1(state,1996,df_1996)
    t4 = f1(state,1998,df_1998)
    t5 = f1(state,1999,df_1999)
    t6 = f2(state,2004,df_2004)
    
    temp = temp.append(t1, ignore_index=True)
    temp = temp.append(t2, ignore_index=True)
    temp = temp.append(t3, ignore_index=True)
    temp = temp.append(t4, ignore_index=True)
    temp = temp.append(t5, ignore_index=True)
    temp = temp.append(t6, ignore_index=True)
    
    return temp

def Women(request):
    context = dict()
    df_1989 = pd.read_csv("1989.csv")
    states = list(df_1989["TERRITORY"].unique())
    l = dict()
    for i in states:
        temp = func(i)
        l[i] = temp
    context['women'] = l
    return render(request, "election/Women.html", context)

class c:
    
    name = ''
    margin = 0
    
    def __init__(self,name,margin):
        self.name = name
        self.margin = margin

def print_dict(year,d):
    count = 0
    df = pd.DataFrame(columns=['constituency', 'votes'])

    for i in d.keys():
        df = df.append({"constituency" : i, "votes" : d[i]},ignore_index=True)
        count+=1
        if(count==5):
            break
    return df

def print_max(year,d):
    l1 = list(d.keys())
    l1 = l1[-5:][::-1]

    df = pd.DataFrame(columns=['constituency', 'votes'])
    for i in l1:
        df = df.append({"constituency" : i, "votes" : d[i]},ignore_index=True)
    return df

def Misc(request):
    context = dict()
    df_1989 = pd.read_csv("1989.csv")
    df_1991 = pd.read_csv("1991.csv")
    df_1996 = pd.read_csv("1996.csv")
    df_1998 = pd.read_csv("1998.csv")
    df_1999 = pd.read_csv("1999.csv")
    df_2004 = pd.read_csv("2004.csv")
    df_2009 = pd.read_csv("2009.csv")
    df_2014 = pd.read_csv("2014.csv")
    const = list(df_2004["CONSTITUENCY"].unique())
    d_1989 = {}
    d_1991 = {}
    d_1996 = {}
    d_1998 = {}
    d_1999 = {}
    d_2004 = {}
    for i in const:
    
        t1 = df_1989.loc[df_1989["CONSTITUENCY"] == i]
        t2 = df_1991.loc[df_1991["CONSTITUENCY"] == i]
        t3 = df_1996.loc[df_1996["CONSTITUENCY"] == i]
        t4 = df_1998.loc[df_1998["CONSTITUENCY"] == i]
        t5 = df_1999.loc[df_1999["CONSTITUENCY"] == i]
        t6 = df_2004.loc[df_2004["CONSTITUENCY"] == i]
        
        if t1.shape[0] != 0:
            
            v1 = t1.loc[t1["No."] == 1]
            if len(list(v1.index)) !=0:
                v1 = v1["VOTES"][v1.index[0]]
            else:
                v1 = 0
            v2 = t1.loc[t1["No."] == 2]
            if len(list(v2.index)) !=0:
                v2 = v2["VOTES"][v2.index[0]]
            else:
                v2 = 0
            d_1989[i] = abs(v1-v2)
        
        if t2.shape[0] != 0:
            
            v1 = t2.loc[t2["No."] == 1]
            if len(list(v1.index)) !=0:
                v1 = v1["VOTES"][v1.index[0]]
            else:
                v1 = 0
            v2 = t2.loc[t2["No."] == 2]
            if len(list(v2.index)) !=0:
                v2 = v2["VOTES"][v2.index[0]]
            else:
                v2 = 0
            d_1991[i] = abs(v1-v2)
        
        if t3.shape[0] != 0:
            
            v1 = t3.loc[t3["No."] == 1]
            if len(list(v1.index)) !=0:
                v1 = v1["VOTES"][v1.index[0]]
            else:
                v1 = 0
            v2 = t3.loc[t3["No."] == 2]
            if len(list(v2.index)) !=0:
                v2 = v2["VOTES"][v2.index[0]]
            else:
                v2 = 0
            d_1996[i] = abs(v1-v2)
        
        if t4.shape[0] != 0:
            
            v1 = t4.loc[t4["No."] == 1]
            if len(list(v1.index)) !=0:
                v1 = v1["VOTES"][v1.index[0]]
            else:
                v1 = 0
            v2 = t4.loc[t4["No."] == 2]
            if len(list(v2.index)) !=0:
                v2 = v2["VOTES"][v2.index[0]]
            else:
                v2 = 0
            d_1998[i] = abs(v1-v2)
        
        if t5.shape[0] != 0:
            
            v1 = t5.loc[t5["No."] == 1]
            if len(list(v1.index)) !=0:
                v1 = v1["VOTES"][v1.index[0]]
            else:
                v1 = 0
            v2 = t5.loc[t5["No."] == 2]
            if len(list(v2.index)) !=0:
                v2 = v2["VOTES"][v2.index[0]]
            else:
                v2 = 0
            d_1999[i] = abs(v1-v2)
            
        if t6.shape[0] != 0:
            
            v1 = t6.loc[t6["No"] == 1]
            v1 = v1["TOTAL VOTES RECEIVED"][v1.index[0]]
            v2 = t6.loc[t6["No"] == 2]
            v2 = v2["TOTAL VOTES RECEIVED"][v2.index[0]]
            d_2004[i] = abs(v1-v2)
    final_dict_min = dict()
    final_dict_max = dict()

    temp = print_dict(1989,d_1989)
    final_dict_min[1989] = temp
    temp = print_dict(1991,d_1989)
    final_dict_min[1991] = temp
    temp = print_dict(1996,d_1989)
    final_dict_min[1996] = temp
    temp = print_dict(1998,d_1989)
    final_dict_min[1998] = temp
    temp = print_dict(1999,d_1989)
    final_dict_min[1999] = temp
    temp = print_dict(2004,d_1989)
    final_dict_min[2004] = temp

    temp = print_max(1989,d_1989)
    final_dict_max[1989] = temp
    temp = print_max(1991,d_1989)
    final_dict_max[1991] = temp
    temp = print_max(1996,d_1989)
    final_dict_max[1996] = temp
    temp = print_max(1998,d_1989)
    final_dict_max[1998] = temp
    temp = print_max(1999,d_1989)
    final_dict_max[1999] = temp
    temp = print_max(2004,d_1989)
    final_dict_max[2004] = temp

    context['min'] = final_dict_min
    context['max'] = final_dict_max
    return render(request, "election/Misc.html", context)