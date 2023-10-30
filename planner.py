import os

clear = lambda: os.system("cls")

class TreeCell:
    __slots__ = ("_name","_sub_cells","open","note")
    def __init__(self,name:str,sub_cells:list=None,note:str=''):
        self._name = name
        self._sub_cells=sub_cells
        self._open=False
        self._note=note

    @property
    def sub_cells(self):
        return self._sub_cells
    
    @sub_cells.setter
    def sub_cells(self,value):
        if not value: self._sub_cells=[]
        if not isinstance(value,list): raise ValueError('sub_cells should be a list')
        for cell in value:
            if not isinstance(cell,TreeCell): raise ValueError('sub_cells should be a list of TreeCell instances or empty list')
        self._sub_cells=value


if __name__=='__main__':
    a=TreeCell('name')
    a.sub_cells=[TreeCell('name')]
