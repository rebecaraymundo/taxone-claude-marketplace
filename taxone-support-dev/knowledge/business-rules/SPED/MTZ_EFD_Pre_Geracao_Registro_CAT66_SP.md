# MTZ_EFD_Pre_Geracao_Registro_CAT66_SP

> Fonte: MTZ_EFD_Pre_Geracao_Registro_CAT66_SP.docx


‘’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’



THOMSON REUTERS

Módulo Sped Fiscal


Pré-Geração Registros C195/C197/C595/C597 e D195/D197 – Portaria CAT 66/2018 - SP



Localização: Menu Sped, Módulo: Escrituração Fiscal Digital à Pré-Geração à Portaria CAT 66/2018 - SP
Localização: Menu Sped, Módulo: Escrituração Fiscal Digital à Pré-Geração à Registros C195/C197 e D195/D197 – Portaria CAT 66/2018 - SP



DOCUMENTO DE REQUISITO





Sumário

1.	Introdução	4
2.	Parâmetros de Tela	8
3.	Críticas	10
4.	Processamento	15
4.1 – Etapa 1: Limpeza das tabelas resultantes do processamento:	15
4.2 - Etapa 2: Geração das Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113)	18
4.3 - Etapa 2: Geração das Observações - Utilities (SAFX293) e Ajustes do Lançamento Fiscal - Utilities (SAFX294)	29
4.4 – Etapa 3: Geração de Relatório de Conferência Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113)	34
4.5 – Etapa 3: Geração de Relatório de Conferência Observações - Utilities (SAFX293) e Ajustes do Lançamento Fiscal - Utilities (SAFX294)	35


## Introdução


Diferentemente da GIA-SP, os registros C190/D190/C590 do Sped Fiscal não demonstram os valores das operações sem crédito de ICMS e Imposto Substituído discriminados abaixo:
- Valor Isentas/Não tributadas de ICMS
- Valor Outras de ICMS,
- ICMS ST na condição de substituído
Veja, na Gia de São Paulo existem as colunas Isenta ou Não Tributada, Outras, e a coluna Imposto Substituído, informações estas que não existe no layout do Sped Fiscal.


Para tratar tal situação, São Paulo então lançou a Portaria CAT 66/2018 que estabeleceu a geração dos registros C197/D197/C597 para demonstração de ICMS que não existente nos registros C190/D190/C590, através dos códigos de ajuste:
SP90090104 - Valor correspondente à coluna Isentas/Não tributadas e Outras (artigos 214 e 215 do RICMS/00).
SP90090278 - Valor correspondente ao ICMS ST na condição de substituído (artigo 278, § 1º, do RICMS/00).” (NR);

Esses registros estão organizados na seguinte hierarquia:
C100 – Capa do Documento Fiscal (Nível 2)
.... C170 – Item do Documento Fiscal (Nível 3)
.... C190 – Registro Analítico do Documento (Nível 3)
.... C195 – Obs Lançamento Fiscal (Nível 3)
.... .... C197 – Ajustes Provenientes do Documento Fiscal (Nível 4)

A portaria orienta que, seja gerado um registro C195/D195/C595 para cada CFOP presente na nota fiscal (C100/C500) contendo pelo menos um dos valores de Isentas/Não tributadas de ICMS, Outras de ICMS e ICMS ST na condição de substituído. O total dos Valores de Isentas/Não tributadas de ICMS e Outras de ICMS deve ser demonstrado no registro C197/D197/C597 com código de ajuste SP90090104. E O total dos valores de ICMS ST na condição de substituído demonstrado no registro C197/D197/C597 com código de ajuste SP90090278.

Exemplo:
Nota Fiscal 100001 de modelo 55:

Os CFOPs 5102, 5103 e 5104 geram registro C195, pois seus itens possuem pelo menos um dos valores preenchidos: Isentas/Não tributadas de ICMS, Outras de ICMS, ICMS ST na condição de substituído. O CFOP 5101 não gera C195 pois só tem valor tributado de ICMS.
Cada CFOP precisa de um código de observação para gerar o C195. Este código deve ser criado pelo usuário através do Cadastro de Observações (SAFX2009).
O total por CFOP dos valores de Isentas/Não tributadas de ICMS e Outras de ICMS presentes nos itens, gera um registro C197 com código de ajuste SP90090104.
O total por CFOP dos valores ICMS ST na condição de substituído presentes nos itens, gera um registro C197 com código de ajuste SP90090278.




Base Legal: Portaria CAT nº 66, de 25-07-2018.

Obs.:  A geração dos registros C195/C197/D195/D197 são baseados nas notas fiscais (SAFX07/SAFX08). A geração dos registros C595/C597 são baseados nas notas fiscais (SAFX07/SAFX08) para as notas de entrada e nas notas fiscais de utilities (SAFX42/SAFX43) para as notas de saída.


## Parâmetros de Tela


[MFS889333]

Criar um informativo na Tela em destaque na cor Vermelha, antes do Campo “Data Inicial” com o descritivo abaixo:

“Comunicado Importante
A partir de 1º de janeiro de 2026, conforme Portaria SRE nº 44/2025, a geração dos registros C197 para os códigos de ajuste SP90090104 e SP90090278 não será mais necessária. Portanto, a Pré-Geração desses registros não deverá ser realizada a partir desta data.”





[MFS582717] Alteração da desrição do parâmetro “Elimina registros inseridos...”

Data Inicial: [ DD/MM/AAAA]
Data Final:  [ DD/MM/AAAA]

Identificação ICMS-ST Substituído:  (o) Apropria (Indicador crédito de ICMS-ST – item 78 SAFX08)
(  ) Ind ICMS-ST (Substituto-Substituído – item 131 SAFX08)
(  ) CST (Situação Tributária B – item 31 SAFX08)
Cód Ajuste Isentas/N Trib e Outras:        [SP90090104]
Cód Ajuste ICMS-ST Substituído: [SP90090278]

[ x ] Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113
[ x ] Elimina registros inseridos manual ou importados via SAFX112/SAFX113/SAFX293/SAFX294

Funcionamento dos campos:




## Críticas


Antes de iniciar o processamento, vamos checar se os pré-requisitos estão atendidos.

Validar Códigos de Ajustes p/ Isentas/Não Tributadas e Outras (C197/C597/D197) e ICMS-ST na condição de substituído (C197/C597/D197):
Verificar se os códigos de ajustes informados na tela, existem no cadastro de Códigos de Ajuste provenientes de NF’s (Sped Fiscal) – tabela DWT_COD_AJUSTE_SPED.
Para que a geração seja realizada, os dois códigos devem estar cadastrados.
Se o “Cód Ajuste Isentas/N Trib e Outras”, não estiver cadastrado exibir a mensagem e abortar a geração:
Erro: Não é possível realizar a pré-geração, pois o Código de Ajuste informado para Isentas/Não Tributadas e Outras não está cadastrado. A manutenção do cadastro está disponível na opção de menu Manutençãoà Cadastros à Códigos de Ajuste provenientes de NF’s (Sped Fiscal), no Módulo Data Warehouse”.
Chave: Estabelecimento – Data Inicial – Data Final
Se o “Cód Ajuste ICMS-ST Substituído”, não estiver cadastrado exibir a mensagem e abortar a geração:
Erro: Não é possível realizar a pré-geração, pois o Código de Ajuste informado para ICMS-ST na condição de substituído não está cadastrado. . A manutenção do cadastro está disponível na opção de menu Manutençãoà Cadastros à Códigos de Ajuste provenientes de NF’s (Sped Fiscal), no Módulo Data Warehouse”.
Chave: Estabelecimento – Data Inicial – Data Final

Parametrizar os CFOPs no Cadastro das Observações (tabela X2009_OBSERVACAO):
Verificar se existe algum registro de Observação, no Cadastro das Observações (SAFX2009) com campo “CFOP Port. CAT 66/18 – SP” preenchido considerando o grupo vigente do Estabelecimento foco da geração.
Para isso consultar a “Relação Tabela Grupo”, e recuperar o grupo vigente considerando os critérios:
- Data inicial informada na tela
- Código da Tabela = 2009
- Estabelecimento informado.

Se não for encontrado nenhum registro no cadastro de observação com o campo “CFOP Port. CAT 66/18 – SP” preenchido, exibir a seguinte mensagem e abortar a geração:
Erro: Não é possível realizar a pré-geração, pois faltou preencher o campo CFOP Port. CAT 66/18 – SP no Cadastro de Observações (SAFX2009). É necessário cadastrar um código de observação para cada CFOP presente em operações com isenção de ICMS, com valor Outras de ICMS e com ICMS-ST na condição de substituído. A manutenção do Cadastro de Observações (SAFX2009) está disponível na opção de menu Manutençãoà Códigos à Cadastro de Observações, no Módulo Data Warehouse”.
Chave: Estabelecimento – Data Inicial – Data Final

