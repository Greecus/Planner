import os
import sys
from colorama import Fore, Back, Style
import keyboard
from time import sleep

clear = lambda: os.system("cls")
write = sys.stdout.write
class TreeCell:
    __slots__ = ("_name","_sub_cells","_open","_note",'_depth')
    def __init__(self,name:str,sub_cells:list=None,note:str='',open:bool = True):
        if not name.strip(): raise ValueError('Name can\'t be empty')
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

    @property
    def depth(self):
        return self._depth
    
    @property
    def note(self):
        return self._note
    
    @property
    def name(self):
        return self._name
    
    
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
    
    def add_subcell(self,new_cell):
        if not isinstance(new_cell,TreeCell): raise TypeError("Only instances of TreeCell class can be added")
        new_cell._depth=self._depth+1
        self._sub_cells.append(new_cell)
    
    def show_branches(self)->list:
        branch_list=[self]
        if self._open and bool(self):
            for cell in self._sub_cells:
                branch_list.extend(cell.show_branches())
        return branch_list
    
    def switch_state(self):
        self._open = not self._open

def add_subcell(cell:TreeCell):
    print('Adding subsection')
    sleep(0.2)
    keyboard.press('backspace')
    while True:
        try:
            name=input('Name: ')
            note=input('Note(optional):')
            cell.add_subcell(TreeCell(name,note=note.strip()))
        except ValueError as e:
            print(e)
        else:
            break
    

def highlight(text:str)->str:
    return Fore.BLACK + Back.WHITE + text + Style.RESET_ALL
    
def project_display(visible_branch:TreeCell,selected_cell:int=0)->None:
    for id,cell in enumerate(visible_branch):
        line=cell.depth*' '+cell.name
        if id==selected_cell:
            line=highlight(line)
        print(line)
        
def display(project:TreeCell):
    selected_cell=0
    while True:
        clear()
        visible_cells=project.show_branches()
        project_display(visible_cells,selected_cell)
        sleep(0.1)
        key=None
        while not key:
            key=keyboard.read_key()
            if key not in ['up','down','esc','enter','a','n']: key=None
        if key=='up': selected_cell-=1
        elif key=='down': selected_cell+=1
        elif key=='enter': visible_cells[selected_cell].switch_state()
        elif key=='esc': break
        elif key=='a': add_subcell(visible_cells[selected_cell])
        elif key=='n':
            print(visible_cells[selected_cell].note)
            sleep(0.2)
            keyboard.read_key()
        keyboard.release(key)
        selected_cell %= len(visible_cells)



if __name__=='__main__':
    projects=[]  #get_saved_projects
    display(TreeCell('1',note='asdfg'))
