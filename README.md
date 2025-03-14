# Exemplos de Programação Paralela com OpenMPI

Este repositório contém exemplos simples para demonstrar conceitos básicos de programação paralela usando a biblioteca OpenMPI.

## Pré-requisitos

* OpenMPI instalado no seu sistema.

## Exemplos

### Hello World

Antes de tudo você pode instalar o OpenMPI com estes comandos:

```
sudo apt update
sudo apt install openmpi-bin openmpi-doc libopenmpi-dev
```

Este programa demonstra a inicialização básica do OpenMPI e exibe informações sobre o processo em execução.

```c
#include <mpi.h>
#include <stdio.h>

int main() {
    MPI_Init(NULL, NULL);
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    printf("Hello world (rank %d de %d workers)\n", world_rank, world_size);
    MPI_Finalize();
    return 0;
}