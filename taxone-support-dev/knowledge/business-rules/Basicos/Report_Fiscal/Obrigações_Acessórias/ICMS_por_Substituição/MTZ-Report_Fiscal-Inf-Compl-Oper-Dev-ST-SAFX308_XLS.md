# MTZ-Report_Fiscal-Inf-Compl-Oper-Dev-ST-SAFX308_XLS

- **Fonte:** MTZ-Report_Fiscal-Inf-Compl-Oper-Dev-ST-SAFX308_XLS.docx
- **Modificado:** 2023-11-07
- **Tamanho:** 68 KB

---

# Report Fiscal 

#  Relatório de Informações Complementares das Operações de Devolução Sujeitas ao ST \(SPED\-EFD \- C181, C186\) – Formato XLS

__Localização: __

__Módulo__: Básicos 🡪 Report Fiscal

__Menu__: Menu: Obrigações Acessórias 🡪 ICMS por Substituição 🡪 Operações com Substituição Tributária 🡪 Inf\. Compl\. Operações de Devolução Sujeitas ao ST \(SPED\-EFD \- C181, C186\) – Formato XLS

# DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

MFS67589

Aline Melo

Criação do relatório das Informações Complementares das Operações de Devolução Sujeitas ao ST \(SPED\-EFD \- C181, C186\) – Formato XLS\. 

MFS566368

Andréa Rocha

Inclusão de um parâmetro para definir se serão geradas as colunas de valores totais no arquivo\.

# REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### MFS

__RN00__

__Parâmetros de tela:__

\[MFS566368\] Inclusão do parâmetro para indicar se serão geradas as colunas de valores totais

\- Data Inicial: campo do tipo data no formato DD/MM/AAAA\.

\- Data Final: campo do tipo data no formato DD/MM/AAAA\.

\- Gerar as Colunas de Valores Totais: campo do tipo checkbox, default desmarcado\. 

\- UF: campo do tipo listbox que exibirá todas as UFs da tabela Estado mais a opção “Todas”\.

\- Estabelecimentos: Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\. Incluir botão “Selecionar” para seleção de estabelecimento e o botão “Marcar Todos” caso o usuário queira marcar todos os estabelecimentos\.

MFS67589

MFS566368

__RN01__

__Regra geral \- Critérios para a recuperação dos dados:__

Para a geração deste relatório serão filtradas as Informações Complementares das Operações de Devolução Sujeitas ao ST e os documentos fiscais relacionados\.

\- Origem dos dados: Informações Complementares Complementares das Operações de Devolução Sujeitas ao ST \(SAFX308\);

\- Período para seleção, será considerada a data fiscal \(campo DATA\_FISCAL da SAFX308\)\.

Serão demonstradas todas as colunas da tabela SAFX308, ordenadas por empresa, estabelecimento, data fiscal, número e série do documento fiscal, número do item da nota de devolução\.  

MFS67589

__RN02__

__Layout do Relatório__

  O relatório não terá opção de impressão, ele somente terá a opção de salvar em excel\.

Os campos abaixo serão mostrados no excel:

MFS67589

Empresa 

Empresa da geração

Estabelecimento

Estabelecimento da geração

CPF\_CGC do estabelecimento

CPF\_CGC da tabela Estabelecimento

Razão Social do estabelecimento

Razão social da tabela Estabelecimento

Dt Fiscal NF Devolução

Data Escrita Fiscal \(campo 03 da SAFX308\)

Tipo Movimento NF Devolução

Movimento Entrada/Saída \(campo 04 da SAFX308\)

Norm/Dev NF Devolução

Normal ou Devolução \(campo 05 da SAFX308\)

Tipo Documento NF Devolução

Tipo do Documento \(campo 06 da SAFX308\)

Ind\./Cód\. Pessoa Fis/Jur NF Devolução

Indicador e Código da Pessoa Física/Jurídica \(campos 07 e 08 da SAFX308\)

