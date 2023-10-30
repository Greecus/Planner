import os

clear = lambda: os.system("cls")

class TreeCell:
    __slots__ = ("_name","_sub_cells","_open","_note")
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
        if not isinstance(value,list): raise TypeError('sub_cells should be a list')
        for cell in value:
            if not isinstance(cell,TreeCell): raise TypeError('sub_cells should be a list of TreeCell instances or empty list')
        self._sub_cells=value
    
    def __add__(self,new_cell):
        if not isinstance(new_cell,TreeCell): raise TypeError("Only instances of TreeCell class can be added")
        self._sub_cells.append(new_cell)

    def __bool__(self):
        if self._sub_cells: return True
        else: return False
    
    def __str__(self):
        return self._name
    
    def __iter__(self):
        return iter(self._sub_cells)
    


if __name__=='__main__':
    a=TreeCell('name')
    a.sub_cells=[TreeCell('name')]
    print(bool(a))
    print(list(a))
