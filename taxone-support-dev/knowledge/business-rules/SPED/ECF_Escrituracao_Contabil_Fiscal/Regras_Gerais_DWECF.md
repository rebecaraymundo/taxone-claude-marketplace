# Regras_Gerais_DWECF

- **Fonte:** Regras_Gerais_DWECF.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 84 KB

---

THOMSON REUTERS

Regras de Negócio Gerais

ECF \- Escrituração Contábil Fiscal \(DW\)

##### DOCUMENTO DE REQUISITO

__Data__

__MFS__

__Descrição__

__Autor__

__Projeto__

27/10/2017

\-

Criação do documento

Alessandra Cristina Navatta

DW\-ECF

24/08/2018

MFS\-20563

Atualização das RNGS abaixo devido a versão 4\.00:

RNG00003 e RNG00004

Heloísa Mirthes

DW\-ECF

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

###### __REGRA__

###### __Funcionalidade__

###### __MFS__

RNG00001

Associação Tabela Dinâmica x Plano Empresa

__Bloco M \- Linhas do tipo P ou L __  
  
Não permitir a associação de tabela dinâmica com o plano empresa quando a coluna “Tipo” das linhas for igual a P ou L\.  
Apenas para as linhas do  tipo L considerar as exceções abaixo:   
__Versão 1\.00__   
Linhas 2 e 3 permitir em todos os registros  
Linha 179 permitir no M300A e M350A  
__Versão 2\.00__   
Linha 2 permitir no M300A e M350A  
  
__Legenda: __  
P = Prejuízos Acumulados  
L = Lucro

Tela Associação da Tabela Dinâmica com o Plano Empresa  
Integração SAFX2106

MFS\-12794  
MFS\-14166

RNG00002

Tipo de Linhas

__Tipo de linhas da Tabela Dinâmica__  
  
CA = Cálculo Alterável  
CNA = Cálculo Não Alterável  
E = Editável  
R = Rótulo

Tela Associação da Tabela Dinâmica com o Plano Empresa

MFS\-12794

RNG00003

Versão da Escrituração

A Versão utilizada para Processamento e Geração da ECF deve ser de acordo com o ano da data inicial da  escrituração e deve seguir a seguinte validação :  
  
• Leiaute 1\.00  
Ano calendário 2014  
Ano\-calendário 2015 com situação especial  
  
• Leiaute 2\.00   
Ano calendário 2015 sem situação especial   
Ano calendário 2016 com situação especial   
  
• Leiaute 3\.00  
Ano calendário 2016 sem situação especial   
Ano calendário 2017 com situação especial   


• Leiaute 4\.00  
Ano calendário 2017 sem situação especial   
Ano calendário posterior a 2017

Processamento em Lote  
Integração SAFX2106,2107

MFS\-13202  
MFS\-14166  
MFS\-14165/MFS\-20563

RNG00004

Versão de Layout

Estão disponíveis as seguintes versões de layout:

1\.00 – Ano Calendário 2014 e Situações Especiais de 2015    
2\.00 – Ano Calendário 2015 e Situações Especiais de 2016  
3\.00 – Ano Calendário 2016 e Situações Especiais de 2017

4\.00 – Ano Calendário 2017 e Situações Especiais de 2018

Processamento em Lote  
Integração SAFX2106,2107

MFS\-13202  
MFS\-14166  
MFS\-14165/MFS\-20563

RNG00005

Associações compatíveis com o campo ‘Qualificação da Pessoa Jurídica’ da tela Informação ECF

Se o campo Qualificação da Pessoa Jurídica for:  
  
__PJ em Geral:__  
Recuperar Plano Referencial terminados com ‘A’\. Ex\. L100A,L300A  
  
__PJ Componente do Sistema Financeiro__  
Recuperar Plano Referencial terminados com ‘B’\. Ex\. L100B,L300B  
__  
Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar__  
Recuperar Plano Referencial terminados com ‘C’\. Ex\. L100C,L300C

__Para escriturações a partir da versão 3\.00:__

PJ em Geral e Sociedades Seguradoras, de Capitalização ou Entidade Aberta de Previdência Complementar:

Tabela dinâmica terminados sem a terminação ‘B’\. Ex\. P100, P150

PJ Componente do Sistema Financeiro:

Tabela dinâmica terminados com ‘B’\. Ex\. P100B, P150B

Processamento em Lote

MFS\-13202

RNG00006

Validação Campo Escrituração

Se na Tela de Informações ECF a Escrituração for diferente de “Livro Caixa ou Sem Escrituração” e na tela de Abertura de Apuração a Forma de Tributação for diferente de “Lucro Arbitrado”:  
  
A mensagem DW00002, deve ser exibida quando não for encontrada parametrização na tabela de Plano Referencial com Plano Empresa para para o período informado para o processamento\.  
  
Se na Tela de Informações ECF a Escrituração for igual a “Livro Caixa ou Sem Escrituração”:  
  
A mensagem DW00025, deve ser exibida quando não for encontrada parametrização na tabela de Plano Referencial com Plano Empresa para para o período informado para o processamento\.

Processamento em Lote

MFS\-18089

RNG00007

Associação da Tabela Dinâmica com o Plano Empresa x Informações ECF

Se na Tela de Informações ECF a Escrituração for diferente de “Livro Caixa ou Sem Escrituração”e campos “Apuração do IRPJ”  ou “Apuração da CSLL” for diferente a “Desobrigada”:  
  
A mensagem DW00037, deve ser exibida quando não for preenchido o campo "Associação de Tabela Dinâmica com o Plano Empresa"\.  
  
Se na Tela de Informações ECF a Escrituração for igual a “Livro Caixa ou Sem Escrituração”:  
A mensagem DW00038, deve ser exibida quando não for  preenchido o campo "Associação de Tabela Dinâmica com o Plano Empresa"\.

Informações ECF

MFS\-12691

RNG00008

Data Inicial x Estabelecimento

Se a data informada neste campo for menor que a data  inicial do estabelecimento exibir a mensagem DW00030\.

Informações ECF

MFS\-12691

RNG00009

Data Inicial x Exercício

