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
    if len(sys.argv) < 3:
        raise ValueError("Usage: main.py <projectName> <language> <path(OPTIONAL)>\nLanguage Options: Python, Java, C++")
    
    projectName: str = sys.argv[1].strip().lower()
    langaugePrefix: str = sys.argv[2].strip().lower()
    givenProjectPath: str = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.abspath(__file__))
    
    if not os.path.exists(givenProjectPath):
        raise FileNotFoundError(f"Path does not exist {givenProjectPath}")

    project_path = os.path.join(givenProjectPath, projectName)

    os.makedirs(project_path, exist_ok=False)
    os.chdir(project_path)

    lang: str = None

    if langaugePrefix in {"python","py"}:
        runScript = f"#!/bin/bash\n{project_path}/.venv/bin/python {project_path}/main.py"
        batScript = f"@echo off\r\n\"{project_path}\\.venv\\Scripts\\python.exe\" \"{project_path}\\main.py\""
        lang = "py"

        venv.EnvBuilder(with_pip=True).create(".venv")

        Write2File(batScript, "run.bat")
        Write2File(runScript, "run.sh")
        
    elif langaugePrefix in {"java","jar"}:
        runScript = f"#!/bin/bash\njavac {project_path}/main.java\njava {project_path}/main.java"
        batScript = f"@echo off\r\njavac \"{project_path}\\main.java\"\r\njava \"{project_path}\\main\""

        lang = "java"

        Write2File(batScript, "run.bat")
        Write2File(runScript, "run.sh")

    elif langaugePrefix in {"c++","cpp","cc","cxx"}:
        runScript = f"#!/bin/bash\ncd \"{project_path}\"\ng++ -o run main.cpp\n./run\nrm run"
        batScript = f"@echo off\r\ncd /d \"{project_path}\"\r\ng++ -o run.exe main.cpp\r\nrun.exe\r\ndel run.exe"

        lang = "cpp"

        Write2File(batScript, "run.bat")
        Write2File(runScript, "run.sh")

    else:
        os.remove(project_path) if os.path.isfile(project_path) else None
        raise AttributeError("Unsupported Langauge\nLanguage Options: Python, Java, C++")

    with open(f"main.{lang}",'w') as x:
            pass

    print(f"Sucesfully made project at \"{project_path}\"")

if __name__ == '__main__':
    main()