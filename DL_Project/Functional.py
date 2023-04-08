from ChoiceArea import GetSideBar

class GetResult:
    def __init__(self) -> None:
        self.sidebar = GetSideBar()
        self.df = self.sidebar.set_data()
        self.area, self.choice, self.address = self.sidebar.get_choice_result()

    def choice_address(self) : 
        # if self.df is not None :
        #     if self.choice is not None and "" : return self.handle_index(self.df[self.df['시, 군'] == self.choice])
        #     elif self.address is not None : return self.handle_index(self.df[(self.df['시, 군'] == self.choice) & (self.df['글램핑장'].str.contains(self.address))])
        #     else : return None
        # else : None
        # if self.df is not None : 
        #     if self.choice is not None and "" : return self.handle_index(df)
        #     elif self.address is not None and "" : return self.handle_index(self.df['글램핑장'].str.contains(self.address))
        #     else : return None
        # else :  None

        if self.df is not None : return self.handle_index(self.df)

    def handle_index(self, df):
        df = df.iloc[:, 2:].sort_values('평점', ascending=False).reset_index(drop=True)
        df.index.name = "순위"
        df.index += 1

        if df.empty : 
            columns = list(df.columns)
            df.index.name = "-"
            columns[:] = ["-"] * (len(columns))
            columns[0] = "일치 결과 없음"
            df.columns = columns
        return df

    def get_result(self) : return self.choice_address(), self.area, self.choice, self.address

    # 테스트 끝나면 위에 지울 것
    # def get_result(self) : return self.choice_address()