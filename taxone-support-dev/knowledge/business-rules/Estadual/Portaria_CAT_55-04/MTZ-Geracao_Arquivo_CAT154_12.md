# MTZ-Geracao_Arquivo_CAT154_12

- **Fonte:** MTZ-Geracao_Arquivo_CAT154_12.docx
- **Modificado:** 2026-02-20
- **Tamanho:** 44 KB

---

# Regras de Geração do Arquivo da Portaria CAT 154/12

<a id="_Hlk211962241"></a>Módulo: Estadual <a id="_Hlk211962074"></a>> Portaria CAT 55/04 – Convênio 30/04

Caminho: Meio Magnético > <a id="_Hlk211962194"></a>Geração

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3879

Marcos G\. de Paula

Definição das regras para geração do arquivo da Portaria CAT 154/12\.

CH32690\_2012

Marcos G\. de Paula

Ajuste na regra de seleção do Registro 2\.

CH32690\-C\_2012

Julyana Perrucini

Ajuste na regra de seleção do Registro 2\.

CH32690\-D\_2012

Julyana Perrucini

Ajuste na regra de seleção do Registro 2\.

CH32690\-G\_2012

Julyana Perrucini

Ajuste na regra de seleção dos campos 13 ao 19 do  Registro 2\.

MFS937908

Liliane Assaf

<a id="_Hlk211962093"></a>Tratamento da Portaria SRE 63/25 incluindo nota NF3e e alterando o campo 20 – Hipótise de Estorno do registro tipo 2\.

20/10/2025

REGRAS DE NEGÓCIO

__Registro de Controle \(Registro 1\)__

#### Cód\.

### Descrição

### DR

__RN1\-00__

Regra geral de seleção

- Origem das informações para geração do registro: Cadastro de Estabelecimentos \(ESTABELECIMENTO\) e Responsável por Informações \(RESP\_INFORMACAO\)\.
- Regra de Seleção: este registro será gerado com base em informações do Cadastro de Estabelecimento e Responsável por Informações com base nos parâmetros definidos na tela de geração\.
- Ordenação do registro: não se aplica\. Será gerado apenas um registro por arquivo\.

__Ver planilha “DE\_PARA\_Geracao\_Arq\_Estorno\_Debito\_CAT154\_12\.xlsx”__

OS3879

__RN1\-04__

__Campo Razão Social__

Considerar as 50 primeiras posições do campo Razão Social \(RAZAO\_SOCIAL\) do Cadastro do Estabelecimento\.

OS3879

__RN1\-05__

__Campo Endereço__

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo endereço não informado” e gerar um espaço em branco\.

OS3879

__RN1\-06__

__Campo CEP__

Campo CEP \(CEP\) do Cadastro do Estabelecimento com o seguinte formato: *00000\-000*

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo CEP não informado” e gerar um espaço em branco\.

OS3879

__RN1\-07__

__Campo Bairro__

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo bairro não informado” e gerar um espaço em branco\.

OS3879

__RN1\-08__

__Campo Município__

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo município não informado” e gerar um espaço em branco\.

OS3879

__RN1\-09__

__Campo UF__

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo UF não informado” e gerar um espaço em branco\.

OS3879

__RN1\-10__

__Campo Responsável pela Apresentação__

Campo Nome \(NOM\_RESPONSAVEL\) do Responsável pela Apresentação parametrizado na tela de geração do arquivo\.

OS3879

__RN1\-11__

__Campo Cargo__

Campo Cargo \(DSC\_CARGO\) do Responsável pela Apresentação parametrizado na tela de geração do arquivo\.

OS3879

__RN1\-12__

__Campo Telefone__

Concatenação dos campo DDD \+ Telefone \(NUM\_DDD e NUM\_TELEFONE\) do Responsável pela Apresentação parametrizado na tela de geração do arquivo\. Deve ser considerada as duas últimas posições do campo DDD e as oito últimas posições do campo Telefone, gerando no arquivo a informação no formato: *00\-00000000* \(regra do validador\)\.

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo Telefone não informado” e gerar um espaço em branco\.

OS3879

__RN1\-13__

__Campo E\-mail__

Campo E\-mail \(E\_MAIL\) do Responsável pela Apresentação parametrizado na tela de geração do arquivo\.

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo e\-mail não informado” e gerar um espaço em branco\.

