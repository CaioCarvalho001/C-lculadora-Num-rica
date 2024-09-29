import tkinter as tk
import sys
from tkinter import messagebox
from tkinter import ttk
from sympy import symbols, sympify, diff
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess


# Função para forçar o encerramento do programa
def fechar_programa():
    sys.exit()        # Encerra o programa


# Função para atualizar as opções e os campos
def atualizar_interface(*args):
    # Limpa o frame das opções dinâmicas
    for widget in frame_opcoes.winfo_children():
        widget.destroy()

    tabela_existe = False
    menu = ttk.Combobox(frame_opcoes, textvariable=menu_var, values=menu_opcoes)
    menu.pack(pady=10)

    opcao_selecionada = menu_var.get()

    if opcao_selecionada:
        # Exibir a entrada da função
        label_funcao = tk.Label(frame_opcoes, text="Insira a função f(x):")
        label_funcao.pack()
        entrada_funcao = tk.Entry(frame_opcoes, width=40)
        entrada_funcao.pack(pady=5)

        label_tol = tk.Label(frame_opcoes, text="Tolerância:")
        label_tol.pack()
        entrada_tol = tk.Entry(frame_opcoes, width=40)
        entrada_tol.pack(pady=5)

        label_it = tk.Label(frame_opcoes, text="Número máximo de iterações:")
        label_it.pack()
        entrada_it = tk.Entry(frame_opcoes, width=40)
        entrada_it.pack(pady=5)

        # Exibir intervalos ou valores iniciais conforme o método escolhido
        if opcao_selecionada in ["Bisseção", "Falsa Posição"]:
            label_a = tk.Label(frame_opcoes, text="Intervalo inicial (a):")
            label_a.pack()

            entrada_a = tk.Entry(frame_opcoes)
            entrada_a.pack(pady=5)

            label_b = tk.Label(frame_opcoes, text="Intervalo final (b):")
            label_b.pack()
            
            entrada_b = tk.Entry(frame_opcoes)
            entrada_b.pack(pady=5)

        elif opcao_selecionada in ["Newton-Raphson"]:
            label_a = tk.Label(frame_opcoes, text="Valor inicial (x0):")
            label_a.pack()

            entrada_a = tk.Entry(frame_opcoes)
            entrada_a.pack(pady=5)

            entrada_b = None


        elif opcao_selecionada == "Secante":
            label_a = tk.Label(frame_opcoes, text="Valor inicial (x0):")
            label_a.pack()
            entrada_a = tk.Entry(frame_opcoes)
            entrada_a.pack(pady=5)

            label_b = tk.Label(frame_opcoes, text="Valor inicial (x1):")
            label_b.pack(pady=5)
            entrada_b = tk.Entry(frame_opcoes)
            entrada_b.pack(pady=5)
            

        # Exibir botões de calcular e plotar
        botao_calcular = tk.Button(frame_opcoes, text="Calcular Zero", command=lambda: [plotar_funcao(entrada_funcao), gerar_tabela(entrada_funcao, entrada_a, entrada_b, entrada_tol, entrada_it)])
        botao_calcular.pack(pady=10)

        
# Variável simbólica para funções
x = symbols('x')

# Função para plotar a função
def plotar_funcao(entrada_funcao):
    try:
        funcao_str = entrada_funcao.get()
        funcao_sympy = sympify(funcao_str)
        f = lambda x_val: float(funcao_sympy.subs(x, x_val))

        x_vals = np.linspace(-10, 10, 400)
        y_vals = [f(val) for val in x_vals]

        ax.clear()
        ax.plot(x_vals, y_vals, label=f'f(x) = {funcao_str}', color='blue')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.legend()
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao plotar função: {e}")

def gerar_tabela(entrada_funcao, entrada_a, entrada_b, entrada_tol, entrada_it):

    opcao_selecionada = menu_var.get()
    if opcao_selecionada in ["Bisseção", "Falsa Posição", "Secante"]:
        b = entrada_b.get()
    else:
        b = '0'
    
    if opcao_selecionada == "Bisseção":
        op = "1"
    elif opcao_selecionada == "Falsa Posição":
        op = "2"
    elif opcao_selecionada == "Newton-Raphson":
        op = "3"
    elif opcao_selecionada == "Secante":
        op = "4"
    
    args = [op, entrada_funcao.get(), entrada_tol.get(), entrada_it.get(), entrada_a.get(), b]
    
   
    # Frame para a tabela (abaixo das opções)
    frame_tabela = tk.Frame(frame_opcoes)
    frame_tabela.pack(fill=tk.BOTH, expand=True, pady=10)

    # Criar a tabela (Treeview) dentro do frame de tabela
    tree = ttk.Treeview(frame_tabela, columns=("x", "f(x)"), show="headings")
    tree.heading("x", text="x")
    tree.heading("f(x)", text="f(x)")
    tree.column("x", anchor=tk.CENTER, width=100)
    tree.column("f(x)", anchor=tk.CENTER, width=100)
    tree.pack(fill=tk.BOTH, expand=True)


    

    try:
        # Executa o script C++ e captura a saída
        result = subprocess.run(['./CN.out']+ args, capture_output=True, text=True)
        output = result.stdout.strip()  # Captura a saída e remove espaços em branco extras
        
        # Limpa a tabela antes de inserir novos dados
        for row in tree.get_children():
            tree.delete(row)
        
        # Processa a saída do script C++ (quebra as linhas e colunas)
        linhas = output.split('\n')  # Cada linha da tabela
        
        # A primeira linha contém os nomes das colunas, que podemos ignorar
        for linha in linhas[1:]:
            valores = linha.split('\t')  # Os valores são separados por tabulação
            tree.insert("", "end", values=valores)
    
    except Exception as e:
        print(f"Erro ao executar o script C++: {e}")





# Interface gráfica
janela = tk.Tk()
janela.title("Calculadora Numérica de Raízes")

# Frame para as opções dinâmicas (dentro da barra lateral esquerda)
frame_opcoes = tk.Frame(janela)
frame_opcoes.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)


# Menu principal
menu_var = tk.StringVar(value="Escolha um método")
menu_opcoes = ["Bisseção", "Newton-Raphson", "Secante", "Falsa Posição"]
menu = ttk.Combobox(frame_opcoes, textvariable=menu_var, values=menu_opcoes)
menu.pack(pady=10)

# Caixas de entrada (serão exibidas dinamicamente)
entrada_funcao = tk.Entry(frame_opcoes, width=40)
entrada_a = tk.Entry(frame_opcoes)
entrada_b = tk.Entry(frame_opcoes)

# Conectando o menu com a função que atualiza as opções dinâmicas
menu_var.trace_add("write", atualizar_interface)

# Frame do gráfico
frame_grafico = tk.Frame(janela)
frame_grafico.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)



# Configurando o gráfico
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
canvas.draw()
canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

# Captura o evento de fechamento da janela e chama a função fechar_programa
janela.protocol("WM_DELETE_WINDOW", fechar_programa)

# Inicia o loop da interface
janela.mainloop()