import tkinter as tk
import sys
from tkinter import messagebox
from tkinter import ttk
from sympy import symbols, sympify, diff
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess

# Variável simbólica para funções
x = symbols('x')

global label_resultado 
global raiz
global tree 
tree = None

# Função para forçar o encerramento do programa
def fechar_programa():
    sys.exit()


# Função para atualizar as opções e os campos
def atualizar_interface(*args):
    # Limpa o frame das opções dinâmicas
    for widget in frame_opcoes.winfo_children():
        widget.destroy()
    global tree
    tree = None

    label_metodos = tk.Label(frame_opcoes, text="Métodos:")
    label_metodos.pack()    
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
            label_a = tk.Label(frame_opcoes, text="Inicio do Intervalo [a,b]:")
            label_a.pack()

            entrada_a = tk.Entry(frame_opcoes, width=40)
            entrada_a.pack(pady=5)

            label_b = tk.Label(frame_opcoes, text="Fim do Intervalo [a,b]:")
            label_b.pack()
            
            entrada_b = tk.Entry(frame_opcoes, width=40)
            entrada_b.pack(pady=5)

        elif opcao_selecionada in ["Newton-Raphson"]:
            label_a = tk.Label(frame_opcoes, text="Valor inicial (x0):")
            label_a.pack()

            entrada_a = tk.Entry(frame_opcoes, width=40)
            entrada_a.pack(pady=5)

            entrada_b = None


        elif opcao_selecionada == "Secante":
            label_a = tk.Label(frame_opcoes, text="Valor inicial (x0):")
            label_a.pack()
            entrada_a = tk.Entry(frame_opcoes, width=40)
            entrada_a.pack(pady=5)

            label_b = tk.Label(frame_opcoes, text="Valor inicial (x1):")
            label_b.pack(pady=5)
            entrada_b = tk.Entry(frame_opcoes, width=40)
            entrada_b.pack(pady=5)
            

        # Exibir botões de calcular e plotar
        botao_calcular = tk.Button(frame_opcoes, text="Calcular Zero", command=lambda: validar_calculo(entrada_funcao, entrada_a, entrada_b, entrada_tol, entrada_it))
        botao_calcular.pack(pady=10)


def validar_calculo(entrada_funcao, entrada_a, entrada_b, entrada_tol, entrada_it):
    
    funcao = entrada_funcao.get() # String do campo função
    a = entrada_a.get() # String do campo a do intervalo

    # Verificar função e intervalo
    funcao_sympy = sympify(funcao)
    f = lambda x_val: float(funcao_sympy.subs(x, x_val))
    opcao_selecionada = menu_var.get() # String do campo b do intervalo
    

    if opcao_selecionada in ["Bisseção", "Falsa Posição", "Secante"]:
        b = entrada_b.get()

        # Verificar se o intervalo contém uma raíz
        if(opcao_selecionada != "Secante"):
            if(f(float(a)) * f(float(b)) > 0):
                messagebox.showerror("Erro", "Intervalo inserido contém nenhuma raíz.")
                return
    
    else:
        b = 'None'

        # Verificar se a derivada no ponto dado é nula
        df_sympy = diff(funcao_sympy, x)
        df = lambda x_val: float(df_sympy.subs(x, x_val))
        if(df(float(a)) == 0):
                messagebox.showerror("Erro", "Derivada é nula no ponto fornecido.")
                return

    tol = entrada_tol.get() # String do campo tolerância
    it = entrada_it.get() # String do campo iteracções
    
    # Verificar se todos os campos estao preenchidos
    strings = [funcao, a, b, tol, it]
    for s in enumerate(strings, start=1):
        if not s[1]:
            messagebox.showerror("Erro", "Cálculo precisa de todos os campos para ser efetuado.")
            return
    
    if(float(tol) >= 1):
        messagebox.showerror("Erro", "Tolerância tem que ser menor que 1.")
        return
    
    if(int(it) < 0):
        messagebox.showerror("Erro", "Número de iterações não pode ser negativo.")
        return
    

    
    
    # Método escolhido
    if opcao_selecionada == "Bisseção":
        op = "1"
    elif opcao_selecionada == "Falsa Posição":
        op = "2"
    elif opcao_selecionada == "Newton-Raphson":
        op = "3"
    elif opcao_selecionada == "Secante":
        op = "4"

    gerar_tabela(funcao, a, b, tol, it, op)
    plotar_funcao(entrada_funcao)
    
    return




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
        ax.grid(True)
        ax.plot(float(raiz), 0, marker="o", markersize=4, color="red", label="Raiz Encontrada")
        ax.legend()
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao plotar função: {e}")