OS3879

__RN1\-14__

__Campo Qtde\. de registros de estorno de débitos__

Informar a quantidade total de registros do tipo estorno \(tipo 2\)\.

MFS937908:

Ver regras de recuperação das notas que compõe o registro tipo 2:

Modelo 06 🡪 __RN2\-00 __

Modelo 66 🡪 __RN2\-00\-a__

OS3879

__RN1\-15__

__Campo Valor Total__

Somatória o campo Valor Total \(VLR\_TOT\_NOTA\) das NFs informadas no arquivo de estorno cujo imposto foi objeto de estorno\. Será a somatória do campo 10 – Valor Total de todos os registros de estorno\.

MFS937908:

Ver regras de recuperação das notas que compõe o registro tipo 2:

Modelo 06 🡪 __RN2\-00 __

Modelo 66 🡪 __RN2\-00\-a__

OS3879

__RN1\-16__

__Campo BC ICMS__

Somatória o campo BC ICMS \(VLR\_BASE\_ICMS\_1\) das NFs informadas no arquivo de estorno cujo imposto foi objeto de estorno\. Será a somatória do campo 11 – BC ICMS de todos os registros de estorno\.

MFS937908:

Ver regras de recuperação das notas que compõe o registro tipo 2:

Modelo 06 🡪 __RN2\-00 __

Modelo 66 🡪 __RN2\-00\-a__

OS3879

__RN1\-17__

__Campo ICMS__

Somatória o campo ICMS \(VLR\_TRIB\_ICMS\) das NFs informadas no arquivo de estorno cujo imposto foi objeto de estorno\. Será a somatória do campo 12 –ICMS de todos os registros de estorno\.

MFS937908:

Ver regras de recuperação das notas que compõe o registro tipo 2:

Modelo 06 🡪 __RN2\-00 __

Modelo 66 🡪 __RN2\-00\-a__

OS3879

__Registro de Estorno de Débito \(Registro 2\)__

#### Cód\.

### Descrição

### DR

__RN2\-00__

Regra geral de seleção para Notas de Modelo 06

Regra parte da recuperação da nota cancelada \(objeto de estorno\) para recuperar a nota substituta\.

- Origem das informações para geração do registro: tabela de Capa de Documentos Fiscais de Utilities \(SAFX42\) e tabela de Cadastro de Pessoas Físicas/Jurídicas \(SAFX04\)\.
- Regra de Seleção: no momento a geração do arquivo devem ser considerados os registros da tabela de Capa de Documentos Fiscais de Utilities \(SAFX42\) considerando os seguintes critérios de seleção:
- Empresa \(COD\_EMPRESA\) de login
- Estabelecimento \(COD\_ESTAB\) selecionado na tela de geração
- Modelo do Documento \(COD\_MODELO\) deve ser igual a 06
- Situação \(SITUACAO\) deve ser igual a “S \- Nota Fiscal regularmente cancelada”

__\[ALTERADA \- CH32690\-D\_2012\]__

- Data do Cancelamento \(DAT\_CANCELAMENTO\) deve compreender o período parametrizado na tela de geração que será referência à tomada de crédito\.
- Data Fiscal \(DAT\_FISCAL\) deve ser de período anterior ao compreender o período parametrizado na tela de geração considerando que não há limite de data do cancelamento no seguimento, basta ser de período anterior à data da tomada de crédito\.

\(__exemplo dos dois últimos itens especificados:__

- Se na geração a tomada de crédito tem referência 08/2013:
	- Então o cancelamento vai compreender dentro desse período 01/08/2013 a 31/08/2013 __E__ a data fiscal vai compreender qualquer período anterior a da geração, ou seja, <= 31/07/2013\)\.
- Ordenação do registro: Número dos documentos fiscais cujo imposto destacado deva ser objeto de estorno \(campo 06\), Série \(campo 07\) e Data de Emissão \(campo 08\), em ordem crescente:
	- NUM\_DOCFIS \(item 06 da SAFX42\)
	- SERIE\_DOCFIS \(item 07 da SAFX42\)
	- DAT\_FISCAL \(item 03 da SAFX42\)

__Ver planilha “DE\_PARA\_Geracao\_Arq\_Estorno\_Debito\_CAT154\_12\.xlsx”__

