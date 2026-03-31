# MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2058

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_Online_Batch_SAFX2058.docx
- **Modificado:** 2022-06-07
- **Tamanho:** 76 KB

---

THOMSON REUTERS

__Cadastro de Processos Administrativos/Judiciais__

__Localização__

__Módulo:__ Básicosà MasterSAF DW

__Menu:__ 	Manutenção à Códigos à Cadastro Processo Administrativo/Judicial \(REINF\)

\- Carga à Execução

\- Importação à Execução

\- Importação Batch à Programação à Execução

\- Exportação Dados à Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-9755

Elenilson Coutinho

Definição das regras de importação, Online e Batch, da SAFX2058\.

MFS\-13810

Lara Aline 

Campo Indicador de Autoria passa a ser Obrigatório\.

MFS15147

Criação de campos p/o eSocial\.

Criação dos campos “Indicador de Incidência no eSocial”, “Matéria do Processo” e “Abrangência do Processo” \(ver __RN10__, __RN11__ e __RN12__\)\.

MFS15332

Lara Aline 

Campo Indicador de Autoria teve que ser alterado para não obrigatório\.

MFS18065

Atualização do eSocial p/ vrs 2\.4\.02

Inclusão de nova opção na lista de valores do campo Tipo de Processo;

Inclusão do campo “Observação”; 

MFS20913

João Henrique

Alteração no tamanho do campo 7 – COD\_VARA

MFS\-87292

Elisabete Costa

Alteração para o e\-social do conteúdo do campo 12 – Abrangência do processo

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

RN00

A rotina de importação online e batch do módulo JOB Servidor deverão ser ajustadas para que contemple as informações da tabela SAFX2058 – Cadastro de Processos Administrativos/Judiciais, que deve ser criada com a seguinte estrutura:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Indicador do Tipo de Processo

A

001

SIM

SIM

Número do Processo

A

021

SIM

SIM

Data Início/Inclusão/Alteração da Validade

N

008

NÃO

NAO

Data Término da Validade

N

008

NÃO

NÃO

UF

A

002

NÃO

NÃO

Município

N

005

NÃO

NÃO

Código da Vara

A

004

NÃO

NÃO

Indicador de Autoria

A

001

NÃO

NÃO

Indicador de Incidência no Reinf

A

001

NAO

NÃO

 

Alteração MFS15147: Criação dos campos “Matéria do Processo” e “Abrangência do Processo” p/o eSocial\. Vide estrutura no Manual de Layout\.

MFS\-9755

MFS\-13810

MFS15147

MFS15332

MFS20913

RN01

__Indicador do Tipo de Processo__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Indicador do Tipo de Processo Não Preenchido”\.

__MFS18065__: Inclusão do tipo de processo = 4 \(Processo FAP\)

 

Crítica: Valor esperado 1, 2 ou 4, caso contrário exibir a seguinte mensagem: *“Indicador do Tipo de Processo deve ser <1>, <2> ou <4>”*\.

O tipo 4 \(Processo FAP\) só pode ser utilizado para o eSocial, pois foi incluído na versão 2\.4\.02 do layout, e não consta no REINF\. Assim será feita a seguinte crítica:

Se “Tipo de Processo” = 4 e “Indicador de Incidência REINF” = “S”:

      O registro não será importado e será gerada a seguinte mensagem de erro *“O Tipo de Processo = 4 não deve ser utilizado*

*      quando o indicador de incidência REINF  = S” *   

MFS\-9755

MFS18065

RN02

__Número do Processo__

Campo de preenchimento obrigatório caso não preenchido exibir a seguinte mensagem: “Numero do processo não informado”\.

MFS\-9755

RN03

__Data Início/Inclusão/Alteração da Validade__

Crítica: Caso não for uma data válida exibir a seguinte mensagem: O Campo de Data de Validade com formato invalido\.

Caso Não for o primeiro dia do mês exibir a seguinte mensagem: O Campo Data de Inicio de Validade deve ser o primeiro dia do mês\.

Caso não preenchido, deverá ser informado o primeiro dia do mês\.

MFS\-9755

RN04

__Data Término Validade__

Crítica: Caso não for uma data válida exibir a seguinte mensagem: Campo Data Término Validade com formato inválido\.

