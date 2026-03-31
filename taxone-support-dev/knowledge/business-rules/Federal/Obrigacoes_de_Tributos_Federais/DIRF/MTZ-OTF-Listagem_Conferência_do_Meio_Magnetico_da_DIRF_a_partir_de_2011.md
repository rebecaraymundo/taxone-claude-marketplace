# MTZ-OTF-Listagem_Conferência_do_Meio_Magnetico_da_DIRF_a partir de 2011

- **Fonte:** MTZ-OTF-Listagem_Conferência_do_Meio_Magnetico_da_DIRF_a partir de 2011.docx
- **Modificado:** 2024-02-27
- **Tamanho:** 45 KB

---

# Obrigações de Tributos Federais \- Geração de Relatório de Conferência da DIRF 2011

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3171\-A

Obrigações de Tributos Federais \- Geração de Relatório de Conferência da DIRF 2011

<a id="_Toc282417742"></a>__Módulo: Obrigações de Tributos Federais__

- Criação de tela de filtro para geração do relatório de conferência da DIRF 2011
- Criação de layout para o relatório de conferência da DIRF 2011

MFS\-90689

Elisabete Costa – 27/09/2022

No relatório de conferência “Valores de Rendimentos Isentos”, acrescentou o RIRPC e RIJMRE

#### Cód\.

### Descrição

### DR

# RN01

Deverá ser criado uma nova Listagem de Conferência para a obrigação acessória DIRF 2011\. A tela contendo os filtros para geração desse relatório será disponibilizada no módulo Obrigações de Tributos Federais, menu: DIRF >> Listagens >> Conferência DIRF >> Ano\-Referência a partir de 2011 >> Por Estabelecimento Central\.

OS3171\-A

# RN02

Os seguintes campos serão disponibilizados para que o usuário execute a geração do relatório:

- __Número Processo:__ o usuário poderá selecionar o número do processo gerado pela rotina de Geração da DIRF \(menu: DIRF >> Geração DIRF\)\. Serão exibidos os números de processo de acordo com a Empresa e Ano Referência informados\. Além disso, só serão exibidos os Números de Processo cuja geração da DIRF tenha sido informada o Ano Referência a partir de 2011 com Ano Calendário de 2010\. Campo obrigatório de preenchimento\.
- __Ano Base:__ será informado o ano calendário de geração da DIRF de acordo com o Número do Processo selecionado\. Esse campo não será passível de alteração por parte do usuário\.
- __Código Retenção:__ o usuário deverá informar o código de retenção\. Deverá ser um campo numérico de 4 \(quatro\) posições\. Caso nenhum Código de Retenção seja informado, todos os códigos existentes no arquivo serão gerados\. Campo não obrigatório de preenchimento\.
- __Pessoa Física:__ o usuário deverá selecionar essa opção caso o mesmo queira que na listagem sejam exibidas somente pessoas físicas da Folha de Pagamento \(SAFX21\) e/ou Retenções \(SAFX53\)\.
- __Pessoa Jurídica:__ o usuário deverá selecionar essa opção caso o mesmo queira que na listagem sejam exibidas somente pessoas jurídicas das Retenções \(SAFX53\)\.
- __Beneficiário:__ o usuário poderá selecionar um beneficiário específico gerado de acordo com o Número do Processo informado\. Caso nenhum beneficiário seja informado, todos os beneficiários informados no arquivo – pessoas físicas e jurídicas – serão informados\. Campo não obrigatório de preenchimento\.

OS3171\-A

# RN03

O relatório de conferência será exibido quebrando as informações por Estabelecimento, Código de Retenção e Beneficiário\. Logo o mesmo Beneficiário do mesmo Código de Retenção poderá ter suas informações exibidas em até 4 \(folhas\) do relatório\. Essas informações são diferentes\. 

As informações serão recuperadas pelo Número do Processo, que recupera as mesmas das tabelas de Ficha Financeira \(SAFX21\) e do Controle de Tributos \(SAFX53\)\.

OS3171\-A

# RN04

As informações comuns aos relatórios são as seguintes:

- __<<Código \+ Descrição da Empresa>>:__ será exibido nesse campo o Código e a Descrição da Empresa informada na tela de Formatação das Mídias \(menu: DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia\)\. Será exibido o Código e a Descrição separados por “\-“\.
- __<<Data:__ __dd/mm/aaaa>>:__ será exibida a data de geração do meio magnético
- __<<Hora:__ __00:00:00>>__: será exibida a hora, minuto e segundo da geração do meio magnético
- __<<Número Processo>>:__ será informado o Número do Processo de acordo com o informado no menu: DIRF >> Geração do Meio Magnético >> Ano\-Referência a partir de 2011 >> Formatação Mídia do módulo Obrigações de Tributos Federais\.
- __<<Ano Referência>>:__ será informado o ano de referência da geração da DIRF\.
- __<<Ano Calendário>>__: será informado o ano calendário da geração da DIRF\.
- __<<Estabelecimento>>: __será exibido o código e a descrição do estabelecimento\. Trata\-se da primeira quebra informada na RN03\.
- __<<Código Receita>>: __será informado o código de receita \(retenção\)\. Trata\-se da segunda quebra informada na RN03\.
- __<<Beneficiário>>: __será informado o CPF/CNPJ, Código e Descrição do Beneficiário\. Trata\-se da terceira quebra informada na RN03\.

