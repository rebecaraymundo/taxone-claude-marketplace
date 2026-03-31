# MTZ-DW-Manutencao_SAFX112

- **Fonte:** MTZ-DW-Manutencao_SAFX112.docx
- **Modificado:** 2024-07-12
- **Tamanho:** 70 KB

---

THOMSON REUTERS

__Módulo Data Warehouse__

__Manutenção das Observações da Nota Fiscal \(SAFX112\)__

__Localização__: Menu Básicos, Módulo Data Warehouse, item Manutenção 🡪 Documento Fiscal 🡪 Observações da Nota Fiscal

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS62589

Andréa Rocha 

Criação da tela de manutenção das Observações da Nota Fiscal, em um item de menu separado da manutenção do documento fiscal\.  Deste modo, serão disponibilizadas 2 telas de manutenção da tabela SAFX112, uma através da tela de manutenção do documento fiscal \(Aba Observações do Lançamento Fiscal\) e outra através desta tela\.

26/03/2021

MFS613525

Graciela Soares 

Criação de Novos Campos – Tabela SAFX112 para atendimento à NFCom

12/07/2024

REGRAS DE NEGÓCIO

__RN00 – Regras Gerais__

Esta tela deve permitir ao usuário incluir, alterar e/ou excluir registros na tabela de Observações da Nota Fiscal\.

 \- A pasta “abre” deve selecionar os documentos fiscais, a partir da tabela de documentos fiscais \(SAFX07\)\.

 – A apresentação da tela será sempre em 2 quadros, na parte superior os dados do documento fiscal selecionado \(RN02 \- RN09/10/11\), e na parte inferior, os dados da tela de Observações da Nota Fiscal \(RN12 \- RN15\)\.  Na parte superior da tela, os campos demonstrados serão somente para consulta\.

__Obs__\.: Ao excluir um registro da tabela de Observações da Nota Fiscal, deve\-se verificar se este registro não está relacionado a nenhum das tabelas relacionadas a SAFX112 \(tabelas filhas, como exemplo SAFX113\)\.  Se houver algum registro relacionado em alguma das tabelas filhas, dar a mensagem abaixo na tela e perguntar se desejar realmente excluir o registro da SAFX112, com as opções “Sim” e “Não”:

	“Existem registros cadastrados em tabelas relacionadas a X112\_OBS\_DOCFIS\. Deseja excluir a tabela de Observações da Nota Fiscal mesmo assim?”

__RN02 – Estabelecimento__

Campo Estabelecimento: campo destinado ao código e a descrição do Estabelecimento, somente para consulta\.

__RN03 – Data da Escrita Fiscal__

Campo Data Escrita Fiscal: campo destinado a data fiscal, somente para consulta\.

__RN04 – Movimento Entrada/Saída__

Campo Movimento Entrada/Saída: campo destinado a informar o Movimento Entrada/Saída, de acordo com:

1 \- Documento de Entrada, Documento de Terceiros;

2 \- Documento de Entrada emitida pelo Estabelecimento, acolhendo Notas de Produtores Agropecuários;

3 \- Documento de Entrada emitida pelo Estabelecimento, por retorno de mercadorias não entregues ao destinatário;                                                                                                                                        

4 \- Documento de Entrada emitida pelo Estabelecimento, outros motivos legais;

5 \- Documento de Entrada emitida pelo Estabelecimento, globalizando Conhecimento de Frete ou Material Uso/Consumo;

9 \- Documento de Saída\.

Campo somente para consulta\.

__RN05 – Normal ou Devolução__

Campo Normal ou Devolução: campo destinado a informar o motivo da Entrada / Saída, de acordo com:

1 \- Normal;

2 \- Devolução\.

Campo somente para consulta\.

__RN06 – Tipo do Documento__

Campo Tipo do Documento: campo destinado a informar o Tipo de Documento de acordo com a Tabela de Tipo de Documentos  \(SAFX2005\)\. Mostrar o código e a descrição\.

Campo somente para consulta\.

__RN07/08 – Pessoa Física/Jurídica__

Campo Pessoa Física/Jurídica: campo destinado a informar o Indicador/Código/Descrição da Pessoa Física/Jurídica relacionada \(SAFX04\)\.

 Informar o Indicador de Pessoa Física/Jurídica relacionada \(SAFX04\), de acordo com:

1 \- Fornecedor;

2 \- Cliente;

3 \- Estabelecimento;

4 \- Transportadora;

5 \- Cliente/Fornecedor/Transportadora\.ao código e a descrição do Estabelecimento, somente para consulta\.

Campo somente para consulta\.

__RN09/10/11 – Número do Documento Fiscal__

Campo Número do Documento Fiscal: campo destinado a informar o número, a série e subsérie do documento fiscal\.

Campo somente para consulta\.

__RN12 – Código da Observação__

Campo Código da Observação: campo destinado a informar o código da observação de acordo com a Tabela de Cadastro das Observações \(SAFX2009\)\. Mostrar o código e a descrição da observação\.

Este campo trabalha com janela de seleção dos dados da Tabela de Cadastro das Observações \(SAFX2009\)\.

Quando o campo for digitado e o código não for encontrado na tabela, será exibida a mensagem de erro abaixo, e a operação não será salva:

*                     “Código de Observação não cadastrado”*

Campo obrigatório\.

Obs\.: Como o campo código de observação faz parte da PK, uma vez incluído, ele não pode ser alterado\.

__RN13 – Tipo de Observação__

Campo Tipo de Observação: campo do tipo listbox, destinado a informar o Tipo de Observação, de acordo com:

I \- Observação referente às Informações Complementares da Nota

L \- Observação referente aos Lançamentos Fiscais da Nota

Campo obrigatório\.

Obs\.: Como o campo tipo de observação faz parte da PK, uma vez incluído, ele não pode ser alterado\.

__RN14 – Descrição Complementar__

Campo Descrição Complementar: campo destinado a informar a Descrição Complementar da Observação\.  Campo alfanumérico de 500 posições\.

Campo não obrigatório\.

__RN15 –__ __Vinculação__

Campo Vinculação: campo do tipo listbox, destinado a informar a vinculação da informação complementar do documento fiscal, de acordo com:

1 \- EFD ICMS/IPI;

2 \- EFD PIS/COFINS;

3 \- Ambas as Obrigações\.  

O preenchimento desse campo é obrigatório para os registros da SAFX112 com Tipo de Observação \(campo 13\) = I \- Observação referente às Informações Complementares da Nota\.

Após o preenchimento dos campos Tipo de Observação e Vinculação, deve ser feita a seguinte verificação:

Se o Tipo de Observação = “I” e a Vinculação <> “2” e a Classificação do Documento Fiscal \(campo 12 da SAFX07\) = “2”

   Será exibida a mensagem de erro abaixo, e a operação não será salva:

*      “Para informacoes complementares do documento fiscal de servico, o indicador de vinculacao deve ser igual a  2 \- EFD PIS/COFINS\.”*

<a id="_Hlk171687353"></a>__RN16 – Informações adicionais de interesse do Fisco__

Campo Descrição Complementar: campo destinado a informar a Informações adicionais de interesse do Fisco\.  Campo alfanumérico de 2000 posições\.

Campo não obrigatório\.

__RN17 – Informações complementares de interesse do Contribuinte__

Campo Descrição Complementar: campo destinado a informar a Informações complementares de interesse do Contribuinte\.  Campo alfanumérico de 3000 posições\.

Campo não obrigatório\.