OS3879/

CH32690\_2012

CH32690\-C\_2012

CH32690\-D\_2012

__RN2\-00\-a__

\[MFS937908\]: Inclusão do Modelo 66

Regra geral de seleção para Notas de Modelo 66 \(NF3e\)

Ao contrário do modelo 06 \(RN2\-00\), a regra parte da recuperação da nota __Substituta__ para recuperar a nota __Substituída__ \(objeto de estorno\)\. E a nota __Substituída__ \(objeto de estorno\) não pode estar cancelada\.

- Origem das informações para geração do registro: tabela de Capa de Documentos Fiscais de Utilities \(SAFX42\) e tabela de Cadastro de Pessoas Físicas/Jurídicas \(SAFX04\)\.
- Regra de Seleção das Notas __Substitutas__: no momento a geração do arquivo devem ser considerados os registros da tabela de Capa de Documentos Fiscais de Utilities \(SAFX42\) considerando os seguintes critérios de seleção:
- Empresa \(COD\_EMPRESA\) de login
- Estabelecimento \(COD\_ESTAB\) selecionado na tela de geração
- Data de Emissão \(DAT\_FISCAL\) deve compreender o período parametrizado na tela de geração que será referência à tomada de crédito\.
- Modelo do Documento \(COD\_MODELO\) deve ser igual a ‘66’ 
- Situação \(SITUACAO\) =  “__R__ \- Refaturamento/ Substituto;”
- Finalidade Emissão da Nfe \(126\-IND\_FIN\_EMISSAO\_NFE\) = __2__\-Substituição;

Recuperar os campos referente à Nota fiscal __Substituída __\(objeto de estorno\):

- NUM\_DOCFIS\_SUBST \(item 119 da SAFX42\) preenchido
- SERIE\_DOCFIS\_SUBST \(item 120 da SAFX42\)
- COD\_MODELO\_SUBST  \(item 121 da SAFX42\)
- DAT\_EMIS\_SUBST \(item 122 da SAFX42\)

Se o campo NUM\_DOCFIS\_SUBST \(item 119 da SAFX42\) não estiver preenchido, gravar mensagem no log:

“Não foi possível gerar o registro Tipo 2 para a NF3e Substituta, pois faltou referência para nota Substituída \(objeto de estorno\)\. O campo Número do Documento Fiscal Substituído \(item 119 da SAFX42\) não foi informado”\. 

Se o campo COD\_MODELO\_SUBST  \(item 121 da SAFX42\) não estiver preenchido, gravar mensagem no log:

“Não foi possível gerar o registro Tipo 2 para a NF3e Substituta, pois faltou referência para nota Substituída \(objeto de estorno\)\. O campo Modelo do Documento Fiscal Substituído \(item 121 da SAFX42\) não foi informado\.”

Se o campo DAT\_EMIS\_SUBST \(item 122 da SAFX42\) não estiver preenchido, exibir mensagem no log:

“Não foi possível gerar o registro Tipo 2 para a NF3e Substituta, pois faltou referência para nota Substituída \(objeto de estorno\)\. O campo Data da Emissão do Documento Fiscal Substituído \(item 122 da SAFX42\) não foi informado\.”

Todas as mensagens devem conter a chave de identificação da NF3e__ Substituta__: Data Emissão – Número – Série – Pessoa Fis/Jur

Para as Notas fiscais __Substitutas__ recuperadas acima, recuperar suas notas __Substituídas__:

Para isso, fazer uma consulta na tabela de Capa de Documentos Fiscais de Utilities \(SAFX42\) considerando os seguintes critérios de seleção:

- Empresa \(COD\_EMPRESA\) de login
- Estabelecimento \(COD\_ESTAB\) selecionado na tela de geração
- Data de Emissão \(DAT\_FISCAL\) da NF __Substituída__ = DAT\_EMIS\_SUBST \(item 122 da SAFX42\) da NF __Substituta__
- Situação \(SITUACAO\) da NF __Substituída__ diferente de “S \- Nota Fiscal regularmente cancelada”
- Pessoa Física/Jurídica da NF __Substituída__ = Pessoa Física/Jurídica da NF __Substituta__
- Número do Documento Fiscal \(NUM\_DOCFIS\) da NF __Substituída__ = NUM\_DOCFIS\_SUBST \(item 119 da SAFX42\) da NF __Substituta__
- Série \(SERIE\_DOCFIS\) da NF __Substituída__ = SERIE\_DOCFIS\_SUBST \(item 120 da SAFX42\) da NF __Substituta__ obs: pode estar nulo
- Modelo \(COD\_MODELO\) da NF __Substituída__ = COD\_MODELO\_SUBST  \(item 121 da SAFX42\) da NF __Substituta__

