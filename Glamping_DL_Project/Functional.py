from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().create_data()
        # self.df, self.area, self.direction = GetSideBar().choice_result_sidebar()
        # self.audio = GetData().create_audio()

    def handle_df(self, df) :
        if df is not None :
            df = df.drop_duplicates(subset=['name'], keep='first')
            df.sort_values(by='ranking', ascending=False, inplace=True)
            df = df[['name', 'ranking']].reset_index(drop=True)
            df.index.name = "순위"
            df = df.rename(columns={'name': '업체명', 'ranking': '별점'})
            df.index += 1
            return df
        else : return None

    def choice_result_df(self) : return self.handle_df(self.df) if self.df is not None else None

    def get_result(self) : return self.choice_result_df()