CPF\_CGC Pessoa Fis/Jur

CPF\_CGC \(campo 06 da SAFX04\)

Razão Social Pessoa Fis/Jur

Razão Social \(campo 06 da SAFX04\)

Número NF Devolução

Número do Documento Fiscal \(campo 09 da SAFX308\)

Série NF Devolução

Série do Documento Fiscal \(campo 10 da SAFX308\)

Subsérie NF Devolução

Subsérie do Documento Fiscal \(campo 11 da SAFX308\)

Ind\./Cód\. Produto NF Devolução

Indicador e Código de Produto \(campos 12 e 13 da SAFX308\)

Descrição do Produto

Descrição do Produto \(campo 04 da SAFX2013\)

Unid\. Padrão NF Devolução

Unidade Padrão \(campo 14 da SAFX308\)

Item NF Devolução

Item da Nota Fiscal \(campo 15 da SAFX308\)

Espécie Doc Ref Devolução

Espécie do Documento de Referência da Devolução \(campo 16 da SAFX308\)

Número Doc Fiscal Ref

Número do Documento Fiscal de Referência \( campo 17 da SAFX308\)

Série Doc Fiscal Ref

Série do Documento Fiscal de Referência \(campo 18 da SAFX308\)

Subsérie Doc Fiscal Ref

Subsérie do Documento Fiscal de Referência \(campo 19 da SAFX308\)

Tipo Doc Ref

Tipo do Documento de Referência \(campo 20 da SAFX308\)

Data Fiscal Doc Ref

Data Escrita Fiscal do Documento de Referência \(campo 21 da SAFX308\)

Ind\./Código Pessoa Física/Jurídica Doc Ref

Indicador e Código Pessoa Física/Jurídica do Documento de Referência \(campos 22 e 23 da SAFX308\)

Modelo Cupom Fiscal Ref

Modelo do Cupom Fiscal de Referência \(campo 24 da SAFX308\)

Número Caixa do Cupom Fiscal Ref

Número do Caixa do Cupom Fiscal de Referência \(campo 25 da SAFX308\)

COO \(Contador de Ordem de Operação\) do Cupom Fiscal Ref

COO \(Contador de Ordem de Operação\) do Cupom Fiscal de Referência \(campo 26 da SAFX308\)

Data Emissão do Cupom Fiscal Ref

Data de Emissão do Cupom Fiscal de Referência \(campo 27 da SAFX308\)

Número Equipamento SAT do Cupom Fiscal Ref

Número do Equipamento SAT do Cupom Fiscal de Referência \(campo 28 da SAFX308\)

Número Cupom Fiscal Ref 

Número do Cupom Fiscal do Referência \(campo 29 da SAFX308\)

Número Item Doc Ref

Número do Item do Documento de Referência \(campo 30 da SAFX308\)

Código Motivo

Código Motivo \(campo 31 da SAFX308\)

Quantidade Convertida

Quantidade Convertida \(campo 32 da SAFX308\)

Unidade de Medida

Unidade de Medida \(campo 33 da SAFX308\)

Vlr Unit Conv

Valor Unitário Conv \(campo 34 da SAFX308\)

Vlr Unit ICMS OP Conv

Valor Unitário ICMS OP Conv \(campo 35 da SAFX308\)

Vlr Unit Base ICMS ST Conv da Entrada

Valor Unitário Base ICMS ST Conv da Entrada \(campo 36 da SAFX308\)

Vlr Unit ICMS ST Conv da Entrada

Valor Unitário ICMS ST Conv da Entrada \(campo 37 da SAFX308\)

Vlr Unit FCP ST Conv da Entrada

Valor Unitário FCP ST Conv da Entrada \(campo 38 da SAFX308\)

Vlr Unit ICMS OP Estoque Conv \(Saída\)

Valor Unitário ICMS OP Estoque Conv \(campo 39 da SAFX308\)

