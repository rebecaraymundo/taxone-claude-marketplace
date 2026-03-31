# MTZ-EFD_PIS-COFINS-Analise-Divergencia-Credito

- **Fonte:** MTZ-EFD_PIS-COFINS-Analise-Divergencia-Credito.docx
- **Modificado:** 2021-09-01
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Matriz da Análise da Divergência do Crédito Disponível

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS69152

Andréa Rocha

Definição das regras para a Análise da Divergência do Crédito Disponível\.

__Localização da tela:__ 

Módulo: SPED 🡪 EFD\-Escrituração Fiscal Digital das Contribuições

Menu:    Obrigações  🡪 Análise das Divergências dos Créditos Disponíveis

__Título da tela: __Análise das Divergências dos Créditos Disponíveis

__Funcionamento da Tela: __No primeiro passo, a tela vai permitir o usuário visualizar as divergências entre o crédito disponível e o utilizado\.  Num segundo passo, <a id="_Hlk81392786"></a>será possível fazer a correção de base dos valores dos créditos utilizados\. A correção poderá ser feita registro a registro, ou para vários registros\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/default__

__Regra__

__OS/CH__

Estabelecimento

Dropdown

S

S

Lista de todos os estabelecimentos cadastrados na tabela ESTABELECIMENTO e que o usuário tenha acesso, e que estejam cadastrados na empresa selecionada\.

Campo obrigatório, caso não preenchido retornar a mensagem “Campo Estabelecimento não preenchido”\.

MFS69152

Período de Seleção dos  Créditos

Editbox

S

S

Formato:

DD/MM/AAAA                a

DD/MM/AAAA

Campo obrigatório, caso não preenchido retornar a mensagem “Campo Período não preenchido”\.

MFS69152

<a id="_Hlk81403917"></a>Tipo de Contribuição

Radiobutton

S

S

Campo do tipo Radiobutton com as opções:

\- PIS/PASEP

\- COFINS

Opção marcada como default \-  PIS/PASEP

MFS69152

Cod\. Tipo Crédito

Dropdown

S

S

Lista de todos os códigos e suas descrições cadastrados na TFIX93 \(EPC\_COD\_CRED\_TRANS\) mais a opção “Todos”\.

Campo obrigatório, caso não preenchido retornar a mensagem “Campo Código Tipo de Crédito não preenchido”\.

MFS69152

<a id="_Hlk81403880"></a>Mostrar Somente os Registros com Diferença

Checkbox

N

S

Campo do tipo checkbox, sendo o default marcado\.

MFS69152

__Processamento – Comparação entre Crédito Disponível e Utilizado__:

Após o preenchimento de todos os campos em tela, a rotina irá comparar os valores dos créditos disponíveis com os créditos utilizados para cada empresa, estabelecimento, período e código do tipo do crédito informados, de acordo com a seleção da contribuição \(PIS/PASEP ou COFINS\)\. 

Os registros devem ser demonstrados de acordo com o campo “Mostrar Somente os Registros com Diferença”\.  Se estiver desmarcado, serão mostrados todos os registros comparados, mesmo os que não tiverem diferença de valores de crédito\.  Caso contrário, serão mostrados somente os registros que tiverem diferença de valores de crédito\.

As tabela utilizadas para a verificação dos créditos são:

\- Tabela da Apuração  \(EPC\_APURACAO\)

\- Tabela dos Créditos Disponíveis  \(EPC\_APUR\_CRED\_DISP\)

\- Tabela dos Créditos Utilizados  \(EPC\_CRED\_UTIL\)

Os campos de Créditos que serão comparados são:

\- Crédito Utilizado para Desconto \(Tabela dos Créditos Disponíveis\) x Crédito Utilizado para Desconto \(Tabela dos Créditos Utilizados\);

\- Crédito Utilizado por Pedido de Ressarcimento \(Tabela dos Créditos Disponíveis\) x Crédito Utilizado por Pedido de Ressarcimento \(Tabela dos Créditos Utilizados\);

\- Crédito Utilizado por Compensação intermediária \(Tabela dos Créditos Disponíveis\) x Crédito Utilizado por Compensação intermediária \(Tabela dos Créditos Utilizados\);

\- Crédito Utilizado por Transferência \(Cisão, Fusão e Incorporação\) \(Tabela dos Créditos Disponíveis\) x Crédito Utilizado por Transferência \(Tabela dos Créditos Utilizados\);

