from SideBar import GetSideBar

class GetResult:
    def __init__(self) -> None:
        self.df, self.area, self.choice, self.address = GetSideBar().get_choice_result()

    def handle_index(self, df):
        df = df.iloc[:, 2:].sort_values('평점', ascending=False).reset_index(drop=True)
        df.index.name = "순위"
        df.index += 1
        return df

    def choice_result_df(self): 
        return self.handle_index(self.df) if self.df is not None else None

    def get_result(self): 
        return self.choice_result_df(), self.area, self.choice, self.address