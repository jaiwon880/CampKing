from SideBar import GetSideBar
import pandas as pd
class GetResult:
    def __init__(self) -> None:
        self.sidebar = GetSideBar()
        self.df = self.sidebar.set_data()
        self.area, self.choice, self.address = self.sidebar.get_choice_result()

    def handle_index(self, df):
        if df.empty:
            columns = list(df.columns)
            df.index.name = "-"
            columns[:] = ["-"] * (len(columns))
            columns[0] = "일치 결과 없음"
            df.columns = columns
        else :
            df = df.iloc[:, 2:].sort_values('평점', ascending=False).reset_index(drop=True)
            df.index.name = "순위"
            df.index += 1
        return df

    def choice_result_df(self) : 
        return self.handle_index(self.df) if self.df is not None else None

    def get_result(self) : 
        return self.choice_result_df(), self.area, self.choice, self.address

    # 테스트 끝나면 위에 지울 것
    # def get_result(self) : return self.choice_result_df()
     # if df.empty:
        #     columns = list(df.columns)
        #     df.index.name = "-"
        #     columns[:] = ["-"] * (len(columns))
        #     columns[0] = "일치 결과 없음"
        #     df.columns = columns
        # else : pass

    # if self.df is not None :
    #     return self.handle_index(self.df)  
    # else : pass