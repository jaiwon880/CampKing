import pandas as pd

import pandas as pd

class GetData:
    def __init__(self):
        self.df_url = "https://raw.githubusercontent.com/cc5547/project/main/DL_Project/Data_csv/glamping_test.csv"
        self.df = self.create_data()

    def create_data(self):
        try: 
            df = pd.read_csv(self.df_url)
            df.index += 1
            return df

        except Exception as e:
            return st.error(e)

    def result_data(self):
        return self.df