O campo data inicial deve estar compreendida no intervalo do ano anterior até o último dia do ano do exercício, caso contrário, exibir a seguinte msg ao usuário: DW00029\.  
  
Exemplo: Exercício 2014  
Data Inicial: \(entre 01/01/2013 à 31/12/2014\)

Informações ECF

MFS\-12691

RNG00010

Campo Obrigatório

Se o um campo obrigatório não for preenchido, exibir mensagem DW00001 

Informações ECF  
Integração SAFX2106, 2106

MFS\-12691  
MFS\-14166

RNG00011

Duplicidade de Registro

Verifica se o registro já existe no banco de dados ou o registro está duplicado no arquivo, caso positivo, emite a seguinte mensagem DW00004

Informações ECF

MFS\-12691

RNG00012

Salvar

Aplica a regra de negócio <<RNG00010>>\.  
Se todos os campos obrigatórios estiverem preenchidos corretamente, armazena o registro no banco de dados e apresenta a seguinte mensagem:  
  
Para inserção: DW00008  
Para alteração: DW00040  
  
Aplica a regra de negócio << RNG00011 \-  Duplicidade de Registro >>\.

Informações ECF

MFS\-12691

RNG00013

Erro de execução de Fórmula

A mensagem  DW00056 deve ser exibida quando:  
  
No momento da execução das fórmulas for encontrado espaço, ausência de fechamento das aspas, ausência fechamento dos parênteses\.\.\.  
  
Exemplo de exibição da mensagem:  
  
No exemplo abaixo, não houve o fechamento das aspas\.  
  
A fórmula pode conter erros na estrutura – Fórmula: L100\(“3\.01\.01\) \(exibir a fórmula\), Registro: N600 \(exibir o registro\) e Cód\. Do Registro: 1 \(exibir a linha responsável pela tentativa de execução da fórmula\)\.

Processamento em Lote

MFS\-12620

RNG00014

Fórmula – Tabela Dinâmica

A mensagem DW00055 deve ser exibida quando no momento do processamento da linha da tabela dinâmica \(Cód\. Do Registro\) que possuir fórmula a ser executada \(Tipo CA ou CNA\), não for encontrada a fórmula para a execução\. 

Processamento em Lote

MFS\-12620

RNG00015

Recuperação de Saldos por Natureza

A – Ativo \(total dos saldos finais das contas contábeis cuja natureza = ‘1’\);    
P – Passivo \(total dos saldos finais das contas contábeis cuja natureza = ‘2’\);  
PL – Patrimônio Líquido \(total dos saldos finais das contas contábeis cuja natureza = ‘7’\);  
D – Despesas \(total dos saldos finais das contas contábeis cuja natureza = ‘3’\);   
R – Receitas \(total dos saldos finais das contas contábeis cuja natureza = ‘4’\)\.   
C – Custos \(total dos saldos finais das contas contábeis cuja natureza = ‘8’\)\.

Processamento em Lote

MFS\-12620

RNG00016

Acesso à Tela

Se o usuário acessar a tela através do botão “Adicionar”, exibi\-la conforme regras definidas na especificação correspondente\.  
Se o usuário acessar a tela através da seleção de um registro, apresentar o registro correspondente com os campos preenchidos, conforme armazenado no banco de dados e permitir que o usuário edite\-o, exceto os campos chaves\.

Abertura de Apuração

MFS\-12692

RNG00017

Validação de Valor

O campo deve aceitar valores que estejam compreendidos entre 0 e 100, caso contrário, apresentar a mensagem DW00076

Abertura de Apuração

MFS\-12692

RNG00018

Alteração de tela com controle de status da abertura da apuração

__Se status da apuração igual a “Cálculo Realizado”:__  
Quando o usuário selecionar uma apuração cujo status seja igual a “Cálculo Realizado”, apresentar a  mensagem DW00082 e não habilitar para edição\.  
__  
Se status da apuração igual a “Aguardando Alteração Manual”, “Alteração Manual Realizada” ou “Importação dos Saldos Realizada”:__  
Quando o usuário  selecionar uma apuração cujo status seja igual a “Aguardando Alteração Manual”, “Alteração Manual Realizada” ou “Importação dos Saldos Realizada”, apresentar a  mensagem DW00083 e não habilitar para edição\.  
  
__Se status da apuração igual a “Apuração em Aberto”__:  
Quando o usuário selecionar uma apuração cujo status seja igual a “Apuração em Aberto”, apresentar a  mensagem DW00084 e não habilitar para edição\.

Ajustes do Bloco K

MFS\-12713

RNG00019

Botão Anexar/Botão Adicionar

Quando este botão for acionado, verifica se há algum arquivo selecionado para ser anexado\.  
Se sim, apresentar a seguinte mensagem: Arquivo anexado com sucesso\.  
Se não, apresentar a mensagem: Por favor, selecione um arquivo para ser anexado\. 

Visualização Registros Tabela Dinâmica \-  
Informativo da Composição de Custos \(L210\)

MFS\-14136

RNG00020

Botão Cancelar

Quando acionado o botão “Cancelar”,  cancelar a operação retornando para a tela imediatamente anterior\.

Visualização Registros Tabela Dinâmica \-  
Informativo da Composição de Custos \(L210\)

MFS\-14136

RNG00021

Validação de valores dos campos de lista

Se o valor a ser importado for diferente dos valores aceitos na lista de valores, apresentar a mensagem DW00085 \(Código, Descrição e Tipo\)

Integração SAFX2107, 2106

MFS\-14165  
MFS\-14166

RNG00022

Recuperar Conta Contábil

Para recuperar a conta contábil, considerar:  
  
Central de Cadastro informada na tela / recuperada \(central válida para o código da tabela 2002\)  
Considerar as Contas Contábeis de acordo com a central de cadastros vigente,   recupera o registro de máxima validade\. 

Integração SAFX2107, 2106

MFS\-14165  
MFS\-14166

RNG00023

Recuperar Centro de Custo

  
Para recuperar o centro de custo, considerar:  
  
