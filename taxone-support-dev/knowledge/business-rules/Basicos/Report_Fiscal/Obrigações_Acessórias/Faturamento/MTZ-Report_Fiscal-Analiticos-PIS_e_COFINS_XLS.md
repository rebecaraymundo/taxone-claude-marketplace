# MTZ-Report_Fiscal-Analiticos-PIS_e_COFINS_XLS

- **Fonte:** MTZ-Report_Fiscal-Analiticos-PIS_e_COFINS_XLS.docx
- **Modificado:** 2021-09-27
- **Tamanho:** 60 KB

---

# Report Fiscal 

#  Relatório Analítico de documentos – PIS e COFINS – Formato XLS

__Localização: __

__Módulo__: Básicos 🡪 Report Fiscal

__Menu__: Obrigações Acessórias 🡪 Faturamento 🡪 PIS/COFINS 🡪 Analítico por Documento – Formato XLS

# DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

MFS29898

Andréa Rocha

Inclusão da coluna de Cancelada no relatório em formato XLS\.

# REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### MFS

__RN00__

__Parâmetros de tela:__

\- Data Inicial: campo do tipo data no formato DD/MM/AAAA\.

\- Data Final: campo do tipo data no formato DD/MM/AAAA\.

\- Período para Seleção: campo do tipo radiobutton com as opções, sendo a opção default “Data Fiscal”:

     \- Data Fiscal

     \- Data Lançto PIS/COFINS

\- Movimento: campo do tipo radiobutton com as opções, sendo a opção default “Ambos”:

      \- Entrada

      \- Saída

      \- Ambos

\- Tipo do Imposto: campo do tipo radiobutton com as opções, sendo a opção default “PIS COFINS”:

      \- PIS COFINS

      \- PIS\-ST COFINS\-ST

\- Considerar notas fiscais canceladas: campo do tipo checkbox, sendo o default desmarcado

MFS29898

__RN01__

__Regra geral \- Critérios para a recuperação dos dados:__

Para a geração deste relatório serão filtrados os documentos fiscais com os itens de mercadorias e serviços, e documentos de telecom que possuírem valores de PIS e COFINS\.

\- Origem dos dados: Tabelas de Documentos Fiscais de Mercadorias e Serviços, e Documentos de Telecom \(SAFX07, SAFX08, SAFX09, SAFX42, SAFX43\);

\- Período para seleção por Data Fiscal: 

       Para documentos fiscais Utilities será considerado a data de emissão do documento Fiscal \(campo 03 da SAFX42\)\.  

       Para documentos fiscais será considerada a data fiscal \(campo DATA\_FISCAL da SAFX07\)\.

\- Período para seleção por Data Lançto PIS/COFINS:

       Para documentos fiscais Utilities será considerado a data de emissão do documento Fiscal \(campo 03 da SAFX42\)\.  

       Para documentos fiscais será considerada a Data de Lançamento na EFD\-PIS/PASEP\-COFINS \(campo 247 da SAFX07\)\.

  \- Movimento deve buscar o campo MOVTO\_E\_S \(campo 03 da SAFX07\), onde:

          Quando selecionado “Entrada” deve ser igual a “1” ou “2” ou “3” ou “4” ou “5”\.

          Quando selecionado “Saída” deve ser igual a “9”\.

          Quando selecionado “Ambos”, buscar todos\.

\- Considerar notas fiscais canceladas

    Se marcado, considerar as notas fiscais canceladas 🡪 Se campo 30 da SAFX07 \(SITUACAO\) for igual a “S”;

    Se desmarcado, gerar o relatório normalmente, sem considerar as notas fiscais canceladas__, ou seja __quando o__ __campo 30  

      da SAFX07 \(SITUACAO\) for igual a “N”;

Serão desconsiderados os documentos fiscais de Telecom SAFX42 / SAFX43 quando o campo __IND\_ORIGEM\_INFO__ da X07 for igual “1”\.  

\- Somente se o documento possuir item;

\- Somente os dados que possuem um ou mais dos campos abaixo maiores que zero:

\- Considerar notas fiscais conjugadas 🡪 Se campo 12 da SAFX07 \(COD\_CLASS\_DOC\_FIS\) = “3” e o Campo 50 da SAFX42 \(COD\_CLASS\_DOC\_FIS\) = “3”\.

MFS29898

__RN02__

Coluna Cancelada

Mostrar a informação se a nota fiscal está cancelada ou não\.

Campo 30 \- Situação da Nota da SAFX07\.

Campo 21 \- Situação da Nota da SAFX42\.

Se Situação da Nota = “S”

      Mostrar “Sim”

Senão

      Mostra “Não”

MFS29898

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

