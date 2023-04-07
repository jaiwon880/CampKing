from ChoiceArea import GetSideBar
from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().result_data()
        self.choice, self.address = GetSideBar().result_sidebar()

    def choice_address(self) : 
        if self.choice != "" :
            return self.df[(self.df['시, 군'] == self.choice)]
        elif self.choice and self.address != "" : 
            return self.df[(self.df['시, 군'] == self.choice) & (self.df['글램핑장'].str.contains(self.address))]
        else : return None
    def result_function(self) : return self.choice_address(), self.choice, self.address