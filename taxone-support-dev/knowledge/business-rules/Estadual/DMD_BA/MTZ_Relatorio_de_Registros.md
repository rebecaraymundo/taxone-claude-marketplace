# MTZ_Relatorio_de_Registros

- **Fonte:** MTZ_Relatorio_de_Registros.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 37 KB

---

# Regras de Relatório

# Relatório de Registros 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3805\-A

Criação do documento

Definição das regras para o relatório de registros\.

REGRAS DE NEGÓCIO

####    Cód\.

###   Descrição

###       DR

__RN00__

__Regra de seleção__: este relatório será gerado quando, o usuário executar o arquivo na tela de geração do meio magnético DMD\-BA e for processado com sucesso\. O sistema exibe relatório com todos as dados que foram parametrizados e processados pelo estabelecimento\.

OS3805\-A

__Cabeçalho__

__RN01__

__Empresa__

Campo Razão Social da tabela de Estabelecimento\.

OS3805\-A

__RN02__

__Estabelecimento__

Campo Razão Social da tabela de Estabelecimento\.

OS3805\-A

__RN03__

__Inscrição Estadual__

Código da Inscrição Estadual cadastrada para a UF do Estabelecimento\.

OS3805\-A

__RN04__

__CNPJ__

Campo CNPJ do Estabelecimento\.

OS3805\-A

__REGISTRO TIPO 00 – Registro Mestre da DMD e Registro Tipo 01 \- Identificação__

__RN05__

__Regra de seleção Registro Tipo 00 e 01__: será gerado considerando as informações do Registro Tipo 00 – Registro Mestre e registro Tipo01 – Identificação da DMD\-BA, tendo como base os mesmos critérios de recuperação do meio magnético\. Apesar de serem gerados vários registros 01, será considerada a informação de apenas um registro, pois estamos demonstrando informações relativas ao arquivo como um todo\.

OS3805\-A

__RN06__

__Ano do Layout: __será gerado considerando o ano padrão do layout existente no registro Tipo 00 – Registro Mestre da DMD\.

OS3805\-A

__RN07__

__Nome do Responsável: __será gerado considerando o nome do responsável  informado na tela Parâmetros, em  Dados Iniciais do módulo DMD – BA, conforme o registro Tipo00 do DMD\-BA\.

OS3805\-A

__RN08__

__N° do CPF do Responsável: __será gerado com base nos dados do CPF informado, conforme o registro Tipo00 do DMD\-BA\.

OS3805\-A

__RN09__

__Declaração Retificada: __será gerado com base no campo Tipo de Declaração da Tela de Geração do Registro 01, conforme critérios de recuperação do meio magnético\.

OS3805\-A

__REGISTRO TIPO 01 – Identificação__

__RN09__

__Regra de seleção Registro Tipo 01: S__erá gerado considerando as informações do Registro Tipo 01 – Identificação da DMD\-BA, tendo como base os mesmos critérios de recuperação do meio magnético\. 

OS3805\-A

__RN10__

__Mês/Ano Referência: __Será gerado com base nos campos Mês de Referência e Ano de Referência do Registro 01, considerando a seguinte formatação: MM/AAAA\.

OS3805\-A

__RN11__

__Declaração por Motivo de Baixa: __será gerado com base no campo Tipo de Declaração da Tela de Geração do Registro 01, conforme critérios de recuperação do meio magnético\.

OS3805\-A

__RN12__

__Código Produto Diferimento: __Será gerado com base nas informações do código do produto da DMD, conforme registro 01\.

OS3805\-A

__RN13__

__Número de Habilitação: __Será gerado com base nas informações do campo Número de Habilitação, conforme registro 01\.

OS3805\-A

__REGISTRO TIPO 02 \- ENTRADAS__

__RN10__

__Regra de seleção Registro Tipo 02 \- Entradas__: será gerado considerando as informações do Registro Tipo 02 – Entradas da DMD\-BA, tendo como base os mesmos critérios de recuperação do meio magnético\. 

__Ordenação: __Mês/Ano de referência, código de município e produto diferimento\.

OS3805\-A

__RN11__

__Mês/Ano Referência__

Será gerado com base nos campos Mês de Referência e Ano de Referência do Registro 02, considerando a seguinte formatação: MM/AAAA\.

OS3805\-A

__RN12__

__Cód\. Município__

Será gerado com base na informação do Código do Município da Pessoa Fis/Jur do registro 02\.

OS3805\-A

__RN13__

__Produto Diferimento__

Será gerado com base nas informações do código do produto da DMD, conforme registro 02\. 

OS3805\-A

__RN14__

__Qtd\. Produto Contribuinte Inscrito__

Será gerado com base no campo Quantidade Cont\. Inscrito Quantidade do Registro 02\. 

OS3805\-A

__RN15__

__Valor Contribuinte Inscrito__

Será gerado com base nas informações do campo Valor Contribuinte Inscrito do Registro 02\.

OS3805\-A

__RN16__

__Qtd\. Produto Contribuinte Não Inscrito__

Será gerado com base na informação do campo Quantidade Cont\. Não Inscrito do Registro 02\.

OS3805\-A

__RN17__

__Valor Contribuinte Não Incrito__

Será gerado com base nas a informação do campo Valor Contribuinte Não Inscrito do Registro 02\.

OS3805\-A

__REGISTRO TIPO 03 \- SAÍDAS__

__RN18__

__Regra de seleção Registro Tipo 03 \- Saídas__: será gerado considerando as informações do Registro Tipo 03 – Saída da DMD\-BA, tendo como base os mesmos critérios de recuperação do meio magnético\. 

__Ordenação: __Mês/Ano de referência, código de município e produto diferimento\.

OS3805\-A

__RN19__

__Mês/Ano Referência__

Será gerado com base nos campos Mês de Referência e Ano de Referência do Registro 03, considerando a seguinte formatação: MM/AAAA\.

OS3805\-A

__RN20__

__Cód\. Município__

Será gerado com base na informação do Código do Município da Pessoa Fis/Jur do Registro 03\.

OS3805\-A

__RN21__

__Produto Diferimento__

Será gerado com base nas informações do código do produto da DMD, conforme registro 03\.

OS3805\-A

__RN22__

__Qtd\. Produto Contribuinte Inscrito__

Será gerado com base no campo Quantidade Cont\. Inscrito Quantidade do Registro 03\. 

OS3805\-A

__RN23__

__Valor Contribuinte Inscrito__

Será gerado com base nas informações do campo Valor Contribuinte Inscrito do Registro 03\.

OS3805\-A

__RN24__

__Qtd\. Produto Contribuinte Não Inscrito__

Será gerado com base na informação do campo Quantidade Cont\. Não Inscrito do Registro 03\.

OS3805\-A

__RN25__

__Valor Contribuinte Não Incrito__

Será gerado com base nas a informação do campo Valor Contribuinte Não Inscrito do Registro 03\.

OS3805\-A

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

