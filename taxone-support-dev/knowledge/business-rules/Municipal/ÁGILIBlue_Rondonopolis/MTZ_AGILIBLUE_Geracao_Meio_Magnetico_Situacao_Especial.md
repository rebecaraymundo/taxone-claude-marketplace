# MTZ_AGILIBLUE_Geracao_Meio_Magnetico_Situacao_Especial

- **Fonte:** MTZ_AGILIBLUE_Geracao_Meio_Magnetico_Situacao_Especial.docx
- **Modificado:** 2025-11-27
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Municipal

                                  [ÁGILIBlue](http://www.rondonopolis.mt.gov.br/servicos/nfse/infos-web-service-nfse-agiliblue/) 

Declaração de serviços de prestadores estabelecidos fora do município\.

DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-708439

Rosemeire Santos

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador ÁGILIBlue\.

__REGRAS DE NEGÓCIO__

__CÓD__

__DESCRIÇÃO__

__MFS/CH__

RN01

__Estrutura de menus do módulo __[__ÁGILIBlue__](http://www.rondonopolis.mt.gov.br/servicos/nfse/infos-web-service-nfse-agiliblue/)__:__

Deverão ser criados os seguintes menus e sub\-menus no módulo [ÁGILIBlue](http://www.rondonopolis.mt.gov.br/servicos/nfse/infos-web-service-nfse-agiliblue/):

- Obrigações
	- Geração do Meio Magnético
	- Geração – Arquivo de Entradas de Serviços \(Const\. Civil/Utilities/Telecom\)
- Janela
- Ajuda 

MFS\-708439

RN02

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__       ST\_AGILIBLUE\_MUNICIPIO\_DDMMAAAA\.TXT__, onde:

       __ST\_AGILIBLUE__: representa a obrigação que está sendo gerada\. 

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __DDMMAAAA__: representa a data inicial da geração

       __\.TXT__: extensão do arquivo\.

*Exemplo:* ST\_AGILEBLUE\_RONDONOPOLIS\_01012010\.TXT

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_AGILIBLUE\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.TXT__, onde:

__        ST\_AGILIBLUE__: representa a obrigação que está sendo gerada\.    

__        MUNICIPIO__: representa o município que está sendo gerado\.   

        __DDMMAAAA__: representa a data inicial da geração\.   

__        MMAAAA:__ mês da competência referente à nota gerada

        __\.TXT__: extensão do arquivo\.

Ex: ST\_AGILIBLUE\_RONDONOPOLIS\_01012014\_122013\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

MFS\-708439

RN03

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS\-708439

RN04

__Regras referentes à formatação dos registros gerados no meio magnético:__

O arquivo a ser gerado para ser importado no ÁGILIBlue NFS\-e precisa ser no formato texto \(__TXT__\) e na codificação “__UTF\-8__” e apresentar o tipo de registro conforme o layout deste documento\. É obrigatório ter no mínimo 1 registro no arquivo\. 

- 
	1. __Considerações de preenchimento de campos do layout:__
- Campo de formato numérico deverá ser preenchido com zeros à esquerda para completar o tamanho deste\. Preenchendo assim toda a posição disponibilizada para ele no arquivo\. 
- Campo de formato alfanumérico deverá ser preenchido com brancos à direita para completar o tamanho deste\. Preenchendo assim toda a posição disponibilizada para ele no arquivo\. 
	- Para campo que não tenha conteúdo para ser preenchido ao gerar o arquivo, deve seguir as regras abaixo: 

1\. Campo numérico deve ser preenchido com zeros: a\. Se o campo é tamanho N \(005\), deverá ser preenchido com “00000” \(5 zeros\)\. 

2\. Campo alfanumérico deve ser preenchido com espaços\. a\. Se o campo é tamanho A \(005\), deverá ser preenchido com “ “ \(5 espaços em branco\)\. 

MFS\-708439

RN05

__Regra p/ Recuperação das notas fiscais de serviços tomados \(só geraremos serviços tomados no arquivo\)\.__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Situação <> ‘S’

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS\-708439

### INCLUSÃO – MANAGER

