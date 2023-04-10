from SideBar import GetSideBar
# from Data import GetData
# import numpy as np

class GetResult:
    def __init__(self) -> None:
        result_sb = GetSideBar()
        self.area, self.choice, self.address = result_sb.get_choice_result()
        self.df = result_sb.set_data()
        # self.audio = GetData().create_audio()

    def handle_df(self, df) :
        # df = df.iloc[:, 2:].sort_values('평점', ascending=False)
        # df.index = np.arange(1, len(df) + 1)
        if df is not None:
            # df = df.drop_duplicates(subset=['name'], keep='first')
            # df.sort_values(by='ranking', ascending=False, inplace=True)
            # df = df[['name', 'ranking']].reset_index(drop=True)
            # df.index.name = "순위"
            # df = df.rename(columns={'name': '업체명', 'ranking': '별점'})
            # df.index += 1
            df = (
            df.drop_duplicates(subset=['name'], keep='first')
            .sort_values(by='ranking', ascending=False)
            [['name', 'ranking']]
            .reset_index(drop=True)
            .rename(columns={'name': '업체명', 'ranking': '별점'})
            .rename_axis("순위")
            .reset_index()
            )
            
            return df
        else : return None

    def choice_result_df(self): 
        return self.handle_df(self.df) if self.df is not None else None

    def get_result(self) : return self.choice_result_df(), self.area, self.choice, self.address