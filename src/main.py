import sys
import os
import venv
import shutil

def Write2File(text: str, file: str | os.PathLike[str]) -> None:
    try:
        with open(file, 'w') as f:
            f.write(text)
    except OSError as e:
        raise RuntimeError(f"Failed to write to file '{file}': {e}")
    
def createMainFile(langSuffix: str, projectPath: str | os.PathLike[str]) -> bool:
    if os.path.exists(projectPath):
        respone: str = input("This file already exists do you want to overwrite it? [Y/n]")
        if respone == "" or respone.lower() == "y":
            shutil.rmtree(projectPath)
        elif respone.lower() == "n":
            exit()
        
    os.makedirs(projectPath, exist_ok=False)
    os.chdir(projectPath)

    language, batScript, bashScript = determineLanguage(langSuffix, projectPath)

    if language == "py": venv.EnvBuilder(with_pip=True).create(".venv")

    Write2File(batScript, "run.bat")
    Write2File(bashScript, "run")
    os.chmod("run", 0o755)

    with open(f"main.{language}",'w') as x: pass
    print(f"Sucesfully made project at \"{projectPath}\"")

    return True


def determineLanguage(language: str, projectPath: str | os.PathLike[str]) -> tuple[str, str, str]:
    """
    takes the langauge and project path and returns the language suffix, a bat script, and a bash script as strings
    """
    if language in {"python", "py"}: 
        Language: str = "py"
        batScript: str = f"@echo off\r\n\"{projectPath}\\.venv\\Scripts\\python.exe\" \"{projectPath}\\main.py\""
        bashSctipt: str = f"#!/bin/bash\n{projectPath}/.venv/bin/python {projectPath}/main.py"
        return Language, batScript, bashSctipt
    
    elif language in {"java","jar"}:
        Language: str = "java"
        batScript: str = f"@echo off\r\njavac \"{projectPath}\\main.java\"\r\njava \"{projectPath}\\main\""
        bashSctipt: str = f"#!/bin/bash\njavac {projectPath}/main.java\njava {projectPath}/main.java"
        return Language, batScript, bashSctipt
    
    elif language in {"c++","cpp","cc","cxx"}:
        Language: str = "cpp"
        batScript: str = f"@echo off\r\ncd /d \"{projectPath}\"\r\ng++ -o run.exe main.cpp\r\nrun.exe\r\ndel run.exe"
        bashSctipt: str = f"#!/bin/bash\ncd \"{projectPath}\"\ng++ -o run main.cpp\n./run\nrm run"
        return Language, batScript, bashSctipt
    
    else:
        shutil.rmtree(projectPath)
        raise AttributeError("Unsupported Langauge\nLanguage Options: Python, Java, C++")

def main() -> None:
    if len(sys.argv) < 3:
        raise ValueError("Usage: main.py <projectName> <language> <path(OPTIONAL)>\nLanguage Options: Python, Java, C++")
    
    projectName: str = sys.argv[1].strip().lower()
    langaugeSuffix: str = sys.argv[2].strip().lower()
    givenProjectPath: str = sys.argv[3] if len(sys.argv) > 3 else os.getcwd()

    createMainFile(
        langSuffix=langaugeSuffix,
        projectPath=os.path.join(givenProjectPath, projectName)
    )
    
if __name__ == '__main__':
    main()