OS3171\-A

# RN05

No relatório de conferência descrito como “Valores de Rendimentos Tributáveis, Deduções \(Previdência Oficial, Dependentes, Pensão Alimentícia e Previdência Privada/FAPI\) e IRRF” irá exibir os valores mês a mês, incluindo também o 13º\. Salário para o Beneficiário informado na RN04\.

As informações serão recuperadas dos registros RTRT, RTPO, RTPP, RTPA e RTIRF\.

No final do relatório os valores devem ser totalizados conforme descrito no layout\.

OS3171\-A

# RN06

No relatório de conferência descrito como “Valores de IRRF, Compensação do Imposto Decisão Judicial – anos calendário e Compensação – anos anteriores” serão exibidos os valores mês a mês \(Janeiro a Dezembro\) e também o valor pertinente ao 13º\. Salário para o Beneficiário informado na RN04\.

As informações serão recuperadas dos registros RTIRF, CJAC e CJAA\.

No final do relatório os valores devem ser totalizados conforme descrito no layout\.

OS3171\-A

# RN07

No relatório de conferência descrito como “Valores de Tributação com Exigibilidade Suspensa” serão exibidos os valores mês a mês \(Janeiro a Dezembro\) e também o valor pertinente ao 13º\. Salário para o Beneficiário informado na RN04\.

As informações serão recuperadas dos registros ESRT, ESPO, ESPP, ESDP, ESPA, ESIR e ESDJ\.

No final do relatório os valores devem ser totalizados conforme descrito no layout\.

OS3171\-A

# RN08

No relatório de conferência descrito como “Valores de Rendimentos Isentos” serão exibidos os valores mês a mês \(Janeiro a Dezembro\) e também o valor pertinente ao 13º\. Salário para o Beneficiário informado na RN04\.

As informações descritas mês a mês serão recuperadas dos registros RIP65, RIDAC, RIIRP, RIRPC e RIAP\.

As informações no final desse mesmo relatório \(Lucros e Dividendos, Valores pagos a titular ou sócio de micro\-empresa e Outros\) serão recuperadas dos rendimentos isentos anuais que são RIL96, RIPTS, RIJMRE e RIO\.

No final do relatório os valores devem ser totalizados conforme descrito no layout\.

OS3171\-A

MFS\-90689

# RN09

Deverá ser criado uma nova Listagem de Conferência para a obrigação acessória DIRF 2011\. A tela contendo os filtros para geração desse relatório será disponibilizada no módulo Obrigações de Tributos Federais, menu: DIRF >> Listagens >> Conferência DIRF >> Ano\-Referência a partir de 2011 >> Por Estabelecimento\.

OS3171\-A

# RN10

Os seguintes campos serão disponibilizados para que o usuário execute a geração do relatório:

- __Número Processo:__ o usuário poderá selecionar o número do processo gerado pela rotina de Geração da DIRF \(menu: DIRF >> Geração DIRF\)\. Serão exibidos os números de processo de acordo com a Empresa e Ano Referência informados\. Além disso, só serão exibidos os Números de Processo cuja geração da DIRF tenha sido informada o Ano Referência a partir de 2011 com Ano Calendário de 2010\. Campo obrigatório de preenchimento\.
- __Ano Base:__ será informado o ano calendário de geração da DIRF de acordo com o Número do Processo selecionado\. Esse campo não será passível de alteração por parte do usuário\.
- __Código Retenção:__ o usuário deverá informar o código de retenção\. Deverá ser um campo numérico de 4 \(quatro\) posições\. Caso nenhum Código de Retenção seja informado, todos os códigos existentes no arquivo serão gerados\. Campo não obrigatório de preenchimento\.
- __Pessoa Física:__ o usuário deverá selecionar essa opção caso o mesmo queira que na listagem sejam exibidas somente pessoas físicas da Folha de Pagamento \(SAFX21\) e/ou Retenções \(SAFX53\)\.
- __Pessoa Jurídica:__ o usuário deverá selecionar essa opção caso o mesmo queira que na listagem sejam exibidas somente pessoas jurídicas das Retenções \(SAFX53\)\.
- __Beneficiário:__ o usuário poderá selecionar um beneficiário específico gerado de acordo com o Número do Processo informado\. Caso nenhum beneficiário seja informado, todos os beneficiários informados no arquivo – pessoas físicas e jurídicas – serão informados\. Campo não obrigatório de preenchimento\.
- __Estabelecimentos:__ o usuário deverá selecionar o\(s\) estabelecimento\(s\) para visualização das listagens\. Serão exibidos somente os estabelecimentos referente ao Número de Processo informado\.

OS3171\-A

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