\- Central de Cadastro informada na tela / recuperada \(central válida para o código da tabela 2002Considerar os Centros de Custo de acordo com a central de cadastros vigente,recupera o registro de máxima validade\.  
  
OBS: \)\. A mesma central de cadastro do Plano de Contas dever ser a mesma do Centro de Custo, logo na recuperação do Centro de Custo deverá ser considerada a  central de cadastro da tabela  plano de contas 2002\.

Integração SAFX2107, 2106

MFS\-14165  
MFS\-14166

RNG00024

Recuperar Conta Referencial

Para recuperar a conta referencial, considerar:  
  
\- Versão informada   
\- Registro selecionado   \(L100A,\.\.\.\)  
\- Data Inicial da parametrização:  
  
Considerar as Contas Referenciais com Data  final da Conta Referencial nula ou >= Data Inicial da parametrização\. Se existir mais de um registro considerar o registro de maior validade\.

Integração SAFX2107

MFS\-14165

RNG00025

Validação de tamanho de campo

Se o campo for preenchido com um valor maior \(em extensão\) que o permitido para o campo, exibir a mensagem DW00091

Integração SAFX2107, 2106

MFS\-14165  
MFS\-14166

RNG00026

Validação de conteúdo de data

Se o campo de data for preenchido com um valor inválido \(valor alfanumérico, data inexistente etc\.\), exibir a mensagem DW00092  


Integração SAFX2107, 2106

MFS\-14165  
MFS\-14166

RNG00027

Validação de campos numéricos/numéricos sinalizado

Se o campo numérico ou  numérico sinalizado estiver preenchido com um valor inválido, exibir a mensagem DW00093  
OBS: Campos que possuem o formato NS – Numérico Sinalizado, podem receber o sinal negativo

Integração SAFX2107, 2106

MFS\-14165  
MFS\-14166

RNG00028

Identificação de registros com erro

Para cada erro encontrado, informar ao usuário os campos identificadores do registro na mensagem de erro e o conteúdo dos campos \(Caso estas informações não estejam contidas na mensagem de erro\)\.  
  
Obs\.: Estes campos serão demonstrados apenas no Relatório de Erros\.

Integração SAFX2107, 2106

MFS\-14165  
MFS\-14166

RNG00029

Duplicidade Chave de Registro

No momento da integração dos dados, na ocorrência de duplicidade de Registro com as mesmas informações para o campo chave, o sistema deve sobrepor ou ignorá\-los, , conforme cenários abaixo:

Caso o registro importado for totalmente igual ao que está na base, o mesmo será ignorado\.

Caso o registro possuir alguma informação de campo que não for chave diferente do que está na base, o registro será sobreposto\.

Integração SAFX2107, 2106

MFS\-14165  
MFS\-14166

RNG00030

Validação de conteúdo de data

  
Se o campo de data não estiver no formato definido conforme layout da obrigação/interface do produto exibir a mensagem DW00094

Integração SAFX2107, 2106

MFS\-14165  
MFS\-14166

RNG00031

Recuperação de Saldos 

__A recuperação de saldos para as linhas da tabela dinâmica ou plano referencial deverá atender a regra abaixo:__  
  
Para cada linha referencial \(linha da tabela dinâmica ou conta do plano referencial\) que possua associação com conta contábil e centro de custo na tela associação da Tabela Dinâmica com Plano Empresa ou Associação do Plano Referencial com o Plano Empresa, buscar na tabela de saldos os valores que serão atribuídos as linhas referenciais com base na parametrização realizada na tela Processamento em Lote utilizando como parâmetro de busca o Exercício e as Aberturas das Apurações selecionadas para o processamento\.  
  
Os saldos devem ser recuperados de forma totalizada \(verificar   RNG00035 – Soma dos Saldos\), a mesma linha possui mais de uma conta contábil associada\. Neste caso, deve ser gerado um único valor na linha totalizando as contas contábeis associadas\.  
  
Os saldos devem ser recuperados de forma agrupada pelo período, ou seja, na seleção do dado na tabela de saldos deve conter somente os contas contábeis e respectivos valores do período à ser processado\.

Processamento em Lote

MFS\-13997

RNG00032

Recuperação do Movimento do Saldo

A recuperação com base no movimento consiste na verificação dos débitos e/ou créditos no período sendo ele mensal ou trimestral\.   
  
Visão de recuperação do movimento contábil Exemplo \- Tabela de Saldos Mensais  
  


__Mês__

__C\. Contábil__

__Linha __

__Saldo Inicial__

__Débitos__

__Créditos__

__Saldo Final__

Jan

2\.3\.1

X

400D

100

             \-   

500D

Fev

2\.3\.1

X

400D

300

             \-   

700D

Mar

2\.3\.1

X

400D

400

             \-   

800D

Abr

2\.3\.1

X

400D

500

25

875D

  
Observe que para a linha X da tabela dinâmica, deverá ser recuperado em Janeiro 100D, Fevereiro 200D e Março 100D e em Abril será recuperado 75D\.

Processamento em Lote

MFS\-13995

RNG00033

 Recuperação Acumulada dos Saldos

Recuperação acumulada corresponde ao total até o período não há uma separação por mês se trata dos valores até o mês ou trimestre\.

Visão de recuperação acumulada com base nos saldos do Exemplo \- Tabela de Saldos Mensais

__Mês__

__C\. Contábil__

__Linha __

__Saldo Inicial__

__Débitos__

__Créditos__

__Saldo Final__

Jan

2\.3\.1

X

400D

100

             \-   

500D

Fev

2\.3\.1

X

400D

300

             \-   

700D

Mar

2\.3\.1

X

400D

400

             \-   

800D

Abr

2\.3\.1

X

400D

500

25

875D

Observe que para a linha da tabela dinâmica X, até o mês de Abril o Saldo Inicial corresponderá a 400, a movimentação de Débitos corresponderá a 500, a movimentação de Créditos corresponderá a 25 e o Saldo Final corresponderá 875\.

Na apuração de forma acumulada o saldo inicial não é alterado, ele é o mesmo desde o primeiro período\. No nosso exemplo 400,00D começa em Janeiro e deverá ser replicado até o fim do período no nosso exemplo Abril\. O Saldo Final é o acumulado do ultimo mês \(ou dia\) do Período de Apuração e para os Totais de Débitos e Créditos, deve ser recuperado a somatória de todos os meses do Período de Apuração\.

