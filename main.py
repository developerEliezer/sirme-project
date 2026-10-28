import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# --- DADOS INICIAIS (Mock Database) ---
USUARIOS = [
    {
        "id": 1,
        "nome": "Maria Administradora",
        "email": "admin@ufr.br",
        "senha": "123",
        "tipo": "Administrador",
    },
    {
        "id": 2,
        "nome": "João Professor",
        "email": "professor@ufr.br",
        "senha": "123",
        "tipo": "Professor",
    },
    {
        "id": 3,
        "nome": "Carlos Técnico",
        "email": "tecnico@ufr.br",
        "senha": "123",
        "tipo": "TecnicoManutencao",
    },
]

EQUIPAMENTOS = [
    {
        "id": 1,
        "nome": "Projetor Epson X49",
        "categoria": "Projetor",
        "descricao": "Projetor multimídia 3300 lumens",
        "quantidade": 3,
        "estado": "Disponível",
    },
    {
        "id": 2,
        "nome": "Notebook Dell Latitude",
        "categoria": "Notebook",
        "descricao": "Core i5, 8GB RAM, SSD 256GB",
        "quantidade": 5,
        "estado": "Disponível",
    },
    {
        "id": 3,
        "nome": "Kit de Robótica LEGO",
        "categoria": "Robótica",
        "descricao": "Kit educacional Mindstorms EV3",
        "quantidade": 2,
        "estado": "Disponível",
    },
    {
        "id": 4,
        "nome": "Caixa de Som Amplificada",
        "categoria": "Áudio",
        "descricao": "Caixa portátil com microfone sem fio",
        "quantidade": 2,
        "estado": "Em manutenção",
    },
]

RESERVAS = [
    {
        "id": 1,
        "equipamento": "Projetor Epson X49",
        "solicitante": "João Professor",
        "data_inicio": "2026-10-30",
        "data_fim": "2026-10-30",
        "status": "Pendente",
    }
]

EMPRESTIMOS = []
MANUTENCOES = [
    {
        "id": 1,
        "equipamento": "Caixa de Som Amplificada",
        "descricao": "Troca de bateria e conector de energia",
        "status": "Em andamento",
    }
]

# --- CONFIGURAÇÃO DE CORES (TEMA DARK) ---
BG_DARK = "#1e1e1e"
BG_PANEL = "#2d2d2d"
BG_INPUT = "#3c3c3c"
FG_LIGHT = "#ffffff"
FG_MUTED = "#b0bec5"
ACCENT_COLOR = "#00acc1"  # Ciano / Azul moderno
ACCENT_HOVER = "#00838f"
BTN_DANGER = "#e53935"


