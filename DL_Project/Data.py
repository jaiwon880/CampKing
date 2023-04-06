import pandas as pd

class GetData:
    def __init__(self) -> None:
        self.df_url = None
        self.df = self.load_data()

    def load_data(self) :
        # try : 
        #     return pd.read_csv(self.df_url)
        # except Exception as e : 
        #     return st.error(e)
        # pass
        return self.df_url

    def create_data(self) : 
        return self.df
        
    def result_data(self) : 
        return self.create_data()