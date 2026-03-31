# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX241

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX241.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX241

Tabela Relação dos Eventos Societários / Empresas Participantes do Evento

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Carga 🡪 Execução

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

\- Exportação Dados 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-9667

Lara Aline

Definição das regras de carga, exportação, importação Online e Batch da SAF241\.

MFS30647

Andréa Rocha

Alteração da regra do campo data do evento societário

MFS\-32775 \(CH26646/2019\)

Alessandra Cristina Navatta

Inclusão de regra para permitir importar registros com data de consolidação campos 3 e 4 \(DATA\_INI\_CONS e DATA\_FIM\_CONS\) da SAFX 241 compreendida na data de consolidação \(DATA\_INI\_CONS e DATA\_FIM\_CONS\) da SAFX240, para a empresa Consolidada Campo 07 \- COD\_EMP\_OPER da SAFX241\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN01

A rotina de importação, online e batch, do módulo JOB Servidor deve ser ajustada para que contemple as informações da tabela SAFX241 – Relação dos Eventos Societários / Empresas Participantes do Evento, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Data Inicial do período consolidado

N

008

SIM

SIM

Data Final do período consolidado

N

008

SIM

SIM

Código da Empresa Participante

A

004

SIM

SIM

Evento Societário ocorrido no período

A

001

SIM

SIM

Código da Empresa envolvida na operação

A

004

NAO

SIM

Data do Evento Societário

N

008

SIM

NAO

Condição da empresa relacionada à operação

A

001

NAO

NAO

Percentual da empresa participante envolvido na operação

A

008

NAO

NAO

 

__Verificação de existência do registro pai__

Por ser esta tabela filha da SAFX240, no momento da importação deve ser verificada a existência de registro correspondente na tabela pai, considerando como chave de relacionamento os campos Código da Empresa, Código do Estabelecimento, Data Inicial do período consolidado, Data Final do período consolidado, Código da Empresa Participante\. Caso não encontre, retornar a mensagem: “SAFX240 correspondente a SAFX241 não localizada”\. 

Será necessário verificar também se na SAFX240 \(pai\) o campo Evento Ocorrido no Período é igual a ‘S’, caso contrário retornar a mensagem: “SAFX240 correspondente a SAFX241 com o indicador Evento Ocorrido no Período diferente de ‘S’”\.

MFS\-9667

RN02

__Código da Empresa__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Empresa não está preenchido”\.

*\(registros das tabelas SAFX sem a informação da Empresa serão desconsiderados\)*

MFS\-9667

RN03

__Código do Estabelecimento__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Código de Estabelecimento deve ser preenchido”\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento serão desconsiderados\)*

MFS\-9667

RN04

__Data Inicial do período consolidado__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Data Início do período consolidado é obrigatório \- deve ser preenchido”\. Quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data Início do período consolidado com formato invalido”\.

MFS\-9667

RN05

__Data Final do período consolidado__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Data Final do período consolidado é obrigatório \- deve ser preenchido”\. Quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data Final do período consolidado com formato invalido”\. 

A data informada neste campo deve ser maior ou igual a data informada no campo Data Início da Consolidação\. Caso seja menor, retornar mensagem de erro: “A Data Final do período consolidado não pode ser menor que a Data Inicial do período consolidado”\.

\[__MFS\-32775\(CH26646/2019\)\]__

Será permitido importar registro com período consolidado \(campos 3 \-DATA\_INI\_CONS e 4 \- DATA\_FIM\_CONS da SAFX241\) menor ou igual ao período consolidado da SAFX240 \(considerando a empresa envolvida\)\.

Exemplo: Período de consolidação da SAFX240 igual a 01/01/2018 a 31/12/2018 \(datas utilizadas no K030\)\. Serão permitidos incluir registros da SAFX241 compreendidos neste período e não apenas igual a informação do período indicado na consolidação\. Isto se faz necessário, pois a empresa que está participando da consolidação pode ter sofrido uma situação especial no período e começou ou finalizou suas atividades no período diferente da consolidação \(indicado na SAFX240\)\. 

MFS\-9667

MFS\-32775 \(CH26646/2019\)

RN06

__Código da Empresa Participante __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Código da Empresa Participante é obrigatório \- deve ser preenchido”\. 

Crítica da existência do Código da Empresa Participante na SAFX240:

Será verificada a existência do Código da Empresa Participante informado \(Código da Empresa Participante\) na Tabela SAFX240, e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Código da Empresa Participante nao esta cadastrado”\.

MFS\-9667

RN07

__Evento Societário ocorrido no período __

Opções válidas:

1 – Aquisição 

2 – Alienação 

3 – Fusão 

4 – Cisão Parcial 

5 – Cisão Total 

6 – Incorporação 

7 – Extinção 

8 – Constituição 

Campo de preenchimento obrigatório, caso não preenchido exibir a seguinte mensagem: “O Campo Evento Societário ocorrido no período é obrigatório \- deve ser preenchido”\. Quando informado uma opção inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo Evento Societário ocorrido no período com opção invalida”\.

MFS\-9667

RN08

__Data do Evento Societário __

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “O Campo Data do Evento Societário é obrigatório \- deve ser preenchido”\. Quando informado se for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Campo de Data do Evento Societário com formato invalido”\.

__\[MFS30647\]__