Processamento em Lote

MFS\-13997

RNG00034

Dependência de informações entre registros da Tabela Dinâmica

A mensagem DW00113 deve ser exibida quando para a geração de um registro existir a dependência de geração de linhas de outros registros e no momento do processamento o valor não for identificado\. Neste caso o valor não identificado deverá ser considerado igual a zero e a execução das demais operações contidas na linha deverá prosseguir\.

__Exemplo de exibição da mensagem:__ “Verificar a geração da linha 1 do registro N500, pois as informações da\(s\) linha\(s\) 175, 349 do registro M300 é igual a zero”\.

Processamento em Lote

MFS\-13997

RNG00035

Soma dos Saldos Contábeis

Recuperar os saldos das contas contábeis de todos os estabelecimentos para as linhas da tabela dinâmica ou contas referenciais correspondentes à associação\.

- Somar todos os saldos CREDORES das contas contábeis associadas às linhas das tabelas referenciais, onde o indicador seja "C”;
- Somar todos os saldos DEVEDORES das contas contábeis associadas às linhas das tabelas referenciais onde o indicador seja "D"\.

Após esta somatória, deverá ser identificada a diferença positiva entre os saldos a débito e a crédito e deverá ser mantido o indicador de débito ou crédito do maior valor\.

Exemplo:

Saldo Credor Total 	= 	1\.000,00

Saldo Devedor Total 	= 	1\.800,00

- Saldo Final \(Devedor\) – Saldo a ser atribuído a linha da tabela dinâmica = 800,00\*
- Saldo Final \(Devedor\) – Saldo a ser atribuído a conta refrencial = 800,00D

__*\*linha da tabela dinâmica não possui indicador de débito ou crédito*__

Processamento em Lote

MFS\-13997

RNG00036

Escrituração X Forma de Tributação

Se na Tela de Informações ECF a Escrituração for diferente de “Livro Caixa ou Sem Escrituração” e na tela de Abertura de Apuração a Forma de Tributação for diferente de “Lucro Arbitrado”:

A mensagem DW00114 deve ser exibida quando não for encontrada  associação informada no campo  Associação Tabela Referencial com o Plano Empresa\.

Se na Tela de Informações ECF a Escrituração for igual a “Livro Caixa ou Sem Escrituração”:

A mensagem DW00115 deve ser exibida quando não for informada Associação Tabela Referencial com o Plano Empresa\.

Processamento em Lote

MFS\-13995

RNG00037

Dependência de informações entre registros do Plano Referencial

A mensagem DW00120 deve ser exibida quando para a geração de um registro existir a dependência de geração de linhas de outros registros e no momento do processamento o valor não for identificado\. Neste caso o valor não identificado deverá ser considerado igual a zero e a execução das demais operações contidas na linha deverá prosseguir\.

__Exemplo de exibição da mensagem:__ “Verificar a geração da linha 21 do registro N600, pois a informação da\(s\) conta\(s\) 3 do registro L300 é igual a zero”\.

Processamento em Lote

MFS\-13997

RNG00038

Fórmula – Tabela Dinâmica

No momento do processamento da linha da tabela dinâmica\. Para \(Cód\. Do Registro\) que possuir fórmula a ser executada do Tipo “CA” \(Cálculo Alterável\) e tiver valor informado, a fórmula não deve ser executada\. O valor informado deve ser mantido\.

Processamento em Lote

MFS\-13997

RNG00039

Conversão de valores para totalização

Somar o valor das contas contábeis encontradas considerando a conversão dos valores para totalização  conforme tabela a seguir:

__Natureza da conta__

__Ind\. do saldo da conta __

__TIPO\_LANÇAMENTO \(TABELA DINÂMICA\)__

__Sinal __

__Observação__

1, 2 ou 7

Crédito

A – Adições

Positivo

1, 2 ou 7

Débito

A – Adições

Negativo

3, 4 ou 8

Crédito

A – Adições

Negativo

3, 4 ou 8

Débito

A – Adições

Positivo

0, 5, 6, 9

Crédito

A – Adições

\-

Não geramos no momento

0, 5, 6, 9

Débito

A – Adições

\-

Não geramos no momento

1, 2 ou 7

Crédito

E\- Exclusões

Negativo 

1, 2 ou 7

Débito

E\- Exclusões

Positivo

3, 4 ou 8

Crédito

E\- Exclusões

Positivo

3, 4 ou 8

Débito

E\- Exclusões

Negativo

0, 5, 6, 9

Crédito

E\- Exclusões

\-

Não geramos no momento

0, 5, 6, 9

Débito

E\- Exclusões

\-

Não geramos no momento

Todas

Crédito 

P – Compensação de Prejuízos

\-

Não geramos valor

Todas

Débito

P – Compensação de Prejuízos

\-

Não geramos valor

1, 2 ou 7

Crédito 

L \- Lucro

\- \*Positivo

Não geramos valor

\*Se CÒDIGO \(da tabela dinâmica\) = 2, 3 ou 179 Sinal = Positivo

1, 2 ou 7

Débito

L \- Lucro

\- \*Negativo

Não geramos valor

\*Se CÒDIGO \(da tabela dinâmica\) = 2, 3 ou 179 Sinal = Negativo

3, 4 ou 8

Crédito

L \- Lucro

\- \*Negativo

Não geramos valor

\*Se CÒDIGO \(da tabela dinâmica\) = 2, 3 ou 179 Sinal = Negativo

3, 4 ou 8

Débito

L \- Lucro

\- \*Positivo

Não geramos valor

\*Se CÒDIGO \(da tabela dinâmica\) = 2, 3 ou 179 Sinal = Positivo\.

Processamento em Lote

MFS\-14779

RNG00040

Somatória coluna Lançamentos/Ajustes

Considerar a somatória dos valores contidos na coluna Lançamentos/Ajustes \+ o valor da coluna Saldo correspondente às linhas onde o campo lançamentos/Ajustes for igual a zero, conforme exemplo abaixo:

