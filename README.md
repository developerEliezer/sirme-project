# 📦 SIRME - Sistema Integrado de Recursos e Materiais Extracurriculares

![Status do Projeto](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Instituição](https://img.shields.io/badge/UDF-Centro%20Universit%C3%A1rio%20do%20Distrito%20Federal-blue)
![Tecnologias](https://img.shields.io/badge/Tecnologias-HTML5%20%7C%20CSS3%20%7C%20JavaScript%20%7C%20Python-orange)

O **SIRME** é uma plataforma desenvolvida para otimizar e centralizar o gerenciamento, controle de disponibilidade, solicitações de reserva, empréstimos, devoluções e manutenção de equipamentos e materiais tecnológicos utilizados em atividades extracurriculares de instituições de ensino.

---

## 📌 Visão Geral do Sistema

Em ambientes acadêmicos, o compartilhamento de recursos (como projetores, notebooks, kits de robótica, instrumentos musicais e equipamentos de áudio/vídeo) exige controle para evitar conflitos de agenda, perdas ou falhas de manutenção. O SIRME resolve esse problema através de:

- **Controle de Acesso por Perfil:** Interfaces e permissões adaptadas para **Administrador**, **Professor** e **Técnico de Manutenção**.
- **Gestão de Equipamentos:** Cadastro, consulta por filtros/categoria e atualização de estado de conservação.
- **Fluxo Completo de Reservas e Empréstimos:** Solicitação por docentes, análise/aprovação por gestores e baixa automática na devolução.
- **Ocorrências e Manutenção:** Registro de danos/defeitos e acompanhamento do status de ordens de serviço.
- **Relatórios e Logs:** Registro auditável de atividades e geração de relatórios consolidados.

---

## 🛠️ Implementações Disponíveis

Para oferecer máxima flexibilidade de implantação, o projeto conta com **duas versões totalmente funcionais**:

### 1. 🌐 Versão Web (`index.html`)
- **Arquitetura:** *Single-file Application* (HTML5, CSS3 com variáveis/Flexbox/Grid e JavaScript ES6+ em um único arquivo).
- **Sem Dependências Externa:** Roda diretamente no navegador sem necessidade de servidor local ou backend adicional.
- **Persistência de Dados:** Armazenamento via `localStorage` do navegador.
- **Interface:** Dark Mode moderno, dinâmico e responsivo com simulação de papéis em tempo real.

### 2. 🐍 Versão Desktop (Python)
- **Arquitetura:** Aplicação nativa com interface gráfica em Python (Tkinter / CustomTkinter / PySimpleGUI).
- **Execução:** Executável via interpretador Python nativo.
- **Persistência de Dados:** Gerenciamento local em arquivos de estado (JSON/SQLite).

---

## 🚀 Como Executar o Projeto

### Repositório Oficial
```bash
git clone https://github.com/developerEliezer/sirme-project.git
cd sirme-project
```

---

### 🌐 Executando a Versão Web
1. Abra a pasta do projeto.
2. Dê um duplo clique no arquivo `index.html` (ou abra em qualquer navegador moderno como Chrome, Edge ou Firefox).

---

### 🐍 Executando a Versão Python
1. Certifique-se de ter o **Python 3.8+** instalado.
2. No terminal, navegue até a pasta do projeto e execute:
   ```bash
   python main.py
   ```
   *(Nota: Se o script principal do Python tiver outro nome, substitua `main.py` pelo nome correspondente, ex: `app.py`)*

---

## 📋 Regras de Negócio e Funcionalidades

| Módulo | Descrição / Regras de Negócio |
| :--- | :--- |
| **Autenticação** | Permissões diferenciadas conforme o perfil (Admin, Professor, Técnico). |
| **Disponibilidade** | Equipamento só é exibido como disponível se não houver reserva ou manutenção ativa. |
| **Aprovação** | Toda solicitação de reserva passa por validação do Administrador antes da liberação. |
| **Manutenção** | Equipamentos com defeito grave têm status atualizado automaticamente para "Em Manutenção". |
| **Histórico** | Auditoria permanente de movimentações e logs de operações críticas. |

---

## 👥 Equipe de Desenvolvimento

Trabalho desenvolvido para a disciplina de **Análise e Projeto de Sistemas** — **UDF (Centro Universitário do Distrito Federal)**.

- **Eliezer Câmara Silva Filho** - RGM: 49339648
- **David dos Santos da Silva** - RGM: 43645224
- **Dérick Alves Tavares de Lima** - RGM: 42927757
- **João Pedro Cardoso Silva** - RGM: 43854907
- **Nichollas Improta Monteiro** - RGM: 43812350

---