Verificar registros na tabela SAFX112 – OBSERVAÇÕES DA NOTA FISCAL inseridos via manutenção ou importação:
Podem existir registros de Observações da Nota Fiscal (SAFX112) no período, inseridos via manutenção ou importação, para os Códigos de Observação cujo campo “CFOP Port. CAT 66/18 – SP” esteja preenchido no “Cadastro de Observações (SAFX2009)”. Nesse caso, vamos exibir uma mensagem de aviso, pois esses registros serão eliminados pela execução da pré-geração.
Fazer uma consulta na tabela X112_OBS_DOCFIS com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Tipo de Observação (campo 13 – SAFX112) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”
- Código de Observação (campo 12 – SAFX112) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- IND_GRAVACAO <> '0', '6','7','8'. (caso que foi incluído via digitação ou importação)
Caso a consulta acima retorne registro, dar mensagem e continuar a geração:
Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” estiver marcado, então:
“Aviso: Foram identificados registros de Observações da Nota Fiscal inseridos manualmente ou importados através da SAFX112 para o estabelecimento, período e código de observação cadastrado com “CFOP Portaria CAT 66/2018 – SP” preenchido. Tais registros foram excluídos uma vez que o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” foi marcado.”
Chave: Estabelecimento – Período – Código de Observação
Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” estiver desmarcado, então:
“Aviso: Foram identificados registros de Observações da Nota Fiscal inseridos manualmente ou importados através da SAFX112 para o estabelecimento, período e código de observação cadastrado com “CFOP Portaria CAT 66/2018 – SP” preenchido. Tais registros não foram alterados uma vez que o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” foi desmarcado.”
Chave: Estabelecimento – Período – Código de Observação

Verificar registros na tabela SAFX113 – AJUSTES DO LANÇAMENTO FISCAL inseridos via manutenção ou importação:
Podem existir registros de Ajustes no período, inseridos via manutenção ou importação, para os códigos de Observação cujo campo “CFOP Port. CAT 66/18 – SP” esteja preenchido no “Cadastro de Observações (SAFX2009)”.  Nesse caso, vamos exibir uma mensagem de aviso, pois esses registros serão eliminados pela execução da pré-geração
Fazer uma consulta na tabela X113_AJUSTE_APUR com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Tipo de Observação (campo 13 – SAFX112) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”
- Código de Observação (campo 12 – SAFX112) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- IND_GRAVACAO <> '0', '6','7','8'. (caso que foi incluído via digitação ou importação)
Caso a consulta acima retorne registro, dar mensagem e continuar a geração:
Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” estiver marcado, então:
“Aviso: Foram identificados registros de Ajustes de Lançamento Fiscal inseridos manualmente ou importados através da SAFX113 para o estabelecimento, período e código de observação cadastrado com “CFOP Portaria CAT 66/2018 – SP” preenchido. Tais registros foram excluídos de acordo com o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” informado marcado.”
Chave: Estabelecimento – Período – Código de Observação
Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” estiver desmarcado, então:
“Aviso: Foram identificados registros de Ajustes de Lançamento Fiscal inseridos manualmente ou importados através da SAFX113 para o estabelecimento, período e código de observação cadastrado com “CFOP Portaria CAT 66/2018 – SP” preenchido. Tais registros não foram alterados de acordo com o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” informado desmarcado.”

Chave: Estabelecimento – Período – Código de Observação

Acontecendo qualquer erro, finalizar a geração com status = “-1” – Erro. Se ocorrer aviso, a geração continua com status = 1 – Aviso.

[MFS582717] Inclusão limpeza das tabelas SAFX293 e SAFX294

Verificar registros na tabela SAFX293 – Observações do Documento Fiscal – Utilities - inseridos via manutenção ou importação:
Podem existir registros de Observações da Nota Fiscal – Utilities (SAFX293) no período, inseridos via manutenção ou importação, para os Códigos de Observação cujo campo “CFOP Port. CAT 66/18 – SP” esteja preenchido no “Cadastro de Observações (SAFX2009)”. Nesse caso, vamos exibir uma mensagem de aviso, pois esses registros serão eliminados pela execução da pré-geração.
Fazer uma consulta na tabela X293_OBS_DOCFIS_UTILITIES com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Tipo de Observação (campo 10 – SAFX293) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”
- Código de Observação (campo 09 – SAFX293) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- IND_GRAVACAO <> '0', '6','7','8'. (caso que foi incluído via digitação ou importação)
Caso a consulta acima retorne registro, dar mensagem e continuar a geração:
Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” estiver marcado, então:
“Aviso: Foram identificados registros de Observações da Nota Fiscal inseridos manualmente ou importados através da SAFX293 para o estabelecimento, período e código de observação cadastrado com “CFOP Portaria CAT 66/2018 – SP” preenchido. Tais registros foram excluídos uma vez que o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” foi marcado.”
Chave: Estabelecimento – Período – Código de Observação
Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” estiver desmarcado, então:
“Aviso: Foram identificados registros de Observações da Nota Fiscal inseridos manualmente ou importados através da SAFX293 para o estabelecimento, período e código de observação cadastrado com “CFOP Portaria CAT 66/2018 – SP” preenchido. Tais registros não foram alterados uma vez que o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” foi desmarcado.”
Chave: Estabelecimento – Período – Código de Observação

Verificar registros na tabela SAFX294 – AJUSTES DO LANÇAMENTO FISCAL – UTILITIES - inseridos via manutenção ou importação:
Podem existir registros de Ajustes no período, inseridos via manutenção ou importação, para os códigos de Observação cujo campo “CFOP Port. CAT 66/18 – SP” esteja preenchido no “Cadastro de Observações (SAFX2009)”.  Nesse caso, vamos exibir uma mensagem de aviso, pois esses registros serão eliminados pela execução da pré-geração
Fazer uma consulta na tabela X294_AJUSTE_APUR_UTILITIES com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Tipo de Observação (campo 10 – SAFX293) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”
- Código de Observação (campo 09 – SAFX293) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- IND_GRAVACAO <> '0', '6','7','8'. (caso que foi incluído via digitação ou importação)
Caso a consulta acima retorne registro, dar mensagem e continuar a geração:
Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” estiver marcado, então:
“Aviso: Foram identificados registros de Ajustes de Lançamento Fiscal inseridos manualmente ou importados através da SAFX294 para o estabelecimento, período e código de observação cadastrado com “CFOP Portaria CAT 66/2018 – SP” preenchido. Tais registros foram excluídos de acordo com o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” informado marcado.”
Chave: Estabelecimento – Período – Código de Observação
Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” estiver desmarcado, então:
“Aviso: Foram identificados registros de Ajustes de Lançamento Fiscal inseridos manualmente ou importados através da SAFX294 para o estabelecimento, período e código de observação cadastrado com “CFOP Portaria CAT 66/2018 – SP” preenchido. Tais registros não foram alterados de acordo com o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” informado desmarcado.”

Chave: Estabelecimento – Período – Código de Observação

Acontecendo qualquer erro, finalizar a geração com status = “-1” – Erro. Se ocorrer aviso, a geração continua com status = 1 – Aviso.

## Processamento


Depois de realizada as críticas, vamos seguir com as etapas de processamento.

[MFS568425] Inclusão dos modelos de documentos utilizados na geração dos registros C590, C595 e C597


### 4.1 – Etapa 1: Limpeza das tabelas resultantes do processamento:


Tabelas:
X112_OBS_DOCFIS – Observações da Nota Fiscal
X113_AJUSTE_APUR – Ajustes do Lançamento Fiscal
X293_OBS_DOCFIS_UTILITIES – Observações do Documento Fiscal - Utilities
X294_AJUSTE_APUR_UTILITIES – Ajustes/Outros Valores do Documento Fiscal - Utilities

Eliminação dos Ajustes do Lançamento Fiscal – SAFX113

[MFS77259] Inclusão da verificação do modelo do documento na exclusão das tabelas SAFX112 e SAFX113
Excluir os registros resultantes da consulta a tabela X113_AJUSTE_APUR com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Código de Observação (campo 12 – SAFX113) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- Código de Ajuste (campo 13 – SAFX113) = “Cód Ajuste Isentas/N Trib e Outras”; ou
“Cód Ajuste ICMS-ST Substituído”;

