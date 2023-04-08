import pandas as pd

class GetData:
    def __init__(self):
        self.df_url = "DL_Project/Data_csv/glamping_test.csv"
        self.df = self.load_data()

    def load_data(self):
        try: 
            df = pd.read_csv(self.df_url)
            df.index += 1
            return df

        except Exception as e:
            return st.error(e)
    @st.cache
    def create_data(self) : return self.df