__Conta__

__Saldo__

__D/C__

__Natureza__

__Tipo de Lançamento__

__Lançamentos/Ajustes__

__D/C__

__Valor  considerado para o Total__

CT01

5\.000,00

 C 

1

Adição

 

 

5000,00

CT02

10\.000,00

 C 

3

Adição

6\.000,00

 C 

\-6000,00

CT03

15\.000,00

 C 

4

Adição

4\.000,00

C

\-4000,00

CT04

1\.000,00

D

1

Adição

 

 

\-1000,00

CT05

2\.000,00

D

2

Adição

 

 

\-2000,00

CT06

3\.000,00

D

3

Adição

 

 

3000,00

CT07\*

4\.000,00

D

5

Adição

 

 

0,00

CT08\*

6\.000,00

C

6

Adição

 

 

0,00

CT09

5\.000,00

 C 

1

Exclusão

 

 

\-5000,00

CT10

10\.000,00

 C 

3

Exclusão

6\.000,00

 C 

6000,00

CT11

15\.000,00

 C 

4

Exclusão

4\.000,00

C

4000,00

CT12

1\.000,00

D

1

Exclusão

 

 

1000,00

CT13

2\.000,00

D

2

Exclusão

 

 

2000,00

CT14

4\.000,00

D

3

Exclusão

 

 

\-4000,00

CT15\*

4\.000,00

D

5

Adição

 

 

0,00

CT16\*

6\.000,00

C

6

Adição

 

 

0,00

CT17\*

4\.000,00

D

5

Lucro

 

 

0,00

CT18\*

6\.000,00

C

6

Lucro

 

 

0,00

CT19\*

4\.000,00

D

5

Comp\.Prejuízos

 

 

0,00

CT20\*

6\.000,00

C

6

Comp\.Prejuízos

 

 

0,00

\* Exemplo ilustrativo\. As contas de natureza 0, 5, 6, 9 não devem ter o resultado gravado e não devem ser apresentadas para consulta posterior na tela de lançamento da parte A\.

__Total__

\-1\.000,00

MFS\-14779

RNG00041

Remover

Quando este botão for acionado, apresentar a seguinte mensagem: 

Deseja remover este\(s\) registro\(s\)? Com as opções “Sim” e “Não”

Se o usuário clicar em “Sim”, remover o\(s\) registro\(s\) e exibir a mensagem: Registro\(s\) removido com sucesso\.

Se o usuário clicar em “Não”, fechar a mensagem\.

Tela Lançamentos da Parte A \(M300/M350\)

MFS\-14939

RNG00042

Validação de CNPJ

Se o CNPJ não tiver 14 posições, ou se a quantidade de caracteres informados para o campo for igual a 14 e o CNPJ for inválido exibir a mensagem DW00150\.

Tela Lançamentos da Parte B \(M410\)

MFS\-15272

RNG00043

Remover2

Quando este botão for acionado, apresentar a mensagem DW00159, com as opções “Sim” e “Não”\. Se o usuário clicar em “Sim”, remover o registro do banco de dados e exibir a mensagem DW00160\.

Caso exista restrição referencial no banco de dados, exibir a mensagem DW00155\.

Se o usuário clicar em “Não”, fechar a mensagem, retornar a tela e não remover o registro do banco de dados\.

Tela Lançamentos da Parte B \(M410\)

MFS\-15272

RNG00044

Cálculo do Registro M500

Criar o registro M500, que é composto pelos campos: Saldo Inicial, Lançamentos da Parte A, Lançamentos da Parte B, Lançamento da Parte B \(Contrapartida\) e Saldo Final\.

Abaixo, segue como cada campo deve ser calculado:

__Saldo Inicial:__

__Se apuração Anual:__

Exibir a informação do campo Saldo Inicial da Escrituração e seu respectivo indicador \(campo da tela de Ajustes da Parte B\)\.

__Se apuração Trimestral:__

Para o primeiro período de apuração: considerar a informação do campo Saldo Inicial da Escrituração e seu respectivo indicador \(campo da tela de Ajustes da Parte B\)\.

Para os demais trimestres, considerar a informação do campo Saldo Final e seu respectivo indicador do Registro M500 do trimestre anterior já calculado\.

__Lançamentos da Parte A:__

Fazer o somatório dos valores dos lançamentos da parte A \(considerando o estabelecimento, conta e período\), exibidos na tela de lançamentos da parte A\. Nesta somatória, devem ser considerados os indicadores dos lançamentos\.

Considerar as regras abaixo:

1. Somar todos os valores de indicadores iguais,
2. Subtrair os valores de indicadores diferentes, 
3. Manter o indicador do maior valor\.

Exibir o valor calculado e seu indicador\.

__Lançamentos da Parte B:__

Fazer o somatório\* dos valores dos lançamentos da parte B \(considerando a empresa, conta e período\*\), exibidos na aba M410\. Nesta somatória, devem ser considerados os indicadores dos lançamentos\.

__Se apuração Anual:__

\*a soma deve considerar todos os lançamentos com Origem na Parte B = “Incremental” que estão no período\. \(considerando os ajustes lançados no próprio período e os ajustes que foram copiados dos períodos anteriores para o atual\) e a soma dos lançamentos com Origem na Parte B = “Cumulativo” do período atual\.

__Se apuração Trimestral:__

\*a soma deve considerar todos os lançamentos com Origem na Parte B = “Incremental” que foram criados no período\. \(sem considerar os ajustes que foram copiados dos períodos anteriores para o atual\)\.

__Para ambas apurações \(Anual e Trimestral\):__

Os indicadores Prejuízo do Exercício e Base de Cálculo Negativa da CSLL devem ser considerados para a soma como Débito\.

Considerar as regras abaixo:

1. Somar todos os valores de indicadores iguais,
2. Subtrair os valores de indicadores diferentes,
3. Manter o indicador do maior valor\.

Exibir o valor calculado e seu indicador\.

__Lançamentos da Parte B \- Contrapartida:__

