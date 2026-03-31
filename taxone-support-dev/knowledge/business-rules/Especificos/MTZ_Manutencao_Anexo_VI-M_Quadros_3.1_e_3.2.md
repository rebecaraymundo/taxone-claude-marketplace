# MTZ_Manutenção_Anexo_VI-M_Quadros 3.1 e 3.2

> Fonte: MTZ_Manutenção_Anexo_VI-M_Quadros 3.1 e 3.2.docx






THOMSON REUTERS

Manutenção Anexo VI-M Quadros 3.1 a 3.2
Módulo Combustível e Derivados de Petróleo (SCANC)

Localização: Movimento de Refinaria  Manutenção Anexo VI-M  Quadros 3.1 e 3.2


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Específicos >> Combustível e Derivados de Petróleo
Movimento de Refinaria  Manutenção Anexo VI-M  Quadros 3.1 e 3.2

Tabela de Destino: CBT_ANEXO6M_QUADR31_32



Definição dos campos a serem apresentados na tela:

Estabelecimento:
Habilitado se o usuário entrou sem estabelecimento de login.
Desabilitado se o estabelecimento foi informado no login do módulo.
Campo Obrigatório
Gravar campo COD_ESTAB CBT_ANEXO6M_QUADR31_32

Mês/Ano Referência:
Habilitado
Campo obrigatório.
Gravar DAT_APURACAO CBT_ANEXO6M_QUADR31_32, com o último dia do mês/ano informado.

UF Destinatária do Anexo VI-M:
Habilitado
Campo Obrigatório
Gravar IDENT_ESTADO_DESTINO CBT_ANEXO6M_QUADR31_32


Quadro:
Habilitado
Campo Obrigatório
Lista fixa composta pelos itens abaixo:
3.1 - OPERAÇÕES COM GLGN REALIZADAS PELO EMITENTE DO RELATÓRIO COM IMPOSTO DEVIDO A UF DE ORIGEM
3.2 - DEDUÇÃO POR OPERAÇÕES COM GLGN REALIZADAS PELO EMITENTE DO RELATÓRIO COM IMPOSTO DEVIDO A UF DE ORIGEM

Gravar o campo COD_TAG CBT_ANEXO6M_QUADR31_32 conforme regra abaixo:


UF do Quadro (label “UF a Deduzir” ou “UF a Repassar”):
Campo obrigatório.
A label do campo é alterada de acordo com a escolha do quadro:
- Se Quadro escolhido foi o 3.1, a label do campo deve ser “UF a Deduzir”
- Se Quadro escolhido foi o 3.2, a label do campo deve ser “UF a Repassar”
Gravar IDENT_ESTADO_QUAD CBT_ANEXO6M_QUADR31_32


Produto:
Habilitado
Campo Obrigatório
Lista fixa composta pelos itens abaixo:
01 - GLGNn
02 - GLGNi
Não apresentar o código, só a descrição.
Gravar COD_PRODUTO CBT_ANEXO6M_QUADR31_32.

Qtd (Base de Cálculo)
Habilitado
- Gravar QTD_COMB CBT_ANEXO6M_QUADR31_32

- Vlr ICMS Cobrado
Habilitado
- Gravar VLR_ICMS_COB CBT_ANEXO6M_QUADR31_32

- Vlr ICMS Retido
Habilitado
- Gravar VLR_ICMS_RET CBT_ANEXO6M_QUADR31_32

- Vlr ICMS Total:
Desabilitado.
Apresetar o somatório dos campos Vlr ICMS Cobrado e Vlr ICMS Retido.
- Gravar VLR_ICMS_TOT CBT_ANEXO6M_QUADR31_32


No Processo
Desabilitado
Gravar NUM_PROCESSO CBT_ANEXO6M_QUADR31_32

Ind Dig Calc:
Não apresentar na tela.
Gravar:
1 – inserido via tela de manutenção
2 – inserido via geração do Anexo VI-M
3 - inserido via geração do Anexo VI-M e atualizado pela tela de manutenção

Usuário
Não apresentar na tela.
Gravar o usuário de login da aplicação.


Tratamentos da Janela:
Ao acionar a janela, verificar se a tela dos Quadros 1 e 2 está aberta. Se estiver, exibir mensagem abaixo e não abrir a janela dos Quadros 3.1 e 3.2.



Ao salvar o registro, verificar se os campos obrigatórios estão preenchidos. Se algum campo obrigatório não estiver preenchido exibir mensagem e não salvar o registro. Exemplo:


Atualização do Quadro 1:
Ao incluir, excluir ou alterar registros dos quadros 3.1, 3.2, atualizar Quadro 1 do Anexo VI-M:
Linha 1.1.1.2: Somatório dos registros do quadro 3.1
1.1.1.2 ICMS SOBRE OPERAÇÕES COM GLGN DEVIDO A UF DE ORIGEM (QUADRO 3.1)

Linha 1.2.0.1: Somatório dos registros do quadro 3.2
1.2.0.1 DEDUÇÃO DE ICMS SOBRE OPERAÇÕES COM GLGN DEVIDO A UF DE ORIGEM (QUADRO 3.2)

Linha 1.1.7: adicionar o valor da linha 1.1.1.2 no somatório das linhas 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5, 1.1.6:
1.1.7 SUB-TOTAL (1.1.1+1.1.1.2 + 1.1.2 + 1.1.3 + 1.1.4 + 1.1.5 + 1.1.6)

Linha 1.2.8: adicionar o valor da linha 1.2.0.1 no somatório das linhas 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7:
1.2.8 SUB-TOTAL DAS DEDUÇÕES (1.2.0.1+1.2.1 + 1.2.2 + 1.2.3 + 1.2.4 + 1.2.5 + 1.2.6 + 1.2.7)

| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS917434 | Liliane Assaf | Criação da janela. |
|  |  |  |
|  |  |  |


| Item | COD_TAG |
| --- | --- |
| 3.1 | A6MQ31 |
| 3.2 | A6MQ32 |