- Somente devem ser excluídos os ajustes de notas fiscais cujo modelo seja igual a ‘01’, ‘1B’, ‘04’, ‘55’, ‘65’, ‘07’, ‘08’, ‘8B’, ‘09’, ‘10’, ‘11’, ‘26’, ‘27’, ‘57’, ‘63’, ‘67’, ‘06’, ‘66’, ‘28’ ou ‘29’.  Para identificar o modelo da nota, deve-se utilizar os campos chaves da nota que estão na SAFX113 (campos 1 ao 11) para recuperar a nota na SAFX07 e verificar qual é o seu código do modelo (campo 13 da SAFX07), pois o código do modelo não existe na SAFX113.

- Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” estiver marcado, então:
Considerar todos os IND_GRAVACAO.
- Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” estiver desmarcado, então:
Considerar apenas IND_GRAVACAO = '0', '6','7','8'.


Definição do IND_GRAVACAO:
Valores padrão do campo ( tabelas de importação ):
1.  Incluído por Importação
2.  Atualizado por Importação
3.  Incluído por Importação / Atualizado por Digitação
4.  Incluído por Digitação
5.  Incluído por Digitação / Atualizado por Digitação
6.  Gerado pelo Sistema
7.  Gerado pelo Sistema  / Atualizado por Digitação
8. Gerado pelo Sistema  / Atualizado por Importação
O valor 8 foi criado na OS2388-AA, A4, e somente é considerado nas importações das SAFX112 e SAFX113.
9. Atualizado pelo Sistema

Eliminação das Observações da Nota Fiscal – SAFX112

[MFS77259] Inclusão da verificação do modelo do documento na exclusão das tabelas SAFX112 e SAFX113
Excluir os registros resultantes da consulta a tabela X112_OBS_DOCFIS com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Código de Observação (campo 12 – SAFX112) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- Tipo de Observação (campo 13 – SAFX112) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”
- Somente devem ser excluídas as observações de notas fiscais cujo modelo seja igual a ‘01’, ‘1B’, ‘04’, ‘55’, ‘65’, ‘07’, ‘08’, ‘8B’, ‘09’, ‘10’, ‘11’, ‘26’, ‘27’, ‘57’, ‘63’, ‘67’, ‘06’, ‘66’, ‘28’ ou ‘29’.  Para identificar o modelo da nota, deve-se utilizar os campos chaves da nota que estão na SAFX112 (campos 1 ao 11)  para consultar a nota na SAFX07 e verificar qual é o seu código do modelo (campo 13 da SAFX07), pois o código do modelo não existe na SAFX112.

- Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” estiver marcado, então:
Considerar todos os IND_GRAVACAO.
- Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113” estiver desmarcado, então:
Considerar apenas IND_GRAVACAO = '0', '6','7','8'.

Eliminação dos Ajustes do Lançamento Fiscal – Utilities – SAFX294
Excluir os registros resultantes da consulta a tabela X294_AJUSTE_APUR_UTILITIES com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Código de Observação (campo 09 – SAFX294) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- Código de Ajuste (campo 11 – SAFX294) = “Cód Ajuste Isentas/N Trib e Outras”; ou
“Cód Ajuste ICMS-ST Substituído”;

- Somente devem ser excluídos os ajustes de notas fiscais cujo modelo seja igual a ‘06’, ‘66’, ‘28’ ou ‘29’.  Para identificar o modelo da nota, deve-se utilizar os campos chaves da nota que estão na SAFX294 (campos 1 ao 08) para recuperar a nota na SAFX42 e verificar qual é o seu código do modelo (campo 13 da SAFX42), pois o código do modelo não existe na SAFX294.

- Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” estiver marcado, então:
Considerar todos os IND_GRAVACAO.
- Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” estiver desmarcado, então:
Considerar apenas IND_GRAVACAO = '0', '6','7','8'.


Eliminação das Observações da Nota Fiscal – Utilities - SAFX293
Excluir os registros resultantes da consulta a tabela X293_OBS_DOCFIS_UTILITIES com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Código de Observação (campo 09 – SAFX293) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- Tipo de Observação (campo 13 – SAFX293) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”
- Somente devem ser excluídas as observações de notas fiscais cujo modelo seja igual a ‘06’, ‘66’, ‘28’ ou ‘29’.  Para identificar o modelo da nota, deve-se utilizar os campos chaves da nota que estão na SAFX293 (campos 1 ao 08), para consultar a nota na SAFX42 e verificar qual é o seu código do modelo (campo 13 da SAFX42), pois o código do modelo não existe na SAFX293.

- Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” estiver marcado, então:
Considerar todos os IND_GRAVACAO.
- Se o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294” estiver desmarcado, então:
Considerar apenas IND_GRAVACAO = '0', '6','7','8'.


### 4.2 - Etapa 2: Geração das Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113)


Nesta etapa, a partir dos Documentos Fiscais do período, serão geradas as Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113).

Origem dos dados - Mercadoria:
- SAFX07 / SAFX08 – Tabelas dos Documentos Fiscais;


Critérios da recuperação das Notas Fiscais de Mercadoria:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data da nota:
Notas com data fiscal enquadrada no período de geração
Notas com data extemporânea enquadrada no período de geração

- Classificação do Documento Fiscal = '1' - Mercadoria, ’2’ – Serviço, '3' – Mercadoria e Serviço, ‘4’ – Conhecimento de Frete (COD_CLASS_DOC_FIS)

- Notas de Entradas e Saídas (MOVTO_E_S da SAFX07)

- Somente notas não canceladas;

- Não considerar as notas de mapa resumo de Utilities (Ind_Origem_Info <> '1' )

- Considerar notas fiscais com e sem itens de mercadoria

[MFS77259] Inclusão do tratamento do modelo do documento na recuperação das notas fiscais para a geração

- Notas fiscais de modelo igual a ‘01’, ‘1B’, ‘04’, ‘55’, ‘65’, ‘07’, ‘08’, ‘8B’, ‘09’, ‘10’, ‘11’, ‘26’, ‘27’, ‘57’, ’63’, ‘67’, ‘06’, ‘66’, ‘28’ ou ‘29’ (COD_MODELO)

Recuperar os campos a seguir, totalizando os valores pela chave de Identificação da Capa da Nota e CFOP.
A totalização dos valores da nota fiscal deverá ser a partir dos itens de mercadoria da nota, ou no caso das notas sem itens, a partir dos dados da capa da nota.

[MFS77300] Inclusão do tratamento para a nota fiscal de Saída com destaque de IPI sem direito a crédito para o adquirente, fazendo o cálculo do Valor de Outros Impostos.  Este valor está sendo calculado conforme o cálculo feito na GIA-SP para o campo Outros Impostos.  Na EFD, o valor do IPI informado é transportado para a apuração de IPI, ao contrário do que ocorre na GIA, em que o valor informado de IPI é apenas uma informação da composição do valor da operação (Outros Impostos). Por isso, nas situações em que o adquirente não pode se apropriar do IPI na entrada, na GIA o valor do IPI é informado e na EFD é preenchido com valor zero.

[MFS92977] Inclusão do tratamento para o parâmetro “Valor de FECEP está embutido no valor de ICMS-ST nos itens (SAFX08)” no cálculo do Valor do ICMS-ST na condição de Substituído.  Esse parâmetro só será utilizado quando o valor do ICMS-ST vier do campo 52- Valor ICMS Substituição Tributária da SAFX08, que é o campo ao qual é somado o valor do FECEP ICMS-ST na equalização do DATAMART.  Os demais campos utilizados para o cálculo do valor do ICMS-ST não são somados ao valor do FECEP ICMS-ST na equalização, portanto, não vão utilizar o parâmetro e serão sempre somados ao valor do FECEP ICMS-ST.

[MFS94510] Alteração no tratamento do cenário 2 do manual da Portaria CAT66/2018 (Saída com destaque de IPI sem direito a crédito para o adquirente), para passar a considerar somente notas fiscais de entrada.

[MFS509292] Alteração no tratamento do cenário 2 do manual da Portaria CAT66/2018 (Saída com destaque de IPI sem direito a crédito para o adquirente), para passar a considerar somente notas fiscais de entrada e que não sejam notas fiscais de devolução.

[MFS538162] Alteração no tratamento do cenário 2 do manual da Portaria CAT66/2018 (Saída com destaque de IPI sem direito a crédito para o adquirente), para passar a considerar as notas fiscais de saída que sejam de devolução.


[MFS77938] Inclusão do tratamento para a nota fiscal eletrônica conjugada com item de serviço sujeito a ISSQN, que tem que gerar um registro C197.

Origem dos dados - Serviços:
- SAFX07 / SAFX09 – Tabelas dos Documentos Fiscais;


Critérios da recuperação das Notas Fiscais de Serviço:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data da nota:
Notas com data fiscal enquadrada no período de geração
Notas com data extemporânea enquadrada no período de geração

- Classificação do Documento Fiscal = '3' – Mercadoria e Serviço

