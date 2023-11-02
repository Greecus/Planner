import os
import sys
from colorama import Fore, Back, Style
import keyboard
from time import sleep
import pickle

from project_tree_class import TreeCell

DEFAULT_FILE_PATH = os.path.join(__file__.rsplit('\\',1)[0],'projects.pickle')

clear = lambda: os.system("cls")
write = sys.stdout.write



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
        
def display_logic(project:TreeCell):
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

def save_projects(project_to_save,file_path:str=DEFAULT_FILE_PATH):
    with open(file_path,'bw') as fh:
        pickle.dump(project_to_save,fh)

def load_projects(file_path:str=DEFAULT_FILE_PATH):
    try:
        with open(file_path,'br') as fh:
            return pickle.load(fh)
    except FileNotFoundError:
        open(file_path,'x')
        return []
    except EOFError:
        return []
    
def main():
    projects=load_projects()
    print('0. Create new project plan')
    for id,project in enumerate(projects):
        print(f"{id+1}. {project}")
    project_id=int(input('Project id:'))
    if project_id==0:
        while True:
            print('Create project')
            try:
                name=input('Name: ')
                note=input('Note(optional):')
                projects.append(TreeCell(name,note=note.strip()))
            except ValueError as e:
                print(e)
            else:
                break
        display_logic(projects[-1])
    else: display_logic(projects[project_id-1])
    save_projects(projects)

if __name__=='__main__':
    main()