Se a consulta acima não retornar registro \(nota substituída\), gravar mensagem no log:

“Não foi possível gerar o registro Tipo 2 para a NF3e Substituta, pois a nota Substituída \(objeto de estorno\) não foi encontrada na base\.”

Mensagem devem conter a chave de identificação da NF3e__ Substituta__: Data Emissão – Número – Série – Pessoa Fis/Jur e da NF __Substituída__: Data Emissão \(DAT\_EMIS\_SUBST\) – Número \(NUM\_DOCFIS\_SUBST\) – Série \(SERIE\_DOCFIS\_SUBST\) – Modelo \(COD\_MODELO\_SUBST\)

- Ordenação do registro: Número dos documentos fiscais __Substituídos__, cujo imposto destacado deva ser objeto de estorno \(campo 06\), Série \(campo 07\) e Data de Emissão \(campo 08\), em ordem crescente:
	- NUM\_DOCFIS\_SUBST \(item 119 da SAFX42\)
	- SERIE\_DOCFIS\_SUBST \(item 120 da SAFX42\)
	- DAT\_EMIS\_SUBST \(item 122 da SAFX42\)

__Ver planilha “DE\_PARA\_Geracao\_Arq\_Estorno\_Debito\_CAT154\_12\.xlsx”__

\[MFS937908\]

__RN2\-02__

__Campo CNPJ ou CPF do destinatário__

Campo CNPJ/CPF \(CPF\_CGC\) informado na tabela de Cadastro de Pessoas Físicas/Jurídicas \(SAFX04\) considerando o registro vinculado à NF que está sendo apresentada\.

OS3879

__RN2\-03__

__Campo IE do Destinatário__

Campo Inscrição Estadual \(INSC\_ESTADUAL\) informado na tabela de Cadastro de Pessoas Físicas/Jurídicas \(SAFX04\) considerando o registro vinculado à NF que está sendo apresentada\.

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo IE do Destinatário não informado” e gerar um espaço em branco\.

OS3879

__RN2\-04__

__Campo Razão Social do destinatário__

Campo Razão Social \(RAZAO\_SOCIAL\) informado na tabela de Cadastro de Pessoas Físicas/Jurídicas \(SAFX04\) considerando o registro vinculado à NF que está sendo apresentada\.

Devem ser consideradas apenas as primeiras 35 posições do campo\.

OS3879

__RN2\-05__

__Campo Código de Identificação da Unidade Cons\.__

Será gerado com base no parâmetro Código de Identificação do Cliente existente na tela geração: Se for selecionada a opção “Código Usuário Final”, considerar o conteúdo informado do campo Código do Usuário Final \(COD\_USU\_FINAL\) da tabela de Capa de Documentos Fiscais de Utilities \(SAFX42\)\. Se for selecionada a opção “Número Medidor”, considerar o conteúdo do campo N° Medidor \(NUM\_MEDIDOR\)\.

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo Código de Identificação da Unidade Cons\. Não informado” e gerar um espaço em branco\.

OS3879

__RN2\-09__

__Campo Data de Vencimento__

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo Data de Vencimento não informado” e gerar um espaço em branco\.

OS3879

__RN2\-13__

__Campo Número da NFCEE substituta__

__\[ALTERADA \- CH32690\-G\_2012\]__

Esse campo será preenchido apenas quando a nota fiscal for de refaturamento/substituto \(campo 21\-Situação da Nota da SAFX42 igual a “R”\), caso contrário não preencher\. Exemplo: ;;

Quando este campo não estiver preenchido considerando o tratamento anterior, retornar mensagem na LOG: “Campo Número da NFCEE substituta não informado” e gerar um espaço em branco\.

\[MFS937908\]:

Para as notas de modelo 66 __Substitutas__ esse campo é preenchido com a NUM\_DOCFIS, que é obrigatório\. Logo não tem necessidade de tratamento de log\.

