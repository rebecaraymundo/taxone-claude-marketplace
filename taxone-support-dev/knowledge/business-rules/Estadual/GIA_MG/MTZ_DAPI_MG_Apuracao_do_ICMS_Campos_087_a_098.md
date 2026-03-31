# MTZ_DAPI_MG_Apuracao_do_ICMS_Campos_087_a_098

- **Fonte:** MTZ_DAPI_MG_Apuracao_do_ICMS_Campos_087_a_098.docx
- **Modificado:** 2024-09-19
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Estadual – GIA\-MG – DAPI\-MG

Apuração do ICMS – Linha Tipo 10

\* Vide módulo *Estadual >> ICMS*, menu *DATA MART >> Apuração do ICMS Ajuste SINIEF* e *DATA MART >> Livros Fiscais p/ Empresa c/ Insc\. Estadual Única  >> Apuração do ICMS – Convênio ICMS*\.

Em complemento às informações contidas neste documento, consulte demais itens correspondentes aos detalhamentos existentes na DAPI\-MG\.

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

CH72951

Pedro Nascimento

Chamado através do qual foram implementados ajustes no tamanho do campo de Número do Certificado para dados referentes ao Incentivo à Cultura, além disto, foi realizado certo para tratamento do campo de Saldo Credor do Período Anterior para o Incentivo à Cultura\.

OS3706

Juliana Garcia

Inclusão de itens no detalhamento Tipo 90 do campo “Estorno de Débitos” relativos à atividade de Comunicação e criação de campos do FEM\.

OS4662

Julyana Perrucini

Este documento tem como objetivo alterar a totalização do campo 95 da Apuração do ICMS \(Anexos\)\.

CH27262\_2014

Julyana Perrucini

Este documento tem como objetivo alterar o motivo do campo 90 da Apuração do ICMS\.

MFS507767

Rogério Ohashi

Alteração na regra da geração das Deduções de Incentivo à Cultura, para efetuar o cálculo independentemente se a linha 25 estiver preenchida\. 

MFS673243

Graciela Soares

Ajuste Regra Campo 98 – Incentivo à Cultura: ajuste no programa, que atualmente fixa o valor de 3% no cálculo do Valor limite para dedução, para utilizar o valor informado pelo usuário no campo “Alíquota de Dedução”

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

Regra geral:

Este documento tem por objetivo descrever as regras a serem aplicadas à geração dos dados relativos à apuração do ICMS para a DAPI\-MG, que compreende o conjunto de campos compreendidos de 087 a 098, assim relacionados:

- Créditos:
	- 087 – Saldo Credor do Período Anterior;
	- 088 – Por Entradas;
	- 089 – Outros Créditos;
	- 090 – Estorno de Débitos;
	- 091 – Total dos Créditos;
	- 092 – Saldo Credor para o Período Seguinte;
- Débitos:
	- 093 – Por Saídas;
	- 094 – Outros Débitos;
	- 095 – Estorno de Créditos;
	- 096 – Total dos Débitos;
	- 097 – Saldo Devedor Apurado;
	- 098 – Deduções\.

CH72951

RN01

__Campo 087 – Saldo Credor do Período Anterior__

Este será obtido a partir do RESUMO do livro de apuração do ICMS, representando o valor da linha 009 do livro\. Deve\-se observar que, de acordo com o tipo de escrituração adotada pela empresa, Normal ou Centralizada por Inscrição Estadual Única, os livros de origem serão o 108 ou 165 respectivamente\. \*

CH72951

RN02

__Campo 088 – Por Entradas__

O valor apurado das operações de entrada será obtido a partir da linha 43, que corresponde a soma das operações/prestações de entrada \(linhas 25, 35 e 42\)\. Para saber mais sobre a geração das linhas 16 a 43 verifica documento específico\.

CH72951

RN03

__Campo 089 – Outros Créditos__

Este representará a soma de outros créditos, informada no campo 072 – Total de Outros Créditos, e referente à soma dos campos 066 a 071 da DAPI\. Para maiores informações sobre esta geração observe documento específico para geração dos campos 066 a 071\.

CH72951

RN04

__Campo 090 – Estorno de Débitos__

O valor dos estornos de débitos será obtido a partir do RESUMO do livro de apuração do ICMS, representando o valor da linha 007 do livro\. Deve\-se observar que, de acordo com o tipo de escrituração adotada pela empresa, Normal ou Centralizada por Inscrição Estadual Única, os livros de origem serão o 108 ou 165 respectivamente\. \*

Note que na DAPI, o campo 090 representa a soma dos detalhamentos 3, informados através das linhas de código 22, contendo dados das notas fiscais com valor de estorno do ICMS\. O preenchimento destes detalhamentos poderá ser realizado através do menu “*Obrigações >> DAPI >> Manutenção >> Detalhamento*”, na aba com descrição “Campo 90”\.

Alternativamente a geração destes detalhamentos poderá ser realizada diretamente a partir das notas de saída registradas no sistema que contenham valor informado no campo “Valor de Estorno de ICMS” \(campo 234 da SAFX07\)\.

