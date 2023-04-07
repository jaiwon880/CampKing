from ChoiceArea import GetSideBar
from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().result_data()
        self.area, self.choice, self.address = GetSideBar().result_sidebar()

    def choice_address(self) : 
        if self.choice != None and "" : return self.plus_index(self.df[self.df['시, 군'] == self.choice].reset_index(drop=True))
        elif self.address != None : return self.plus_index(self.df[(self.df['시, 군'] == self.choice) & (self.df['글램핑장'].str.contains(self.address))].reset_index(drop=True))
        else : return None

    def plus_index(self, result) :
        if result != None : result.index += 1
        else : result = ""
        return result
    
    def result_function(self) : return self.choice_address(), self.area, self.choice, self.address

    # 테스트 끝나면 위에 지울 것 
    # def result_function(self) : return self.choice_address()