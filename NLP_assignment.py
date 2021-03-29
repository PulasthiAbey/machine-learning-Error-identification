import os
import PySimpleGUI as sg
import os.path
import pep8

fchecker = pep8.Checker('C:/Users/Dilum Darshana/Documents/python/position.py', show_source=True)
file_errors = fchecker.check_all()
print("Found %s errors (and warnings)" % file_errors)  


file_list_column = [
    [
        sg.Text("Select the file"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=["Found %s errors (and warnings)" % file_errors], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

image_viewer_column = [
    [sg.Text("Results")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

if event == "-FOLDER-":
    folder = values["-FOLDER-"]
    try:
        # Get list of files in folder
        file_list = os.listdir(folder)
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith((".java", ".js",".py"))
    ]
    window["-FILE LIST-"].update(fnames)        

filepaths = ["C:/Users/Dilum Darshana/Documents/python/position.py"]  

for fp in filepaths:
    
    ext = os.path.splitext(fp)[-1].lower()

    if ext == ".java":
    	java()

    elif ext == ".js":
        javascript()

    elif ext == ".py":
        python()


def java():
  print("this is java file")

def javascript():
  print("this is java Script file")         
  
def python():
  print("this is python file")   
