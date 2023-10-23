# Manual to use requirements.txt and venv
## Create and activate VENV:
To create a virtual environment execute na pasta raiz do projeto o código:

```
python -m venv nome_do_ambiente
```

From this point on, you will have a virtual environment free from any libraries installed on your computer. To activate it, you need to run the following command:
* Windows (CMD):
```
cd nome_do_ambiente\Scripts
```
```
activate.bat
```

* Windows (Powershell):
```
cd nome_do_ambiente\Scripts
```
```
Activate.ps1
```
* Linux (Bash/Zsh):
```
source nome_do_ambiente/bin/activate
```
* Linux (Fish):
```
nome_do_ambiente/bin/activate.fish
```

Once the environment is activated, you should install the libraries using the following command:
```
pip install requirements.txt
```
Inside the requirements.txt file, you will find all the libraries necessary for the project's execution. To update the requirements file with the new libraries, execute:
```
pip freeze > requirements.txt
```