import folium
from ChoiceArea import GetSideBar
from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().result_data()
        self.choice = self.backend_function()

    def backend_function(self) : 
        return GetSideBar().result_sidebar()

    def result_function(self) : 
        return self.choice, self.df

class Map:
    def __init__(self) -> None:
        pass