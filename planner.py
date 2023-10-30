import os
from typing import NewType

clear = lambda: os.system("cls")

class TreeCell:
    __slots__ = ("_name","_sub_cells","_open","_note",'_depth')
    def __init__(self,name:str,sub_cells:list=None,note:str='',open:bool = True):
        self._name = name
        if sub_cells:self._sub_cells=sub_cells
        else: self._sub_cells=[]
        self._open=open
        self._note=note
        self._depth=0

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
    
    @property
    def open(self):
        return self._open
    
    @open.setter
    def open(self,value):
        if not isinstance(value,bool): raise TypeError('open should be True or False')
        value=bool(value)
        self._open=value

    '''def __getitem__(self,key):
        return self._sub_cells[key]'''
    
    '''def __setitem__(self,key,value):
        self._sub_cells[key]+=value'''

    def __iadd__(self,new_cell):
        if not isinstance(new_cell,TreeCell): raise TypeError("Only instances of TreeCell class can be added")
        new_cell._depth=self._depth+1
        self._sub_cells.append(new_cell)
        return self

    def __bool__(self):
        if self._sub_cells: return True
        else: return False
    
    def __str__(self):
        return self._name
    
    def __iter__(self):
        return iter(self._sub_cells)
    
    def show_branches(self,prefix:str='  ')->list:
        branch_list=[self]
        if self._open and bool(self):
            for cell in self._sub_cells:
                branch_list.extend(cell.show_branches(prefix))
        return branch_list
    

    


if __name__=='__main__':
    a=TreeCell('1')
    print(False or bool(a))
    a+=TreeCell('2')
    a.sub_cells[0]+=TreeCell('3')
    branches=a.show_branches()
    for cell in branches:
        print(cell._depth*' '+str(cell))