- Notas de Entradas e Saídas (MOVTO_E_S da SAFX07)

- Somente notas não canceladas;

- Não considerar as notas de mapa resumo de Utilities (Ind_Origem_Info <> '1' )

- Considerar notas fiscais com e sem itens de serviço

- Notas fiscais de modelo igual a  ‘55’ (COD_MODELO)

- Notas fiscais de CFOP igual a  ‘1933’, ‘2933’, ‘5933’ ou ‘6933’ (COD_CFOP), que são os serviços tributados pelo ISSQN


Recuperar os campos a seguir, totalizando os valores pela chave de Identificação da Capa da Nota e CFOP.
A totalização dos valores da nota fiscal deverá ser a partir dos itens de serviço da nota, ou no caso das notas sem itens, a partir dos dados da capa da nota.



[MFS77938] Inclusão do tratamento para a nota fiscal de Saída com destaque de IPI sem direito a crédito para o adquirente

Caso “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0 OU “Valor do ICMS-ST na condição de Substituído” >0 OU “Outros Impostos” >0 executar a lógica a seguir cujo objetivo é gerar os registros de Observação e Ajustes do Lançamento Fiscal nas tabelas X112_OBS_DOCFIS e X113_AJUSTE_APUR.



1) Geração da Observação da Nota Fiscal
Recuperar o Código de Observação (SAFX2009) referente ao CFOP recuperado da nota.
Para isso, fazer uma consulta na tabela de Cadastro de Observações (SAFX2009)” com os critérios a seguir:
- Grupo do cadastro vigente em relação ao código do estabelecimento selecionado para geração
- Campo “CFOP Portaria CAT 66/2018 – SP” = CFOP da nota;
Caso a consulta acima retorne mais de um registro, considerar aquele cuja Data de Validade Inicial é a máxima menor ou igual a Data Fiscal da nota.

[MFS75746] Inclusão da mensagem de erro para tratar a situação de ter o mesmo CFOP cadastrado para mais de uma observação, na mesma data de validade

Caso a consulta acima retorne mais de um registro e as datas de validade inicial sejam iguais, exibir a mensagem a seguir, e não gravar registro de Observação da Nota Fiscal na X112_OBS_DOCFIS.
“Não foi possível gravar a Observação para a Nota Fiscal (SAFX112), pois o mesmo CFOP está relacionado a mais de um código de observação.”
Chave: Estabelecimento – Data Fiscal – Pessoa Fis/Jur – Núm/Série/Subsérie - CFOP

Recuperar o campo Código de Observação (campo 01 – SAFX2009).
Caso a consulta acima não retorne registro, exibir a mensagem a seguir, e não gravar registro de Observação da Nota Fiscal na X112_OBS_DOCFIS.
“Não foi possível gravar a Observações para a Nota Fiscal (SAFX112), pois faltou cadastrar código de observação para o CFOP informado na nota. É necessário cadastrar um código de observação para o CFOP. A manutenção do Cadastro de Observações (SAFX2009) está disponível na opção de menu Manutençãoà Códigos à Cadastro de Observações, no Módulo Data Warehouse.”
Chave: Estabelecimento – Data Fiscal – Pessoa Fis/Jur – Núm/Série/Subsérie - CFOP
Caso contrário, gravar um registro de Observação na X112_OBS_DOCFIS c/ Código de Observação recuperado para o CFOP.

2) Geração dos Ajustes do Lançamento Fiscal
Caso “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0, GRAVAR:
Um registro de Ajuste do Lançamento Fiscal na X113_AJUSTE_APUR considerando:
- Código do Ajuste (SAFX113 - Campo 13)= “Cód Ajuste Isentas/N Trib e Outras” informado em tela
- Descrição Complementar (SAFX113 - Campo 14)= CFOP
- Valor do ICMS (SAFX113 - Campo 18)    =  “Valor Isenta/Não Tributada”
- Valor Outros (SAFX113 - Campo 19)    = “Valor Outras”

Caso “Valor do ICMS-ST na condição de Substituído” >0 e GRAVAR:
Um registro de Ajuste do Lançamento Fiscal na X113_AJUSTE_APUR considerando:
- Código do Ajuste (SAFX113 - Campo 13)= “Cód Ajuste ICMS-ST Substituído” informado em tela
- Descrição Complementar (SAFX113 - Campo 14)= CFOP
- Valor do ICMS (SAFX113 - Campo 18)    = “Valor do ICMS-ST na condição de Substituído”

3) Gravação das Tabelas:

- Informações da Observações da Nota Fiscal  (SAFX112) p/o C195/D195:

[MFS82871] Alteração da regra de preenchimento do campo Vinculação da SAFX112, uma vez que este campo só deve ser preenchido quando o campo Tipo de Observação for igual a “I”.


Obs:
1) Os campos NUM_PROCESSO e IND_GRAVACAO existem na tabela definitiva (X112_OBS_DOCFIS) e não na SAFX112.

2) Caso o registro já exista na base com IND_GRAVACAO <> '0', '6','7','8', não atualizar, uma vez que ele foi inserido via manutenção/importação e não foi excluído pois o usuário desmarcou o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113”.

[MFS77300] Inclusão do tratamento para a nota fiscal de Saída com destaque de IPI sem direito a crédito para o adquirente.  Para este tipo de nota, o registro C197, deve ser gerado com o código de ajuste de Isentas/Não Tributadas, com os valores zerados e o campo da alíquota deve ser preenchido com 0,01 para identificar esta situação, conforme manual da Portaria CAT66.

- Informações do Ajustes do Lançamento Fiscal (SAFX113) p/o C197/C597/D197:

Obs:
1) Os campos NUM_PROCESSO e IND_GRAVACAO existem na tabela definitiva (X113_AJUSTE_APUR) e não na SAFX113.
2) Caso o registro já exista na base, não atualizar, uma vez que ele foi inserido via manutenção/importação e não foi excluído pois o usuário desmarcou o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX112/SAFX113”.

### 4.3 - Etapa 2: Geração das Observações - Utilities (SAFX293) e Ajustes do Lançamento Fiscal - Utilities (SAFX294)


Nesta etapa, a partir dos Documentos Fiscais de Utilities do período, serão geradas as Observações - Utilities (SAFX293) e Ajustes do Lançamento Fiscal - Utilities (SAFX294).

Origem dos dados:
- SAFX42 / SAFX43 – Tabelas dos Documentos Fiscais de Utilities;


Critérios da recuperação das Notas Fiscais de Utilities:

- Empresa – código da empresa do login;

- Estabelecimento – código do estabelecimento selecionado para geração;

- Data da nota:
Notas com data fiscal enquadrada no período de geração
Notas com data extemporânea enquadrada no período de geração

- Somente notas não canceladas;

- Não considerar os itens informativos (itens da SAFX43 com o campo 10-Tipo de Item = 1)

- Notas fiscais de modelo igual a  ‘06’, ‘66’, ‘28’ ou ‘29’ (COD_MODELO)

Recuperar os campos a seguir, totalizando os valores pela chave de Identificação da Capa da Nota e CFOP.
A totalização dos valores da nota fiscal deverá ser a partir dos itens da nota,


Caso “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0, executar a lógica a seguir cujo objetivo é gerar os registros de Observação e Ajustes do Lançamento Fiscal nas tabelas X293_OBS_DOCFIS_UTILITIES e X294_AJUSTE_APUR_UTILITIES.


1) Geração da Observação da Nota Fiscal
Recuperar o Código de Observação (SAFX2009) referente ao CFOP recuperado da nota.
Para isso, fazer uma consulta na tabela de Cadastro de Observações (SAFX2009)” com os critérios a seguir:
- Grupo do cadastro vigente em relação ao código do estabelecimento selecionado para geração
- Campo “CFOP Portaria CAT 66/2018 – SP” = CFOP da nota;
Caso a consulta acima retorne mais de um registro, considerar aquele cuja Data de Validade Inicial é a máxima menor ou igual a Data Fiscal da nota.

Caso a consulta acima retorne mais de um registro e as datas de validade inicial sejam iguais, exibir a mensagem a seguir, e não gravar registro de Observação da Nota Fiscal na X293_OBS_DOCFIS_UTILITIES.
“Não foi possível gravar a Observação para a Nota Fiscal (SAFX293), pois o mesmo CFOP está relacionado a mais de um código de observação.”
Chave: Estabelecimento – Data Fiscal – Pessoa Fis/Jur – Núm/Série/Subsérie - CFOP

