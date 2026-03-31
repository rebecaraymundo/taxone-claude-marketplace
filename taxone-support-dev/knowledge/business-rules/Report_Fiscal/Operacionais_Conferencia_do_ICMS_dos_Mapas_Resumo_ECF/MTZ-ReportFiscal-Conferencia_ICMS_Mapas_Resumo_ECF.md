---
source: "MTZ-ReportFiscal-Conferencia_ICMS_Mapas_Resumo_ECF.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Relatório de Conferência do ICMS dos Mapas Resumo ECF

Localização: Menu Básicos, Módulo Report Fiscal, item Operacionais --> Conferência do ICMS dos Mapas Resumo ECF 


                                           Documento de Requisito

Doc
Alteração
Data
Resp
OS4083
Relatório de conferência do ICMS dos Mapas Resumo de ECF
23/09/2013	
(Criação do doc)
Vânia Mattos


RN00 - Regras Gerais

Este relatório demonstra os valores totais de ICMS da movimentação de ECF carregada para as seguintes tabelas:

      - SAFX07/SAFX08 - Mapas resumo de ECF
      - SAFX991/SAFX993/SAFX994 - Detalhamento dos cupons fiscais

O objetivo é permitir ao usuário identificar as diferenças, e evitar os erros de validação do Sped Fiscal, em relação à crítica dos valores do registro C490 e o valor a débito do campo 02 do registro E110 (ver maiores detalhes no help deste item de menu). 

RN01 - Parâmetros de Tela

Parâmetros para emissão do relatório:

Período -->Neste campo o usuário informará uma data inicial e uma data final, que serão utilizadas como filtro para recuperação da movimentação de ECF a ser considerada na emissão do relatório.

UF --> Este campo exibe a lista das UF's da tabela dos estados + opção "Todas" 

Estabelecimentos -->Este campo exibe a lista dos estabelecimentos da Empresa do login. Caso o usuário tenha optado por selecionar uma UF, serão considerados apenas os estabelecimentos desta UF.


RN02 - Processamento dos Dados

Origem dos Dados: SAFX07 e SAFX08      (Mapas Resumo)
                                   SAFX991                    (Reduções Z)
                                   SAF993 e SAFX994   (Capa e Itens dos Cupons Fiscais)

Layout do relatório: vide planilha "Layout Conferencia ICMS Mapas Resumo"
 
Para cada Estabelecimento, serão recuperados os movimentos de ECF e gerado o relatório.

Recuperação dos dados dos mapas resumo (SAFX07/SAFX08):

   - Empresa --> código da empresa do login
   - Estabelecimento --> código do estabelecimento da geração 
   - Data Fiscal --> deve ser uma data enquadrada no intervalo de datas informado em tela
   - Movimento E/S --> somente saídas (03-Movimento E/S = 9)
   - Indicador de Cancelamento -->somente notas não canceladas (30-Situação da Nota <> 'S')
   - Modelo -->somente o modelos 02, 2D e 60 (verificar pelo campo 13-Modelo de Documento)

Para cada documento fiscal recuperado na SAFX07, serão totalizados os seguintes valores dos itens da SAFX08:

   - Base de cálculo do ICMS (base tributada)
   - Valor do ICMS

Recuperação dos dados das reduções Z e cupons fiscais (SAFX991/SAFX993/SAFX994):

Recuperação dos dados das Reduções Z (SAFX991):

   - Empresa --> código da empresa do login
   - Estabelecimento --> código do estabelecimento da geração 
   - Data do Movimento --> deve ser uma data enquadrada no intervalo de datas informado em tela
   - Modelo -->somente o modelos 02, 2D e 60 

Para cadaRedução Z recuperada na SAFX991, serão identificados os cupons fiscais e itens que compõe a redução Z, da seguinte forma:

Recuperação dos cupons fiscais (SAFX993) a partir da Redução Z:

Os cupons fiscais que compõe a redução Z serão obtidos na SAFX993 a partir dos dados chave das tabelas, considerando o período de duas horas de tolerância dos Equipamentos de ECF (***), e tratando a faixa de documentos emitidos de acordo com o COO_INI e COO_FIM da redução Z:


SAFX993 (Cupons)
SAFX991 (Redução Z)
Empresa 
= Empresa da SAFX991
Estabelecimento
= Estabelecimento da SAFX991
Data de Emissão (***)
= Data Fiscal da Redução Z ou data do dia imediatamente posterior a ela
Número do Caixa
= Número do Caixa da SAFX991
Número do documento (NUM_COO)
Deve constar da faixa de documentos indicada na Redução Z, de acordo com a regra descrita abaixo.


A recuperação dos cupons da SAFX993 depende da faixa de documentos (cupons) existente na redução Z, da seguinte forma:

Se COO_INI <= COO_FIM 

Neste caso, serão recuperados todos os cupons da SAFX993 cujo número de documento (campo 05-COO) se enquadre na faixa entre COO_INI e COO_FIM indicados na redução Z (SAFX991).

