from ChoiceArea import GetSideBar
from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().result_data()
        self.area, self.choice, self.address = GetSideBar().result_sidebar()

    def choice_address(self) : 
        if self.choice is not None and self.choice != "" and self.address is not None :
            df_selected = self.df[(self.df['시, 군'] == self.choice) & (self.df['글램핑장'].str.contains(self.address))]
        
        elif self.choice is not None and self.choice != "" :
            df_selected = self.df[self.df['시, 군'] == self.choice]

        else:
            df_selected = None

        if df_selected is not None :
            df_selected = self.plus_index(df_selected.reset_index(drop=True))
            
        return df_selected

        # if self.choice is not None and "" : return self.plus_index(self.df[self.df['시, 군'] == self.choice].reset_index(drop=True))
        # elif self.address is not None : return self.plus_index(self.df[(self.df['시, 군'] == self.choice) & (self.df['글램핑장'].str.contains(self.address))].reset_index(drop=True))
        # else : return None

    def plus_index(self, result) :
        result = result.iloc[:, 2:].sort_values('평점', ascending=False)
        
        if result.empty : result.loc[0] = ["결과 없음"] * len(result.columns)
        else : result.index += 1
        
        return result
    
    def result_function(self) : return self.choice_address(), self.area, self.choice, self.address

    # 테스트 끝나면 위에 지울 것
    # def result_function(self) : return self.choice_address()

    