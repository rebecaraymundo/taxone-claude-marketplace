# MTZ-DW-Manutencao_SAFX113

- **Fonte:** MTZ-DW-Manutencao_SAFX113.docx
- **Modificado:** 2021-04-06
- **Tamanho:** 71 KB

---

THOMSON REUTERS

__Módulo Data Warehouse__

__Manutenção do Ajuste/Outros Valores do Lançamento Fiscal \(SAFX113\)__

__Localização__: Menu Básicos, Módulo Data Warehouse, item Manutenção 🡪 Documento Fiscal 🡪 Ajuste/Outros Valores do Lançamento Fiscal

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS62590

Andréa Rocha 

Criação da tela de manutenção do Ajuste/Outros Valores do Lançamento, em um item de menu separado da manutenção do documento fiscal\.  Deste modo, serão disponibilizadas 2 telas de manutenção da tabela SAFX113, uma através da tela de manutenção do documento fiscal \(Aba Observações do Lançamento Fiscal\) e outra através desta tela\.

26/03/2021

REGRAS DE NEGÓCIO

__RN00 – Regras Gerais__

Esta tela deve permitir ao usuário incluir, alterar e/ou excluir registros na tabela de Ajuste/Outros Valores do Lançamento\.

 \- A pasta “abre” deve selecionar as observações relacionadas aos documentos fiscais, a partir da tabela de Observações da Nota Fiscal \(SAFX112\)\.  Somente devem ser recuperados os registros em que o campo Tipo de Observação seja igual a “L” \(Observação referente aos Lançamentos Fiscais da Nota\)\.

 – A apresentação da tela será sempre em 2 quadros, na parte superior os dados das Observações da Nota Fiscal selecionada \(RN02 \- RN12\), e na parte inferior, os dados da tela de Ajuste/Outros Valores do Lançamento \(RN13 \- RN19\)\.

__RN02 – Estabelecimento__

Campo Estabelecimento: campo destinado ao código e a descrição do Estabelecimento, somente para consulta\.

__RN03 – Data da Escrita Fiscal__

Campo Data da Escrita Fiscal: campo destinado a data fiscal, somente para consulta\.

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

__RN12 – Código da Observação e Tipo da Observação__

Campo Código da Observação: campo destinado a informar o código da observação de acordo com a Tabela de Cadastro das Observações \(SAFX2005\)\. Mostrar o código e a descrição da observação\.

Campo Tipo de Observação: campo do tipo listbox, destinado a informar o Tipo de Observação, de acordo com:

I \- Observação referente às Informações Complementares da Nota

L \- Observação referente aos Lançamentos Fiscais da Nota

Campos somentes para consulta\.

__RN13 – Código do Ajuste__

Campo Código do Ajuste: campo destinado a informar o código de ajuste de acordo com a Tabela de Códigos de Ajustes provenientes de NF's \(SPED Fiscal\), cadastrada através do item de menu: Manutenção 🡪 Cadastros 🡪 Códigos de Ajustes provenientes de NF's \(SPED Fiscal\)\. Mostrar o código e a descrição do ajuste\.

Quando o campo for digitado e o código não for encontrado na tabela, será exibida a mensagem de erro abaixo, e a operação não será salva:

*                     “Código de Ajuste não cadastrado”*

Campo obrigatório\.

Obs\.: Como o campo código de ajuste faz parte da PK, uma vez incluído, ele não pode ser alterado\.

__RN14 – Descrição Complementar do Ajuste__

Campo Descrição Complementar do Ajuste: campo destinado a informar a Descrição Complementar do Ajuste\.  Campo alfanumérico de 255 posições\.

Campo não obrigatório\.

__RN15 – Número do Item da Nota / Produto__

Campo Número do Item da Nota: campo do tipo Listbox, destinado a informar o número do item da nota fiscal ao qual se refere o ajuste\.  Devem ser mostrados todos os números de itens cadastrados na SAFX08, referentes ao documentos fiscal selecionado através da SAFX112\.  E também dever ter uma linha em branco no Listbox para o usuário, caso o ajuste não seja relacionado a um item específico da nota fiscal\.

Campo numérico de 5 posições\.

Campo Produto: campo destinado a informar a descrição do produto referente ao item da nota fiscal selecionado\.  Quando for informado um número de item, o campo Produto deve ser preenchido com a descrição do produto da SAFX08 referente a este item\.

Campo somente para consulta\.

__RN16 –__ __Base de Cálculo do ICMS__

Campo Base de Cálculo do ICMS: campo destinado a informar o valor da base de cálculo do ICMS\. Campo numérico, sendo 15 inteiros e 2 decimais\.

Campo não obrigatório\.

__RN17 –__ __Alíquota do ICMS__

Campo Alíquota do ICMS: campo destinado a informar a alíquota utilizada no cálculo\. Campo numérico, sendo 3 inteiros e 4 decimais\.

Campo não obrigatório\.

__RN18 –__ __Valor do ICMS__

Campo Valor do ICMS: campo destinado a informar o o valor preenchido do imposto calculado\. Campo numérico, sendo 15 inteiros e 2 decimais\.

Campo não obrigatório\.

__RN19 –__ __Outros Valores__

Campo Outros Valores: campo destinado a informar outros valores a serem\.  Campo numérico, sendo 15 inteiros e 2 decimais\.

Campo não obrigatório\.

__RN – Validação dos registros__

Quando for salvar um registro, deve ser feita a seguinte validação:

Pelo menos um dos campos de valor deve estar preenchido e com valor maior que zero, Base de Cálculo do ICMS ou Alíquota do ICMS ou Valor do ICMS ou Outros Valores, se não estiver será exibida a mensagem de erro abaixo, e a operação não será salva:

*“Ao menos um dos valores: <Aliquota de ICMS>, <Valor Base ICMS>, <Valor ICMS> ou <Valor Outros> deve ser preenchido ou maior que zero\.”*

   