Considerar os lançamentos que foram gerados pelo processamento, de lançamentos com oriundos de Contrapartida, conforme RNG00046 \-  Criação do registro de origem Contrapartida\. 

__Saldo Final:__

Fazer o somatório dos campos Saldo Inicial, Lançamentos da Parte A , Lançamentos da Parte B e Lançamentos da Parte B – contrapartida, \(considerando a empresa, conta e período\), exibidos na aba M500\. Nesta somatória, devem ser considerados os indicadores dos campos\.

Considerar as regras abaixo:

1. Somar todos os valores de indicadores iguais,
2. Subtrair os valores de indicadores diferentes, 
3. Manter o indicador do maior valor\.

Exibir apenas o valor do calculo realizado\.

__Exemplo de Cálculo:__

Saldo Inicial da Escrituração

Ind\. Saldo Inicial da Escrituração

100,00

C

M305:

Apuração

Lançamentos Parte A

Ind\. do Valor  Parte A

Janeiro

20,00

D

M410:

Apuração

Lançamentos Parte B

Ind\. do Valor  Parte B

Ajuste com Origem na Parte B

Histórico

Janeiro

50,00

 D 

Incremental

Historico01 – incremental \-APURAÇÃO JANEIRO

Janeiro

10,00

C

Cumulativo

Historico01 \- cumulativo

M500:

Apuração

Saldo Inicial 

Ind\. do Saldo Inicial 

Lançamentos Parte A

Ind\. do Valor  Parte A

Lançamentos Parte B

Ind\. do Valor Parte B

Saldo Final

Ind\. Saldo Final

Janeiro

100,00

C

20,00

D

40,00

D

40,00

C

M305:

Apuração

Lançamentos Parte A

Ind\. do Valor  Parte A

Fevereiro

80,00

D

M410:

Apuração

Lançamentos Parte B

Ind\. do Valor  Parte B

Ajuste com Origem na Parte B

Histórico

Fevereiro

50,00

D

Incremental

Historico01 – incremental \-APURAÇÃO JANEIRO

Fevereiro

100,00

D

Incremental

Historico02 \- incremental

M500:

Apuração

Saldo Inicial 

Ind\. do Saldo Inicial 

Lançamentos Parte A

Ind\. do Valor  Parte A

Lançamentos Parte B

Ind\. do Valor Parte B

Saldo Final

Ind\. Saldo Final

Fevereiro

100,00

C

80,00

D

150,00

D

130,00

D

Tela Lançamentos da Parte B \(M410\) e Processamento

MFS\-15678

RNG00045

Criação dos registros M410 

__Criação dos registros M410 se existir lançamentos com o campo ‘Ajuste com Origem na Parte B’ = Incremental, na apuração anterior:__

Deve ser criado um registro M410, para cada registro encontrado na apuração anterior \(desta escrituração\) que esteja com o campo ‘Ajuste com Origem na Parte B’ = “Incremental”\. Este registro terá as mesmas informações que o registro da apuração anterior\. Após o processo de cálculo, caso esses registros sejam criados, os mesmos passam a ser visualizados na tela de Lançamentos da Parte B\(M410\)\. 

Processamento 

MFS\-15678

RNG00046

Criação do registro de origem Contrapartida 

__Criação dos registros de origem de Contrapartida:__

Recuperar todos os lançamentos da parte B que possuam o campo contrapartida preenchido\.

Para cada registro recuperado, deve ser gerado um registro de contrapartida, na conta da parte B indicada no campo contrapartida, conforme detalhado abaixo:

__Conta da Parte B \(contrapartida\):__ Conta indicada no campo contrapartida do lançamento de origem

__Conta da Parte B \(origem\):__ Conta indicada no campo do lançamento de origem

__Data Lançamento:__ Mesma Informação do campo do lançamento de origem

__Contrapartida:__ Não recuperar a informação do campo do lançamento de origem\.

__Ajuste com Origem Parte B:__  Mesma Informação do campo do lançamento  de origem

__Tributação Diferida:__  Mesma Informação do campo do lançamento  de origem 

__Valor e Indicador__: Valor do lançamento original, com o indicador invertido

__Histórico__: Apagar o histórico do lançamento de origem e gravar o texto fixo “Lançamento realizado automaticamente em DD/MM/AAAA devido o preenchimento do campo Contrapartida\.”

O registro criado será visualizado na tela Lucro Real \(Contrapartida\) e o valor do mesmo, será totalizado nos dados do registro M500 \(campo Lançamentos da Parte B Contrapartida\) da tela de Lançamentos da Parte B \(M410\)\.

Atenção: Escolhemos não considerar o valor como um ajuste físico do registro M410, pois esse lançamento de ajuste não será exibido no arquivo do meio magnético\. Por isso, optamos por gerá\-lo apenas para visualização\. 

Os totais de lançamentos realizados decorrente da contrapartida refletirão na demonstração dos valores do registro M500 no período em que os lançamentos de ajuste foram realizados, pois alterarão o Saldo Final da conta da parte B \(Conta de Origem\) e Contrapartida \(Conta de Destino\)\. 

Processamento

MFS\-15678

RNG00047

Recalculo do Valor 

__	__ 

__Tipo de Lançamento__

__Sinal no campo "Valor"__

__Indicador do somatório de todos os ajustes da parte B__

Adição ou Lucro

\+ \(positivo\)

D – Devedor

Adição ou Lucro

\- \(negativo\)

C – Credor

Exclusão ou Compensação de Prejuízo

\+ \(positivo\)

C – Credor

Exclusão ou Compensação de Prejuízo

\- \(negativo\)

D \- Devedor

Processamento em Lote

MFS\-15958

<a id="_Hlk506883219"></a>RNG00048

Registros N620 e N660

__Para os registros N620 e N660:__

Quando o usuário optar pelo tipo de receita “Receita Bruta” através da tela “Abertura de Apuração” ou “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, as linhas abaixo \(referente a visão Receita Bruta\) deverão ser zeradas nos processos Transcrição dos Valores Empresa para Referenciais Fisco e Cálculo dos Registros e Fórmulas, além de serem exibidas sem detalhamento \(na demonstração da memória de cálculo na tela Lucro Real\):