class SIRMEApp:

  def __init__(self, root):
    self.root = root
    self.root.title(
        "SIRME - Sistema Integrado de Recursos e Materiais Extracurriculares"
    )
    self.root.geometry("1000x650")
    self.root.config(bg=BG_DARK)

    self.usuario_atual = None

    # Configuração de Estilos ttk para o Tema Dark
    self.style = ttk.Style()
    self.style.theme_use("clam")

    self.style.configure(
        "TNotebook", background=BG_DARK, borderwidth=0, tabmargins=[2, 5, 2, 0]
    )
    self.style.configure(
        "TNotebook.Tab",
        background=BG_PANEL,
        foreground=FG_LIGHT,
        padding=[15, 8],
        font=("Segoe UI", 10, "bold"),
    )
    self.style.map(
        "TNotebook.Tab",
        background=[("selected", ACCENT_COLOR)],
        foreground=[("selected", FG_LIGHT)],
    )

    self.style.configure(
        "Treeview",
        background=BG_PANEL,
        foreground=FG_LIGHT,
        fieldbackground=BG_PANEL,
        rowheight=25,
        font=("Segoe UI", 10),
    )
    self.style.configure(
        "Treeview.Heading",
        background="#333333",
        foreground=FG_LIGHT,
        font=("Segoe UI", 10, "bold"),
    )
    self.style.map(
        "Treeview", background=[("selected", ACCENT_HOVER)], foreground=[("selected", FG_LIGHT)]
    )

    # Iniciar tela de login
    self.criar_tela_login()

  def limpar_janela(self):
    for widget in self.root.winfo_children():
      widget.destroy()

  # ==========================================
  # TELA DE LOGIN
  # ==========================================
  def criar_tela_login(self):
    self.limpar_janela()

    frame_login = tk.Frame(self.root, bg=BG_PANEL, padx=40, pady=40)
    frame_login.place(relx=0.5, rely=0.5, anchor="center")

    lbl_titulo = tk.Label(
        frame_login,
        text="SIRME - Login",
        font=("Segoe UI", 18, "bold"),
        bg=BG_PANEL,
        fg=FG_LIGHT,
    )
    lbl_titulo.pack(pady=(0, 20))

    lbl_email = tk.Label(
        frame_login,
        text="E-mail institucional:",
        font=("Segoe UI", 10),
        bg=BG_PANEL,
        fg=FG_MUTED,
    )
    lbl_email.pack(anchor="w")

    self.entry_email = tk.Entry(
        frame_login,
        font=("Segoe UI", 11),
        bg=BG_INPUT,
        fg=FG_LIGHT,
        insertbackground=FG_LIGHT,
        relief="flat",
        width=30,
    )
    self.entry_email.pack(pady=(5, 15), ipady=5)
    self.entry_email.insert(0, "admin@ufr.br")  # Valor padrão para facilitar

    lbl_senha = tk.Label(
        frame_login,
        text="Senha:",
        font=("Segoe UI", 10),
        bg=BG_PANEL,
        fg=FG_MUTED,
    )
    lbl_senha.pack(anchor="w")

    self.entry_senha = tk.Entry(
        frame_login,
        font=("Segoe UI", 11),
        bg=BG_INPUT,
        fg=FG_LIGHT,
        insertbackground=FG_LIGHT,
        relief="flat",
        show="*",
        width=30,
    )
    self.entry_senha.pack(pady=(5, 20), ipady=5)
    self.entry_senha.insert(0, "123")

    btn_entrar = tk.Button(
        frame_login,
        text="Entrar",
        font=("Segoe UI", 11, "bold"),
        bg=ACCENT_COLOR,
        fg=FG_LIGHT,
        activebackground=ACCENT_HOVER,
        activeforeground=FG_LIGHT,
        relief="flat",
        cursor="hand2",
        command=self.fazer_login,
        width=20,
    )
    btn_entrar.pack(ipady=5)

    lbl_dica = tk.Label(
        frame_login,
        text=(
            "Dica: Use admin@ufr.br, professor@ufr.br ou tecnico@ufr.br (senha:"
            " 123)"
        ),
        font=("Segoe UI", 8),
        bg=BG_PANEL,
        fg=FG_MUTED,
    )
    lbl_dica.pack(pady=(15, 0))

  def fazer_login(self):
    email = self.entry_email.get()
    senha = self.entry_senha.get()

    for u in USUARIOS:
      if u["email"] == email and u["senha"] == senha:
        self.usuario_atual = u
        messagebox.showinfo(
            "Sucesso", f"Bem-vindo(a), {u['nome']} ({u['tipo']})!"
        )
        self.criar_painel_principal()
        return

    messagebox.showerror("Erro", "E-mail ou senha inválidos.")

  # ==========================================
  # PAINEL PRINCIPAL (DASHBOARD COM ABAS)
  # ==========================================
  def criar_painel_principal(self):
    self.limpar_janela()

    # Barra superior de navegação/perfil
    top_bar = tk.Frame(self.root, bg=BG_PANEL, height=50)
    top_bar.pack(side="top", fill="x")

    lbl_user = tk.Label(
        top_bar,
        text=(
            f"Usuário: {self.usuario_atual['nome']} | Perfil:"
            f" {self.usuario_atual['tipo']}"
        ),
        font=("Segoe UI", 10, "bold"),
        bg=BG_PANEL,
        fg=ACCENT_COLOR,
    )
    lbl_user.pack(side="left", padx=20)

    btn_sair = tk.Button(
        top_bar,
        text="Sair",
        font=("Segoe UI", 9),
        bg=BTN_DANGER,
        fg=FG_LIGHT,
        relief="flat",
        command=self.criar_tela_login,
    )
    btn_sair.pack(side="right", padx=20, pady=10)

    # Abas do Sistema (Notebook)
    self.notebook = ttk.Notebook(self.root)
    self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # Criando as Abas
    self.aba_equipamentos = tk.Frame(self.notebook, bg=BG_DARK)
    self.aba_reservas = tk.Frame(self.notebook, bg=BG_DARK)
    self.aba_emprestimos = tk.Frame(self.notebook, bg=BG_DARK)
    self.aba_manutencao = tk.Frame(self.notebook, bg=BG_DARK)

    self.notebook.add(self.aba_equipamentos, text="📦 Equipamentos")
    self.notebook.add(self.aba_reservas, text="📅 Reservas")
    self.notebook.add(self.aba_emprestimos, text="📋 Empréstimos")
    self.notebook.add(self.aba_manutencao, text="🔧 Manutenção")

    # Popular Abas
    self.construir_aba_equipamentos()
    self.construir_aba_reservas()
    self.construir_aba_emprestimos()
    self.construir_aba_manutencao()

  # ------------------------------------------
  # ABA 1: EQUIPAMENTOS
  # ------------------------------------------
  def construir_aba_equipamentos(self):
    frame = self.aba_equipamentos

    # Tabela
    columns = ("ID", "Nome", "Categoria", "Descrição", "Qtd", "Estado")
    self.tree_eq = ttk.Treeview(
        frame, columns=columns, show="headings", selectmode="browse"
    )

    for col in columns:
      self.tree_eq.heading(col, text=col)
      self.tree_eq.column(col, width=120, anchor="w")
    self.tree_eq.column("ID", width=40, anchor="center")
    self.tree_eq.column("Qtd", width=50, anchor="center")

    self.atualizar_tabela_equipamentos()
    self.tree_eq.pack(
        side="left", fill="both", expand=True, padx=(10, 0), pady=10
    )

    # Painel de Ações à Direita
    panel_acoes = tk.Frame(frame, bg=BG_DARK, padx=15, pady=10)
    panel_acoes.pack(side="right", fill="y")

    tk.Label(
        panel_acoes,
        text="Gerenciar Equipamentos",
        font=("Segoe UI", 11, "bold"),
        bg=BG_DARK,
        fg=FG_LIGHT,
    ).pack(anchor="w", pady=(0, 10))

    if self.usuario_atual["tipo"] == "Administrador":
      btn_add = tk.Button(
          panel_acoes,
          text="Cadastrar Novo",
          bg=ACCENT_COLOR,
          fg=FG_LIGHT,
          relief="flat",
          width=18,
          command=self.abrir_modal_equipamento,
      )
      btn_add.pack(pady=5, ipady=3)

    btn_detalhes = tk.Button(
        panel_acoes,
        text="Ver Disponibilidade",
        bg=BG_PANEL,
        fg=FG_LIGHT,
        relief="flat",
        width=18,
        command=self.ver_disponibilidade_equipamento,
    )
    btn_detalhes.pack(pady=5, ipady=3)

  def atualizar_tabela_equipamentos(self):
    for row in self.tree_eq.get_children():
      self.tree_eq.delete(row)
    for eq in EQUIPAMENTOS:
      self.tree_eq.insert(
          "",
          "end",
          values=(
              eq["id"],
              eq["nome"],
              eq["categoria"],
              eq["descricao"],
              eq["quantidade"],
              eq["estado"],
          ),
      )

  def abrir_modal_equipamento(self):
    modal = tk.Toplevel(self.root)
    modal.title("Cadastrar Equipamento")
    modal.geometry("400x350")
    modal.config(bg=BG_PANEL)

    tk.Label(
        modal,
        text="Novo Equipamento",
        font=("Segoe UI", 12, "bold"),
        bg=BG_PANEL,
        fg=FG_LIGHT,
    ).pack(pady=15)

    tk.Label(modal, text="Nome:", bg=BG_PANEL, fg=FG_MUTED).pack(anchor="w", padx=20)
    e_nome = tk.Entry(modal, bg=BG_INPUT, fg=FG_LIGHT, relief="flat", width=35)
    e_nome.pack(padx=20, ipady=3, pady=(0, 10))

    tk.Label(modal, text="Categoria:", bg=BG_PANEL, fg=FG_MUTED).pack(
        anchor="w", padx=20
    )
    e_cat = tk.Entry(modal, bg=BG_INPUT, fg=FG_LIGHT, relief="flat", width=35)
    e_cat.pack(padx=20, ipady=3, pady=(0, 10))

    tk.Label(modal, text="Quantidade:", bg=BG_PANEL, fg=FG_MUTED).pack(
        anchor="w", padx=20
    )
    e_qtd = tk.Entry(modal, bg=BG_INPUT, fg=FG_LIGHT, relief="flat", width=35)
    e_qtd.pack(padx=20, ipady=3, pady=(0, 15))

    def salvar():
      try:
        novo = {
            "id": len(EQUIPAMENTOS) + 1,
            "nome": e_nome.get(),
            "categoria": e_cat.get(),
            "descricao": "Cadastrado via Sistema",
            "quantidade": int(e_qtd.get()),
            "estado": "Disponível",
        }
        EQUIPAMENTOS.append(novo)
        self.atualizar_tabela_equipamentos()
        messagebox.showinfo("Sucesso", "Equipamento cadastrado com sucesso!")
        modal.destroy()
      except ValueError:
        messagebox.showerror("Erro", "Quantidade inválida.")

    tk.Button(
        modal,
        text="Salvar",
        bg=ACCENT_COLOR,
        fg=FG_LIGHT,
        relief="flat",
        command=salvar,
        width=15,
    ).pack(ipady=3)

  def ver_disponibilidade_equipamento(self):
    selected = self.tree_eq.selection()
    if not selected:
      messagebox.showwarning("Aviso", "Selecione um equipamento.")
      return
    item = self.tree_eq.item(selected[0])
    eq_nome = item["values"][1]
    eq_estado = item["values"][5]
    messagebox.showinfo(
        "Consulta de Disponibilidade",
        f"Equipamento: {eq_nome}\nStatus Atual: {eq_estado}\nPeríodo Consultado:"
        " Hoje\nResultado: Disponível para reserva.",
    )

  # ------------------------------------------
  # ABA 2: RESERVAS
  # ------------------------------------------
  def construir_aba_reservas(self):
    frame = self.aba_reservas

    columns = ("ID", "Equipamento", "Solicitante", "Data Início", "Status")
    self.tree_res = ttk.Treeview(
        frame, columns=columns, show="headings", selectmode="browse"
    )
    for col in columns:
      self.tree_res.heading(col, text=col)
      self.tree_res.column(col, width=150, anchor="w")

    self.atualizar_tabela_reservas()
    self.tree_res.pack(
        side="left", fill="both", expand=True, padx=(10, 0), pady=10
    )

    panel_acoes = tk.Frame(frame, bg=BG_DARK, padx=15, pady=10)
    panel_acoes.pack(side="right", fill="y")

    tk.Label(
        panel_acoes,
        text="Ações de Reserva",
        font=("Segoe UI", 11, "bold"),
        bg=BG_DARK,
        fg=FG_LIGHT,
    ).pack(anchor="w", pady=(0, 10))

    btn_solicitar = tk.Button(
        panel_acoes,
        text="Solicitar Reserva",
        bg=ACCENT_COLOR,
        fg=FG_LIGHT,
        relief="flat",
        width=18,
        command=self.abrir_modal_reserva,
    )
    btn_solicitar.pack(pady=5, ipady=3)

    if self.usuario_atual["tipo"] == "Administrador":
      btn_aprovar = tk.Button(
          panel_acoes,
          text="Aprovar Selecionada",
          bg="#2e7d32",
          fg=FG_LIGHT,
          relief="flat",
          width=18,
          command=self.aprovar_reserva,
      )
      btn_aprovar.pack(pady=5, ipady=3)

  def atualizar_tabela_reservas(self):
    for row in self.tree_res.get_children():
      self.tree_res.delete(row)
    for r in RESERVAS:
      self.tree_res.insert(
          "",
          "end",
          values=(
              r["id"],
              r["equipamento"],
              r["solicitante"],
              r["data_inicio"],
              r["status"],
          ),
      )

  def abrir_modal_reserva(self):
    modal = tk.Toplevel(self.root)
    modal.title("Solicitar Reserva")
    modal.geometry("380x300")
    modal.config(bg=BG_PANEL)

    tk.Label(
        modal,
        text="Nova Solicitação de Reserva",
        font=("Segoe UI", 11, "bold"),
        bg=BG_PANEL,
        fg=FG_LIGHT,
    ).pack(pady=15)

    tk.Label(modal, text="Equipamento:", bg=BG_PANEL, fg=FG_MUTED).pack(
        anchor="w", padx=20
    )
    nomes_eq = [e["nome"] for e in EQUIPAMENTOS if e["estado"] == "Disponível"]
    combo_eq = ttk.Combobox(modal, values=nomes_eq, width=32, state="readonly")
    combo_eq.pack(padx=20, pady=(0, 10))
    if nomes_eq:
      combo_eq.current(0)

    tk.Label(modal, text="Data de Utilização (AAAA-MM-DD):", bg=BG_PANEL, fg=FG_MUTED).pack(
        anchor="w", padx=20
    )
    e_data = tk.Entry(modal, bg=BG_INPUT, fg=FG_LIGHT, relief="flat", width=34)
    e_data.pack(padx=20, ipady=3, pady=(0, 15))
    e_data.insert(0, str(datetime.date.today()))

    def solicitar():
      if not combo_eq.get():
        messagebox.showerror("Erro", "Nenhum equipamento selecionado.")
        return
      nova_res = {
          "id": len(RESERVAS) + 1,
          "equipamento": combo_eq.get(),
          "solicitante": self.usuario_atual["nome"],
          "data_inicio": e_data.get(),
          "data_fim": e_data.get(),
          "status": "Pendente",
      }
      RESERVAS.append(nova_res)
      self.atualizar_tabela_reservas()
      messagebox.showinfo("Sucesso", "Reserva solicitada com sucesso!")
      modal.destroy()

    tk.Button(
        modal,
        text="Enviar Solicitação",
        bg=ACCENT_COLOR,
        fg=FG_LIGHT,
        relief="flat",
        command=solicitar,
        width=18,
    ).pack(ipady=3)

  def aprovar_reserva(self):
    selected = self.tree_res.selection()
    if not selected:
      messagebox.showwarning("Aviso", "Selecione uma reserva para aprovar.")
      return
    item = self.tree_res.item(selected[0])
    res_id = item["values"][0]
    for r in RESERVAS:
      if r["id"] == res_id:
        r["status"] = "Aprovada"
        # Adicionar automaticamente aos empréstimos ativos
        EMPRESTIMOS.append({
            "id": len(EMPRESTIMOS) + 1,
            "equipamento": r["equipamento"],
            "responsavel": r["solicitante"],
            "status": "Ativo",
        })
    self.atualizar_tabela_reservas()
    self.atualizar_tabela_emprestimos()
    messagebox.showinfo("Sucesso", "Reserva aprovada e empréstimo gerado!")

  # ------------------------------------------
  # ABA 3: EMPRÉSTIMOS
  # ------------------------------------------
  def construir_aba_emprestimos(self):
    frame = self.aba_emprestimos

    columns = ("ID", "Equipamento", "Responsável", "Status")
    self.tree_emp = ttk.Treeview(
        frame, columns=columns, show="headings", selectmode="browse"
    )
    for col in columns:
      self.tree_emp.heading(col, text=col)
      self.tree_emp.column(col, width=180, anchor="w")

    self.atualizar_tabela_emprestimos()
    self.tree_emp.pack(
        side="left", fill="both", expand=True, padx=(10, 0), pady=10
    )

    panel_acoes = tk.Frame(frame, bg=BG_DARK, padx=15, pady=10)
    panel_acoes.pack(side="right", fill="y")

    tk.Label(
        panel_acoes,
        text="Controle de Empréstimos",
        font=("Segoe UI", 11, "bold"),
        bg=BG_DARK,
        fg=FG_LIGHT,
    ).pack(anchor="w", pady=(0, 10))

    if self.usuario_atual["tipo"] == "Administrador":
      btn_devolver = tk.Button(
          panel_acoes,
          text="Registrar Devolução",
          bg=ACCENT_COLOR,
          fg=FG_LIGHT,
          relief="flat",
          width=18,
          command=self.registrar_devolucao,
      )
      btn_devolver.pack(pady=5, ipady=3)

  def atualizar_tabela_emprestimos(self):
    for row in self.tree_emp.get_children():
      self.tree_emp.delete(row)
    for e in EMPRESTIMOS:
      self.tree_emp.insert(
          "", "end", values=(e["id"], e["equipamento"], e["responsavel"], e["status"])
      )

  def registrar_devolucao(self):
    selected = self.tree_emp.selection()
    if not selected:
      messagebox.showwarning("Aviso", "Selecione um empréstimo ativo.")
      return
    item = self.tree_emp.item(selected[0])
    emp_id = item["values"][0]
    for e in EMPRESTIMOS:
      if e["id"] == emp_id:
        e["status"] = "Devolvido"
    self.atualizar_tabela_emprestimos()
    messagebox.showinfo("Sucesso", "Devolução registrada com sucesso!")

  # ------------------------------------------
  # ABA 4: MANUTENÇÃO
  # ------------------------------------------
  def construir_aba_manutencao(self):
    frame = self.aba_manutencao

    columns = ("ID", "Equipamento", "Descrição", "Status")
    self.tree_man = ttk.Treeview(
        frame, columns=columns, show="headings", selectmode="browse"
    )
    for col in columns:
      self.tree_man.heading(col, text=col)
      self.tree_man.column(col, width=180, anchor="w")

    self.atualizar_tabela_manutencao()
    self.tree_man.pack(
        side="left", fill="both", expand=True, padx=(10, 0), pady=10
    )

    panel_acoes = tk.Frame(frame, bg=BG_DARK, padx=15, pady=10)
    panel_acoes.pack(side="right", fill="y")

    tk.Label(
        panel_acoes,
        text="Gestão de Manutenção",
        font=("Segoe UI", 11, "bold"),
        bg=BG_DARK,
        fg=FG_LIGHT,
    ).pack(anchor="w", pady=(0, 10))

    if self.usuario_atual["tipo"] in ["Administrador", "TecnicoManutencao"]:
      btn_concluir = tk.Button(
          panel_acoes,
          text="Concluir Manutenção",
          bg=ACCENT_COLOR,
          fg=FG_LIGHT,
          relief="flat",
          width=18,
          command=self.concluir_manutencao,
      )
      btn_concluir.pack(pady=5, ipady=3)

  def atualizar_tabela_manutencao(self):
    for row in self.tree_man.get_children():
      self.tree_man.delete(row)
    for m in MANUTENCOES:
      self.tree_man.insert(
          "", "end", values=(m["id"], m["equipamento"], m["descricao"], m["status"])
      )

  def concluir_manutencao(self):
    selected = self.tree_man.selection()
    if not selected:
      messagebox.showwarning("Aviso", "Selecione um registro de manutenção.")
      return
    item = self.tree_man.item(selected[0])
    man_id = item["values"][0]
    for m in MANUTENCOES:
      if m["id"] == man_id:
        m["status"] = "Concluída"
    self.atualizar_tabela_manutencao()
    messagebox.showinfo("Sucesso", "Manutenção concluída e equipamento liberado!")


# --- EXECUÇÃO DO PROGRAMA ---
if __name__ == "__main__":
  root = tk.Tk()
  app = SIRMEApp(root)
  root.mainloop()