CH32690\-G\_2012

__RN2\-14__

__Campo Série da NFCEE substituta__

__\[ALTERADA \- CH32690\-G\_2012\]__

Esse campo será preenchido apenas quando a nota fiscal for de refaturamento/substituto \(campo 21\-Situação da Nota da SAFX42 igual a “R”\), caso contrário não preencher\. Exemplo: ;;

Quando este campo não estiver preenchido considerando o tratamento anterior, retornar mensagem na LOG: “Campo Série da NFCEE substituta não informado” e gerar um espaço em branco\.

\[MFS937908\]:

Para as notas de modelo 66 __Substitutas__ esse campo é preenchido com a SERIE\_DOCFIS, que é obrigatório\. Logo não tem necessidade de tratamento de log\.

OS3879

CH32690\-G\_2012

__RN2\-15__

__Campo Data de Emissão__

__\[ALTERADA \- CH32690\-G\_2012\]__

Esse campo será preenchido apenas quando a nota fiscal for de refaturamento/substituto \(campo 21\-Situação da Nota da SAFX42 igual a “R”\), caso contrário não preencher\. Exemplo: ;;

Quando este campo não estiver preenchido considerando o tratamento anterior, retornar mensagem na LOG: “Campo Data de Emissão da NFCEE substituta não informado” e gerar um espaço em branco\.

\[MFS937908\]:

Para as notas de modelo 66 __Substitutas__ esse campo é preenchido com a DAT\_FISCAL, que é obrigatório\. Logo não tem necessidade de tratamento de log\.

OS3879

CH32690\-G\_2012

__RN2\-16__

__Campo Data de Vencimento__

__\[ALTERADA \- CH32690\-G\_2012\]__

Esse campo será preenchido apenas quando a nota fiscal for de refaturamento/substituto \(campo 21\-Situação da Nota da SAFX42 igual a “R”\), caso contrário não preencher\. Exemplo: ;;

Quando este campo não estiver preenchido considerando o tratamento anterior, retornar mensagem na LOG: “Campo Data de Vencimento da NFCEE substituta não informado” e gerar um espaço em branco\.

\[MFS937908\]:

Para as notas de modelo 66 __Substitutas__ se o campo DAT\_VENCTO não estiver preenchido, retornar mensagem na LOG: “Campo Data de Vencimento da NF3e substituta não informado” e gerar um espaço em branco

OS3879

CH32690\-G\_2012

__RN2\-17__

__Campo Valor Total \(com 2 decimais\)__

__\[ALTERADA \- CH32690\-G\_2012\]__

Esse campo será preenchido apenas quando a nota fiscal for de refaturamento/substituto \(campo 21\-Situação da Nota da SAFX42 igual a “R”\), caso contrário não preencher\. Exemplo: ;;

Quando este campo não estiver preenchido considerando o tratamento anterior, retornar mensagem na LOG: “Campo Valor Total da NFCEE substituta não informado” e gerar um espaço em branco\.

\[MFS937908\]:

Para as notas de modelo 66 __Substitutas__ se o campo VLR\_TOT\_NOTA não estiver preenchido, retornar mensagem na LOG: “Campo Valor Total da NF3e substituta não informado” e gerar um espaço em branco\.

CH32690\-G\_2012

__RN2\-18__

__Campo BC ICMS \(com 2 decimais\)__

__\[ALTERADA \- CH32690\-G\_2012\]__

Esse campo será preenchido apenas quando a nota fiscal for de refaturamento/substituto \(campo 21\-Situação da Nota da SAFX42 igual a “R”\), caso contrário não preencher\. Exemplo: ;;

Quando este campo não estiver preenchido considerando o tratamento anterior, retornar mensagem na LOG: “Campo BC ICMS da NFCEE substituta não informado” e gerar um espaço em branco\.

\[MFS937908\]:

Para as notas de modelo 66 __Substitutas__ se o campo VLR\_BASE\_ICMS não estiver preenchido, retornar mensagem na LOG: “Campo Valor BC ICMS da NF3e substituta não informado” e gerar um espaço em branco\.

CH32690\-G\_2012

__RN2\-19__

__Campo ICMS \(com 2 decimais\)__

__\[ALTERADA \- CH32690\-G\_2012\]__

