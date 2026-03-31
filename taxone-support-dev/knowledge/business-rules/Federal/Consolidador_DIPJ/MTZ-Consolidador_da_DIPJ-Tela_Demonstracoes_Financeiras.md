# MTZ-Consolidador_da_DIPJ-Tela_Demonstracoes_Financeiras

- **Fonte:** MTZ-Consolidador_da_DIPJ-Tela_Demonstracoes_Financeiras.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 29 KB

---

# Consolidador da DIPJ – Tela Demonstrações Financeiras

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3278

Criar a opção "Utilizar Conta Reduzida" \.

Inserir campo "Utilizar Conta Reduzida" na tela Demonstrações Financeiras, dentro do módulo Consolidador da DIPJ\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Incluir o campo "Utilizar Conta Reduzida" que deve vir desmarcado por padrão\.

OS3278

__RN01__

Se o campo "Utilizar Conta Reduzida" estiver marcado, a janela "Selecionar Plano de Contas" deverá ser exibida com a coluna "Cod Conta Reduz" na segunda posição, caso contrário deverá ser exibido na sexta posição\.

OS3278

__RN02__

Se o usuário possuir contas cadastradas da forma padrão \(código da conta contábil\), e marcar o campo “Utilizar Conta Reduzida”, deverá ser exibida uma mensagem informando que, no caso de alteração, a parametrização já existente será apagada\.

OS3278

__RN03__

Se o usuário possuir contas cadastradas da forma nova \(código da conta reduzida\), e desmarcar o campo “Utilizar Conta Reduzida”, deverá ser exibida uma mensagem informando que, no caso de alteração, a parametrização já existente será apagada\.

OS3278

__RN04__

Registrar na tabela das Demonstrações Financeiras  o uso ou não das contas reduzidas, para que a recuperação dos registro fique de acordo com a parametrização feita pelo cliente\.

OS3278

	