def gerar_tabela(funcao, a, b, tol, it, op):
    global tree
    global label_resultado
    args = [op, funcao, tol, it, a, b]

    if tree == None:
        
        label_resultado = tk.Label(frame_opcoes, text="", font=("Times New Roman", 12, "bold"))
        label_resultado.pack(pady=10)
        
        # Frame para a tabela (abaixo das opções)
        frame_tabela = tk.Frame(frame_opcoes)
        frame_tabela.pack(fill=tk.BOTH, expand=True, pady=10)

        



        if op == '1' or op == '2': # Tabela pra Bisseccao

            tree = ttk.Treeview(frame_tabela, columns=("k", "a", "b", "x", "f(x)", "e"), show="headings")
            tree.heading("k", text="K")
            tree.column("k", anchor=tk.CENTER, width=40)

            tree.heading("a", text="a")
            tree.column("a", anchor=tk.CENTER, width=90)

            tree.heading("b", text="b")
            tree.column("b", anchor=tk.CENTER, width=90)

            tree.heading("x", text="x")
            tree.column("x", anchor=tk.CENTER, width=90)

            tree.heading("f(x)", text="f(x)")
            tree.column("f(x)", anchor=tk.CENTER, width=90)

            tree.heading("e", text="Erro")
            tree.column("e", anchor=tk.CENTER, width=90)

            tree.pack(fill=tk.BOTH, expand=True)

        elif op == '3':

            tree = ttk.Treeview(frame_tabela, columns=("k", "x", "f(x)", "e"), show="headings")
            tree.heading("k", text="K")
            tree.column("k", anchor=tk.CENTER, width=10)

            tree.heading("x", text="x")
            tree.column("x", anchor=tk.CENTER, width=100)

            tree.heading("f(x)", text="f(x)")
            tree.column("f(x)", anchor=tk.CENTER, width=100)

            tree.heading("e", text="Erro")
            tree.column("e", anchor=tk.CENTER, width=100)

            tree.pack(fill=tk.BOTH, expand=True)

        elif op == '4':

            tree = ttk.Treeview(frame_tabela, columns=("k", "x1", "x2", "x", "f(x)", "e"), show="headings")
        
            tree.heading("k", text="K")
            tree.column("k", anchor=tk.CENTER, width=40)

            tree.heading("x1", text="x1")
            tree.column("x1", anchor=tk.CENTER, width=90)

            tree.heading("x2", text="x2")
            tree.column("x2", anchor=tk.CENTER, width=90)

            tree.heading("x", text="x")
            tree.column("x", anchor=tk.CENTER, width=90)
        
            tree.heading("f(x)", text="f(x)")
            tree.column("f(x)", anchor=tk.CENTER, width=90)

            tree.heading("e", text="Erro")
            tree.column("e", anchor=tk.CENTER, width=90)

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
        for linha in linhas:
            valores = linha.split('\t')  # Os valores são separados por tabulação
            tree.insert("", "end", values=valores)
      
        it_raiz = tree.item(tree.get_children()[-1])["values"][0]
        global raiz
        raiz = tree.item(tree.get_children()[-1])["values"][-3]
        erro_final = tree.item(tree.get_children()[-1])["values"][-1]
        
        label_resultado.config(text=f"Raiz: {raiz}, com erro de {erro_final} ---> Iteração {it_raiz}")
    
    except Exception as e:
        print(f"Erro ao executar o script C++: {e}")



# Interface gráfica
janela = tk.Tk()
janela.title("Calculadora Numérica de Raízes Reais")

# Frame para as opções dinâmicas (dentro da barra lateral esquerda)
frame_opcoes = tk.Frame(janela)
frame_opcoes.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)


# Menu principal
label_metodos = tk.Label(frame_opcoes, text="Métodos:")
label_metodos.pack()

menu_var = tk.StringVar(value="Escolha um método")
menu_opcoes = ["Bisseção", "Falsa Posição", "Newton-Raphson", "Secante"]
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
