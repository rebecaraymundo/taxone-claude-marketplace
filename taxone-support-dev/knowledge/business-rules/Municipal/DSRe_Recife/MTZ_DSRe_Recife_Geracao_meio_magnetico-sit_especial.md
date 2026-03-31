# MTZ_DSRe_Recife_Geracao_meio_magnetico-sit_especial

- **Fonte:** MTZ_DSRe_Recife_Geracao_meio_magnetico-sit_especial.docx
- **Modificado:** 2026-03-09
- **Tamanho:** 42 KB

---

# Recife \- DSRe

# Geração do meio magnético p/ estabelecimentos fora do município em questão 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__MFS\-1037617__

Este documento tem como objetivo criar a geração do meio magnético para os segmentos de Construção Civil, Utilities e Telecom para os municípios atendidos pelo validador DSRe\.

__MFS\-1057892__

Rosemeire Santos

Alteração da geração do arquivo para desconsiderar as notas fiscais de prestadores de dentro do município para notas fiscais eletrônicas\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo “Recife” deve ficar localizado no grupo “Municipal”\.

 A descrição funcional do módulo será: “O módulo irá gerar o meio magnético permitindo a importação de notas fiscais convencionais recebidas para o Sistema de Notas Fiscais de Serviço Eletrônicas\.”

__MFS\-1037617__

__RN02__

__Regra p/ inclusão do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “PE” e ao código de município do IBGE igual a “11606” \(Recife\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Recife, Pernambuco\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS\-1037617__

__RN03__

__Estrutura de menus do módulo DSRe:__

Deverão ser criado o seguinte menu e sub\-menus no módulo DSRe:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__

__MFS\-1037617__

__RN04__

__Regra de criação do nome do arquivo__

__Serviços Tomados:__

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__MMAAAA__: representa a data inicial da geração\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\.TXT

           

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_ MMAAAA\_ MMAAAA\.TXT__, onde:

       __ST__: Apenas registros de serviços tomados\.

__MMAAAA__: representa a data inicial da geração

__MMAAAA:__ mês da competência referente à nota gerada\.   

       __MUNICIPIO__: representa a obrigação que está sendo gerada\. 

__       ESTABELECIMENTO: __Representa o tomador de serviço

__       EMPRESA: __Representa o tomador de serviço

__       \.TXT__: extensão do arquivo

Ex: ST\_EMPRESA\_ESTABELECIMENTO\_MUNICIPIO\_012010\_012010\.TXT

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

__ MFS\-1037617__

RN05

__Regra p/ tela da Geração do Meio Magnético__

A tela de geração do meio magnético deve exibir os seguintes campos:

Data Inicial: O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE\.

Data Final: O campo deve ser um text Box com a seguinte máscara: DD/MM/AAAA\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE\. 

Quebrar arquivo por Data de Emissão: deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

Se o usuário informar uma data que ultrapasse o último dia do mês preenchido na data inicial, o sistema deve exibir a seguinte mensagem no log de processo: “A data final digitada ultrapassa o último dia do mês informado na data inicial\. Favor preencher uma data final válida\.” E deve interromper a geração\.

Estabelecimento: o sistema deve exibir os estabelecimentos pertencentes ao município do Recife, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS\-1037617__

__RN06__

__Regra de Estrutura e Disposição de cada registro no arquivo__

Registro Tipo 10 \(Obrigatório\): Uma linha de cabeçalho\. Primeira linha do arquivo\.

Registro Tipo 40 \(Opcional\): Zero ou mais linhas de detalhe\. Cada linha corresponde a uma Nota Fiscal Convencional Recebida\.

Registro Tipo 90 \(Obrigatório\): Uma linha de rodapé\. Última linha do arquivo\.

__MFS\-1037617__

__RN07__

__Regra de formatação do arquivo__

Todos os campos numéricos deverão ser preenchidos alinhados pela direita e sem formatação \(sem ponto e sem vírgula\)\. Se necessário, preencher com zeros à esquerda até completar seu tamanho máximo\. Quando o campo for opcional, ou seja, o conteúdo do campo não seja fornecido, este deverá ser preenchido com zeros até completar seu tamanho máximo\.

Todos os campos alfanuméricos deverão ser preenchidos alinhados pela esquerda\. Se necessário, preencher com espaços em branco à direita até completar seu tamanho máximo, com exceção do campo de Discriminação dos Serviços da linha de detalhe do registro 40\. Quando o campo for opcional, ou seja, quando o conteúdo do campo não é fornecido, este deverá ser preenchido com espaços em branco até completar seu tamanho máximo\.

__MFS\-1037617__

__RN08__

__Regra do Registro Tipo 40 – Declaração Eletrônica de Serviços Recebidos__

Recuperar notas com as seguintes características:

- Nota de Entrada \(movto\_e\_s <> ‘9’\)
- Classificação do Documento fiscal = 2 ou 3
- Empresa e estabelecimentos escolhidos na tela de geração

__\[ALTERADA – CH15059\_2016\]__

__\[ALTERADA \- CH20796\_2017 \(MFS\-16040\)\]__

- Data fiscal de emissão dentro do período de referência \[*Observação:* O chamado 15059 foi retificado pela Maíra\]

__\[ALTERADA – CH9089\_2016\]__

- Para considerar notas fiscais eletrônicas verificar: 

\- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do módulo selecionado para geração \(COD\_MUNICIPIO da tabela ESTABELECIMENTO\), recuperar os documentos com uma das situações abaixo:

             \- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’\) __OU__

             \- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\)

__\[ALTERADA \- MFS\-1057892\] \- __Tratamento das notas fiscais eletrônicas

- Para considerar notas fiscais eletrônicas verificar:
- Se o parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada”\*\* estiver marcado
- Se o município do prestador \(campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR\) for __DIFERENTE__ do município do da inscrição eventual \(x156\) selecionado para geração, recuperar os documentos com uma das situações abaixo:
- Modelo do Documento \(campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL = ‘55’ ou 70\) __OU__
- Indicador de Tipo de Documento para Nota Fiscal Eletrônica \(campo IND\_NF\_ELETRONICA da SAFX2005 = ‘S’\) referente ao tipo de documento da nota fiscal\.

\*\* “Parâmetro “Desconsiderar Notas Fiscais Eletrônicas de Entrada” \- Menu: Parâmetros por Município > Parâmetros > Notas Fiscais Eletrônicas\.

__MFS\-1057892__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

