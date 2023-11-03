import os
import sys
from colorama import Fore, Back, Style, just_fix_windows_console
import keyboard
from time import sleep
import pickle

try:
    from project_tree_class import TreeCell
except ModuleNotFoundError:
    from Planner.project_tree_class import TreeCell

just_fix_windows_console()

DEFAULT_FILE_NAME = 'projects.pickle'
DEFAULT_FILE_PATH = os.path.join(__file__.rsplit('\\',1)[0],DEFAULT_FILE_NAME)

clear = lambda: os.system("cls")
write = sys.stdout.write

def input_safeguard():
    for _ in range(20):
        keyboard.press('backspace')

def add_subcell(cell:TreeCell):
    print('Adding subsection')
    sleep(0.2)
    keyboard.press('backspace')
    while True:
        try:
            input_safeguard()
            name=input('Name: ')
            if name=='__quit':break
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
        visible_cells:list[TreeCell]=project.show_branches()
        project_display(visible_cells,selected_cell)
        sleep(0.1)
        key=None
        while not key:
            key=keyboard.read_key()
            if key not in ['up','down','esc','enter','a','n','r']: key=None
        if key=='up': selected_cell-=1
        elif key=='down': selected_cell+=1
        elif key=='enter': visible_cells[selected_cell].switch_state()
        elif key=='esc': break
        elif key=='a': add_subcell(visible_cells[selected_cell])
        elif key=='n':
            print(visible_cells[selected_cell].note)
            sleep(0.2)
            keyboard.read_key()
        elif key=='r':
            print('del')
            visible_cells[selected_cell].parent.sub_cells.remove(visible_cells[selected_cell])
            
        keyboard.release(key)
        selected_cell %= len(visible_cells)

def save_projects(project_to_save,file_path:str=DEFAULT_FILE_PATH):
    with open(file_path,'bw') as fh:
        pickle.dump(project_to_save,fh)

def load_projects(file_path:str=DEFAULT_FILE_PATH):
    for _ in range(2):
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
    print('File loaded')
    print('0. Create new project plan')
    for id,project in enumerate(projects):
        print(f"{id+1}. {project}")
    sleep(0.2)
    input_safeguard()
    project_id=int(input('Project id:'))
    if project_id==0:
        while True:
            print('Create project')
            try:
                input_safeguard()
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
    clear()
    print('App started')
    main()