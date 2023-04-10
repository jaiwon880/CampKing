from SideBar import GetSideBar
# from Data import GetData
# import numpy as np

class GetResult:
    def __init__(self) -> None:
        result_sb = GetSideBar()
        self.area, self.choice, self.address = result_sb.get_choice_result()
        self.df = result_sb.set_data()
    #     # self.audio = GetData().create_audio()

    def handle_df(self, df) :
        # df = df.iloc[:, 2:].sort_values('평점', ascending=False)
        # df.index = np.arange(1, len(df) + 1) 
        df = df.iloc[:, 0:].drop_duplicates() 
        df = df.iloc[:, 8:].sort_values('평점', ascending=False).reset_index(drop=True)
        df.index.name = "순위"
        df.index += 1
        return df

    def choice_result_df(self): 
        return self.handle_df(self.df) if self.df is not None else None

    def get_result(self) : return self.choice_result_df(), self.area, self.choice, self.address