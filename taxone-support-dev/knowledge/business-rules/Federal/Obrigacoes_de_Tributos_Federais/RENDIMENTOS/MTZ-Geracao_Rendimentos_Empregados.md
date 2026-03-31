# MTZ-Geracao_Rendimentos_Empregados

- **Fonte:** MTZ-Geracao_Rendimentos_Empregados.docx
- **Modificado:** 2025-12-03
- **Tamanho:** 53 KB

---

# Obrigações de Tributos Federais \- Geração dos Dados de Rendimentos dos Empregados

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH20637\_2012

Obrigações de Tributos Federais \- Geração dos Dados de Rendimentos dos Empregados

O objetivo deste documento de requisito é definir as regras para geração dos dados do Informe de Rendimentos de Empregados utilizando ou não a Centralização por Estabelecimento e também a geração de mais de um Informe de Rendimentos nos casos de um Funcionário que foi demitido e readmitido em um mesmo ano calendário\.

# RN01

O cliente ao gerar os dados do Informe de Rendimentos do Empregado \(menu: Rendimentos >> Rendimentos Empregados >> Geração dos Dados\) deverá verificar o estado dos campos “Tipo de Centralização” e “Gerar 2 Informes de Rendimentos por Funcionário?”\. De acordo com a opção selecionada a geração do Informe será realizada da seguinte forma:

- Campo “Tipo de Centralização” = “__Centralizado p/ Empresa__” e campo “Gerar 2 Informes de Rendimentos por Funcionário?” marcado:
	- Deverá ser gerado tantos informes de rendimento para o mesmo funcionário para cada incidência do funcionário dentro do ano calendário\. *Exemplo:*

*Cadastro do Funcionário*:

__Estabelecimento__

__Código Funcionário__

__CPF__

__Nome__

__Data Admissão__

__Data Demissão__

001

01

548\.368\.883\-01

João da Silva

01/01/2011

31/03/2011

002

02

548\.368\.883\-01

João da Silva

01/04/2011

30/06/2011

001

03

548\.368\.883\-01

João da Silva

01/07/2011

*Ficha Financeira:*

__Estabelecimento__

__Data do Pagamento__

__Competência \(Mês/Ano\)__

__Funcionário__

__Verba__

__Valor da Verba__

001

31/01/2011

01/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

001

31/01/2011

01/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

002

30/04/2011

04/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

002

30/04/2011

04/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

001

31/07/2011

07/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

001

31/07/2011

07/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

Nesse caso serão gerados 3 \(três\) informes de Rendimento para o funcionário “João da Silva”:

		

- Estabelecimento Centralizador
	- Informe de Rendimento 1 – Rendimentos Tributáveis: R$ 25\.000,00 – IRRF: R$ 1\.000,00\.
	- Informe de Rendimento 2 – Rendimentos Tributáveis: R$ 25\.000,00 – IRRF: R$ 1\.000,00\.
	- Informe de Rendimento 3 – Rendimentos Tributáveis: R$ 25\.000,00 – IRRF: R$ 1\.000,00\.

Todos os Informes de Rendimento deverão estar para o Estabelecimento informado como Centralizador\.

CH20637\_2012

# RN02

O cliente ao gerar os dados do Informe de Rendimentos do Empregado \(menu: Rendimentos >> Rendimentos Empregados >> Geração dos Dados\) deverá verificar o estado dos campos “Tipo de Centralização” e “Gerar 2 Informes de Rendimentos por Funcionário?”\. De acordo com a opção selecionada a geração do Informe será realizada da seguinte forma:

- Campo “Tipo de Centralização” = “__Centralizado p/ Empresa__” e campo “Gerar 2 Informes de Rendimentos por Funcionário?” desmarcado:
	- Deverá ser gerado um único informe de rendimento para o mesmo funcionário em todo o ano calendário\. *Exemplo:*

*Cadastro do Funcionário*:

__Estabelecimento__

__Código Funcionário__

__CPF__

__Nome__

__Data Admissão__

__Data Demissão__

001

01

548\.368\.883\-01

João da Silva

01/01/2011

31/03/2011

002

02

548\.368\.883\-01

João da Silva

01/04/2011

30/06/2011

001

03

548\.368\.883\-01

João da Silva

01/07/2011

*Ficha Financeira:*

__Estabelecimento__

__Data do Pagamento__

__Competência \(Mês/Ano\)__

__Funcionário__

__Verba__

__Valor da Verba__

001

31/01/2011

01/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

001

31/01/2011

01/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

002

30/04/2011

04/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

002

30/04/2011

04/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

001

31/07/2011

07/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

001

31/07/2011

07/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

Nesse caso será gerado 1 \(um\) informe de Rendimento para o funcionário “João da Silva”:

		

