import sys
import os
import venv
from typing import Union

def Write2File(text: str, file: Union[str, os.PathLike[str]]) -> None:
    try:
        with open(file, 'w') as f:
            f.write(text)
    except OSError as e:
        raise RuntimeError(f"Failed to write to file '{file}': {e}")

def main() -> None:
    if len(sys.argv) < 2:
        raise ValueError("Usage: script.py <projectName> <language> <path(OPTIONAL)>")
    
    projectName: str = sys.argv[1].strip().lower()
    langaugePrefix: str = sys.argv[2].strip().lower()
    givenProjectPath: str = sys.argv[3]

    if not projectName:
        raise AttributeError("Missing project name")
        
    if not langaugePrefix:
        raise AttributeError("Missing langauge prefix")
    
    if not givenProjectPath:
        givenProjectPath = os.path.basename(os.path.abspath(__file__))
    
    if not os.path.exists(givenProjectPath):
        raise AttributeError("Path does not exist")

    project_path = os.path.join(givenProjectPath, projectName)

    os.makedirs(project_path, exist_ok=False)
    os.chdir(project_path)

    lang: str = None

    if langaugePrefix in {"python","py"}:
        runScript = f"#!/bin/bash\n{project_path}/.venv/bin/python {project_path}/main.py"
        batScript = f"@echo off\r\n\"{project_path}\\.venv\\Scripts\\python.exe\" \"{project_path}\\main.py\""
        lang = "py"

        print("Making python venv")
        venv.EnvBuilder(with_pip=True).create(".venv")
        
        print("Making run script")
        Write2File(batScript, "run.bat")
        Write2File(runScript, "run.sh")
        
    elif langaugePrefix in {"java","jar"}:
        runScript = f"#!/bin/bash\njavac {project_path}/main.java\njava {project_path}/main.java"
        batScript = f"@echo off\r\njavac \"{project_path}\\main.java\"\r\njava \"{project_path}\\main\""

        lang = "java"

        print("Making run script")
        Write2File(batScript, "run.bat")
        Write2File(runScript, "run.sh")

    elif langaugePrefix in {"c++","cpp","cc","cxx"}:
        runScript = f"#!/bin/bash\ncd \"{project_path}\"\ng++ -o run main.cpp\n./run\nrm run"
        batScript = f"@echo off\r\ncd /d \"{project_path}\"\r\ng++ -o run.exe main.cpp\r\nrun.exe\r\ndel run.exe"

        lang = "cpp"

        print("Making run script")
        Write2File(batScript, "run.bat")
        Write2File(runScript, "run.sh")

    else:
        os.remove(project_path) if os.path.isfile(project_path) else None
        raise AttributeError("Langauge not supported")

    print("Making main file")
    with open(f"main.{lang}",'w') as x:
            pass

    print("Sucesfully made project")

if __name__ == '__main__':
    main()