\- Linhas 18, 19, 25, 25\.01 e 25\.02 da tabela dinâmica referente ao Registro N620\. 

\- Linhas 5, 6, 7, 8, 9 e 10 referente ao Registro N660\.

Na tela Entrada Manual de Valores, as linhas dos registros citadas acima \(referente a visão Receita Bruta\), devem ser apresentadas desabilitadas e zeradas, sem ser possível editá\-las\.

Processamento em Lote

MFS\-12632

MFS\- 16531

MFS\-12695

RNG00049

Sem escolha do tipo de receita

Se o campo “Tipo de Receita” da tela Abertura da Apuração for igual a “Comparativo” e não houver um tipo de receita selecionado na tela “Comparativo entre Receita Bruta X Balanço de Suspensão/Redução”, seja através de uma interação manual do usuário ou regra automática do sistema \(quando o campo “Considerar automaticamente o menor valor de imposto no comparativo” da tela  Abertura da Apuração estiver selecionado\), não iniciar o processamento da apuração selecionada e exibir a mensagem DW00171\.

Processamento em Lote

MFS\-16928

RNG00050

Menor Valor

Quando o campo “Considerar automaticamente o menor valor de imposto no comparativo” da tela Abertura da Apuração, estiver selecionado no momento do cálculo, verificar através do campo TOTAL qual tipo de receita \(Receita Bruta ou Balanço de Suspensão/Redução\) possui o menor valor e apresentar este campo selecionado para a que possuir menor valor\. Essa verificação deve ser realizada período a período\.

Tela  Comparativo entre Receita Bruta X Balanço de Suspensão/Redução

MFS\-16929

RNG00051

Geração dos Registros

As validações existentes nesta documentação \(independentemente do tipo: erro/aviso\), não impedirão a geração do registro\. Todas as mensagens de validações serão apresentadas no final da geração\.

Caso exista alguma exceção, esta será tratada de forma pontual\.

Geração Meio Magnético 

MFS\-17096

RNG00052

Validação do campo data inicial/data final

Se a data informada no campo Data Inicial não pertencer ao mesmo ANO informado no campo Data Final, exibir a mensagem DW00191\.

Tela Geração Meio Magnético

MFS\-12684

RNG00053

Data Inicial x Exercício

O campo data inicial deve estar compreendida no intervalo do ano anterior até o último dia do ano do exercício, caso contrário, exibir a mensagem ao usuário DW00192\.

Exemplo: Exercício 2014

Data Inicial: \(entre 01/01/2013 à 31/12/2014\)

Tela Geração Meio Magnético

MFS\-12684

RNG00054

Incentivos Fiscais

Parametrização que será considerada para calcular os incentivos:

\- UF do estabelecimento matriz/SCP = ‘ES’ e

\- Parâmetro ‘FINOR/FINAM/FUNRES ‘ da Tela Informações ECF deve ser marcado e

\- Forma de tributação = Lucro Real \(tela Abertura da Apuração\), independente de tipo de Apuração \(Anual e Trimestral\)\.  Quando Apuração = Anual, considerar o parâmetro ‘Tipo de Receita’ igual a Balanço Suspensão ou Redução\. Se Apuração = Trimestral, o parâmetro ‘Tipo de Receita’ deve ser desconsiderado\.

Tela Incentivos Fiscais

MFS\-12666

RNG00055

Validação de cadastros correspondentes

__Para tabelas sem data de vigência:__

Se a tabela correspondente não possuir campo de data inicial e o código informado não estiver cadastrado, exibir a mensagem DW00215\.

__Para tabelas com apenas data Inicial:__

Se a tabela correspondente possuir o campo data inicial, e não for encontrado registro correspondente com data inicial igual ou anterior à data de referência, exibir a mensagem DW00214\.

__Para tabelas com data inicial e data final:__

Se a tabela correspondente possuir o campo data inicial e data final e não for encontrado registro correspondente com data inicial igual ou anterior à data de referência e a data final nula ou posterior a data de referência, exibir a mensagem DW00214\.

Tela Informações Econômicas e Gerais

MFS\-12630

RNG00056

Registros sem campos obrigatórios

__IMPORTAÇÃO__

Se o registro informado no arquivo possuir somente o campo 

1 – REG como obrigatório e só este campo estiver preenchido, exibir a mensagem DW00220

Importação Bloco X

MFS\-12631

RNG00057

Importação de Arquivos

__Formatação do Arquivo:__

- Arquivo lido deverá ter extensão txt\.
- Os campos podem ser dos tipos:

C – Alfanumérico

D – Data

N – Numérico

NS – Numérico Sinalizado

- Separador decimal “,”
- Formato de Data \(DDMMAAAA\)

__Validações do Arquivo:__

Validações Estruturais:

- Em todos os registros dos arquivos, entre cada campo, deve ser colocado o separador ‘|’\(Pipe\)\. O ‘|’ deve ser inserido na primeira posição gerada e na última, caso contrário, exibir a mensagem DW00219\.
- Todos os campos devem conter o caracter delimitador ‘|’ no final de cada linha do arquivo, seguidos pelos caracteres “CR’ e ‘LF’ correspondentes a ‘retorno do carro’ e ‘salto de linha’ 
- O caracter delimitador ‘|’ \(Pipe\) não deve ser incluído como parte integrante do conteúdo de quaisquer campos numéricos, alfanuméricos ou datas\.
- Caso a formatação e a obrigatoriedade das informações de estrutura do arquivo, não forem iguais ao esperado, o processo será abortado, conforme os cenários descritos abaixo: 

__Registro000:__

- Verificar se registro inicia com “0000”, caso contrário exibir a mensagem DW00223\.
- Quantidade de campos na composição do registro “0000”, exibir a mensagem DW00223\.

__Campo CNPJ do Estabelecimento:__

- 
	- Se o CNPJ do Estabelecimento/SCP nao for informado no arquivo, exibir DW00223\.
	- Se não for possível localizar o Codigo do Estabelecimento com o CNPJ informado no arquivo, exibir a mensagem DW\.00223
	- Se no Registro <0000>, o Campo<CNPJ> não possuir o tamanho esperado, exibir a mensagem DW00223\.