__\[ALTERADA – CH27262\_2014\]__

Quando o preenchimento destes detalhamentos for através da Manutenção, no campo: “Motivo”, deverá ser preenchido com:

Gravar 1 quando for “1 – Outros”

Gravar 2 quando for “2 – Estorno débito serviço transporte recolhido ST”

Gravar 3 quando for “3 – Estorno debito serviço comunicação \- Art\. 44\-E do Anexo IX do RICMS/02” 

Gravar 4 quando for “4 – Estorno debito serviço comunicação – Regime Especial”

Gravar 5 quando for “5 – Estorno Débito TTD”

Gravar 6 quando for “6 – Estorno de Débito Sub\-apuração\- Recolhimento Efetivo”

CH72951

CH27262\_2014

RN05

__Campo 090\.1 – Estorno do FEM__

Este valor não será gerado: o usuário deverá entrar com o valor na tela de manutenção\. Em caso de não possuir valor, preencher com zeros\.

OS3706

RN06

__Campo 091 – Total dos Créditos__

Este campo representa a soma total dos campos de créditos informados acima\.

CH72951

RN07

__Campo 092 – Saldo Credor para o Período Seguinte__

O valor deste campo deverá obrigatoriamente corresponder à diferença entre os campos 091 \(Total dos Créditos\) e 096 \(Total dos Débitos\), caso esta seja positiva, do contrário será preenchido com zero\.

CH72951

RN08

__Campo 093 – Por Saídas__

O valor apurado das operações de saída será obtido a partir da linha 65, que corresponde a soma das operações/prestações de saída \(linhas 51, 59 e 64\)\. Para saber mais sobre a geração das linhas 44 a 65 verifica documento específico\.

CH72951

RN09

__Campo 094 – Outros Débitos__

Este representará a soma de outros débitos, informada no campo 075 – Total de Outros Débitos, e referente à soma dos campos 073 a 074 da DAPI\.

CH72951

RN10

__Campo 095 – Estorno de Créditos__

__\[ALTERADA – OS4662\]__

Totalizar somando o Valor do Campo 95 – Estorno de Crédito do Detalhamento \(Linha Tipo 29 – Detalhamento 10\) independentemente do Motivo do Estorno\.

__Observação:__ Essa totalização é somente para rotina automática, ou seja, através da Geração dos Registros, então quando o usuário preencher o detalhamento manualmente deverá preencher a totalização manualmente\.

CH72951

OS4662

RN11

__Campo 096 – Total dos Débitos__

Este campo representa a soma total dos campos de débito informados acima\.

CH72951

RN12

__Campo 097 – Saldo Devedor Apurado__

O valor deste campo deverá obrigatoriamente corresponder à diferença entre os campos 096 \(Total dos Débitos\) e 091 \(Total dos Créditos\), caso esta seja positiva, do contrário será preenchido com zero\.

CH72951

RN13

__Campo 098 – Deduções__

O valor dos estornos de créditos será obtido a partir do RESUMO do livro de apuração do ICMS, representando o valor da linha 012 do livro\. Deve\-se observar que, de acordo com o tipo de escrituração adotada pela empresa, Normal ou Centralizada por Inscrição Estadual Única, os livros de origem serão o 108 ou 165 respectivamente\. \*

O valor para deduções será considerado apenas para estabelecimentos com apuração de Saldo Devedor, não cabendo aos estabelecimentos com Saldo Credor a ser transportado para o período seguinte\.

__\[ALTERAÇÃO\-MFS507767\]__ Alteração na regra da geração das Deduções de Incentivo à Cultura

O cálculo do valor de Deduções do período referente ao “Incentivo à Cultura”, é calculado conforme o somatório do campo de Valor Deduzido Mês Referência informado nas linhas do tipo 25, lançado no sistema através do menu *Obrigações >> DAPI >> Manutenção >> Detalhamento*, na aba “*Campo 98*”, subitem “*Incentivo à Cultura*”, a partir dessa demanda, o valor de “Incentivo à Cultura” do período, deverá ser calculado independentemente se a Linha 25 estiver preenchido ou não, com isso seguir conforme regra abaixo:

__Se__ o campo “Valor Deduzido Mês Referência” da Linha 25 da aba Campo 98, for maior que 0; \(somatório maior que zero – Incentivo = S\)

  __Se __o campo “Valor Deduzido Mês Referência” da Linha 25 da aba Campo 98, for igual 0; \(somatório igual à zero – Incentivo = N\)

__Regra do cálculo__

__\[ALTERAÇÃO\-__ MFS673243__\]__

 

“Valor Limite para dedução” = multiplicar o “Valor Limite” \* “Alíquota de Dedução”

  

__Se “__Incentivo à Cultura” = S, multiplicar o “Valor Limite” \* 0,03 

__Senão__ “Incentivo à Cultura” = N, multiplicar o “Valor Limite” \* “Alíquota de Dedução”

  

   __Obs\.:__ Valor Limite é igual ao Valor Outros = Campo 97

__Senão__ não preencher

CH72951

MFS507767

MFS673243

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

