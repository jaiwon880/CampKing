import pandas as pd

class GetData:
    def __init__(self) -> None:
        self.df_url = "https://raw.githubusercontent.com/cc5547/project/main/DL_Project/Data_csv/glamping_test.csv"
        self.df = self.load_data()

    def load_data(self) :
        try : 
            return pd.read_csv(self.df_url)
        except Exception as e : 
            return st.error(e)

    def create_data(self) : 
        self.df.index = pd.RangeIndex(start=1, stop=len(df)+1, step=1)
        return self.df
        
    def result_data(self) : 
        return self.create_data()