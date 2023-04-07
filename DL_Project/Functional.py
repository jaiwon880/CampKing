from ChoiceArea import GetSideBar
from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().result_data()
        self.choice, self.address = GetSideBar().result_sidebar()

    def choice_address(self) : 
        if self.choice and self.address != "":
            pass
            # return df[df[choice] == address]

    def result_function(self) : 
        return self.df, self.choice, self.address