Esse campo será preenchido apenas quando a nota fiscal for de refaturamento/substituto \(campo 21\-Situação da Nota da SAFX42 igual a “R”\), caso contrário não preencher\. Exemplo: ;;

Quando este campo não estiver preenchido considerando o tratamento anterior, retornar mensagem na LOG: “Campo ICMS da NFCEE substituta não informado” e gerar um espaço em branco\.

\[MFS937908\]:

Para as notas de modelo 66 __Substitutas__ se o campo VLR\_TRIB\_ICMS não estiver preenchido, retornar mensagem na LOG: “Campo Valor ICMS da NF3e substituta não informado” e gerar um espaço em branco\.

CH32690\-G\_2012

__RN2\-20__

__Campo Hipótese do estorno__

Preencher com campo 81\-HIPOTESE\_ESTORNO da SAFX42\.

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo Hipótese do estorno não informado” e gerar um espaço em branco\.

MFS937908:

Preencher com base nos campos <a id="_Hlk211962318"></a>81\- HIPOTESE\_ESTORNO e 139\-COD\_MOTIVO\_SUBST da SAFX42 das notas:

\- de modelo 06 nota cancelada \(objeto de estorno\) recuperadas pela RN2\-00 

\- de modelo 66 __Substitutas__, recuperadas pela RN2\-00\-a 

Se 81\-HIPOTESE\_ESTORNO igual a ‘2’ – Erro na Medição, Faturamento ou Tarifação do produto, então:

    Preencher o campo 20\-Hipótese do Estorno com ‘01’ – Erro de Leitura

Senão:

   Se 81\-HIPOTESE\_ESTORNO igual a ‘4’ – Cobrança em duplicidade, então:

       Preencher o campo 20\-Hipótese do Estorno com ‘06’ – Cobrança em Duplicidade  
   Senão

      Se 139\-COD\_MOTIVO\_SUBST for igual a ‘01’ – Erro de Preço, então:

          Preencher o campo 20\-Hipótese do Estorno com ‘02’ – Erro de Preço ou Erro de Tarifa 

      Senão

         Se 139\-COD\_MOTIVO\_SUBST for igual a ‘02’ – Erro Cadastral, então:

             Preencher o campo 20\-Hipótese do Estorno com ‘04’ – Erro Cadastral

         Senão

            Se 139\-COD\_MOTIVO\_SUBST for igual a ‘03’ – Decisão Judicial, então:

                Preencher o campo 20\-Hipótese do Estorno com ‘03’ – Decisão Judicial

            Senão

               Se 139\-COD\_MOTIVO\_SUBST for igual a ‘04’ \- Erro de Tributação, então:

                   Preencher o campo 20\-Hipótese do Estorno com ‘05’ – Erro de Tributação

                Senão 

                      Preencher o campo 20\-Hipótese do Estorno com um espaço em branco\.

                      Retornar mensagem na LOG: 

                      Para nota de modelo 06 nota cancelada \(objeto de estorno\) recuperadas pela RN2\-00: 

“Campo 20\-Hipótese de estorno do registro tipo 2 gerado sem informação\. Ajuste a nota preenchendo os campos da SAFX42: 81 \- Hipótese do estorno da SAFX42 \(valores 2, 4\) ou 139 \- Motivo da Substituição \(valores 01, 02, 03 ou 04\)”\.

                      Para nota de modelo 66 __Substitutas__, recuperadas pela RN2\-00\-a:

“Campo 20\-Hipótese de estorno do registro tipo 2 gerado sem informação\. Ajuste a NF3e substituta preenchendo os campos da SAFX42: 81 \- Hipótese do estorno da SAFX42 \(valores 2, 4\) ou 139 \- Motivo da Substituição \(valores 01, 02, 03 ou 04\)”\.

OS3879

__RN2\-21__

__Campo Motivo do Estorno__

Quando este campo não estiver preenchido, retornar mensagem na LOG: “Campo Motivo do Estorno não informado” e gerar um espaço em branco\.

MFS937908:

Preencher com base nos campos 82\- MOTIVO\_ESTORNO da SAFX42 das notas:

\- de modelo 06 nota cancelada \(objeto de estorno\) recuperadas pela RN2\-00 

\- de modelo 66 __Substitutas__, recuperadas pela RN2\-00\-a 

OS3879

 

