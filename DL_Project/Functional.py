from ChoiceArea import GetSideBar

class GetResult:
    def __init__(self) -> None:
        self.choice = self.backend_function()

    def backend_function(self) : return GetSideBar().result_sidebar()

    def result_function(self) : return self.choice
