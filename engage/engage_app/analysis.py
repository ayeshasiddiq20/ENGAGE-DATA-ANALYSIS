import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO


def duplicates(df):
    duplicate_df = df[df.duplicated()]
    print("Number of Duplicate rows : ", duplicate_df.shape)
    print(df.count())
    df = df.drop_duplicates()
    return df


def missing(df):
    print('Number of null values in the dataset:\n', df.isnull().sum())
    df = df.dropna()
    print(df.count())
    return df


df = pd.read_csv(r"C:\Users\ayesh\OneDrive\Desktop\A123\engage\engage\data[1].csv")

df = df.drop(
    ["Market Category", "Number of Doors", "Vehicle Size"], axis=1)
df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission",
                        "Driven_Wheels": "Drive Mode", "highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price", "Engine Fuel Type": "Fuel"})

df = duplicates(df)
df = missing(df)


def hist():
    fig = plt.figure()
    df.hist(figsize=(10,10))
    return fig


def val_counts():
    fig =  plt.figure(figsize=(10, 10))
    df.Make.value_counts().nlargest(40).plot(
        kind='bar', figsize=(10, 5), color="purple")
    plt.title("Number of Cars by Make")
    plt.ylabel("Number of Cars")
    plt.xlabel("Make")
    return fig


def top_ten():
    print('TOP 10 CARS MANUFACTURE !')
    top_ten = df.groupby("Make").size().sort_values(ascending=False).head(10)
    top_ten_df = pd.DataFrame(top_ten.reset_index(name="Count"))

    fig =  plt.figure(figsize=(10, 10))
    sns.barplot(x='Make', y='Count', data=top_ten_df)
    plt.title('Top 10 car makers')
    plt.ylabel('Number of cars')
    plt.xticks(rotation=90)
    return fig


def year_plot():
    print('Cars produced over the years')
    fig = plt.figure(figsize=(10, 5))
    cars_prod_df = pd.DataFrame(
        df.groupby("Year")
        .size()
        .reset_index(name="Count")
    )

    plt.bar(cars_prod_df['Year'], cars_prod_df['Count'])
    plt.title('Cars production over the years')
    plt.xticks(rotation=90)
    plt.xlabel('Year')
    plt.ylabel('Count')
    return fig


def fuel_type():
    print('Fuel types per Year')
    fig = plt.figure(figsize=(10, 5))
    fueldf = df[(df['Year'] > 2007) & (df['Year'] < 2017)].copy()
    ax = sns.countplot(x="Year", hue="Fuel", data=fueldf)
    return fig




def scatter_plots():
    print('Scatterplot')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['HP'], df['Price'])
    ax.set_xlabel('HP')
    ax.set_ylabel('Price')

    return fig
    # sns.relplot(data=df,x="HP",y="Price",hue="Popularity")


def violin():
    print('voilin-plot')
    sns.violinplot(data=df)
    sns.violinplot(data=df, x="Popularity", y="Vehicle Style")

   

def cat():
    print('Cat-Plot')
    fig = plt.figure()
    sns.catplot(data=df,
                x="Vehicle Style",
                y="Year",
                kind="strip",
                aspect=4)
    plt.xticks(rotation=90)
    sns.set(rc={'figure.figsize':(15,10)})
    return fig
  


def heat_map():
    print('Heatmaps')
    plt.figure(figsize=(15, 5))
    c = df.corr()
    sns.heatmap(c, cmap="YlGnBu_r", annot=True)
    print(c)



def diesel_car():
    print('Has use of diesel cars increased or decresed over the years?')
    fig = plt.figure(figsize=(10, 5))
    diesel_df = df[df['Fuel'].str.contains('diesel')].copy()
    sns.countplot(x="Year", hue="Fuel", data=diesel_df)
    return fig


def suv_year():
    print('Has production of SUVs increased over the years?')
    vs_df = df[df['Vehicle Style'].str.contains('SUV')].groupby(
        ['Year', 'Vehicle Style']).size().reset_index(name="Count")
    df_pivot = pd.pivot_table(
        vs_df,
        values="Count",
        index="Year",
        columns="Vehicle Style",
        aggfunc=np.mean
    )

    df_pivot.plot(kind="bar", figsize=(20, 7))


def brand_car():
    print('Which brand is least popular and which one is most popular?')
    fig = plt.figure()
    popcars_df = df[['Make', 'Popularity']].sort_values('Popularity')
    popcars_df = popcars_df.drop_duplicates()
    popcars_df.plot(kind="bar", x="Make", figsize=(20, 10), color="green")


def outliers():
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)

    IQR = Q3 - Q1
    print(IQR)





def data_preprop():
    df = df.drop(
        ["Market Category", "Number of Doors", "Vehicle Size"], axis=1)
    df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission",
                   "Driven_Wheels": "Drive Mode", "highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price", "Engine Fuel Type": "Fuel"})

    print('\n', '*'*50)
    df = duplicates(df)

    print('\n', '*'*50)
    df = missing(df)

    return df


def plots(df):
    print('\n', '*'*50)
   
    hist(df)
    print('\n', '*'*50)
    val_counts(df)
    print('\n', '*'*50)
    top_ten(df)
    print('\n', '*'*50)
    year_plot(df)
    print('\n', '*'*50)
    fuel_type(df)
    print('\n', '*'*50)
    
    scatter_plots(df)
    print('\n', '*'*50)
    violin(df)
    print('\n', '*'*50)
    cat(df)
    print('\n', '*'*50)
    heat_map(df)
    print('\n', '*'*50)
    diesel_car(df)
    print('\n', '*'*50)
    suv_year(df)
    print('\n', '*'*50)
    brand_car(df)
    print('\n', '*'*50)


# def data_read():
#     df = pd.read_csv("data[1].csv")

#     print(df.head(5))
#     print(df.tail(5))
#     data_preprop(df)


# data_read()
