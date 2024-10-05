# Calculadora Numérica de Raízes de Funções Reais

Este projeto é uma calculadora numérica para encontrar raízes de funções reais utilizando métodos iterativos. Ele combina uma interface gráfica em Python com `Tkinter`, cálculos simbólicos com `SymPy` e uma implementação de métodos iterativos em C++ usando a biblioteca `GiNaC`. O programa foi desenvolvido e testado no ambiente **Ubuntu**, sendo recomendado rodá-lo nessa plataforma para garantir total compatibilidade.

## Funcionalidades

- Interface gráfica para entrada de funções e parâmetros.
- Métodos iterativos para cálculo de raízes (implementados em C++ e Python).
- Visualização gráfica das funções e das raízes usando `Matplotlib`.

## Requisitos

### Dependências Python

As principais bibliotecas Python necessárias são:

- **Tkinter**: para a interface gráfica.
- **SymPy** e **NumPy**: para operações simbólicas e numéricas.
- **Matplotlib**: para geração de gráficos.
- **subprocess**: comunicação entre o código Python e o C++.

##### Instalação das dependências Python

**Opção 1: Instalação via PIP**

1. Primeiro, certifique-se de que o `PIP` está instalado:
   ```bash
   sudo apt-get install python3-pip
   ```

2. Em seguida, instale as bibliotecas Python necessárias:
   ```bash
   pip install sympy numpy matplotlib
   ```

**Opção 2: Instalação via APT** (caso não tenha o PIP disponível)

Se você preferir instalar as bibliotecas diretamente via `APT`, use os seguintes comandos:

1. Instale o **Tkinter**:
   ```bash
   sudo apt-get install python3-tk
   ```

2. Instale as demais bibliotecas:
   ```bash
   sudo apt-get install python3-numpy python3-matplotlib python3-sympy
   ```
### Dependências C++

O código C++ utiliza a biblioteca **GiNaC** para manipulação de expressões matemáticas.

##### Instalação do GiNaC:

1. **Instale o GiNaC**:
   ```bash
   sudo apt-get update
   sudo apt-get install libginac-dev
   ```

## Clonando o Repositório

Primeiro, clone o repositório do projeto para a sua máquina local:

```bash
git clone https://github.com/CaioCarvalho001/Calculadora-Numerica.git
cd calculadora-raizes
```

## Executando o Programa

O repositório já inclui um arquivo `Makefile` que facilita a execução do programa. Este arquivo irá compilar o código C++ e em seguida rodar a interface gráfica automaticamente. Para executar o programa, basta rodar o comando `make` no terminal dentro do diretório do projeto:

```bash
make
```
### Exemplo de Uso

1. Escolha o método numérico dentro os listados, ou a combinação deles.
2. Insira a função no formato aceito pelo **GiNaC** (ex: `x^2-5*x+6`).
3. Preencha os demais valores necessários para o determinado método.
4. Aperte o botão de cálculo da raiz.

---

Para mais informações sobre as bibliotecas utilizadas, consulte:

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [SymPy](https://www.sympy.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [GiNaC](http://www.ginac.de/)

## Contribuições

Contribuições são bem-vindas! Se encontrar algum bug ou tiver sugestões de melhoria, fique à vontade para abrir uma issue ou enviar um pull request.

## Autoria

Este programa foi desenvolvido em conjunto com [Pedro Lucas](https://github.com/Lucasferreira08/) e Heitor Wolf Queiroz para a disciplina de Cálculo Numérico.