- Estabelecimento Centralizador
	- Informe de Rendimento 1 – Rendimentos Tributáveis: R$ 75\.000,00 – IRRF: R$ 3\.000,00\.

Os Informe de Rendimento deverão estar para o Estabelecimento informado como Centralizador\.

CH20637\_2012

# RN03

O cliente ao gerar os dados do Informe de Rendimentos do Empregado \(menu: Rendimentos >> Rendimentos Empregados >> Geração dos Dados\) deverá verificar o estado dos campos “Tipo de Centralização” e “Gerar 2 Informes de Rendimentos por Funcionário?”\. De acordo com a opção selecionada a geração do Informe será realizada da seguinte forma:

- Campo “Tipo de Centralização” = “__Não Centralizado__” e campo “Gerar 2 Informes de Rendimentos por Funcionário?” marcado:
	- Deverá ser gerado tantos informes de rendimento para o mesmo funcionário para cada incidência do funcionário dentro do ano calendário\. *Exemplo:*

*Cadastro do Funcionário*:

__Estabelecimento__

__Código Funcionário__

__CPF__

__Nome__

__Data Admissão__

__Data Demissão__

001

01

548\.368\.883\-01

João da Silva

01/01/2011

31/03/2011

002

02

548\.368\.883\-01

João da Silva

01/04/2011

30/06/2011

001

03

548\.368\.883\-01

João da Silva

01/07/2011

*Ficha Financeira:*

__Estabelecimento__

__Data do Pagamento__

__Competência \(Mês/Ano\)__

__Funcionário__

__Verba__

__Valor da Verba__

001

31/01/2011

01/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

001

31/01/2011

01/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

002

30/04/2011

04/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

002

30/04/2011

04/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

001

31/07/2011

07/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

001

31/07/2011

07/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

Nesse caso serão gerados 3 \(três\) informes de Rendimento para o funcionário “João da Silva”:

		

- Estabelecimento 001
	- Informe de Rendimento 1 – Rendimentos Tributáveis: R$ 25\.000,00 – IRRF: R$ 1\.000,00\.
	- Informe de Rendimento 3 – Rendimentos Tributáveis: R$ 25\.000,00 – IRRF: R$ 1\.000,00\.
- Estabelecimento 002
	- Informe de Rendimento 2 – Rendimentos Tributáveis: R$ 25\.000,00 – IRRF: R$ 1\.000,00\.

Os Informes de Rendimento deverão estar para o Estabelecimento informado como Centralizador ou Centralizado\.

CH20637\_2012

# RN04

O cliente ao gerar os dados do Informe de Rendimentos do Empregado \(menu: Rendimentos >> Rendimentos Empregados >> Geração dos Dados\) deverá verificar o estado dos campos “Tipo de Centralização” e “Gerar 2 Informes de Rendimentos por Funcionário?”\. De acordo com a opção selecionada a geração do Informe será realizada da seguinte forma:

- Campo “Tipo de Centralização” = “__Não Centralizado__” e campo “Gerar 2 Informes de Rendimentos por Funcionário?” desmarcado:
	- Deverá ser gerado um único informe de rendimento para o mesmo funcionário em todo o ano calendário separados por Estabelecimento\. *Exemplo:*

*Cadastro do Funcionário*:

__Estabelecimento__

__Código Funcionário__

__CPF__

__Nome__

__Data Admissão__

__Data Demissão__

001

01

548\.368\.883\-01

João da Silva

01/01/2011

31/03/2011

002

02

548\.368\.883\-01

João da Silva

01/04/2011

30/06/2011

001

03

548\.368\.883\-01

João da Silva

01/07/2011

*Ficha Financeira:*

__Estabelecimento__

__Data do Pagamento__

__Competência \(Mês/Ano\)__

__Funcionário__

__Verba__

__Valor da Verba__

001

31/01/2011

01/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

001

31/01/2011

01/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

002

30/04/2011

04/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

002

30/04/2011

04/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

001

31/07/2011

07/2011

01 – João da Silva

01 – Pagamento de Salário

R$ 25\.000,00

001

31/07/2011

07/2011

01 – João da Silva

02 – IRRF

R$ 1\.000,00

Nesse caso será gerado 2 \(dois\) informes de Rendimento para o funcionário “João da Silva”:

		

- Estabelecimento 001
	- Informe de Rendimento 1 – Rendimentos Tributáveis: R$ 50\.000,00 – IRRF: R$ 2\.000,00\.
- Estabelecimento 002
	- Informe de Rendimento 2 – Rendimentos Tributáveis: R$ 25\.000,00 – IRRF: R$ 1\.000,00\.

Os Informes de Rendimento deverão estar para o Estabelecimento informado como Centralizador ou Centralizado\.

CH20637\_2012

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

