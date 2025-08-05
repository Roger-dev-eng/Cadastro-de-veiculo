import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert
import os

class ConversorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor DOC/DOCX para PDF")
        self.root.geometry("500x200")
        
        # Variáveis
        self.arquivo_origem = tk.StringVar()
        self.arquivo_destino = tk.StringVar()
        
        # Widgets
        tk.Label(root, text="Conversor de Documentos", font=('Arial', 14)).pack(pady=10)
        
        # Frame para seleção de arquivo
        frame_origem = tk.Frame(root)
        frame_origem.pack(fill='x', padx=20, pady=5)
        tk.Label(frame_origem, text="Arquivo de Origem:").pack(side='left')
        tk.Entry(frame_origem, textvariable=self.arquivo_origem, width=40).pack(side='left', padx=5)
        tk.Button(frame_origem, text="Procurar", command=self.selecionar_arquivo).pack(side='left')
        
        # Frame para destino
        frame_destino = tk.Frame(root)
        frame_destino.pack(fill='x', padx=20, pady=5)
        tk.Label(frame_destino, text="Arquivo de Destino:").pack(side='left')
        tk.Entry(frame_destino, textvariable=self.arquivo_destino, width=40).pack(side='left', padx=5)
        
        # Botão de conversão
        tk.Button(root, text="Converter para PDF", command=self.converter, bg='#4CAF50', fg='white').pack(pady=20)
        
        # Status
        self.status = tk.Label(root, text="", fg='gray')
        self.status.pack()
    
    def selecionar_arquivo(self):
        arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo DOC/DOCX",
            filetypes=[("Documentos Word", "*.doc *.docx"), ("Todos os arquivos", "*.*")]
        )
        if arquivo:
            self.arquivo_origem.set(arquivo)
            # Sugere automaticamente o nome do arquivo de destino
            caminho, extensao = os.path.splitext(arquivo)
            self.arquivo_destino.set(f"{caminho}.pdf")
            self.status.config(text="Arquivo selecionado com sucesso!", fg='green')
    
    def converter(self):
        origem = self.arquivo_origem.get()
        destino = self.arquivo_destino.get()
        
        if not origem:
            messagebox.showerror("Erro", "Por favor, selecione um arquivo de origem!")
            return
        
        try:
            self.status.config(text="Convertendo...", fg='blue')
            self.root.update()  # Atualiza a interface
            
            convert(origem, destino)
            
            self.status.config(text="Conversão concluída com sucesso!", fg='green')
            messagebox.showinfo("Sucesso", f"Arquivo convertido e salvo como:\n{destino}")
            
        except Exception as e:
            self.status.config(text="Erro na conversão", fg='red')
            messagebox.showerror("Erro", f"Ocorreu um erro na conversão:\n{str(e)}")

# Criar e rodar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorApp(root)
    root.mainloop()