Recuperar o campo Código de Observação (campo 01 – SAFX2009).
Caso a consulta acima não retorne registro, exibir a mensagem a seguir, e não gravar registro de Observação da Nota Fiscal na X293_OBS_DOCFIS_UTILITIES.
“Não foi possível gravar a Observações para a Nota Fiscal (SAFX293), pois faltou cadastrar código de observação para o CFOP informado na nota. É necessário cadastrar um código de observação para o CFOP. A manutenção do Cadastro de Observações (SAFX2009) está disponível na opção de menu Manutençãoà Códigos à Cadastro de Observações, no Módulo Data Warehouse.”
Chave: Estabelecimento – Data Fiscal – Pessoa Fis/Jur – Núm/Série/Subsérie - CFOP
Caso contrário, gravar um registro de Observação na X293_OBS_DOCFIS_UTILITIES c/ Código de Observação recuperado para o CFOP.

2) Geração dos Ajustes do Lançamento Fiscal
Caso “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0, GRAVAR:
Um registro de Ajuste do Lançamento Fiscal na X294_AJUSTE_APUR_UTILITIES considerando:
- Código do Ajuste (SAFX294 - Campo 11) = “Cód Ajuste Isentas/N Trib e Outras” informado em tela
- Descrição Complementar (SAFX294 - Campo 12) = CFOP
- Valor do ICMS (SAFX294 - Campo 16)    =  “Valor Isenta/Não Tributada”
- Valor Outros (SAFX294 - Campo 17)    = “Valor Outras”


3) Gravação das Tabelas:

- Informações da Observações da Nota Fiscal - Utilities  (SAFX293) p/ o C595:



Obs:
1) Os campos NUM_PROCESSO e IND_GRAVACAO existem na tabela definitiva (X293_OBS_DOCFIS_UTILITIES) e não na SAFX293.

2) Caso o registro já exista na base com IND_GRAVACAO <> '0', '6','7','8', não atualizar, uma vez que ele foi inserido via manutenção/importação e não foi excluído pois o usuário desmarcou o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294”.

- Informações do Ajustes do Lançamento Fiscal (SAFX294) p/ o C597:

Obs:
1) Os campos NUM_PROCESSO e IND_GRAVACAO existem na tabela definitiva (X294_AJUSTE_APUR_UTILITIES) e não na SAFX294.
2) Caso o registro já exista na base, não atualizar, uma vez que ele foi inserido via manutenção/importação e não foi excluído pois o usuário desmarcou o parâmetro “Elimina registros inseridos manualmente ou importados via SAFX293/SAFX294”.


### 4.4 – Etapa 3: Geração de Relatório de Conferência Observações (SAFX112) e Ajustes do Lançamento Fiscal (SAFX113)


Gerar um arquivo excel a partir da leitura da tabela X112_OBS_DOCFIS com as observações das notas fiscais que foram geradas na etapa 2. Todos os campos especificados para gravação da SAFX112, devem ser demonstrados no relatório, inclusive o número do processo e o indicador de gravação, que são campos que só existem na tabela definitiva (X112).
Nome do arquivo: Relatório_Conferencia_Observacoes_mm_aaaa_cod_estab.xlsx

Gerar um arquivo excel a partir da leitura da tabela X113_AJUSTE_APUR com os ajustes dos lançamentos fiscais das notas fiscais, que foram gerados na etapa 2. Todos os campos especificados para gravação da SAFX113, devem ser demonstrados no relatório, inclusive o número do processo e o indicador de gravação, que são campos que só existem na tabela definitiva (X113).
Nome do arquivo: Relatório_Conferencia_Ajustes_mm_aaaa_cod_estab.xlsx

Demonstrar no relatório de Observações os registros resultantes da consulta a tabela X112_OBS_DOCFIS com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Código de Observação (campo 12 – SAFX112) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- Tipo de Observação (campo 13 – SAFX112) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”

Demonstrar no relatório de Ajustes os registros resultantes da consulta a tabela X113_AJUSTE_APUR com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Código de Observação (campo 12 – SAFX113) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- Código de Ajuste (campo 13 – SAFX113) = “Cód Ajuste Isentas/N Trib e Outras”; ou
“Cód Ajuste ICMS-ST Substituído”;

### 4.5 – Etapa 3: Geração de Relatório de Conferência Observações - Utilities (SAFX293) e Ajustes do Lançamento Fiscal - Utilities (SAFX294)


Gerar um arquivo excel a partir da leitura da tabela X293_OBS_DOCFIS_UTILITIES com as observações das notas fiscais que foram geradas na etapa 2. Todos os campos especificados para gravação da SAFX293, devem ser demonstrados no relatório, inclusive o número do processo e o indicador de gravação, que são campos que só existem na tabela definitiva (X293).
Nome do arquivo: Relatório_Conferencia_Observacoes_Utilities_mm_aaaa_cod_estab.xlsx

Gerar um arquivo excel a partir da leitura da tabela X294_AJUSTE_APUR_UTILITIES com os ajustes dos lançamentos fiscais das notas fiscais, que foram gerados na etapa 2. Todos os campos especificados para gravação da SAFX294, devem ser demonstrados no relatório, inclusive o número do processo e o indicador de gravação, que são campos que só existem na tabela definitiva (X294).
Nome do arquivo: Relatório_Conferencia_Ajustes_ Utilities_mm_aaaa_cod_estab.xlsx

Demonstrar no relatório de Observações os registros resultantes da consulta à tabela X293_OBS_DOCFIS_UTILITIES com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Código de Observação (campo 09 – SAFX293) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- Tipo de Observação (campo 10 – SAFX293) = “L” – “Observação referente aos Lançamentos Fiscais da Nota”

Demonstrar no relatório de Ajustes os registros resultantes da consulta a tabela X294_AJUSTE_APUR_UTILITIES com os critérios a seguir:
- Empresa de login
- Estabelecimento – código do estabelecimento selecionado para geração;
- Data Fiscal data enquadrada no período informado em tela;
- Código de Observação (campo 09 – SAFX294) existente no “Cadastro de Observações (SAFX2009)” com campo “CFOP Portaria CAT 66/2018 – SP” preenchido (campo 06 SAFX2009)
- Código de Ajuste (campo 10 – SAFX294) = “Cód Ajuste Isentas/N Trib e Outras”; ou
“Cód Ajuste ICMS-ST Substituído”;


= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS67658 | Liliane Videira Assaf | Criação da geração dos registros C195/C197 e D195/D197 em atendimento a Portaria CAT 66/2018 – SP. | 20/08/2021 |
| MFS75746 | Andréa Rocha | Inclusão da mensagem de erro para tratar a situação de ter o mesmo CFOP cadastrado para mais de uma observação, na mesma data de validade inicial. | 13/12/2021 |
| MFS77259 | Andréa Rocha | Inclusão do tratamento do modelo do documento na recuperação das notas fiscais para a geração e na exclusão dos registros das tabelas SAFX112 e SAFX113.  Somente serão recuperadas as notas fiscais dos modelos utilizados pelos registros C100 e D100. | 14/12/2021 |
| MFS77938 | Andréa Rocha | Inclusão do tratamento para a nota fiscal eletrônica conjugada com item de serviço tributado pelo ISSQN. | 22/12/2021 |
| MFS77300 | Andréa Rocha | Inclusão do tratamento para a nota fiscal de Saída com destaque de IPI sem direito a crédito para o adquirente.  Trata-se do cenário 2 do manual da Portaria CAT66/2018. | 23/12/2021 |
| MFS78994 | Liliane Assaf | Alteração na regra do “Valor do ICMS-ST na condição de Substituído”: além do campo 52 - VLR_SUBST_ICMS da SAFX08, passar a considerar os campos referentes ao ICMS-ST não destacado: 145 - VLR_ICMSS_N_ESCRIT, 133 - VLR_ICMSS_NDESTAC e 107 - VLR_TRIB_ICMS_ORIG. Esta regra é bastante utilizada nos módulos de Ressarcimento ICMS-ST. | 07/01/2022 |
| MFS80730 | Andréa Rocha | Alteração do tratamento para a nota fiscal de Saída com destaque de IPI sem direito a crédito para o adquirente. | 10/02/2022 |
| MFS82871 | Andréa Rocha | Alteração da regra de preenchimento do campo Vinculação da SAFX112, uma vez que este campo só deve ser preenchido quando o campo Tipo de Observação for igual a “I”. | 27/04/2022 |
| MFS92977 | Andréa Rocha | Inclusão do parâmetro “Valor de FECEP está embutido no valor de ICMS-ST nos itens (SAFX08)” na Tela de Geração e tratamento na geração do valor do ICMS-ST para verificar o parâmetro. | 24/10/2022 |
| MFS94510 | Andréa Rocha | Alteração no tratamento do cenário 2 do manual da Portaria CAT66/2018 (Saída com destaque de IPI sem direito a crédito para o adquirente), para passar a considerar somente notas fiscais de entrada. | 09/12/2022 |
| MFS509292 | Andréa Rocha | Alteração no tratamento do cenário 2 do manual da Portaria CAT66/2018 (Saída com destaque de IPI sem direito a crédito para o adquirente), para passar a considerar somente notas fiscais de entrada e que não sejam notas de devolução. | 01/02/2023 |
| MFS538162 | Andréa Rocha | Alteração no tratamento do cenário 2 do manual da Portaria CAT66/2018 (Saída com destaque de IPI sem direito a crédito para o adquirente), para passar a considerar as notas fiscais de saída que sejam de devolução.  Essas notas de saída devem ser consideradas, porque elas são as devoluções das notas de entrada que são consideradas para o cenário 2.  Então, para essas notas devem ser gerados os registros C195/C197. | 24/05/2023 |
| MFS568425 | Andréa Rocha | Alteração da descrição do item de menu. Inclusão dos modelos de documentos utilizados na geração dos registros C590, C595 e C597 na recuperação das notas fiscais para a geração e para a exclusão dos registros das tabelas SAFX112 e SAFX113.  A partir dessa alteração, os ajustes da SAFX113 referentes aos movimentos de entrada dos registros C595/C597 serão gerados. | 30/10/2023 |
| MFS582717 | Andréa Rocha | Inclusão da recuperação das notas fiscais de Utilities  para gerar os ajustes nas tabelas SAFX293 e SAFX294, que serão utilizados na geração dos registros C590, C595 e C597. | 01/11/2023 |
| MFS889333 | Graciela Soares | Exibição de Mensagem na Tela, para descontinuação da rotina a partir de 01/2026. | 29/10/2025 |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Data Inicial | Data | S | S | DD/MM/AAAA | Neste campo o usuário informa a data inicial do período para a recuperação dos movimentos.  Deve ser uma data válida. |
| Data Final | Data | S | S | DD/MM/AAAA | Neste campo o usuário informa a data final do período para a recuperação dos movimentos.   Consistências: Deve ser uma data válida. Caso a Data Final informada seja menor que a Data Inicial, gravar no log a seguinte mensagem: “A Data Inicial deve ser menor ou igual a Data Final informada.” Caso a Data Inicial e a Data Final excedam o período de um mês, gravar no log a seguinte mensagem: “Data Inicial e Final deverão pertencer a um mesmo mês.” |
| Identificação ICMS-ST Substituído | Alfanumérico | S | S | Radiobutton Default – Parâmetro Apropria | Neste campo o usuário escolhe a forma de identificar a condição de substituído nas operação de ICMS-ST. Duas opções são disponibilizadas: Apropria (Indicador crédito de ICMS-ST – item 78 SAFX08)     Ind ICMS-ST (Substituto-Substituído – item 131 SAFX08) CST (Situação Tributária B – item 31 SAFX08)  Opção Default: “Apropria (Indicador crédito de ICMS-ST)”      Esse parâmetro existe na Geração dos Registros da GIA-SP, com as duas primeiras opções.  Foi incluída a opção CST, pois em conversa com a área da Informação, verificou-se que essa operação pode ser identificada pela Situação Tributária B = 60.  A finalidade desse parâmetro é disponibilizarmos as mesmas opções existentes hoje na GIA-SP, para que a regra de geração do ICMS-ST na condição do Substituído feita na GIA-SP, seja contemplada no Sped Fiscal. A CAT66/2018 no projeto de substituição da GIA-SP pelo Sped Fiscal. |
| Cód Ajuste Isentas/N Trib e Outras | Alfanumérico | S | S | Texto / “SP90090104” | Campo texto para livre digitação. Default: “SP90090104” |
| Cód Ajuste ICMS-ST Substituído | Alfanumérico | S | S | Texto / “SP90090278” | Campo texto para livre digitação. Default: “SP90090278” |
| Elimina registros inseridos manual ou importados via SAFX112/113/ 293/X294 | Alfanumérico | N |  | Default = “S” | Check-box Default marcado. |
| Valor de FECEP está embutido no valor de ICMS-ST nos itens (SAFX08) | Alfanumérico | N |  | Default = “N” | [MFS92977] Inclusão do parâmetro para definir se o valor FECEP será considerado no cálculo do valor do ICMS-ST  Check-box Default desmarcado. |
| Estabelecimentos | Alfanumérico | S | S |  | Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário.  Serão disponibilizados para seleção apenas os estabelecimentos de São Paulo (UF do Estabelecimento igual a SP); |
| Selecionar |  | N | N |  | Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos.  O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:  - Somente Estabelecimentos da empresa do login;  - Somente Estabelecimentos da UF igual a SP;  Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados. |
| Marcar todos |  | N | N |  | Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”. |