Verificar se a data informada neste campo corresponde ao período informado nos campos Data Inicial do período consolidado e Data Final do período\. Ou que a data seja do ano anterior, do mesmo ano ou do ano posterior do período consolidado\.  Caso esteja fora desses períodos, retornar mensagem de erro: “A Data do Evento Societário não pode ser diferente da data do período consolidado, ou do ano anterior ou do ano posterior deste período”\. 

MFS\-9667

MFS30647

RN09

__Código da Empresa envolvida na operação __

Se o campo “Evento Societário ocorrido no período” estiver preenchido com “1” \(Aquisição\), “2” \(Alienação\), “3” \(Fusão\), “4” \(Cisão Parcial\), “5” \(Cisão Total\) ou “6” \(Incorporação\), esse campo é de preenchimento obrigatório e se não estiver preenchido exibir a seguinte mensagem: “O Campo Código da Empresa envolvida na operação é obrigatório quando o campo “Evento Societário ocorrido no período” estiver preenchido com “1” \(Aquisição\), “2” \(Alienação\), “3” \(Fusão\), “4” \(Cisão Parcial\), “5” \(Cisão Total\) ou “6” \(Incorporação\) \- deve ser preenchido”\. 

Se o campo “Evento Societário ocorrido no período” estiver preenchido com “7” \(Extinção\) ou “8” \(Constituição\), esse campo não deve ser preenchido e se preenchido exibir a seguinte mensagem: “O Campo Código da Empresa envolvida na operação não deve ser preenchido quando o campo “Evento Societário ocorrido no período” estiver preenchido com “7” \(Extinção\) ou “8” \(Constituição\)\.”\. 

Crítica da existência do Código da Empresa envolvida na operação na SAFX240:

Será verificada a existência do Código da Empresa envolvida na operação informado \(Código da Empresa Participante\) na Tabela SAFX240, e caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem: “O Código da Empresa envolvida na operação nao esta cadastrado”\.

Verificar também que o código de empresa informado neste campo não poderá ser igual ao informado no campo Código da Empresa Participante\. Caso o código seja igual, retornar mensagem de erro: “O Código da Empresa envolvida na operação não pode ser igual ao Código da Empresa Participante informado”\. 

MFS\-9667

RN10

__Condição da empresa relacionada à operação __

Opções válidas:

1 – Sucessora; 

2 – Adquirente; 

3 – Alienante\. 

Se o campo “Evento Societário ocorrido no período” estiver preenchido com “1” \(Aquisição\), “2” \(Alienação\), “3” \(Fusão\), “4” \(Cisão Parcial\), “5” \(Cisão Total\) ou “6” \(Incorporação\), esse campo é de preenchimento obrigatório e se não estiver preenchido exibir a seguinte mensagem: “O Campo Condição da empresa relacionada à operação é obrigatório quando o campo “Evento Societário ocorrido no período” estiver preenchido com “1”, “2”, “3”, “4”, “5” ou “6” \- deve ser preenchido”\. 

Se o campo “Evento Societário ocorrido no período” estiver preenchido com “7” \(Extinção\) ou “8” \(Constituição\), esse campo não deve ser preenchido e se preenchido exibir a seguinte mensagem: “O Campo Condição da empresa relacionada à operação não deve ser preenchido quando o campo “Evento Societário ocorrido no período” estiver preenchido com “7” ou “8”\.”\. 

Se a opção for preenchida com “1” \(Sucessora\), verificar se o campo “Evento Societário ocorrido no período” foi preenchido como “3” \(Fusão\), “4” \(Cisão Parcial\), “5” \(Cisão Total\) ou “6” \(Incorporação\), se não exibir a seguinte mensagem: “A Condição da empresa relacionada à operação não é compatível com o Evento Societário ocorrido no período informado”\.

Se a opção for preenchida com “2” \(Adquirente\), verificar se o campo “Evento Societário ocorrido no período” foi preenchido como “1” \(Aquisição\), se não exibir a seguinte mensagem: “A Condição da empresa relacionada à operação não é compatível com o Evento Societário ocorrido no período informado”\.

Se a opção for preenchida com “3” \(Alienante\), verificar se o campo “Evento Societário ocorrido no período” foi preenchido como “2” \(Alienação\), se não exibir a seguinte mensagem: “A Condição da empresa relacionada à operação não é compatível com o Evento Societário ocorrido no período informado”\.

MFS\-9667

RN11

__Percentual da empresa participante envolvido na operação __

Se o campo “Evento Societário ocorrido no período” estiver preenchido com “1” \(Aquisição\), “2” \(Alienação\), “3” \(Fusão\), “4” \(Cisão Parcial\), “5” \(Cisão Total\) ou “6” \(Incorporação\), esse campo é de preenchimento obrigatório e se não estiver preenchido exibir a seguinte mensagem: “O Campo Percentual da empresa participante envolvido é obrigatório quando o campo “Evento Societário ocorrido no período” estiver preenchido com “1”, “2”, “3”, “4”, “5” ou “6” \- deve ser preenchido”\. 

Se o campo “Evento Societário ocorrido no período” estiver preenchido com “7” \(Extinção\) ou “8” \(Constituição\), esse campo não deve ser preenchido e se preenchido exibir a seguinte mensagem: “O Campo Percentual da empresa participante envolvido na operação não deve ser preenchido quando o campo “Evento Societário ocorrido no período” estiver preenchido com “7” ou “8”\.”\. 

MFS\-9667

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

