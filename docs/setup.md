# Configurando Projeto Local

## Requisitos
    Docker 

## 1. Comando
### Cria container
```sh
docker-compose build
```

### Subindo container
```sh
docker-compose up
```

### Criar o container e subir aplicação
```sh
docker-compose up --build
```

### Parando aplicação
```sh
docker-compose down
```

## 2. Ambiente Virtualizado
### Crie o Ambiente Virtual
```sh
python -m venv windows_venv
```


### Ative o Ambiente Virtual
No Windows
```sh
windows_venv\Scripts\activate
```
No Mac ou Linux
```sh
source <mac/linux>_venv/bin/activate
```

### Sair

```sh
deactivate
```

## 3 Dias Uteis
### Se o VsCode não estiver encontrando os imports
1. Selecione o interpretador correto

- Abra o Command Palette (`Ctrl + Shift + P`)
- Busque por "Python: Select Interpreter"
- Escolha o interpretador correto (windows_venv/Scripts/python ou outro correspondente ao seu ambiente virtual).

2. Recarregue o VSCode

- `Ctrl + Shift + P` → Digite **"Reload Window"** → Pressione Enter