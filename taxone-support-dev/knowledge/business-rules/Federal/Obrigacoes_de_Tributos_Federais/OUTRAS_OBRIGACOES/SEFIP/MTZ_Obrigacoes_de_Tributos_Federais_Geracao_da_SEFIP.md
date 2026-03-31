# MTZ_Obrigacoes_de_Tributos_Federais_Geracao_da_SEFIP

- **Fonte:** MTZ_Obrigacoes_de_Tributos_Federais_Geracao_da_SEFIP.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 31 KB

---

# Obrigações de Tributos Federais \- Geração do Meio Magnético SEFIP

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH113756\-A

Obrigações de Tributos Federais \- Geração do Meio Magnético SEFIP

Este chamado de alteração de regra de negócio tem por objetivo determinar quais Códigos de Pagamento de INSS podem fazer parte da SEFIP\.

OS4658

Geração do Meio Magnético SEFIP

Centralização das informações por estabelecimento Matriz

CH24869\_2014

Ajustar geração do SEFIP

Este documento tem como objetivo ajustar a geração do SEFIP para considerar os registros de acordo com o Período de Competência preenchido\.

CH14786\_2017

\(MFS\-13535\)

Ajuste na geração da SEFIP no campo Ocorrência\.

Este documento tem como objetivo realizar o tratamento para o campo ocorrência do trabalhador na geração da SEFIP visando o preenchimento do campo 37 da SAFX no cadastro da pessoa física/jurídica\.

CH16851\_2017

\(MFS\-13539\)

Ajuste no registro 30 da geração do arquivo magnético da SEFIP\.

Essa alteração tem como objetivo gerar no meio magnético a informação de CNPJ quando este prestador é classificado como \(MEI\) para levar as informações como realizado para Pessoa Física\.

## REGRAS DE NEGÓCIO

__RN01__

Ao gerar o meio magnético da SEFIP, o sistema deverá verificar o Código de Pagamento de INSS na tabela IRT\_COD\_PG\_INSS\. Essa tabela é alimentada pela TFIX34\.

Caso o Código de Pagamento de INSS esteja com o campo IND\_AUTONOMO = “N”, essa informação não deverá ser gerada na SEFIP \(arquivo\) e nem no relatorio contendo as informações do arquivo gerado\.

Somente os Códigos de Pagamento de INSS cujo campo IND\_AUTONOMO = “S” é que devem ser gerados no arquivo\.

__CH113756\-A__

__RN02__

Campo Centralização por estabelecimento Matriz

Tipo Checkbox

Não Obrigatório

Default não selecionado

Quando selecionado, a centralização das informações será por estabelecimento matriz, ou seja, deverá gerar um único registro “10”, correspondente a matriz, com as informações dos estabelecimentos centralizados\.

Obs: Este campo será habilitado somente quando o Radio Button “empresa” do campo “Processar dados Por” estiver selecionado, na tela de “Geração Meio Magnético”\.

__OS4658__

__RN02__

Após a geração dos registros, a geração do MM SEFIP deve considerar a recuperação desses registros, considerando os Documentos Fiscais que estejam dentro do Período de Competência preenchido na tela de geração \(verifica pela data fiscal da NF\) e ainda compreendendo a parametrização da Data de Vigência em Federal >> OTF >> Outras Obrigações >> SEFIP >> Parâmetros, ou seja, se estiver parametrizado dentro do Período de Competência considerar o parâmetro, caso contrário não gerar e emitir a mensagem no log: “Status: Alerta \- Req 10 \- Inf\. Empresa: Não há informações de parâmetros da Sefip p/ o estabelecimento <<levar código do estabelecimento selecionado>>”\.

__CH24869\_2014__

__RN03__

__Ocorrência: __Recuperar a informação do__ __cadastro da PFJ \(SAFX04, campo 37\)\. 

Se o cadastro for vinculado a mais de uma Nota Fiscal de mais de um estabelecimento no período, geraremos o código correspondente a mais de um vínculo na geração da \(Obrigações de Tributos Federais >> Outras Obrigações  >> SEFIP >> Geração do Meio Magnético\)\.

  
Se código = __‘00’__ \- Sem exposição a agente nocivo\. Trabalhador nunca esteve exposto E Cadastro da PFJ vinculado em NFs de mais de um estabelecimento no período, geraremos >> ‘__05’__ \- Não exposto a agente nocivo \- Trabalhador com mais de um vinculo Empregatício\. 

Se código = __‘01’__ \- Não exposição a agente nocivo\. Trabalhador já esteve exposto, não altera\.

  
Se código = __’02’__ \- Exposição a agente nocivo \(aposentadoria especial aos 15 anos de trabalho\) E Cadastro da PFJ vinculado em NFs de mais de um estabelecimento no período, geraremos >> ‘__06’__ \- Exposição a agente nocivo \(aposentadoria especial aos 15 anos de trabalho\) \- Trabalhador com mais de um vinculo Empregatício\.

  
Se código = __‘03’__ \- Exposição a agente nocivo \(aposentadoria especial aos 20 anos de trabalho\) E Cadastro da PFJ vinculado em NFs de mais de um estabelecimento no período, geraremos >> __‘07’__ \- Exposição a agente nocivo \(aposentadoria especial aos 20 anos de trabalho\) \- Trabalhador com mais de um vinculo Empregatício;

  
Se código = __‘04__’ \- Exposição a agente nocivo \(aposentadoria especial aos 25 anos de trabalho\) E Cadastro da PFJ vinculado em NFs de mais de um estabelecimento no período, geraremos >> __‘08’__ \- Exposição a agente nocivo \(aposentadoria especial aos 25 anos de trabalho\) \- Trabalhador com mais de um vinculo Empregatício;

Formato: 9

Tamanho: 2 posições

Tipo: Numérico

__CH1786\_2017__

__\(MFS\-13535\)__

__RN04__

__Registro 30 – Geração do Meio Magnético SEFIP__

Federal > Obrigações de Tributos Federais > Outras Obrigações > SEFIP > Geração Magnético

Se o campo CPF\_CGC da tabela SAFX04 possuir 14 posições \(CNPJ\) E o campo IND\_CLASSE\_EMP for igual = ‘05’ E o campo CATEGORIA\_TRAB = ‘13’, o sistema deverá levar os dados do CNPJ desse prestador de serviços \(MEI\) na geração do meio Magnético da SEFIP, como realizado para pessoa Jurídica\.

__CH16851\_2017__

__\(MFS13539\)__

