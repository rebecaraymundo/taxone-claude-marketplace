# MTZ-DW-Manutencao_SAFX263

- **Fonte:** MTZ-DW-Manutencao_SAFX263.docx
- **Modificado:** 2021-08-20
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Informações de <a id="_Hlk509310579"></a>Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte

Manutenção SAFX263

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS16848

Lara Aline

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de manutenção para os campos da SAFX263\.

MFS18237

Lara Aline

Inclusão campos para atendimento aos processos do evento R\-2020 para Operações de Transporte de Passageiros\.

MFS20750

Lara Aline

Ajuste nos campos de valores para inclusão do evento S\-1250 do eSocial\.

MFS22920

Lara Aline

Inclusão do campo Tipo do Processo Judicial\.

__MFS70413__

Rogério Ohashi

__Retirar__ regra de validação da tela para não gravar se Ind\_Evento = 5 \(S\-1250\)\. E incluir a informação do Registro R\-2055 para o Indicador de Evento\.

Sumário

[1\.	Regras dos Campos	3](#_Toc509319436)

# <a id="_Toc350763252"></a><a id="_Toc509319436"></a>Regras dos Campos 

__\[MFS20750\]__

__Localização da tela:__ Básicos\\ MasterSAF DW\\ <a id="OLE_LINK54"></a><a id="OLE_LINK55"></a>Manutenção\\ Documento Fiscal\\ Novo Documento Fiscal\\ Doc\. Fiscal de Mercadoria\\ Aba Capa \(Botão:  Processos Administrativos/Judiciais – \(R\-2050/S\-1250\)\)

__Título da tela: __Processos Administrativos/Judiciais – \(R\-2050 / S\-1250/R\-2055\)

__Regra Geral Botões:__

__NOVO – __Permite inserir novo registro\.

__EXCLUI – __Permite excluir registro inserido\.

__CONFIRMA – __Permite salvar registro\.

__FECHA – __Permite sair da tela\.

__Regra Geral: __

- Podem existir até 50 Processos Administrativos/Judiciais por NF\. Tipo de Comercialização e NF \(“IND\_TIPO\_AQUIS” da SAFX07\)\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Tipo de Processo

DropDown

S

S

Default = Não selecionado

Deverá listar as seguintes opções:

1\-	Administrativo

2\-	Judicial 

Caso não preenchido exibir a seguinte mensagem: “Tipo de Processo deve ser informado”

MFS16848

Tipo de Processo Judicial

DropDown

N

S

Default = Não selecionado

Esse campo ficará habilitado e obrigatório APENAS se no campo Tipo de Processo estiver selecionada a opção ‘2 \- Judicial’ E o campo Indicador do Evento estiver selecionada a opção 2 \- S\-1250\.

Deverá listar as seguintes opções:

1 – Processo Judicial do Produtor;

2 – Processo Judicial Coletivo\.

Caso não preenchido exibir a seguinte mensagem: “Tipo de Processo Judicial deve ser informado se no campo Tipo do Processo estiver selecionada a opção 2 \- Judicial”

MFS22920

Número do Processo

Pasta

S

S

Default = Não selecionado

Deverão ser listados os processos conforme cadastro de processos na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF\) aba Informações do Processo\) e filtro por tipo de processo\. 

Caso não preenchido exibir a seguinte mensagem: “Número de Processo deve ser informado”

MFS16848

Indicador do Evento

RadioButton

S

S

Default = R\-2050

Deverá listar as seguintes opções:

5\-	R\-2050

A\-	S\-1250/R\-2055

MFS20750

__MFS70413__

Código da Suspensão 

Pasta

N

S

Default = Não selecionado

Deverão ser listados os códigos conforme cadastro de suspensão na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF/eSocial\) aba Informações de Suspensão de Exigibilidade de Tributos\) e filtro por número de processo e tipo de processo\. 

\[__MFS70413__\]Retirar regra de obrigatoriedade, p/ possibilitar geração do R\-2055\.

Esse campo será obrigatório se campo Indicador do Evento \(ind\_evento\) = ‘A’ – S\-1250 e caso não preenchido exibir a seguinte mensagem: “Valor da Contribuição Previdenciária não retida deve ser informado”

MFS16848

MFS20750

Valor da Contribuição Previdenciária não retida com exigibilidade suspensa

Text Box

N

S

Informar o Valor da Contribuição Previdenciária com exigibilidade suspensa\. 

Esse campo só será ficará visível ao usuário se campo Indicador do Evento \(ind\_evento\) = ‘5’ – R\-2050 ou ‘A’ – S\-1250

\[__MFS70413__\]Retirar regra de obrigatoriedade, p/ possibilitar geração do R\-2055\.

Esse campo será obrigatório se campo Indicador do Evento \(ind\_evento\) = ‘A’ – S\-1250 e caso não preenchido exibir a seguinte mensagem: “Valor da Contribuição Previdenciária não retida deve ser informado”

MFS16848

MFS18237

MFS20750

Valor da contribuição para Gilrat não retida com exigibilidade suspensa

Text Box

N

S

Informar o Valor da contribuição para Gilrat com exigibilidade suspensa\.

Esse campo só será ficará visível ao usuário se campo Indicador do Evento \(ind\_evento\) = ‘5’ – R\-2050 ou ‘A’ – S\-1250

\[__MFS70413__\]Retirar regra de obrigatoriedade, p/ possibilitar geração do R\-2055\.

Esse campo será obrigatório se campo Indicador do Evento \(ind\_evento\) = ‘A’ – S\-1250 e caso não preenchido exibir a seguinte mensagem: “Valor da Contribuição Previdenciária não retida deve ser informado”

MFS16848

MFS18237

MFS20750

Valor da contribuição para o Senar não retido com exigibilidade suspensa

Text Box

N

S

Informar o Valor da contribuição para o Senar com exigibilidade suspensa\.

Esse campo só será ficará visível ao usuário se campo Indicador do Evento \(ind\_evento\) = ‘5’ – R\-2050 ou ‘A’ – S\-1250

\[__MFS70413__\]Retirar regra de obrigatoriedade, p/ possibilitar geração do R\-2055\.

Esse campo será obrigatório se campo Indicador do Evento \(ind\_evento\) = ‘A’ – S\-1250 e caso não preenchido exibir a seguinte mensagem: “Valor da Contribuição Previdenciária não retida deve ser informado”

 

MFS16848

MFS18237

MFS20750

Indicador do Processo

RadioButton

S

S

Default = Principal

Deverá listar as seguintes opções:

1\-	Principal

2\-	Adicional 

Esse campo só será ficará visível ao usuário se campo Indicador do Evento \(ind\_evento\) = ‘2’ – R\-2020

MFS18237

Valor Retenção não Efetuada

Text Box

S

S

Informar o Valor Retenção não Efetuada, de acordo com o tipo de processo informado no campo Indicador do Processo\.

Campo obrigatório, caso não preenchido exibir a seguinte mensagem: “Valor Retenção não Efetuada deve ser informado”

Esse campo só será ficará visível ao usuário se campo Indicador do Evento \(ind\_evento\) = ‘2’ – R\-2020

MFS18237

