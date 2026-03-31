# MTZ-GIA-RJ-Geracao_do_registro_0230_da_GIA-RJ_com_Valor_de_Abatimento_ZFM

- **Fonte:** MTZ-GIA-RJ-Geracao_do_registro_0230_da_GIA-RJ_com_Valor_de_Abatimento_ZFM.docx
- **Modificado:** 2022-08-03
- **Tamanho:** 30 KB

---

# Geração dos Registros da GIA\-RJ

##### DOCUMENTO DE REQUISITO

###### Data de Revisão

###### DR

###### Nome

__Descrição__

__Autor__

__Regras de Negócio__

OS2564

Geração do registro 0230 da GIA\-RJ com Valor de Abatimento ZFM\.

O objetivo deste documento de requisito é permitir que o campo “Valor de Isentas” do registro 0230 da GIA\-RJ recupere as informações do campo “Valor Abatimento não tributado” para a geração da GIA\-RJ\. 

Marcos Roberto de Oliveira

RN00, RN01 e RN02

OS2983

GIA\-RJ – Gerar Registro 0230 com os 6 últimos dígitos da NF

Este documento de requisito tem por objetivo permitir que o módulo GIA\-RJ recupere a informação para o campo Número da Nota Fiscal do registro 0230 truncando o mesmo à esquerda\. 

Marcos Roberto de Oliveira

RN03 e RN04

13/07/2010

OS2967

Lançamentos Complementares dos Registros 0140 a 0200

Criação do parâmetro que gera os registros por Lançamentos Complementar

Juliana Garcia

RN05 e RN06

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Após a apuração do ICMS, geração das notas fiscais remetidas da ZFM\-ALC, geração dos dados acessórios, valores de apuração por amparo/texto/ocorrência e dos registros o sistema deve recuperar para o campo “Parc\. Reduzir” da tela NF’s remetidas para ZFM\-ALC \(aba Complemento\) do módulo GIA RJ, a informação que estiver contida no campo 233 – VLR\_ABAT\_NTRIBUTADO da tabela SAFX07\.

OS2564

__RN01__

Gravar no campo “Valor de Isentas” do registro 0230 – Registro de Movimentação de Saídas para ZFM/ALC a informação que estiver contida no campo 233 – VLR\_ABAT\_NTRIBUTADO da tabela SAFX07\.

OS2564

__RN02__

O campo “Valor de Isentas” do registro 0230 – Registro de Movimentação de Saídas para ZFM/ALC não ira mais recuperar suas informações do Valor de Desconto como acontece atualmente,

OS2564

__RN03__

Recuperar para o campo Número da Nota Fiscal do registro __0230__ a informação do Número da Nota Fiscal truncando à esquerda, ou seja, recuperando o número da NF a partir do último dígito da direita até completar 6 \(seis\) posições\. Abaixo segue um exemplo de como recuperar a informação:

__Número da NF__

__Truncando à direita \(sistemática atual\)__

__Truncando à esquerda \(nova sistemática\)__

00257589

002575

257589

OS2893

__RN04__

Essa nova sistemática de geração do campo Número da Nota Fiscal do registro __0230 __deverá ser fixa no sistema\. Não existirá nenhum parâmetro para que o sistema se comporte dessa forma\.

OS2893

__RN05__

Parâmetro na tela de Geração dos Registros

Localização: Módulo 🡪 Estadual 🡪 GIA\-RJ

Menu: Obrigações 🡪 Geração 🡪 Geração dos Registros

Quando o parâmetro for habilitado atingirá os seguintes registros 0140 \(outros débitos\), 0150 \(estorno de crédito\), 0160 \(outros créditos\), 0170 \(estorno de débito\), 0180 \(deduções\), 0190 \(oper\. c/ prazo especial\), 0200 \(outros icms devido\. A partir da criação deste parâmetro no módulo da GIA\-RJ, a regra para demonstrar a montagem dos registros, passa a ser:

- Criar o parâmetro “Gerar registro por item de Lançamento Complementar do ICMS” e trazer “desmarcado”\.
- Se parâmetro Gerar registro por item de Lançamento Complementar do ICMS desmarcado:

Manter a funcionalidade da tabela EST\_GIA\_INFO, agrupar os lançamentos complementares da apuração do ICMS, pelo campo COD\_AMPARO\_LEGAL e COD\_SUB\_ITEM\_OCORR, totalizando o campo VLR\_OUTROS\. \(conforme funcionamento atual\);

- Se parâmetro Gerar registro por item de Lançamento Complementar do ICMS marcado:

Retirar os agrupamentos da rotina referente aos lançamentos complementares da apuração do ICMS, atualmente pelos campos COD\_AMPARO\_LEGAL e COD\_SUB\_ITEM\_OCORR\. A rotina deverá mostrar um registro para cada lançamento complementar de ICMS, mesmo que o código de amparo seja igual e a descrição diferente\. O campo VLR\_OUTROS na tabela EST\_GIA\_INFO não poderá ser totalizado\.

OS2967

__RN06__

__Geração dos Registros__

Localização: Módulo 🡪 Estadual 🡪 GIA\-RJ

Menu: Obrigações 🡪 Geração 🡪 Geração dos Registros 

A procedure SAF\_GERA\_GIA\_RJ sofrerá alteração dos agrupamentos/“desagrupamentos” e quando usar os registros na tabela EST\_RJ\_GIA\_R140\_2 para montar o arquivo texto, deverá obedecer ao critério do parâmetro “Gerar registro por item de Lançamento Complementar do ICMS” para os Registros 0140 a 0200\.

Parâmetro marcado: A rotina deverá gravar um registro para cada lançamento complementar de ICMS, mesmo que o código de amparo seja igual e a descrição diferente\.

Parâmetro desmarcado: Manter a mesma funcionalidade, agrupar os lançamentos complementares da apuração do ICMS, pelo campo COD\_AMPARO\_LEGAL e COD\_SUB\_ITEM\_OCORR, totalizando o campo VLR\_OUTROS da tabela EST\_GIA\_INFO \.

OS2967

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