\- Outros Créditos Utilizados \(Tabela dos Créditos Disponíveis\) x Outros Créditos Utilizados \(Tabela dos Créditos Utilizados\)\.

__Quadro \- Análise dos Créditos:__

 

As colunas relacionadas abaixo devem ser mostradas em uma única linha no quadro de análise dos créditos\.  Cada linha deve ter um checkbox no início,  que servirá para selecionar os registros em que serão feitas as atualizações dos créditos\.  Deve\-se colocar um botão para se fazer a Atualização dos Créditos, que após o usuário analisar as linhas com os valores dos créditos, poderá utilizar para atualizar os valores de créditos que estiverem com diferença\.

\- Mês/Ano 🡪 Mês/Ano da apuração da tabela EPC\_APUR\_CRED\_DISP relativo a EPC\_APURACAO

\- Tipo do Crédito 🡪 Código do Tipo do Crédito da tabela EPC\_APUR\_CRED\_DISP

\- Origem do Crédito 🡪 Origem do Crédito da tabela EPC\_APUR\_CRED\_DISP

\- Crédito Apurado 🡪 Valor do Crédito Apurado da tabela EPC\_APUR\_CRED\_DISP

\- Crédito Extemporâneo 🡪 Valor do Crédito Extemporâneo da tabela EPC\_APUR\_CRED\_DISP

\- Crédito Utilizado para Desconto – Disponível 🡪 Crédito Utilizado para Desconto da tabela EPC\_APUR\_CRED\_DISP

\- Crédito Utilizado para Desconto – Utilizado 🡪 Crédito Utilizado para Desconto da tabela EPC\_CRED\_UTIL

\- Crédito Utilizado por Pedido de Ressarcimento – Disponível 🡪 Crédito Utilizado por Pedido de Ressarcimento da tabela 

   EPC\_APUR\_CRED\_DISP

\- Crédito Utilizado por Pedido de Ressarcimento – Utilizado 🡪 Crédito Utilizado por Pedido de Ressarcimento da tabela 

   EPC\_CRED\_UTIL

\- Crédito Utilizado por Compensação intermediária – Disponível 🡪 Crédito Utilizado por Compensação intermediária da tabela 

   EPC\_APUR\_CRED\_DISP

\- Crédito Utilizado por Compensação intermediária – Utilizado 🡪 Crédito Utilizado por Compensação intermediária da tabela 

   EPC\_CRED\_UTIL

\- Crédito Utilizado por Transferência \(Cisão, Fusão e Incorporação\) – Disponível 🡪 Crédito Utilizado por Transferência da tabela   

  EPC\_APUR\_CRED\_DISP

\- Crédito Utilizado por Transferência \(Cisão, Fusão e Incorporação\) – Utilizado 🡪 Crédito Utilizado por Transferência da tabela   

  EPC\_CRED\_UTIL

\- Outros Créditos Utilizados – Disponível 🡪 Outros Créditos Utilizados da tabela  EPC\_APUR\_CRED\_DISP

\- Outros Créditos Utilizados – Utilizado 🡪 Outros Créditos Utilizados da tabela  EPC\_CRED\_UTIL

\- Crédito Disponível 🡪 Valor do Crédito Disponível da tabela  EPC\_APUR\_CRED\_DISP

	

__Atualização dos Créditos__:

Após fazer a comparação dos créditos disponíveis com os utilizados, o usuário vai ter a opção de corrigir os créditos que estiverem com diferença\.  Podendo selecionar um registro ou vários registros para fazer a correção\.  Deve\-se colocar um botão para selecionar todos os registros e um para desmarcar todos os registros\.

Quando o usuário selecionar a opção de atualização dos créditos, deve\-se dar a mensagem abaixo, com as opções “Sim” e “Não”:

“Deseja realmente atualizar os valores dos créditos disponíveis para os créditos utilizados, para o\(s\) registro\(s\) selecionado\(s\) ?”

Se a opção escolhida for “Sim”, será feita a atualização dos créditos conforme a definição abaixo\.  Senão, nenhum procedimento será feito\.

A correção será feita da seguinte forma:

Para cada registro selecionado, o valor do crédito disponível será atualizado no valor do crédito utilizado, para todos os campos de créditos:

   

\- Crédito Utilizado para Desconto;

\- Crédito Utilizado por Pedido de Ressarcimento;

\- Crédito Utilizado por Compensação intermediária;

\- Crédito Utilizado por Transferência \(Cisão, Fusão e Incorporação\);

           \- Outros Créditos Utilizados\.