__Campo Ano Exercício:__

- Se o ano do exercício não for informado no arquivo, exibir a mensagem DW00223\.
- Se o ano do exercício informado no arquivo for inválido, exibir a mensagem DW00223\.
- Se no Registro <0000>, o campo<ANO> não possuir o tamanho esperado, exibir a mensagem DW00223\.

__Campo Data Inicial:__

- Se Data Inicial não informada no arquivo\. 
- Data Inicial informada no arquivo invalida\. 
- Se no Registro <0000>, o Campo <DATA\_INI\_VIGENCIA> não possuir o tamanho esperado, exibir a mensagem DW00223

__Outras Validações Estruturais:__

- Validação de tamanho de campo, caso não seja atendida, exibir a mensagem DW00230\.
- Se a quantidade de campos, não forem iguais ao esperado, exibir a mensagem DW00218\.
- Se um registro filho for enviado, sem ter o registro pai, exibir a mensagem DW00217 
- Ao importar um arquivo com registros diferentes, dos registros aceitos, exibir a mensagem DW00216\.
- As informações do cabeçalho não serão inseridas na base\. Serão usadas apenas para garantir que os dados serão vinculados na escrituração correta\. Se a Informação ECF selecionada não coincidir com o cabeçalho do arquivo a ser importado, o processo será abortado, conforme os cenários descritos abaixo:
	- Se o CNPJ do Estabelecimento do arquivo é diferente do estabelecimento da Informação ECF, exibir a mensagem DW00222\.
	- Se Ano do Exercício informado no arquivo não corresponde ao Período da Escrituração, exibir a mensagem DW00222\.
	- Se a Data Inicial informada no arquivo não corresponder a Data Inicial da Escrituração, exibir a mensagem DW00222\.

\.

Demais Validações:

- Se as informações do cabeçalho x Informações ECF coincidirem, todas as linhas referentes aos registros \(que não possuírem erro\) serão inseridas na base\.
- Se existir um erro em alguma linha do arquivo, esses dados referentes as estas linhas não serão importadas, mas as demais linhas \(sem erros\), serão inseridas normalmente\. Nas mensagens de erro, sempre devem ser exibidas o número identificador da linha\. 
- As linhas \(sem erros\) serão inseridas na tela ‘Informações Econômicas e Gerais’, vinculados à ‘Informação ECF’ selecionada no momento do processo da importação \(tela Importação\)\.
- Serão aceitos mais de um tipo de registro dentro do mesmo arquivo \(Ex\. X291, X292 e X300\), porém deve ser respeitado os blocos que a importação aceita\.
- No arquivo não será necessário conter todos registros do bloco X e/ou Y sujeito à integração, mas os registros enviados, devem estar de acordo com a hierarquia liberadas no layout da ECF\.
- Respeitar as ocorrências dos registros, por exemplo: um arquivo poderá ter os registros X300 e X310, mas não pode ter um arquivo apenas com registros X310, pois o X300 é pai do registro X310 e este deve ser enviado\. Se no arquivo existir o registro pai e o filho, porém no registro pai for encontrado um erro que impeça a sua importação, aplicar a RNG00058 \- Registro pai com erro\.
- Se durante o processo de importação, um ou mais registros do arquivo não atenderem às condições necessárias de ocorrência não integrar o registro e retornar a mensagem DW00203 para cada registro encontrado neste cenário \(conforme tópico 4 – Permissão de exibição dos registros na tela, definidos do documento Tela Informacoes Economicas e Gerais\.doc\)\. 
- RNG00010 – Campo Obrigatório 
- RNG00021 – Validação de valores dos campos de lista 
- RNG00055 – Validação de cadastros correspondentes 
- RNG00027 – Validação de campos numéricos/numéricos sinalizado 
- RNG00026 – Validação de conteúdo de data 
- RNG00029 – Duplicidade Chave de Registro 
- RNG00028 – Identificação de registros com erro 
- RNG00056 – Registros sem campos obrigatórios
- Os campos de tipo Data devem estar no formato DDMMAAAA, caso contrário, aplicar RNG00026 – Validação de conteúdo de data 

Validações Específicas dos Campos dos Registros

__Bloco X e Y__

- Aplicar as validações existentes nos documentos Validacao\_Bloco\_X\.xlsx’ e Validacao\_Bloco\_Y\.xlsx\.

__Bloco W__

- Aplicar as validações existentes no documento Validacao\_Bloco\_W\.xlsx’\.

__Bloco V__

- Aplicar as validações existentes no documento Validacao\_Bloco\_V\.xlsx’\.

Importação Bloco X e Y

Bloco W

MFS\-12631

MFS\-19131

MFS\-20275

RNG00058

Registro pai com erro

Se no arquivo a ser importado, existir o registro pai e o filho, porém no registro pai for encontrado um erro que impeça a sua importação, verificar se base, já não existe o registro pai\. Caso não seja encontrado o registro pai \(gravado na base\), exibir a mensagem DW00248\.

Se existir o pai, continuar a importação do registro filho, caso este não possua nenhum erro\.

Importação Bloco X e Y

MFS\-18357

RNG00059

Indicador de exclusão

Se o valor informado no campo indicador de exclusão for “S” :

Buscar registro na base com os mesmos campos identificadores do registro

     Se não encontrado, emitir a seguinte mensagem DW00185      

Aplicar a regra de negócio geral <<RNG00028 \-  Identificação de registros com erro >>

     Se encontrado e o registro correspondente não possuir restrição referencial no banco de dados, excluir o registro da base de dados\. 

     Caso exista restrição referencial no banco de dados, emitir a seguinte mensagem DW00266\.    

Importação Bloco X e Y

MFS\-18357

RNG00060

Validação de CPF

 Se a quantidade de caracteres informados para o campo for diferente de 11, exibir a mensagem: DW00092\.

Se a quantidade de caracteres informados para o campo for igual a 11, validar o CPF\. Se o CPF for inválido, exibir a mensagem 

Importação Bloco X e Y

MFS\-21399

