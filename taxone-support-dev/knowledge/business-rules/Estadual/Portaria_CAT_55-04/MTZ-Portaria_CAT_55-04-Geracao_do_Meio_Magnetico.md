# MTZ-Portaria_CAT_55-04-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-Portaria_CAT_55-04-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2026-02-20
- **Tamanho:** 55 KB

---

# Portaria CAT 55/04 \- Gerar Meio Magnético da Portaria CAT 55/04

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Autor__

__OS2768\-N/__

Portaria CAT 55/04 \- Gerar Meio Magnético da Portaria CAT 55/04

Gerar as faturas de Energia Elétrica referentes aos Documentos Fiscais de Utilities no arquivo do meio magnético da Portaria CAT 55/04 considerando quando o mês/ano de cancelamento é maior que o mês/ano de vencimento e quando as hipóteses estão informadas\.

Marcos Roberto de Oliveira

__CH102141__

Portaria CAT 55/04 \- Gerar Meio Magnético da Portaria CAT 55/04

Totalizar os campos:

Campo 09 – Valor Total \(com 2 decimais\)

Campo 10 – BC ICMS \(com 2 decimais\)

Campo 11 – ICMS \(com 2 decimais\)

Vanessa W\. Bravo

__CH100650__

Convênio ICMS 30/2004

Convênio ICMS 30/2004

Vanessa W\. Bravo

__CH100237__

Portaria CAT 55/2004

Alteração da informação do campo Código de Usuário Final

Vanessa W\. Bravo

__OS3424\-E__

Portaria CAT 55/2004

Gerar as faturas de Energia Elétrica referentes aos Documentos Fiscais de Utilities no arquivo do meio magnético da Portaria CAT 55/04 considerando quando o mês/ano de cancelamento é maior que o mês/ano de vencimento e quando as hipóteses estão informadas\.

Ajuste conforme Decreto 57\.177/2011

Vanessa W\. Bravo

__CH420\_2013__

Convênio ICMS 30/2004

Correção na geração para outras UF’s

Vanessa W\. Bravo

__OS3879__

Portaria CAT 154/2012

Remoção da regra do chamado 420/2013

Marcos

__CH420\-B\_2013__

Convênio ICMS 30/2004

Ajustar regra de geração do arquivo da Portaria CAT 55/04 – Convênio 30/04 para que considere registros cuja Data do Cancelamento compreenda o período de geração, mas que tenham emissão em mês anterior\.

Marcos

__CH420\-D\_2013__

Portaria CAT 55/04 – Convênio ICMS 30/04

Alteração na regra de geração do arquivo da Portaria CAT 55/04 – Convênio 30/04 para que considerar registros cuja Data do Cancelamento compreenda o período de geração, mas que tenham emissão em meses anteriores\.

Julyana Perrucini

__Observação__

__TKT 165580__

A portaria válida é a 154/12

