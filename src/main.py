import sys
import os
import platform
import subprocess
from typing import Union

def Write2File(text: str, file: Union[str, os.PathLike[str]]):
    try:
        with open(file, 'w') as f:
            f.write(text)
    except OSError as e:
        raise RuntimeError(f"Failed to write run script: {e}")

def main():
    if platform.system().lower() != "linux":
        raise SystemError("This script was made for linux\ni am NOT bothered to try get this working on linux")

    if len(sys.argv) > 1:
        projectName = str(sys.argv[1]).strip().lower()
        langaugePrefix = str(sys.argv[2]).strip().lower()
        givenProjectPath = str(sys.argv[3])

    if not projectName:
        raise AttributeError("Missing project name")
        
    if not langaugePrefix:
        raise AttributeError("Missing langauge prefix")
    
    if not givenProjectPath:
        raise AttributeError("Missing project path")
    
    if not os.path.exists(givenProjectPath):
        raise AttributeError("Path does not exist")

    project_path = os.path.join(givenProjectPath, projectName)

    os.makedirs(project_path, exist_ok=False)
    os.chdir(project_path)

    lang:str = None

    if langaugePrefix in {"python","py"}:
        runScript = f"#!/bin/bash\n{project_path}/.venv/bin/python {project_path}/main.py"
        lang = "py"

        print("Making python venv")
        subprocess.run(['python3','-m','venv','.venv'])
        
        print("Making run script")
        subprocess.run(['touch','run.sh'])
        Write2File(runScript, "run.sh")
        
    elif langaugePrefix in {"java"}:
        runScript = f"#!/bin/bash\njavac {project_path}/main.java\njava {project_path}/main.java"
        lang = "java"

        print("Making run script")
        subprocess.run(['touch','run.sh'])
        Write2File(runScript, "run.sh")

    elif langaugePrefix in {"c++","cpp"}:
        runScript = f"#!/bin/bash\ncd \"{project_path}\"\ng++ -o run main.cpp\n./run\nrm run"
        lang = "cpp"

        print("Making run script")
        subprocess.run(['touch','run.sh'])
        Write2File(runScript, "run.sh")

    else:
        subprocess.run(["rmdir",project_path])
        raise AttributeError("Langauge not supported")

    print("Making main file")
    subprocess.run(['touch',f'main.{lang}'])

    print("Sucesfully made project")

if __name__ == '__main__':
    main()