| Campos | Totalização pelo item (nota c/ item) | Totalização pela Capa (nota s/item) |
| --- | --- | --- |
| Identificação da Capa da Nota Fiscal | campos 01 ao 11 da SAFX07 | campos 01 ao 11 da SAFX07 |
| CFOP | CFOP do item de mercadoria (campo 22 da SAFX08) | CFOP da capa (campo 14 da SAFX07) |
| Valor Isenta/Não Tributada | Base Isenta de ICMS do item de mercadoria (campo 56- Base ICMS da SAFX08 quando campo 55- Tributação ICMS =2) + Base Redução ICMS do item de mercadoria (campo 57 da SAFX08) | Base Isenta de ICMS da capa (campo 52- Base ICMS Isenta da SAFX07) + Base Redução de ICMS da capa (campo 54- Base Redução ICMS da SAFX07) |
| Valor Outras | Base Outras de ICMS do item de mercadoria (campo 56- Base ICMS da SAFX08 quando campo 55- Tributação ICMS =3) | Base Outras de ICMS da capa (campo 53- Base ICMS Outras da SAFX07) |
| Valor do ICMS-ST na condição de Substituído | Considerar o “Identificação ICMS-ST Substituído” selecionado em tela. Se “Apropria (Indicador crédito de ICMS-ST– item 78 SAFX08)”:     Se o Indicador de Apropria do ICMS-ST (IND_CRED_ICMSS) do     item de mercadoria (campo 78- Apropria da SAFX08) = “N:       Se “Valor de FECEP está embutido no valor de ICMS-ST nos        itens (SAFX08)” estiver desmarcado:             Preencher com:              Valor do ICMS-ST do item de mercadoria + FECEP ICMS-ST            (campo 52- Valor ICMS Substituição Tributária da SAFX08) +            (campo 140- FECEP ICMS-ST da SAFX08)        Senão             Preencher com:              Valor do ICMS-ST do item de mercadoria              (campo 52- Valor ICMS Substituição Tributária da SAFX08)     Senão         Não preencher.  Se “Ind ICMS-ST (Substituto-Substituído – item 131    SAFX08)”:     Se o Indicador de ICMS-ST (IND_FORNEC_ICMSS) do item de      mercadoria (campo 131 da SAFX08) = “2”, então:        [MFS78994]         Preencher com:         Valor do ICMS-ST do item de mercadoria          (campo 52- Valor ICMS Substituição Tributária da SAFX08)         Preencher com um dos quatro valores a seguir, considerando         o valor que estiver preenchido no item, observando a ordem de          prioridade especificada abaixo:         Se o campo “52-Valor ICMS Substituição Tributária” estiver          preenchido no item de mercadoria:            Se “Valor de FECEP está embutido no valor de ICMS-ST              nos itens (SAFX08)” estiver desmarcado:                  Considerar o campo “52-Valor ICMS Substituição                             Tributária” da SAFX08 (VLR_SUBST_ICMS) + 140-                     FECEP ICMS-ST da SAFX08 (VLR_FECP_ICMS_ST)            Senão:                  Considerar o campo “52-Valor ICMS Substituição                     Tributária” da SAFX08 (VLR_SUBST_ICMS).         Senão:             Se o campo “145-Valor de ICMS – ST Não            escriturado” estiver preenchido no item de mercadoria, então:             Considerar o campo“145-Valor de ICMS – ST Não              escriturado” (VLR_ICMSS_N_ESCRIT) + 140-                     FECEP ICMS-ST da SAFX08 (VLR_FECP_ICMS_ST).          Senão:               Se o campo “133-ICMS ST Não Escriturado” estiver                preenchido no item de mercadoria, então:                   Considerar o campo “133-ICMS ST Não Escriturado”                    (VLR_ICMSS_NDESTAC) + 140-                     FECEP ICMS-ST da SAFX08 (VLR_FECP_ICMS_ST)               Senão:                   Se o campo “107-Valor Carga Tributária Origem ICMS”                    estiver preenchido no item de mercadoria, então:                       Considerar o campo “107- Valor Carga Tributária                        Origem ICMS” (VLR_TRIB_ICMS_ORIG) + 140-                     FECEP ICMS-ST da SAFX08 (VLR_FECP_ICMS_ST)                  Senão                       Não preencher.     Senão         Não preencher.  Se “CST (Situação Tributária B – item 31 SAFX08)”:     Se o Código Situação Tributária B (COD_SITUACAO_B) do item     de mercadoria (campo 31 da SAFX08) = “60”, então:         [MFS78994]         Preencher com:         Valor do ICMS-ST do item de mercadoria          (campo 52- Valor ICMS Substituição Tributária da SAFX08)         Preencher com um dos quatro valores a seguir, considerando         o valor que estiver preenchido no item, observando a ordem de          prioridade especificada abaixo:         Se o campo “52-Valor ICMS Substituição Tributária” estiver          preenchido no item de mercadoria:              Se “Valor de FECEP está embutido no valor de ICMS-ST              nos itens (SAFX08)” estiver desmarcado:                  Considerar o campo “52-Valor ICMS Substituição                             Tributária” da SAFX08 (VLR_SUBST_ICMS) + 140-                     FECEP ICMS-ST da SAFX08 (VLR_FECP_ICMS_ST)            Senão:                  Considerar o campo “52-Valor ICMS Substituição                     Tributária” da SAFX08 (VLR_SUBST_ICMS).        Senão:            Se o campo “145-Valor de ICMS – ST Não            escriturado” estiver preenchido no item de mercadoria, então:             Considerar o campo“145-Valor de ICMS – ST Não              escriturado” (VLR_ICMSS_N_ESCRIT) + 140-                     FECEP ICMS-ST da SAFX08 (VLR_FECP_ICMS_ST)          Senão:               Se o campo “133-ICMS ST Não Escriturado” estiver                preenchido no item de mercadoria, então:                   Considerar o campo “133-ICMS ST Não Escriturado”                    (VLR_ICMSS_NDESTAC) + 140-                     FECEP ICMS-ST da SAFX08 (VLR_FECP_ICMS_ST)               Senão:                   Se o campo “107-Valor Carga Tributária Origem ICMS”                    estiver preenchido no item de mercadoria, então:                       Considerar o campo “107- Valor Carga Tributária                        Origem ICMS” (VLR_TRIB_ICMS_ORIG) + 140-                     FECEP ICMS-ST da SAFX08 (VLR_FECP_ICMS_ST)                   Senão                       Não preencher.     Senão         Não preencher. | Considerar o “Identificação ICMS-ST Substituído” selecionado em tela. Se “Apropria (Indicador crédito de ICMS-ST– item 78 SAFX08)”:     Se o Indicador de Apropria do ICMS-ST (IND_CRED_ICMSS)     da capa (campo 82- Apropria da SAFX07) = “N”,     então:         Preencher com:          Valor do ICMS-ST da capa (campo 48- Valor ICMS         Substituição Tributária da SAFX07)     Senão         Não preencher. Se “Ind ICMS-ST (Substituto-Substituído – item 131       SAFX08)”:         Não preencher.  Se “CST (Situação Tributária B – item 31 SAFX08)”:         Não preencher. |
| Outros Impostos | [MFS77300] [MFS80730] Retirar a verificação da NF de saída, ou seja a nota de entrada também é considerada [MFS94510] Considerar somente notas de entrada p/ o cenário 2 [MFS509292] Considerar somente notas de entrada não devolvidas p/ o cenário 2 [MFS538162] Considerar notas de saída devolvidas p/ o cenário 2, além das notas de entrada não devolvidas  Se “IPI Incluso – item 33 da SAFX08”:     Se o Indicador de IPI Incluso (IND_IPI_INCLUSO) do     item de mercadoria (campo 33- Indicador de IPI Incluso da      SAFX08) = “N”           Se (NF Entrada e NF Normal) ou (NF Saída e NF Devolução)          Se (Movimento Entrada/Saída (campo 3- Movimento Entrada/Saída                                da SAFX07) <> ‘9’ e Normal ou Devolução (campo 4- Normal ou                Devolução da SAFX07) <> ‘2’)          Ou (Movimento Entrada/Saída (campo 3- Movimento Entrada/Saída                                da SAFX07) = ‘9’ e Normal ou Devolução (campo 4- Normal ou                Devolução da SAFX07) = ‘2’)  então:               Preencher com:                IPI Não Escriturado do item de mercadoria (campo 81 - IPI Não                    Escriturado da SAFX08) + Valor do IPI (campo 48 - Valor do IPI                 da SAFX08)         Senão                Não preencher. | Não preencher. |


| Campos | Totalização pelo item (nota c/ item) | Totalização pela Capa (nota s/item) |
| --- | --- | --- |
| Identificação da Capa da Nota Fiscal | campos 01 ao 11 da SAFX07 | campos 01 ao 11 da SAFX07 |
| CFOP | CFOP do item de serviço (campo 17 da SAFX09) | CFOP da capa (campo 14 da SAFX07) |
| Valor Isenta/Não Tributada | Valor Total do Serviço (campo 15 da SAFX09) | Valor dos Produtos / Serviços (campo 22 da SAFX07) |
| Valor Outras | Não preencher. | Não preencher. |
| Valor do ICMS-ST na condição de Substituído | Não preencher. | Não preencher. |


| PK | Item SAFX112 | Campo |  |  | Regra de Preenchimento |
| --- | --- | --- | --- | --- | --- |
| (*) | 01 | Código da Empresa |  | COD_EMPRESA | Código da Empresa da Nota Fiscal |
| (*) | 02 | Código do Estabelecimento |  | COD_ESTAB | Código do Estabelecimento da Nota Fiscal |
| (*) | 03 | Data da Escrita Fiscal |  | DATA_FISCAL | Data Fiscal da Devolução da Nota Fiscal |
| (*) | 04 | Movimento Entrada/Saída |  | MOVTO_E_S | Movimento Entrada/Saída da Nota Fiscal |
| (*) | 05 | Normal ou Devolução |  | NORM_DEV | Indicador de Normal ou Devolução da Nota Fiscal |
| (*) | 06 | Tipo do Documento |  | COD_DOCTO | Código do Tipo de Documento da Nota Fiscal |
| (*) | 07 | Indicador Pessoa Física/Jurídica |  | IND_FIS_JUR | Indicador de Pessoa Física/Jurídica da Nota Fiscal |
| (*) | 08 | Código/Destinatário/Emitente/ Remetente |  | COD_FIS_JUR | Código/Destinatário/Emitente/ Remetente da Pessoa Física/Jurídica da Nota Fiscal |
| (*) | 09 | Número do Documento Fiscal/ Número do Mapa Resumo de Caixa |  | NUM_DOCFIS | Número do Documento Fiscal da Nota Fiscal |
|  | 10 | Série do Documento Fiscal |  | SERIE_DOCFIS | Série do Documento Fiscal da Nota Fiscal |
|  | 11 | Subsérie do Documento Fiscal |  | SUB_SERIE_DOCFIS | Subsérie do Documento Fiscal da Nota Fiscal |
| (*) | 12 | Código da Observação |  | COD_OBS_LANCTO_FISCAL | Código de Observação (SAFX2009) referente ao CFOP recuperado da nota |
| (*) | 13 | Tipo de Observação |  | IND_ICOMPL_LANCTO | Informar: L - Observação referente aos Lançamentos Fiscais da Nota |
|  | 14 | Descrição Complementar |  | DSC_COMPLEMENTAR | Não preencher |
|  | 15 | Vinculação |  | VINCULACAO | [MFS82871] Não preencher  Informar: 1 - EFD ICMS/IPI; |
|  |  | Número do Processo |  | NUM_PROCESSO | preencher com o número do processo da execução da geração |
|  |  | Indicador de Gravação |  | IND_GRAVACAO | preencher com ‘6’ |