Vlr Unit ICMS ST Estoque Conv \(Saída\)

Valor Unitário ICMS ST Estoque Conv \(campo 40 da SAFX308\)

Vlr Unit FCP ICMS ST Estoque Conv \(Saída\)

Valor Unitário FCP ICMS ST Estoque Conv \(campo 41 da SAFX308\)

Vlr Unit ICMS Oper Conv \(Saída\)

Valor Unitário ICMS na Operação Conv \(campo 42 da SAFX308\)

Vlr Unit ICMS ST Conv Rest \(Saída\)

Valor Unitário ICMS ST Conv Rest \(campo 43 da SAFX308\)

Vlr Unit FCP ST Conv Rest \(Saída\)

Valor Unitário FCP ST Conv Rest \(campo 44 da SAFX308\)

Vlr Unit ICMS ST Conv Compl \(Saída\)

Valor Unitário ICMS ST Conv Compl \(campo 45 da SAFX308\)

Vlr Unit FCP ST Conv Compl \(Saída\)

Valor Unitário FCP ST Conv Compl \(campo 46 da SAFX308\)

Vlr Item

__\[MFS566368\]__ Inclusão das colunas de valores totais de acordo com o parâmetro de tela

Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado

      Valor Unitário Conv\. \(campo 34 da SAFX308\) \* Quantidade Convertida \(campo 32 da 

      SAFX308\)

Senão 

       Essa coluna não deve ser gerada no arquivo\.

Vlr ICMS Devido

__\[MFS566368\]__ Inclusão das colunas de valores totais de acordo com o parâmetro de tela

Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado

     Valor Unitário ICMS OP Conv\. \(campo 35 da SAFX308\) \* Quantidade Convertida 

     \(campo 32 da SAFX308\)

Senão 

       Essa coluna não deve ser gerada no arquivo\.

Vlr ICMS Pago

__\[MFS566368\]__ Inclusão das colunas de valores totais de acordo com o parâmetro de tela

Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado

     \(Valor Unitário ICMS OP Estoque Conv\. \(Saídas\) \(campo 39 da SAFX308\) \+ Valor 

      Unitário ICMS\-ST Estoque Conv\. \(Saídas\) \(campo 40 da SAFX308\) \+ Vlr Unit FCP ICMS ST Estoque Conv \(Saída\) \(campo 41 da SAFX308\)\) \* Quantidade Convertida 

      \(campo 32 da SAFX308\)

Senão 

       Essa coluna não deve ser gerada no arquivo\.

Vlr Restituição

__\[MFS566368\]__ Inclusão das colunas de valores totais de acordo com o parâmetro de tela

Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado

     \(Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\) \(campo 43 da SAFX308\) \+ Valor Unitário 

      FCP\-ST Conv\. Rest\. \(Saídas\) \(campo 44 da SAFX308\)\) \* Quantidade Convertida 

      \(campo 32 da SAFX308\)

Senão 

       Essa coluna não deve ser gerada no arquivo\.

Vlr Complemento

__\[MFS566368\]__ Inclusão das colunas de valores totais de acordo com o parâmetro de tela

Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado

     \(Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\) \(campo 45 da SAFX308\) \+ Valor 

      Unitário FCP\-ST Conv\. Compl\. \(Saídas\) \(campo 46 da SAFX308\)\) \* Quantidade 

      Convertida \(campo 32 da SAFX308\)

Senão 

       Essa coluna não deve ser gerada no arquivo\.

Alíquota Interna

__\[MFS566368\]__ Inclusão das colunas de valores totais de acordo com o parâmetro de tela

Se o parâmetro “Gerar as Colunas de Valores Totais” estiver marcado

      \(Coluna Vlr ICMS Devido / Coluna Vlr Item\) \* 100

Senão 

       Essa coluna não deve ser gerada no arquivo\.

Obs\.: Mostrar a coluna alíquota com 2 casas decimais\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

