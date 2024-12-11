import pandas as pd

myData= {
    "Cars" :["BMW","Porsche", "McLaren","Pagani","Ford","Lamborghini","Ferari","KTM"],
    "Top Speed":[290,260,375,375,350,300,300,255],
    "Price $" :["600,000","500,000","1.2M","2M","30,000","1.5M","1.5M","1.3M"]
}

myDataFrame =pd.DataFrame(myData)

print(myDataFrame)
print()

print(myDataFrame.head(2))
print()
print(myDataFrame.tail(2))
print()
print(myDataFrame.loc[2]) 