| PK | Item SAFX113 | Campo |  | Regra de Preenchimento |
| --- | --- | --- | --- | --- |
| (*) | 01 | Código da Empresa | COD_EMPRESA | Código da Empresa da Nota Fiscal |
| (*) | 02 | Código do Estabelecimento | COD_ESTAB | Código do Estabelecimento da Nota Fiscal |
| (*) | 03 | Data da Escrita Fiscal | DATA_FISCAL | Data Fiscal da Devolução da Nota Fiscal |
| (*) | 04 | Movimento Entrada/Saída | MOVTO_E_S | Movimento Entrada/Saída da Nota Fiscal |
| (*) | 05 | Normal ou Devolução | NORM_DEV | Indicador de Normal ou Devolução da Nota Fiscal |
| (*) | 06 | Tipo do Documento | COD_DOCTO | Código do Tipo de Documento da Nota Fiscal |
| (*) | 07 | Indicador Pessoa Física/Jurídica | IND_FIS_JUR | Indicador de Pessoa Física/Jurídica da Nota Fiscal |
| (*) | 08 | Código/Destinatário/Emitente/ Remetente | COD_FIS_JUR | Código/Destinatário/Emitente/ Remetente da Pessoa Física/Jurídica da Nota Fiscal |
| (*) | 09 | Número do Documento Fiscal/ Número do Mapa Resumo de Caixa | NUM_DOCFIS | Número do Documento Fiscal da Nota Fiscal |
|  | 10 | Série do Documento Fiscal | SERIE_DOCFIS | Série do Documento Fiscal da Nota Fiscal |
|  | 11 | Subsérie do Documento Fiscal | SUB_SERIE_DOCFIS | Subsérie do Documento Fiscal da Nota Fiscal |
| (*) | 12 | Código da Observação do Lançamento Fiscal | COD_OBS_LANCTO_FISCAL | Código de Observação (SAFX2009) referente ao CFOP recuperado da nota |
| (*) | 13 | Código do Ajuste | COD_AJUSTE_SPED | [MFS77300] Inclusão da verificação de Outros Impostos Para o lançamento quando “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0 OU “Outros Impostos” >0:          	Preencher com Cód Ajuste Isentas/N Trib e Outras informado em tela    Para o lançamento quando “Valor do ICMS-ST na condição de Substituído” >0:          	Preencher com Cód Ajuste ICMS-ST Substituído informado em tela |
|  | 14 | Descrição Complementar do Ajuste | DSC_COMP_AJUSTE | Preencher com o CFOP recuperado da nota |
|  | 15 | Número do Item da Nota | NUM_ITEM | Não preencher. |
|  | 16 | Base de Cálculo do ICMS | VLR_BASE_ICMS | Não preencher. |
|  | 17 | Alíquota do ICMS | ALIQUOTA_ICMS | [MFS77300] Inclusão da verificação de Outros Impostos Para o lançamento quando “Outros Impostos” >0             Preencher com 0,01 Para os demais casos             Não preencher. |
|  | 18 | Valor do ICMS | VLR_ICMS | [MFS77300] Inclusão da verificação de Outros Impostos  Para o lançamento quando “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0:          	Preencher com “Valor Isenta/Não Tributada”    Para o lançamento quando “Valor do ICMS-ST na condição de Substituído” >0:          	Preencher com “Valor do ICMS-ST na condição de Substituído”  Para o lançamento quando “Outros Impostos” >0             Preencher com 0,00 |
|  | 19 | Outros Valores | VLR_OUTROS | [MFS77300] Inclusão da verificação de Outros Impostos  Para o lançamento quando “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0:          	Preencher com “Valor Outras”    Para o lançamento quando “Valor do ICMS-ST na condição de Substituído” >0:          	Não preencher  Para o lançamento quando “Outros Impostos” >0             Preencher com 0,00 |
|  |  | Número do Processo | NUM_PROCESSO | preencher com o número do processo da execução da geração |
|  |  | Indicador de Gravação | IND_GRAVACAO | preencher com ‘6’ |


| Campos | Totalização pelo item |
| --- | --- |
| Identificação da Capa da Nota Fiscal | campos 01 ao 09 da SAFX42 |
| CFOP | CFOP do item de mercadoria (campo 13 da SAFX43) |
| Valor Isenta/Não Tributada | Base Isenta de ICMS do item (campo 24- Base ICMS Isenta da SAFX43) + Base Redução ICMS do item (campo 26- Base de Redução da SAFX43) |
| Valor Outras | Base Outras de ICMS do item de mercadoria (campo 25- Base ICMS Outras da SAFX43) |
| Valor do ICMS-ST na condição de Substituído | Não preencher.  Obs.:  A geração da GIA-SP não preenche a coluna de Imposto Retido por Substituição, sendo assim esse valor não será gerado. |
| Outros Impostos | Não preencher. |


| PK | Item SAFX293 | Campo |  |  | Regra de Preenchimento |
| --- | --- | --- | --- | --- | --- |
| (*) | 01 | Código da Empresa |  | COD_EMPRESA | Código da Empresa da Nota Fiscal |
| (*) | 02 | Código do Estabelecimento |  | COD_ESTAB | Código do Estabelecimento da Nota Fiscal |
| (*) | 03 | Data da Escrita Fiscal |  | DAT_FISCAL | Data Fiscal da Devolução da Nota Fiscal |
| (*) | 04 | Indicador Pessoa Física/Jurídica |  | IND_FIS_JUR | Indicador de Pessoa Física/Jurídica da Nota Fiscal |
| (*) | 05 | Código/Destinatário/Emitente/ Remetente |  | COD_FIS_JUR | Código/Destinatário/Emitente/ Remetente da Pessoa Física/Jurídica da Nota Fiscal |
| (*) | 06 | Número do Documento Fiscal |  | NUM_DOCFIS | Número do Documento Fiscal da Nota Fiscal |
|  | 07 | Série do Documento Fiscal |  | SERIE_DOCFIS | Série do Documento Fiscal da Nota Fiscal |
|  | 08 | Subsérie do Documento Fiscal |  | SUB_SERIE_DOCFIS | Subsérie do Documento Fiscal da Nota Fiscal |
| (*) | 09 | Código da Observação |  | COD_OBS_LANCTO_FISCAL | Código de Observação (SAFX2009) referente ao CFOP recuperado da nota |
| (*) | 10 | Tipo de Observação |  | IND_ICOMPL_LANCTO | Informar: L - Observação referente aos Lançamentos Fiscais da Nota |
|  | 11 | Descrição Complementar |  | DSC_COMPLEMENTAR | Não preencher |
|  |  | Número do Processo |  | NUM_PROCESSO | preencher com o número do processo da execução da geração |
|  |  | Indicador de Gravação |  | IND_GRAVACAO | preencher com ‘6’ |


| PK | Item SAFX294 | Campo |  | Regra de Preenchimento |
| --- | --- | --- | --- | --- |
| (*) | 01 | Código da Empresa | COD_EMPRESA | Código da Empresa da Nota Fiscal |
| (*) | 02 | Código do Estabelecimento | COD_ESTAB | Código do Estabelecimento da Nota Fiscal |
| (*) | 03 | Data da Escrita Fiscal | DAT_FISCAL | Data Fiscal da Devolução da Nota Fiscal |
| (*) | 04 | Indicador Pessoa Física/Jurídica | IND_FIS_JUR | Indicador de Pessoa Física/Jurídica da Nota Fiscal |
| (*) | 05 | Código/Destinatário/Emitente/ Remetente | COD_FIS_JUR | Código/Destinatário/Emitente/ Remetente da Pessoa Física/Jurídica da Nota Fiscal |
| (*) | 06 | Número do Documento Fiscal | NUM_DOCFIS | Número do Documento Fiscal da Nota Fiscal |
|  | 07 | Série do Documento Fiscal | SERIE_DOCFIS | Série do Documento Fiscal da Nota Fiscal |
|  | 08 | Subsérie do Documento Fiscal | SUB_SERIE_DOCFIS | Subsérie do Documento Fiscal da Nota Fiscal |
| (*) | 09 | Código da Observação do Lançamento Fiscal | COD_OBS_LANCTO_FISCAL | Código de Observação (SAFX2009) referente ao CFOP recuperado da nota |
| (*) | 10 | Código do Ajuste | COD_AJUSTE_SPED | Para o lançamento quando “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0 OU “Outros Impostos” >0:          	Preencher com Cód Ajuste Isentas/N Trib e Outras informado em tela |
|  | 11 | Descrição Complementar do Ajuste | DSC_COMP_AJUSTE | Preencher com o CFOP recuperado da nota |
|  | 12 | Número do Item da Nota | NUM_ITEM | Preencher com zero. |
|  | 13 | Base de Cálculo do ICMS | VLR_BASE_ICMS | Não preencher. |
|  | 14 | Alíquota do ICMS | ALIQUOTA_ICMS | Não preencher. |
|  | 15 | Valor do ICMS | VLR_ICMS | Para o lançamento quando “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0:          	Preencher com “Valor Isenta/Não Tributada” |
|  | 16 | Outros Valores | VLR_OUTROS | Para o lançamento quando “Valor Isenta/Não Tributada” >0 OU “Valor Outras” >0:          	Preencher com “Valor Outras” |
|  |  | Número do Processo | NUM_PROCESSO | preencher com o número do processo da execução da geração |
|  |  | Indicador de Gravação | IND_GRAVACAO | preencher com ‘6’ |
