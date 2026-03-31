# MTZ-Consolidador_da_DIPJ-Tela_IRPJ

- **Fonte:** MTZ-Consolidador_da_DIPJ-Tela_IRPJ.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 33 KB

---

# Consolidador da DIPJ – Tela IRPJ

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3209

Consolidador da DIPJ – Tela IRPJ

Trata\-se de uma solicitação de melhoria no módulo Consolidador da DIPJ\. No menu Parâmetros – IRPJ, será criado o botão Copiar na barra de ferramentas\. 

OS3278

Criar a opção "Utilizar Conta Reduzida" \.

Inserir campo "Utilizar Conta Reduzida" na tela  IRPJ, dentro do módulo Consolidador da DIPJ\. 

OS3909

Consolidador DIPJ – Tela IRPJ

Atualizar a regra para utilizar as expressões aritméticas \(Subtração, Multiplicação e Divisão\) na consolidação das contas por linha e ficha\. A expressão adição já é contemplada\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Incluir o botão Copiar, na barra de ferramentas da tela IRPJ, através do __*Módulo: Consolidador da DIPJ,  Menu: Parâmetros\.*__

OS3209

__RN01__

Quando for selecionada a opção de __Copiar__, em __*Módulo: Consolidador da DIPJ,  Menu: Parâmetros 🡪 IRPJ, o usuário terá as seguintes opções:*__

1. Informar os seguintes parâmetros na tela: 
	1. __*Copiar a parametrização para o Ano\-Calendário*__*🡪* Determina para qual ano serão copiadas as parametrizações;
	2. __*Sobrepor os dados das contas já parametrizadas*__*🡪 Determinará se as parametrizações copiadas irão sobrepor as que já estejam cadastradas para o Ano\-Calendário informado no Parâmetro 1\.1\.*
2. A partir da informação do item 1 é feita cópia de toda a parametrização que cujo Ano\-Calendário seja menor que o informado na tela \(Parâmetro 1\.1\)\.  A cópia será sempre feita a partir dos dados existentes para o último ano imediatamente anterior ao ano informado\. 
3.  Na hora da gravação se já existir uma parametrização no Ano\-Calendário \(Parâmetro 1\.1\) para uma determinada __Qualificação da PJ, Ficha e__ __Linha__  se o Parâmetro 1\.2 estiver marcado, a gravação deverá sobrepor a existente, caso contrário, Parâmetro 1\.2 desmarcado, não será copiado e gravado a parametrização\.

OS3209

__RN02__

Ao gravar a copia, emitir a seguinte msg ao usuário: Copia Finalizada\. É recomendável emitir o relatório e realizar a conferência das  informações\.

OS3209

__RN03__

Incluir o botão Abrir, no __*Módulo: Consolidador da DIPJ,  Menu: Parâmetros 🡪 IRPJ\.*__

__*Os critérios de seleção deste botão serão:*__

Ano\-DIPJ, 

Qualificação da PJ, 

Ficha, 

Linha, 

Conta e

Centro de Custo

ATENÇÃO: A funcionalidade solicitada na OS3209 foi transferida para o caminho: Módulo Consolidador da DIPJ, Menu Parametros / Copia Parametrização/Replica Empresas \- Alteração feita na OS3500\.

OS3209

__RN04__

Incluir o campo "Utilizar Conta Reduzida" que deve vir desmarcado por padrão\.

OS3278

__RN05__

Se o campo "Utilizar Conta Reduzida" estiver marcado, a janela "Selecionar Plano de Contas" deverá ser exibida com a coluna "Cod Conta Reduz" na segunda posição, caso contrário deverá ser exibido na sexta posição\.

OS3278

__RN06__

Se o usuário possuir contas cadastradas da forma padrão \(código da conta contábil\), e marcar o campo “Utilizar Conta Reduzida”, deverá ser exibida uma mensagem informando que, no caso de alteração, a parametrização já existente será apagada\.

OS3278

__RN07__

Se o usuário possuir contas cadastradas da forma nova \(código da conta reduzida\), e desmarcar o campo “Utilizar Conta Reduzida”, deverá ser exibida uma mensagem informando que, no caso de alteração, a parametrização já existente será apagada\.

OS3278

__RN08__

Registrar na tabela da parametrização o uso ou não das contas reduzidas, para que a recuperação dos saldos fique de acordo com a parametrização feita pelo cliente\.

OS3278

__RN09__

Campo: Conta Contábil

Deverá permitir também as expressões aritméticas \(Subtração, Multiplicação e Divisão\) ao selecionar as contas, e seguir a ordem de precedência dos cálculos abaixo:

1° Parênteses

2° Multiplicação ou Divisão

3° Adição ou Subtração

Isso deverá refletir na consolidação final após geração das fichas\.    

OS3909

	