A Portaria CAT 55/04 foi revogada pela Portaria SRE 14/22\.  
O documento correto é: [MTZ\-Geracao\_Arquivo\_CAT154\_12\.doc](https://trten.sharepoint.com/:w:/r/sites/REQ_MTZ/_layouts/15/Doc.aspx?sourcedoc=%7B176B6544-A376-46CE-92F1-09E9EDA9D00D%7D&file=MTZ-Geracao_Arquivo_CAT154_12.doc&action=default&mobileredirect=true&DefaultItemOpen=1)

Andrea Rocha / Lyene Benvenutti

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Módulo:__ Estadual → Portaria CAT 55/04 – Convênio 30/04

__Menu:__ Meio Magnético → Geração

Em São Paulo, a apuração do ICMS dos documentos fiscais de Energia Elétrica é realizada pela Data de Vencimento das Faturas, ao contrário de outros estados cuja apuração é realizada de outra forma\. Em algumas situações esses documentos fiscais de Energia Elétrica são cancelados no mês posterior ao mês de vencimento fazendo com que os mesmos sejam gerados no Convênio ICMS 115/03 como cancelados e não com status de documento normal, visto que essa era a situação na época do vencimento\. Para corrigir essa situação foi criada a OS2768\-M que altera a sistemática de geração do convênio, para que os Documentos Fiscais de Energia Elétrica que estejam cancelados sejam gerados corretamente\. Além disso, a Geração Automática dos Mapas Resumo também foi alterada para considerar essa nova sistemática\.

Em contrapartida, a geração do meio magnético Portaria CAT 55/04 exibirá essas faturas canceladas ajustando essa informação para a Secretaria da Fazenda do estado de São Paulo\. A regra deverá ser da seguinte forma:

- UF do Estabelecimento = São Paulo
- NF cujo modelo seja 06 – Energia Elétrica \(campo 13 da SAFX42\)
- NF com situação Cancelada \(campo 30 da SAFX42\)
- Mês/Ano de Cancelamento é maior que o Mês/Ano de Vencimento \(campo 56 > 32 da SAFX42\)

OU

- Mês/Ano de Cancelamento é igual ao Mês/Ano de Vencimento \(campo 56 = 32 da SAFX42\) E se existe NF Substituta \(campo 79 da SAFX42\) E se a hipótese de estorno é 1, 2, 3 ou 4 \(campo 81 da SAFX42\)

__GERAR FATURA NA PORTARIA CAT 55/04 __             Caso contrário            __NÃO GERAR FATURA NA PORTARIA CAT 55/04__\.

__OS2768\-N__

__RN02__

A fatura deverá ser gerada na Portaria CAT 55/04 de acordo com o layout pré\-definido na legislação, conforme segue abaixo:

__Nº__

__Conteúdo__

__Formato__

__Tamanho máximo__

01

Número da NFCEE estornada

N

9

02

Série da NFCEE estornada

X

3

03

Data de emissão

D

12

04

Data de vencimento

D

12

05

CNPJ ou CPF

X

14

06

IE

X

14

07

Razão Social

X

35

08

Código de Identificação do Cliente

X

12

09

Valor Total \(com 2 decimais\)

V

\-

10

BC ICMS \(com 2 decimais\)

V

\-

11

ICMS \(com 2 decimais\)

V

\-

12

Número da NFCEE substituta

N

9

13

Série da NFCEE substituta

X

3

14

Hipótese de estorno

N

1

15

Motivo do estorno

X

200

__OS2768\-N__

__RN03__

Os campos abaixo devem ser totalizados ao final do relatório\.

Módulo estaduais → Portaria CAT 55/04 → Geração → Meio Magnético

Campo 09 – Valor Total \(com 2 decimais\)

Campo 10 – BC ICMS \(com 2 decimais\)

Campo 11 – ICMS \(com 2 decimais\)

__CH102141__

__RN04__

__Regra para mudar o nome do módulo:__

Alterar o nome do módulo de Portaria CAT 55/04 para __Portaria CAT 55/04 – Convênio 30/04\.__

 

__CH100650__

__RN05__

__Regra para mudar item de menu:__

Alterar item de menu Estadual → Portaria CAT 55/04 para Estadual → __Portaria CAT 55/04 – Convênio 30/04\.__

 

__CH100650__

__RN06__

__EXCLUÍDA Regra para inclusão de parâmetro Portaria CAT 55/04:__

Incluir o parâmetro, na tela Geração Meio Magnético: __Portaria CAT 55/04__

Este parâmetro deve estar selecionado por default\.

A geração desse parâmetro deverá ser conforme geração atual, tendo o fato gerador o campo 32 \- DAT\_VENCTO \(safx42\)\.

__CH100650__

__RN07__

__EXCLUÍDO Regra para inclusão de parâmetro Convênio 30/04:__

Incluir o parâmetro, na tela Geração Meio Magnético: __Convênio 30/04__

A geração desse parâmetro deverá ser conforme geração atual, porém deve ter como fato gerador o campo 03 \- DAT\_FISCAL \(safx42\)\.

Quando este campo for selecionado, desmarcar automaticamente o parâmetro Portaria CAT 55/04\.

__CH100650__

__RN08__

__Regra para mudar o log de erros:__

Na aba Log: alterar o nome do Relatório de Log de Erros Meio Magnético \- Portaria CAT 55/04 para __Relatório de Log de Erros Meio Magnético \- Portaria CAT 55/04 – Convênio 30/04\.__

__CH100650__

__RN09__

__Regra para mudar a etiqueta:__

Na aba Etiqueta: alterar o nome de Regisrto Portaria CAT 55/04, de 24/09/2004 para __Registro Portaria CAT 55/04 – Convênio 30/04\.__

__CH100650__

__RN10__

__Regra para inclusão de fleg:__

Inclusão de dois flegs no seguinte caminho:

Estadual → Portaria CAT 55/04 – Convênio 30/04 → Meio Magnético → Geração

Flegs a serem incluídos:

Código de Identificação do Cliente:  

     

- Código Usuário Final
- Número Medidor

Essa nova parametrização deverá ficar abaixo do campo STATUS\.

Os flegs devem ficar por default desmarcados, porém é parametrização obrigatória para geração do arquivo\.

__CH103237__

__RN11__

__Regra para o fleg CÓDIGO USUÁRIO FINAL:__

Quando o usuário selecionar este campo, o arquivo deve recuperar a informação do campo 42 \- COD\_USU\_FINAL, da SAFX42\.

A informação desse campo deverá preencher o campo 8 do meio magnético\.

__CH103237__

__RN12__

__Regra para o fleg NÚMERO MEDIDOR:__

Quando o usuário selecionar este campo, o arquivo deve recuperar a informação do campo 86 \- NUM\_MEDIDOR, da SAFX42\.

A informação desse campo deverá preencher o campo 8 do meio magnético\.

__CH103237__

__RN13__

__\[CH420\-B/2013\]__

__ __

__Módulo: Estadual → Portaria CAT 55/04 – Convênio 30/04__

__Menu: Meio Magnético → Geração__

__ __

Em São Paulo, a apuração do ICMS dos documentos fiscais de Energia Elétrica é realizada pela Data de Vencimento das Faturas, ao contrário de outros estados cuja apuração é realizada de outra forma\. Em algumas situações esses documentos fiscais de Energia Elétrica são cancelados no mês posterior ao mês de vencimento fazendo com que os mesmos sejam gerados no Convênio ICMS 115/03 como cancelados e não com status de documento normal, visto que essa era a situação na época do vencimento\. Para corrigir essa situação foi criada a OS2768\-M que altera a sistemática de geração do convênio, para que os Documentos Fiscais de Energia Elétrica que estejam cancelados sejam gerados corretamente\. Além disso, a Geração Automática dos Mapas Resumo também foi alterada para considerar essa nova sistemática\.

 

Em contrapartida, a geração do meio magnético Portaria CAT 55/04 exibirá essas faturas canceladas ajustando essa informação para a Secretaria da Fazenda do estado de São Paulo\.

 

Com a publicação do Decreto 57\.177/2011 esse cenário mudou\. A apuração passa a ser pela data fiscal, e não mais pela data de vencimento\.

A regra deverá ser da seguinte forma:

 

Quando o campo 13 \- COD\_MODELO \(SAFX42\) = ‘06’, UF Estabelecimento = SP, UF Destinatário = SP \(campo UF da SAFX04\), verificar:

 

\- Se campo 21 \- SITUACAO \(SAFX42\) = ‘S’;

\- Se campo 03 \- DAT\_FISCAL \(SAFX42\) tiver data até 31\.12\.2011, a escrituração deve ser pela data de vencimento, ou seja, pelo campo 32 da SAFX42;

\- Se campo 03 \- DAT\_FISCAL \(SAFX42\) tiver data a partir de 01\.01\.2012, a escrituração deve ser pelo campo 03 \(SAFX42\)\.

\- Se o campo 03 \- Data de Emissão/Escr\. Fiscal \(DAT\_FISCAL\) da SAFX42 tiver data até 31\.12\.2011, considerar registros cujo campo 56 \- Data do Cancelamento \(DAT\_CANCELAMENTO\) compreenda o período de geração e o campo 32 \- Data de Vencimento \(DAT\_VENCTO\) seja de meses imediatamente anteriores ao do cancelamento, restringindo a seleção a documentos que tenham o campo 21 – SITUACAO com conteúdo igual a “S”\.

\- Se o campo 03 \- Data de Emissão/Escr\. Fiscal \(DAT\_FISCAL\) da SAFX42 tiver a partir de 01\.01\.2012, considerar registros cujo campo 56 \- Data do Cancelamento \(DAT\_CANCELAMENTO\) compreenda o período de geração e o campo 03 \- Data de Emissão/Escr\. Fiscal \(DAT\_FISCAL\) seja de meses imediatamente anteriores ao do cancelamento, restringindo a seleção a documentos que tenham o campo 21 – SITUACAO com conteúdo igual a “S”\.

\(__exemplo do último item especificado:__

- Se na geração a tomada de crédito tem referência 08/2013:
	- Então o cancelamento vai compreender dentro desse período 01/08/2013 a 31/08/2013 __E__ a data fiscal vai compreender qualquer período anterior a da geração, ou seja, <= 31/07/2013\)\.

 

__Obs__\.: A UF Destinatário deve ser = SP em virtude de negócios, pois o estabelecimento é situado em SP, porém comercializa energia elétrica para outra UF, como por exemplo as cidades que se localizam em divisas\.

__Obs__\.: A regra acima deve ser válida para reprocessamento

 

Quando o campo 13 \- COD\_MODELO \(SAFX42\) = ‘06’, UF Estabelecimento <> SP __OU__ campo 13 \- COD\_MODELO \(SAFX42\) = ‘06’, UF Estabelecimento = SP, UF Destinatário <> SP \(campo UF da SAFX04\), verificar:

 

\- Se campo 21 \- SITUACAO \(SAFX42\) = ‘S’;

\- Se campo 03 \- DAT\_FISCAL \(SAFX42\) compreende o período de geração do arquivo\.

\- Considerar registros cujo campo 56 \- Data do Cancelamento \(DAT\_CANCELAMENTO\) compreenda o período de geração e o campo 03 \- Data de Emissão/Escr\. Fiscal \(DAT\_FISCAL\) seja de meses imediatamente anteriores ao do cancelamento, restringindo a seleção a documentos que tenham o campo 21 – SITUACAO com conteúdo igual a “S”\.

 

__OS3424\-E/ CH420\_2013/__

__OS3879__

__CH420\-B\_2013__

__CH420\-D\_2013__  
__ __

\(__exemplo do item especificado para UF de SP:__

- Se na geração a tomada de crédito tem referência 08/2013:
	- Então o cancelamento vai compreender dentro desse período 01/08/2013 a 31/08/2013 __E__ a data fiscal vai compreender qualquer período anterior a da geração, ou seja, <= 31/07/2013\)\.

Se houver fatura nas condições acima, GERAR FATURA NA PORTARIA CAT 55/04, atendendo ao solicitado no Convênio 30/04\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