Caso Não for o último dia do mês exibir a seguinte mensagem: O Campo Data de Término da Validade deve ser o último dia do mês\.

Caso não preenchido, deverá ser informado o último dia do mês\.

Caso data menor que data início de validade exibir a seguinte mensagem: "A Data Final deve ser maior ou igual a Data Inicial" 

MFS\-9755

RN05

__UF__

Crítica: Caso UF não existente na TFIX04 exibir a seguinte mensagem: “O Código da Unidade da Federação é invalido”\.

MFS\-9755

RN06

__Município__

Crítica: Caso Município não existente na TACES06 exibir a seguinte mensagem: “Código de município não cadastrado para o Estado correspondente”\.

MFS\-9755

RN07

__Código da Vara__

MFS\-9755

RN08

__Indicador de Autoria__

__Tratamento: __

Para o preenchimento desse campo será necessário verificar a informação preenchida no campo Tipo do Processo:

Caso informado ‘1’ no campo Tipo do Processo, esse campo não deve ser preenchido, ou seja, o campo deverá ser null\. Caso houver valor informado no campo exibir a seguinte mensagem: *“Indicador de Autoria Não deve ser preenchido, quando Tipo de Processo igual a 1\- Administrativo”*\.

Caso informado ‘2’ no campo Tipo do Processo, esse campo deve ser preenchido e o valor esperado 1 ou 2\. Caso NÃO houver valor informado ou esse valor for diferente de 1 e 2 exibir a seguinte mensagem: *“Indicador de Autoria deve ser <1> ou <2>”*\.

Caso informado “4” no campo Tipo de Processo, esse campo poderá *ou não* estar preenchido\. Quando preenchido, o conteúdo informado deve ser = 1 ou 2, caso contrário, o registro não será importado e será exibida a mensagem de erro: *“Indicador de Autoria deve ser <1> ou <2>”\.*  

MFS\-9755

MFS\-13810

MFS15332

MFS18065

RN09

__Indicador de Incidência REINF__

Crítica: Valor esperado S e N, caso contrário exibir a seguinte mensagem: “Indicador de Incidência REINF deve ser <S> ou <N>”\.

MFS\-9755

RN10

__Indicador de Incidência eSocial__

Campo não obrigatório\.

Quando preenchido, o conteúdo deve ser = “S” ou “N”\.

Caso preenchido com um conteúdo inválido, será gerada mensagem de erro padrão no log, e o registro não será importado\.

MFS15147

RN11

__Matéria do Processo__

Campo não obrigatório\.

Quando preenchido, o conteúdo deve ser um dos seguintes valores:__ __

“1” \(Tributária\)

“2” \(Autorização de trabalho de menor\)

“3” \(Dispensa, ainda que parcial, de contratação de pessoa com deficiência \(PCD\)\)

“4” \(Dispensa, ainda que parcial, de contratação de aprendiz\)

“5” \(Segurança e Saúde do Trabalho\)

“6” \(Conversão de Licença Saúde em Acidente de Trabalho\)

“7” \(FGTS\)

“8” \(Contribuição sindical\)

“99” \(Outros assuntos\) 

Caso preenchido com um conteúdo inválido, será gerada mensagem de erro padrão no log, e o registro não será importado\.

Obs: Estas opções são referentes ao campo “20\-indMatProc” do evento S\-1070 \(Processos Administrativos / Judiciais\) do eSocial\.

MFS15147

__RN12__

__Abrangência do Processo__

Campo não obrigatório\.

Quando preenchido, o conteúdo deve ser um dos seguintes valores:

__A partir da versão 2\.5__

“1” \(IRRF\)

“2” \(Contribuições sociais\)

“3” \(FGTS\)

“4” \(Contribuição sindical\)

__A partir da Versão S\-1\.0__

“1” \(IRRF\)

“2” \(Contribuições sociais\)

Caso preenchido com um conteúdo inválido, será gerada mensagem de erro padrão no log, e o registro não será importado\.

__Obs: Estas opções são referentes ao campo “35\-tpTrib” do evento S\-1200 do eSocial\.__

MFS15147

__MFS\-87292__

RN13

__Observação__

Campo não obrigatório\.

Obs: A informação deste campo é utilizada para geração do campo “21\-observacao” do evento S\-1070 \(Processos Administrativos / Judiciais\) do eSocial\.

MFS18064

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

