# Comandos Úteis do Docker

## 1. Gerenciamento de Containers
### Listar containers em execução
```sh
docker ps
```

### Listar todos os containers (incluindo parados)
```sh
docker ps -a
```

### Iniciar um container parado
```sh
docker start <container_id>
```

### Parar um container
```sh
docker stop <container_id>
```

### Remover um container
```sh
docker rm <container_id>
```

---

## 2. Gerenciamento de Imagens
### Listar imagens disponíveis
```sh
docker images
```

### Remover uma imagem
```sh
docker rmi <image_id>
```

### Criar uma nova imagem a partir de um Dockerfile
```sh
docker build -t nome_da_imagem .
```

---

## 3. Trabalhando com Volumes
### Listar volumes
```sh
docker volume ls
```

### Remover um volume
```sh
docker volume rm <volume_name>
```

### Criar um volume
```sh
docker volume create <volume_name>
```

---

## 4. Redes no Docker
### Listar redes disponíveis
```sh
docker network ls
```

### Criar uma nova rede
```sh
docker network create <network_name>
```

### Conectar um container a uma rede
```sh
docker network connect <network_name> <container_id>
```

---

## 5. Docker Compose
### Iniciar serviços com Docker Compose
```sh
docker-compose up -d
```

### Parar serviços
```sh
docker-compose down
```

### Ver logs de um serviço
```sh
docker-compose logs -f <service_name>
```

### Reiniciar serviços
```sh
docker-compose restart <service_name>
```

---

## 6. Execução e Depuração
### Acessar o shell de um container em execução
```sh
docker exec -it <container_id> /bin/sh
```

### Ver logs de um container
```sh
docker logs -f <container_id>
```

### Inspecionar detalhes de um container
```sh
docker inspect <container_id>
```

---

## Resumo
✅ Gerenciar containers e imagens facilmente.
✅ Trabalhar com volumes e redes.
✅ Utilizar Docker Compose para orquestração.
✅ Depurar e inspecionar containers.

Esses comandos são essenciais para o dia a dia com Docker. 🚀

