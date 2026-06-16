# 📘 DESAFIO 3 — DemoQA Form

```markdown
# 🧪 Desafio 3 — Automação de Formulário Completo (DemoQA)

Este projeto automatiza o preenchimento completo de um formulário web complexo utilizando Selenium
WebDriver.

---

## 🔗 Site

https://demoqa.com/automation-practice-form

---

## 🎯 Objetivo

Automatizar preenchimento completo de formulário com:

- Inputs simples
- Selects dinâmicos (React)
- Autocomplete
- Upload de arquivos
- Checkboxes múltiplos
- Validação de modal

---

## 🧾 Campos preenchidos

### Dados pessoais
- Nome
- Sobrenome
- Email
- Telefone
- Gênero

### Informações adicionais
- Data de nascimento
- Subjects (autocomplete)
- Hobbies (checkbox múltiplo)
- Upload de imagem
- Endereço

### Localização
- State (React Select)
- City (React Select)

---

## 🧠 Validações

Após submissão:

- Modal de confirmação exibido
- Título validado:
  - "Thanks for submitting the form"
- Dados validados no corpo do modal:
  - Nome
  - Email
  - Telefone

---

## 📸 Screenshot

Ao final da execução é gerada uma imagem:

## 🚀 Como executar

```bash
pip install -r requirements.txt
python desafio2.py
