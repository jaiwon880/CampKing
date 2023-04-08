from ChoiceArea import GetSideBar

class GetResult:
    def __init__(self) -> None:
        self.sidebar = GetSideBar()
        self.df = self.sidebar.set_data()
        self.area, self.choice, self.address = self.sidebar.get_choice_result()

    def choice_address(self) : 
        if self.df is not None :
            if self.choice is not None and "" : 
                return self.handle_index(self.df[self.df['시, 군'] == self.choice])
            elif self.address is not None : 
                return self.handle_index(self.df[(self.df['시, 군'] == self.choice) & (self.df['글램핑장'].str.contains(self.address))])
            else : return None
        else : None

    def handle_index(self, data):
        data = data.iloc[:, 2:].sort_values('평점', ascending=False).reset_index(drop=True)
        data.index.name = "순위"
        data.index += 1

        if data.empty : 
            columns = list(data.columns)
            columns[-1] = "일치 결과 없음"
            columns[:-1] = ["-"] * (len(columns) - 1)
            data.index.name = "-"
            # data.columns = columns
        return data

    def get_result(self) : return self.choice_address(), self.area, self.choice, self.address

    # 테스트 끝나면 위에 지울 것
    # def get_result(self) : return self.choice_address()