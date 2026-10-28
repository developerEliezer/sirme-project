# 📦 SIRME - Sistema Integrado de Recursos e Materiais Extracurriculares

Sistema desktop desenvolvido em **Python** utilizando a biblioteca gráfica **Tkinter** para o gerenciamento de equipamentos, reservas, empréstimos e manutenções em instituições de ensino.

---

## 🚀 Funcionalidades

- **🔒 Sistema de Autenticação:** Controle de acesso baseado em perfis de usuário (`Administrador`, `Professor` e `Técnico de Manutenção`).
- **📦 Gestão de Equipamentos:** Cadastro, listagem e verificação de disponibilidade de recursos (projetores, notebooks, kits de robótica, etc.).
- **📅 Controle de Reservas:** Solicitação de reservas por datas e fluxo de aprovação por administradores.
- **📋 Gestão de Empréstimos:** Acompanhamento de empréstimos ativos e registro de devoluções.
- **🔧 Controle de Manutenção:** Acompanhamento de equipamentos em reparo e conclusão de manutenções.
- **🎨 Interface Moderna:** Tema escuro (*Dark Mode*) customizado utilizando estilos do `ttk`.

---

## 👥 Credenciais para Teste (Mock Database)

Você pode utilizar os seguintes usuários pré-cadastrados para testar os diferentes níveis de permissão no sistema:

| Perfil | E-mail Institucional | Senha | Permissões Principais |
| :--- | :--- | :--- | :--- |
| **Administrador** | `admin@ufr.br` | `123` | Acesso total (cadastra equipamentos, aprova reservas, registra devoluções e manutenções). |
| **Professor** | `professor@ufr.br` | `123` | Solicita reservas de equipamentos. |
| **Técnico** | `tecnico@ufr.br` | `123` | Gerencia e conclui ordens de manutenção. |

---

## 🛠️ Requisitos e Instalação

O projeto utiliza apenas bibliotecas nativas do Python, portanto, **nenhuma instalação externa via `pip` é necessária**!

1. Certifique-se de ter o **Python 3.x** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo de código-fonte (ex: `main.py`).

---

##  ▶️ Como Executar

Abra o terminal na pasta onde o arquivo do código está salvo e execute o seguinte comando:

```bash
python main.py