Serão considerados apenas os cupons nas seguintes condições:
(= regra de geração do C400 e "filhos" do Sped Fiscal)
 
   - Tipo de Documento = 1
   - Situação do Documento = 1

Se COO_INI  > COO_FIM 

Este caso indica que a numeração foi reinicializada. Assim, será verificado o número máximo a ser utilizado na geração dos cupons. Esta informação fica na SAFX2087, a partir do campo "04-Número do Caixa" da redução Z (SAFX991).

O número máximo é o campo "38-COO Final para Reinício" da SAFX2087.
Neste caso, a recuperação dos cupons fiscais da SAFX993 será feita em duas faixas de documentos, da seguinte forma:

- do COO_INI (da SAFX991) até COO Final para Reinício (da SAFX2087)
- do 1 até COO_FIM (da SAFX991)

Da mesma forma citada na condição acima, serão considerados apenas os cupons nas seguintes condições:
(= regra de geração do C400 e "filhos" do Sped Fiscal)
 
   - Tipo de Documento = 1
   - Situação do Documento = 1


Recuperação dos itens dos cupons fiscais (SAFX994) a partir do cupom fiscal:

Serão recuperados apenas os itens nas seguintes condições:

   - Situação do Item = 1 ou 3     (= regra de geração do C400 e "filhos" do Sped Fiscal)
   - Somente os itens com tributação de ICMS:
 
Para verificar a tributação do item, é necessário acessar a SAFX99, a partir do campo "15-Código do Totalizador Parcial de ECF" do item (SAFX994), da seguinte forma:

Para acessar a SAFX99:

   - 01-Empresa = campo 01-Empresa da SAFX994
   - 02-Estabelecimento = campo 02-Estabelecimento da SAFX994
   - 03-Modelo Documento = campo 03-Modelo Documento da SAFX994 
   - 04-Número do Caixa = campo 04-Número do Caixa da SAFX994
   - 05-Obrigação = 2 (EFD) 
   - 06-Código do Totalizador Parcial do ECF = campo "15-Código do Totalizador Parcial de ECF" da SAFX994
    - 07-Data de Validade = deve ser a > data possível que seja <= a data do movimento em questão (data da
                                           Redução Z)

Se o campo "08- Código do Totalizador Parcial das Obrigações" da SAFX99 for iniciado por "T", significa que o item é tributado pelo ICMS, e sendo assim, será considerado na totalização dos valores para o relatório.


Para cada redução Z recuperada na SAFX991, serão totalizados os seguintes valores dos itens (SAFX994) dos cupons (SAFX993) que compõe a redução Z:

   - 28-Valor da Base de Cálculo
   - 29-Valor do Imposto

RN03 - Preenchimento dos dados 

Os dados recuperados conforme descrito na RN02 serão ordenados por:

     - Modelo, Data e Número do Documento, no caso dos mapas resumo;
     - Modelo, Data, Número do Caixa e Redução Z, no caso das reduções Z;

Para cada Modelo a Data, as informações serão demonstradas da seguinte forma:

     - A esquerda, as informações dos mapas resumo processados;
     - A direita, as informações das reduções Z processadas;


Layout do relatório: vide planilha "Layout Conferencia ICMS Mapas Resumo"

Cabeçalho:
Na primeira linha será impresso a razão social da Empresa, a data da emissão do relatório e a página.

Na segunda linha será impresso o código e a razão social do Estabelecimento, e o seu CNPJ.

Na terceira linha aparece o título do relatório, e o período informado na tela da geração.

Linha de identificação do Modelo e Data:
Os dados do relatório são demonstrados por Modelo e Data, e nesta linha será impresso o código e a descrição do modelo (obtida na SAFX2024), e a data de referência das informações.

Colunas do Relatório:
N. Documento
Número do documento fiscal (campo "08-Número do Documento Fiscal" da SAFX07)
Vlr Total Nota
Valor total do documento (campo "23-Valor Total do Documento" da SAFX07)
Vlr Base ICMS
Totalização da base de cálculo do ICMS dos itens do documento, conforme RN02 
Vlr ICMS
Totalização do valor do ICMS dos itens do documento, conforme RN02
N. Caixa 
Número do equipamento (campo "04-Número do Caixa" da SAFX991)
Redução Z
Número do contador de redução Z (campo "05-CRZ" da SAFX991)
Vlr Total Líquido 
Total da venda líquida (campo "16-Venda Líquida Diária" da SAFX991)
Vlr Base ICMS
Totalização da base de cálculo do ICMS dos itens dos cupons fiscais da redução Z, conforme RN02 
Vlr ICMS
Totalização do valor do ICMS dos itens dos cupons fiscais da redução Z, conforme RN02
Linha de totalização das colunas:
Ao finalizar os dados de um Modelo e Data, serão totalizadas todas as colunas de valor do relatório, conforme aparece no layout. Esta linha será impressa apenas quando acabar os dados em ambas as partes do relatório, ou seja, ao finalizar tanto os mapa resumo, como as reduções Z do dia.


= = = = 	
