# import pandas
import pandas as pd

#create a dataframe for the provided data
fruit_sales = pd.DataFrame({"Apples": [35, 41], "Bananas": [21, 34]},
                            index = ["2017 Sales", "2018 Sales"])

fruit_sales.to_csv("fruit.csv")