# Tela_PAT_Periodos_Anteriores_DW

- **Fonte:** Tela_PAT_Periodos_Anteriores_DW.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 77 KB

---

 

THOMSON REUTERS

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>PAT – Períodos Anteriores ao ONESOURCE

ECF \- Escrituração Contábil Fiscal \(DW\)

##### DOCUMENTO DE REQUISITO

__Data__

__MFS__

__Descrição__

__Autor__

05/06/2018

MFS\-18710

Criação do documento

Alessandra Cristina Navatta

Sumário

[1\.	INTRODUÇÂO	3](#_Toc516041593)

[2\.	DOCUMENTOS DE REFERÊNCIAS	3](#_Toc516041594)

[3\.	TELAS	3](#_Toc516041595)

[3\.1\.	Pesquisa de Registros	3](#_Toc516041596)

[3\.2\.	Regras dos Campos da Tela Principal	5](#_Toc516041597)

# <a id="_Toc515866222"></a><a id="_Toc516041593"></a>INTRODUÇÂO

O objetivo desta especificação é criar a tela de PAT – Períodos Anteriores ao DW possibilitando a entrada manual dos valores \(sobras a serem utilizadas para abater o valor do IRPJ\) do PAT controlados em sistemas anteriores ao ONESOURCE DW\.

# <a id="_Toc516041594"></a>DOCUMENTOS DE REFERÊNCIAS

- Mensagens\_Sistema\_DWECF\.xlsx
- Regras\_Gerais\_DWECF\.docx
- Tela\_Informacoes\_ECF\.doc
- Tela\_Programa\_de\_Alimentação\_do\_Trabalhador\.doc

# <a id="_Toc509319853"></a><a id="_Toc515866224"></a><a id="_Toc516041595"></a><a id="_Toc359406591"></a>TELAS

## <a id="_Toc509319854"></a><a id="_Toc515866225"></a><a id="_Toc516041596"></a>Pesquisa de Registros 

__Localização da tela:__ 

ECF \- Escrituração Contábil Fiscal >> Manutenção >>PAT – Períodos Anteriores ao DW

__Título da tela: __PAT – Períodos Anteriores ao DW

__Condições Gerais:__

Quando o usuário acessar a tela de consulta, apresentar todos os registros contidos na tabela de as escriturações \(Informações ECF\) cadastradas no sistema que não possuem outras escriturações com datas anteriores\. 

__Obs\. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco\.__

__Campo__

__Tipo__

__Regra__

Estabelecimento

LOV

\(Tipo \- Código – Descrição\)

Permite que o usuário busque o registro pelo Código do Estabelecimento\.

Exercício

Texto

AAAA

O usuário poderá informar o exercício\. 

Data Inicial

Data

DD/MM/AAAA

O usuário poderá informar a data inicial da Informação ECF\.

Versão

Lista

\(Código \-Descrição\)

Aplicar a RNG00004\-Versão de Layout

Forma de Tributação

Lista

\(Código \-Descrição\)

Exibe as opções abaixo:

\-Lucro Real, Lucro Presumido, Lucro Arbitrado

\-Imune de IRPJ 

\-Isento do IRPJ 

Apuração

Lista

\(Código \-Descrição\)

Exibe as opções abaixo:

\- Anual

\- Trimestral

## <a id="_Toc350763252"></a><a id="_Toc360443175"></a><a id="_Toc515866226"></a><a id="_Toc516041597"></a>Regras dos Campos da Tela Principal

__Localização da tela:__ 

ECF \- Escrituração Contábil Fiscal >> Manutenção>> PAT \-  Períodos Anteriores ao DW

__Título da tela: __PAT \-  Períodos Anteriores ao DW

__Condições Gerais:__ Quando o usuário acessar a tela de consulta, apresentar todos os registros da tela Informações ECF\.

Desabilitar os botões “Novo”, “Excluir” e “Copiar” na toolbar\.

Botão Editar: Habilitar quando o status da abertura da apuração for “Em Aberto”, “Reapurar” ou não houver dados na tela de Abertura da Apuração \(status da primeira abertura\)\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS__

Confirma

Botão

Aplicar a RNG00012 – Salvar

MFS\-18710

DADOS GERAIS

Estabelecimento

Texto

S

N

Tipo \- Código \- Descrição

Permite que o usuário visualize o estabelecimento correspondente ao registro selecionado na tabela de Informações ECF\.

MFS\-18710

Exercício

Texto

S

N

AAAA

Permite que o usuário visualize o ano correspondente ao registro selecionado na tabela de Informações ECF\.

MFS\-18710

Data Inicial

Texto

S

N

DD/MM/AAAA

Permite que o usuário visualize a data inicial, referente ao registro selecionado na tabela das Informações ECF\.

MFS\-18710

Versão

Texto

S

N

Código \- Descrição

Permite que o usuário visualize a Versão do Layout utilizada para o processamento do registro, referente ao registro selecionado na tabela de Informações ECF\.

MFS\-18710

Forma de Tributação

Texto

S

N

Descrição

Permite que o usuário visualize a forma de tributação, referente ao registro selecionado na tabela das Informações ECF\.

MFS\-18710

Apuração

Texto

S

N

Descrição

Permite que o usuário visualize a apuração, referente ao registro selecionado na tabela das Informações ECF\.

MFS\-18710

Data Final do Último Período da Escrituração

Texto

S

N

DD/MM/AAAA

Permite que o usuário visualize a data final do último período da escrituração

MFS\-18710

PAT – PERÍODOS ANTERIORES AO DW

Ano\(\*\)

Texto

S

N

AAAA

__Tratamento:__

Exibir automaticamente os 2 anos imediatamente anterior ao da escrituração selecionada \(considerando o ano da Data Inicial da Informação ECF\)\.

O label do campo será dinâmico\. Deve ser exibido de acordo com a informação ECF recuperada\. 

AAAA será os dois anos imediatamente anterior ao ano da Informação ECF recuperada\. Exemplo: recuperada a informação ECF de 2014, os campos exibidos serão Ano 2012 e Ano 2013\.

 

MFS\-18710

Valor

Texto

S

S

0,00

__Tratamentos:__

Será habilitado para preenchimento com a ação no botão editar\.

O valor total exibido na tela não será exibido na conta da parte B corresponde ao PAT\. Pelo fato da tela Lançamento da Parte B \(M410\) possuir modo edição, se necessário, o valor da parte B poderá ser ajustado manualmente\.

O valor informado nesta tela será utilizado no cálculo do PAT \. Quando o valor tiver o prazo expirado para utilização, ou seja, o período de dois anos\-calendários for excedido, o valor será desconsiderado\. Neste cenário, não será gerado lançamento da Parte B realizando a baixa do valor utilizado\.

MFS\-18710

