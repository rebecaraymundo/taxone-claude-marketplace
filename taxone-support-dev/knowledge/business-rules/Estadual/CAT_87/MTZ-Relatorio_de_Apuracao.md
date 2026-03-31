# MTZ-Relatorio_de_Apuracao

- **Fonte:** MTZ-Relatorio_de_Apuracao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Portaria CAT87/06 – Protocolo ECF 04/01

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1230

Jefferson Mota

Definição das regras da geração do Relatório de Registros

MFS11281

Andréa Rocha

Inclusão das tabelas SAFX204 e SAFX205 na geração do Relatório\.

Sumário

[1\.	REGRAS DE GERAÇÃO DO RELATÓRIO	3](#_Toc427154757)

[1\.1\.	Layout do Relatório	5](#_Toc427154758)

# <a id="_Toc427154757"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Origem das informações para geração:__ 

__Regra de seleção: __Este relatório será gerado com base nas informações das tabelas SAFX995, SAFX204, SAFX07 e SAFX205 e cadastro do Estabelecimento, considerando os parâmetros de período, e estabelecimento parametrizados na tela de geração do relatório\. Será gerado sempre que na tela de emissão for selecionada a opção “Relatório de Apuração”\.

__ Origem SAFX995:__

Serão considerados os registros da tabela SAFX995, cuja Data de Emissão compreenda o período parametrizado\. Se a geração for realizada por Estabelecimento Administrador, serão considerados os dados de todos os estabelecimentos credenciados associados ao administrador\. Se for selecionado um estabelecimento credenciado, considerar apenas o estabelecimento credenciado selecionado\.

Devem ser considerados apenas os registros da SAFX995 cujo Código do Meio de Pagamento \(COD\_MEIO\_PAGTO\) tenha sido parametrizado na tela de Parametrização do Meio de Pagamento \(considerar a composição completa da parametrização: Empresa, Estabelecimento, Modelo Documento, Número do Caixa e Código do meio de Pagamento\)\.

__Origem SAFX204:__

Serão considerados os registros da tabela SAFX204, cuja Data de Emissão compreenda o período parametrizado\. Se a geração for realizada por Estabelecimento Administrador, serão considerados os dados de todos os estabelecimentos credenciados associados ao administrador\. Se for selecionado um estabelecimento credenciado, considerar apenas o estabelecimento credenciado selecionado\.

__Origem SAFX205:__

Devem ser considerados os registros da SAFX07 e SAFX205 que atendam aos seguintes critérios:

  \- Estabelecimentos credenciados parametrizados,

  \- Data fiscal \(DATA\_FISCAL\) compreenda o período informado,

  \- Somente documentos fiscais de mercadoria \(classificação do documento = ‘1’ ou ‘3’\),

  \- Somente notas não canceladas,

  \- Modelo de documento = ‘55’ ou ‘65’,

  \-Somente notas de saída \(MOVTO\_E\_S = ‘9’\)\.

Se a geração for realizada por Estabelecimento Administrador, serão considerados os dados de todos os estabelecimentos credenciados associados ao administrador\. Se for selecionado um estabelecimento credenciado, considerar apenas o estabelecimento credenciado selecionado\.

Será gerado um relatório para cada estabelecimento credenciado\.

__Agrupamento__: Comprovante de Pagamento, Ponto de Venda \(PV\), Data da Transação\.

__Ordenação do relatório:__ Comprovante de Pagamento, Ponto de Venda \(PV\), Data da Transação\.

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

__Dados do Cabeçalho__

Data:

Data

Formato: 

DD/MM/AA

Informar a Data de Geração do Relatório\.

MFS1230

Pág\.:

Numérico

Este campo deve demosntrar o número da página atual\.

MFS1230

CNPJ:

Numérico

Exibir o CNPJ da tabela estabelecimento do estabelecimento credenciado, conforme relatório que está sendo emitido\.

MFS1230

Razão Social:

Texto

Corresponde ao campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO, do estabelecimento credenciado\.

MFS1230

Número do Estabelecimento:

Texto

Este campo deve ser preenchido com a informação do campo “N° de Cadastro do Estabelecimento Comercial”, criado na tela de “Identificação da Administradora”, localizado em: “Módulo: MasterSAF DW >> Estadual >> Portaria CAT87/06 – Protocolo ECF 04\-01, Menu: Parâmetros >> Identificação da Administradora”\. Caso não tenha sido informado, não será preenchido\.

MFS1230

Período:

Data

Formato: 

DD/MM/AA

Corresponde ao período incial e ao período final, informados na tela de critérios da geração do relátório\. Exemplo: Período: dd/mm/aaaa à dd/mm/aaaa

MFS1230

__Corpo do Relatório__

Comprovante de Pagamento

Texto

__Origem SAFX995:__

Nesta coluna deve exibir Número do Comprovante da tela de Detalhe dos Meios de Pagamento \(NUM\_COMPROVANTE –  SAFX995\)\.

__Origem SAFX204:__

Nesta coluna deve exibir o Comprovante de Pagamento da tela de Formas de Pagamento CFe \(NUM\_COMP\_PAG –  SAFX204\)\.

__Origem SAFX205:__

Nesta coluna deve exibir o Comprovante de Pagamento da tela de Formas de Pagamento NFe \(NUM\_COMP\_PAG –  SAFX205\)\.

Obs\.: Quando não houver a informação, deverá ficar em branco\.

MFS1230/ MFS11281

Ponto de Venda \(PV\)

Texto

__Origem SAFX995:__

Nesta coluna deve exibir o número do caixa da tela de Detalhe dos Meios de Pagamento \(COD\_CAIXA\_ECF – SAFX995\)\.

__Origem SAFX204:__

Nesta coluna deve exibir o Ponto de Venda da tela de Formas de Pagamento CFe \(NUM\_PONTO\_VENDA –  SAFX204\)\.

__Origem SAFX205:__

Nesta coluna deve exibir o Ponto de Venda da tela de Formas de Pagamento NFe \(NUM\_PONTO\_VENDA –  SAFX205\)\.

MFS1230/ MFS11281

Data da Transação

Data 

DD/MM/AAAA

__Origem SAFX995:__

Nesta coluna deve exibir a data de emissão da tela de Detalhe dos Meios de Pagamento do \(DATA\_EMISSAO – SAFX995\)\.

__Origem SAFX204:__

Nesta coluna deve exibir a data de emissão da tela de Formas de Pagamento CFe \(DATA\_EMISSAO –  SAFX204\)\.

__Origem SAFX205:__

Nesta coluna deve exibir a data fiscal da tela de Formas de Pagamento NFe \(DATA\_FISCAL –  SAFX205\)\.

MFS1230/ MFS11281

Valor Crédito

__Origem SAFX995:__

Somatório do campo Valor da Operação \(VLR\_PAGO – SAFX995\) dos registros cuja Natureza da Operação seja igual a “1 – Crédito”\.

__Origem SAFX204:__

Somatório do campo Valor da Operação \(VLR\_OPERACAO – SAFX204\) dos registros cuja Natureza da Operação seja igual a “1 – Crédito”\.

__Origem SAFX205:__

Somatório do campo Valor da Operação \(VLR\_OPERACAO – SAFX205\) dos registros cuja Natureza da Operação seja igual a “1 – Crédito”\.

MFS1230/ MFS11281

Valor Débito

__Origem SAFX995:__

Somatório do campo Valor da Operação \(VLR\_PAGO – SAFX995\) dos registros cuja Natureza da Operação seja igual a “2 – Débito”\.

__Origem SAFX204:__

Somatório do campo Valor da Operação \(VLR\_OPERACAO – SAFX204\) dos registros cuja Natureza da Operação seja igual a “2 – Débito”\.

__Origem SAFX205:__

Somatório do campo Valor da Operação \(VLR\_OPERACAO – SAFX205\) dos registros cuja Natureza da Operação seja igual a “2 – Débito”\.

MFS1230/ MFS11281

Total Dia dd/mm/aaaa

Este Total será exibido após o final do dia, demonstrando a quebra do dia, abaixo das colunas de Crédito e Débito o Total apurado por DIA\.

MFS1230

Total Mês mm/aaaa

Este Total será exibido após o final do dia, demonstrando a quebra do mês, abaixo das colunas de Crédito e Débito o Total apurado por MÊS\.

MFS1230

Total Ano AAAA

Este Total será exibido após o final do dia, demonstrando a quebra do ano, abaixo das colunas de Crédito e Débito o Total apurado por ANO\.

MFS1230

Total Relatório

Este Total será exibido após a quebra por estabelecimento, abaixo das colunas de Crédito e Débito o Total apurado no relatório\.

MFS1230

<a id="_Toc427154758"></a>

## Layout do Relatório

__Data: 13/09/2015__

 

__ __

__ __

__Página: 000001__

__CNPJ:  92754738000162__

__Razão Social: LOJAS RENNER \- MATRIZ__

__ __

__Número do Estabelecimento:__

__991__

 

__Período: 01/08/2015  a  31/08/2015__

__ __

 

__Comprovante de Pagamento__

__Ponto de Venda \(PV\)__

__Data da Transação__

__Valor Crédito__

__Valor Débito__

9999999999

999999

dd/mm/aaaa

999\.999,99

999\.999,99

9999999999

999999

dd/mm/aaaa

999\.999,99

999\.999,99

__Total Dia dd/mm/aaaa__

999\.999,99

999\.999,99

__Total Mês    mm/aaaa__

999\.999,99

999\.999,99

__Total Ano           aaaa__

999\.999,99

999\.999,99

__Total Relatório__

999\.999,99

999\.999,99

