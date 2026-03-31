# MTZ-OTF-Gerar_DCTF

- **Fonte:** MTZ-OTF-Gerar_DCTF.docx
- **Modificado:** 2026-03-04
- **Tamanho:** 58 KB

---

# Módulo – OTF \- DCTF

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2711

- Incluir novos códigos de Receita na TACES14;
- Alterar a descrição do grupo de Tributo código 10 na TACES15;
- Incluir o CNPJ da incorporação, quando utilizar os códigos de receita correspondentes ao Código de Tributo 10, no campo de ordem 13 no registro Tipo 10 \(Débito Apurado e Créditos Vinculados\)\.
- Alteração dos títulos dos menus, telas, telas de pesquisa e relatórios de conferência da DCTF Mensal 1\.5 para DCTF Mensal 1\.6\.
- Alteração dos títulos dos menus, telas, telas de pesquisa e relatórios de conferência da DCTF Semestral 1\.3 para DCTF Semestral 1\.4\.

CH84426

Atualizar DCTF para nova versão

1. Alteração dos títulos dos menus, telas, telas de pesquisa e relatórios de conferência da DCTF Mensal 1\.6 para DCTF Mensal 1\.7\.
2. Alteração dos títulos dos menus, telas, telas de pesquisa e relatórios de conferência da DCTF Semestral 1\.4 para DCTF Semestral 1\.5\.

OS3299

Esse documento tem como objetivo alterar a geração da DCTF para que a mesma passe a atender a nova versão 1\.9 disponibilizada\.

CH92476

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>DCTF – Alterar TACES14 

Esse documento tem como objetivo corrigir a periodicidade do código 115003 de Diário para Decendial\.

OS3333

DCTF – Gerar versão 2\.0 da DCTF

Esse documento tem como objetivo alterar a geração da DCTF para que a mesma passe a atender a nova versão 2\.0 disponibilizada\.

CH113623

DCTF – Gerar versão 2\.2 da DCTF

Este documento tem por objetivo alterar a geração da DCTF para que possa atender a nova versão 2\.2 disponibilizada

CH117675\-A

DCTF – Gerar versão 2\.2 da DCTF

Ajustar o campo Versão para que recupere a versão correta\.

OS3534

DCTF – Gerar versão 2\.3 da DCTF

Ajustar o campo Versão para que recupere a versão correta e atualizar as telas da DCTF para que a versão seja omitida\.

24489\_2012

DCTF alterar TACES 14 e 15

Incluir na TACES14 Códigos de Receita

Alterar na TACES14 a descrição de Códigos de Receita

Alterar na TACES15 a descrição do Código de Tributo 33

CH5725\_2013

DCTF – Gerar versão 2\.5 da DCTF

Ajustar o campo Versão para que recupere a versão correta e atualizar as telas da DCTF\.

CH14395\-A\_2013

Correção da geração do campo 13 do registro R10 da DCTF

O objetivo deste documento de requisito é alterar a geração do campo 13 do registro R10 dos Débitos da DCTF, para que seja considerado o CNPJ do Estabelecimento ao qual pertence a retenção\.

OS4259

Obrigações de Tributos Federais – Gerar Campo 19 do Registro R10 da DCTF a partir do Código de Receita

O objetivo dessa OS é permitir que os débitos de SCP/INC/Demais que são gerados no campo 19 – Débito de SCP/INC da Ficha 10 – Débito Apurado e Créditos Vinculados tenham correlação com o Código de Receita gerado nessa ficha\.

CH11012\_2014

Ajustar a geração do campo 17 do Registro R10

Ajustar a geração do campo 17 do Registro R10 para correta demonstração da geração de Saldo Dividido em Quotas\.

CH11595\_2014

DCTF – Alterar TACES14

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK12"></a>Ajustar alguns códigos de receita com periodicidade Decendial que estão incorretos na TACES14\.

OS4620

DCTF versão 3\.1

Ajustes no processo de geração para atender à versão 3\.1 do layout da DCTF\.

OS4741

DCTF versão 3\.2

Ajustes no processo de geração para atender à versão 3\.2 do layout da DCTF\.

MFS3385

DCTF versão 3\.3

Ajustes no processo de geração para atender à versão 3\.3 do layout da DCTF\.

MFS8129 \(CH22392\_2016\)

Correção da geração do campo 13 do registro R10 da DCTF

O objetivo deste documento de requisito é alterar a geração do campo 13 do registro R10 dos Débitos da DCTF, para que seja considerado o CNPJ do Estabelecimento ao qual pertence a retenção 106801 \- RET\.

MFS\-644857

Rosemeire Santos

Inclusão da __RN80__, para considerar na geração da DCTF os DARFs a partir da tela Código do Darf

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Inclusão dos seguintes códigos na TACES14:

409501 – Regime Especial de Tributação do Patrimônio de Afetação

411201 – IRPJ – Regime Especial de Tributação do Patrimônio de Afetação

413801 – PIS – Regime Especial de Tributação do Patrimônio de Afetação

415301 – CSLL – Regime Especial de Tributação do Patrimônio de Afetação

416601 – COFINS – Regime Especial de Tributação do Patrimônio de Afetação

Incluir os Códigos de Receita  a seguir na TACES14:

172303 \- CPSS – Servidor Civil Ativo – Precatório Judicial e Requisição de Pequeno Valor

173003 – CPSS – Servidor Civil Inativo \- Precatório Judicial e Requisição de Pequeno Valor

175203 \- CPSS – Pensionista – Precatório Judicial e Requisição de Pequeno Valor  

183703 \- CPSS – Patronal – Precatório Judicial e Requisição de Pequeno Valor – Operação Intra\-Orçamentária

Alterar a descrição dos Códigos de Receita a seguir na TACES14:

__De:__

166101

CPSSS\-Servidor Civil Ativo

168401

CPSSS\-Servidor Civil Licenciado/Cedido

169001

CPSSS\-Decisao Judicial Mandado de Seguranca

169002

CPSSS\-Decisao Judicial Mandado de Seguranca

170001

CPSSS\-Servidor Civil Inativo

__Para:__

166101

CPSS\-Servidor Civil Ativo

168401

CPSS\-Servidor Civil Licenciado/Cedido

169001

CPSS\-Decisao Judicial Mandado de Seguranca

169002

CPSS\-Decisao Judicial Mandado de Seguranca

170001

CPSS\-Servidor Civil Inativo

Incluir a DT\_FIM\_VALID 2120731 para o Código de Receita 181401 \-  CPSS – Patronal \- Servidor no Exterior – Operação Intra \- Orcamentaria

                                  

Alterado CH24489\_2012, verificar o documento TACES14\_V2\.xls \(anexo ao chamado\) neste documentos os novos Códigos de Receita  estão em azul e os alterados em amarelo

__OS2711__

__CH24489\_2012__

__RN02__

Alteração do código 10 – ICMS \- Imposto Sobre Circulação de Mercadorias da TACES15 para:

10 – RET/PA \- RET/Patrimônio de Afetação

Alterar ma TACES15 a descrição do Cod\_Tributo 33

__ De: __CPSSS \- Contribuicao do Plano de Seguridade do Servidor Publico 

__Para: __CPSS –  Contribuicao para o  Plano de Seguridade Social do Servidor

Alterada CH24489\_2012 verificar doc TACES15\.xls \(em amarelo\)

__OS2711__

__CH24489\_2012__

__RN03__

Na geração da DCTF quando quando o Grupo de Tributo é igual a 10 e o códigos de Receita iguais a:

409501 – Regime Especial de Tributação do Patrimônio de Afetação

411201 – IRPJ – Regime Especial de Tributação do Patrimônio de Afetação

413801 – PIS – Regime Especial de Tributação do Patrimônio de Afetação

415301 – CSLL – Regime Especial de Tributação do Patrimônio de Afetação

416601 – COFINS – Regime Especial de Tributação do Patrimônio de Afetação

106801 – RET – Pagto Unificado Equiv 1% Receitas Mensais Recebidas p/  Incorporadora

O sistema deverá recuperar o Número do CNPJ do estabelecimento ao qual pertence a retenção e informar nos campos \(CNPJ da Incorporação\) 56 a 69 do Meio Magnético do DCTF\.

__OS2711__

__CH14395\-A\_2013__

__MFS8129__

__RN04__

Alterar o título do menu do módulo Obrigações de Tributos Federais \(Federal – Obrigações de Tributos Federais\):

__De:__

Outras Obrigações → DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.5\)

Outras Obrigações → DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.6\)

Outras Obrigações → DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.7\)

Outras Obrigações → DCTF – DCTF Mensal \(2011\-V1\.9\)

__Para:__

Outras Obrigações → DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.6\)

Outras Obrigações → DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.7\)

Outras Obrigações → DCTF – DCTF Mensal \(2011\-V1\.9\)

Outras Obrigações → DCTF – DCTF Mensal \(2011\-V2\.0\)

__OS2711 / CH84426/ OS3299__

__OS3333__

__RN05__

__\[ALTERADA – CH84426\]__

Alterar o título do menu do módulo Obrigações de Tributos Federais \(Federal – Obrigações de Tributos Federais\):

__De:__

Outras Obrigações → DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.3\)

Outras Obrigações → DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\)

__Para:__

Outras Obrigações → DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\)

Outras Obrigações → DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\)

__OS2711 / CH84426__

__RN06__

Alterar o título de dentro da tela do menu do módulo Obrigações de Tributos Federais \(Federal – Obrigações de Tributos Federais\):

__De:__

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.9\) – Feriados

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.9\) – Dados Iniciais

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.9\) – Geração DCTF

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.9\) – Digitação da Ficha de Débito

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.9\) – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.9\) – Relatórios – Status – Fichas de Débito

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.9\) – Relatórios – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.9\) – Meio Magnético – Declaração Débito e Crédito – Geração \(2006\-V1\.7\)

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.9\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Mensal \(2006\-V1\.7\)

__Para:__

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Feriados

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Dados Iniciais

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Geração DCTF

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Digitação da Ficha de Débito

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Relatórios – Status – Fichas de Débito

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Relatórios – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Meio Magnético – Declaração Débito e Crédito – Geração \(2011\-V2\.0\)

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Mensal \(2011\-V2\.0\)

__OS2711 / CH84426/ OS3299__

__OS3333__

__   __

__RN07__

__\[ALTERADA – CH84426\]__

Alterar o título do menu do módulo Obrigações de Tributos Federais \(Federal – Obrigações de Tributos Federais\):

De:

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.5\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Mensal \(2006\-V1\.5\)

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.6\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Mensal \(2006\-V1\.6\)

Para:

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.6\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Mensal \(2006\-V1\.6\)

Outras Obrigações – DCTF – DCTF Mensal \(2005\-V1\.1/2006\-V1\.7\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Mensal \(2006\-V1\.7\)

__OS2711 / CH84426__

__RN08__

__\[ALTERADA – CH84426\]__

Alterar o título de dentro da tela do menu do módulo Obrigações de Tributos Federais \(Federal – Obrigações de Tributos Federais\):

__De: __

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.3\) – Dados Iniciais

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.3\) – Geração DCTF

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.3\) – Digitação da Ficha de Débito

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.3\) – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.3\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Semestral \(2006\-V1\.3\)

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Dados Iniciais

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Geração DCTF

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Digitação da Ficha de Débito

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Semestral \(2006\-V1\.4\)

__Para:__

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Dados Iniciais

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Geração DCTF

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Digitação da Ficha de Débito

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.4\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Semestral \(2006\-V1\.4\)

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Dados Iniciais

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Geração DCTF

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Digitação da Ficha de Débito

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Semestral \(2006\-V1\.5\)

__OS2711 / CH84426__

__RN09__

Alterar o título da tela de pesquisa e dos relatórios de conferência das telas da DCTF Mensal e DCTF Semestral\. O objetivo é equalizar conforme as alterações das regras anteriores para as versões 2\.0 \(Mensal\) 1\.5 \(Semestral\)\.

Módulo: Federal – Obrigações de Tributos Federais

Menus:

DCTF Mensal

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Feriados

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Dados Iniciais

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Geração DCTF

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Digitação da Ficha de Débito

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Relatórios – Status – Fichas de Débito

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Relatórios – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Meio Magnético – Declaração Débito e Crédito – Geração \(2011\-V2\.0\)

Outras Obrigações – DCTF – DCTF Mensal \(2011\-V2\.0\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Mensal \(2011\-V2\.0\)

DCTF Semestral

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Dados Iniciais

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Geração DCTF

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Digitação da Ficha de Débito

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Pagamento de Débitos

Outras Obrigações – DCTF – DCTF Semestral \(2005\-V1\.0/2006\-V1\.5\) – Meio Magnético – Declaração Débito e Crédito – Relatório de Conferência – DCTF Semestral \(2006\-V1\.5\)

__OS2711 / CH84426/ OS3299__

__RN10__

__\[ALTERADA OS3534\]__

__Regra p/ campo Header – Versão \(09\) __

Gravar no campo 9 – VERSAO o valor “230” na DCTF Mensal\.

\[__ALTERADA CH5725\_2013__\]

__Regra p/ campo Header – Versão \(09\) __

Gravar no campo 9 – VERSAO o valor “250” na DCTF Mensal para gerações a partir do ano calendário 2013\.

__OS2711 / CH84426/ OS3299__

__OS3333__

__CH113623__

__CH117675\-A__

__OS3534__

__RN11__

Gravar no campo 9 – VERSAO o valor “150” na DCTF Semestral\.

__CH84426__

__RN12__

__Regra p/ campo R01 – PJ entregou DCTF Semestral no ano anterior \(15\) __

Preencher com:

0, quando o campo PJ Esteve Obrigado à Apresentação da DCTF Semestral no Ano Anterior da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando o campo PJ Esteve Obrigado à Apresentação da DCTF Semestral no Ano Anterior da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN13__

__Regra p/ campo R01 – Critério de Reconhecimento das Variações Monetárias dos Direitos de Crédito e das Obrigações do Contribuinte, em função da Taxa de Cambio \(16\) __

Preencher com o conteúdo informado no campo “Critério de Reconhecimento das Variações Monetárias dos Direitos de Crédito e das Obrigações do Contribuinte, em função da Taxa de Cambio” na tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais\.

__OS3299__

__RN14__

__Regra p/ campo R01 – Mês com ausência de débito a declarar \- Janeiro \(17\) __

Preencher com:

0, quando a opção Janeiro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Janeiro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN15__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Fevereiro \(18\) __

Preencher com:

0, quando a opção Fevereiro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Fevereiro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN16__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Março \(19\) __

Preencher com:

0, quando a opção Março do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Março do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN17__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Abril \(20\) __

Preencher com:

0, quando a opção Abril do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Abril do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN18__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Maio \(21\) __

Preencher com:

0, quando a opção Maio do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Maio do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN19__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Junho \(22\) __

Preencher com:

0, quando a opção Junho do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Junho do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN20__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Julho \(23\) __

Preencher com:

0, quando a opção Julho do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Julhodo campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN21__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Agosto \(24\) __

Preencher com:

0, quando a opção Agosto do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Agosto do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN22__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Setembro \(25\) __

Preencher com:

0, quando a opção Setembro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Setembrodo campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN23__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Outubro \(26\) __

Preencher com:

0, quando a opção Outubro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Outubro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN24__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Novembro \(27\) __

Preencher com:

0, quando a opção Novembro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Novembro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN25__

__Regra p/ campo R01 –Mês com ausência de débito a declarar \- Dezembro \(28\) __

Preencher com:

0, quando a opção Dezembro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando a opção Dezembro do campo Mês com ausência de débito a declarar da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN26__

__Regra p/ campo R01 – Regime de Apuração da Contribuição para o PIS/Pasep e da Cofins \(29\) __

Preencher com o conteúdo informado no campo “Regime de Apuração da Contribuição para o PIS/Pasep e da Cofins” na tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais\.

__OS3299__

__RN27__

__Regra p/ campo R01 – PJ iniciou atividade no mês da declaração \(30\) __

Preencher com:

0, quando o campo PJ iniciou atividade no mês da declaração da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver desmarcado\.

1, quando o campo PJ iniciou atividade no mês da declaração da tela Outras Obrigações – DCTF – DCTF Mensal \(2011\-V1\.9\) – Dados Iniciais estiver marcado\.

__OS3299__

__RN28__

__\[EXCLUÍDA – OS4259\] Regra p/ campo R10 – Débito de SCP/INC \(19\) __

Preencher com:

2, quando o campo PJ com Débitos de INC a serem Declarados estiver marcado

1, quando o campo PJ com Débitos de SCP a serem Declarados estiver marcado

0, quando nenhum dos dois campos acima estiverem marcados

__OS3299__

__OS4259__

__RN29__

__Regra p/ campo R10 – Reservado \(20\) __

Preencher com brancos\.

__OS3299__

__RN30__

__Regra p/ geração do R12__

Esse registro deverá ser reestruturado a partir do campo 14, devendo obedecer a seguinte ordem:

15 – Valor Compensado do Débito

16 – Formalização do Pedido

17 – Número do PERDCOMP ou Processo

18 – Reservado

19 – Delimitador do Registro

Os campos devem ser recuperados conforme regras atuais\.

A estrutura de campos anterior deve ser descartada\.

__OS3299__

__RN31__

__Regra p/ geração do R13__

Retirar os campos:

20 \- Reservado

21 \- Reservado

22 \- Reservado

23 \- Reservado

__OS3299__

__RN32__

__Regra p/ campo R20 – Débito de SCP/INC \(19\) __

Preencher com:

2, quando o campo PJ com Débitos de INC a serem Declarados estiver marcado

1, quando o campo PJ com Débitos de SCP a serem Declarados estiver marcado

0, quando nenhum dos dois campos acima estiverem marcados

__OS3299__

__RN33__

__Regra p/ campo R20 – Reservado \(20\) __

Preencher com brancos\.

__OS3299__

__RN34__

__Regra p/ geração do R22__

Esse registro deverá ser reestruturado a partir do campo 14, devendo obedecer a seguinte ordem:

15 – Valor Compensado do Débito

16 – Formalização do Pedido

17 – Número do PERDCOMP ou Processo

18 – Reservado

19 – Delimitador do Registro

Os campos devem ser recuperados conforme regras atuais\.

A estrutura de campos anterior deve ser descartada\.

__OS3299__

__RN35__

__Regra p/ geração do R23__

Retirar os campos:

20 \- Reservado

21 \- Reservado

22 \- Reservado

23 \- Reservado

__OS3299__

__RN36__

__Regra p/ geração do R32__

Esse registro deverá ser reestruturado a partir do campo 14, devendo obedecer a seguinte ordem:

15 – Valor Compensado do Débito

16 – Formalização do Pedido

17 – Número do PERDCOMP ou Processo

18 – Reservado

19 – Delimitador do Registro

Os campos devem ser recuperados conforme regras atuais\.

A estrutura de campos anterior deve ser descartada\.

__OS3299__

__RN37__

__Regra p/ geração do R33__

Retirar os campos:

20 \- Reservado

21 \- Reservado

22 \- Reservado

23 \- Reservado

__OS3299__

__RN38__

__Regra p/ geração do campo 06 – Grupo de Tributo__

Se o campo COD\_TRIBUTO da tabela DWT\_TRIBUTO = “33”, a geração deve gravar no meio magnético = “13” para todos os registros que possuírem esse campo\.

__OS3299__

__RN39__

<a id="OLE_LINK8"></a><a id="OLE_LINK9"></a><a id="OLE_LINK10"></a><a id="OLE_LINK11"></a>Alteração da periodicidade do Código de Receita 115003 – IOF – Operações de Credito – Pessoa Jurídica da TACES14 para:

X – Decendial\.

__CH92476__

__RN40__

Alterar o título do menu “Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\)” para a seguinte forma:

De:

Outras Obrigações >> DCTF >> __DCTF Mensal \(2011\-V2\.2\)__

Para:

Outras Obrigações >> DCTF >> __DCTF Mensal \(a partir de 01/01/2006\)__

__OS3534__

__RN41__

O título da tela “Novo Feriado \(DCTF \(2011\-V2\.2\)\)” deverá ser alterado para “Novo Feriado”\.

__OS3534__

__RN42__

O título da tela de pesquisa de registros já cadastrados deve ser alterado de “Selecionar Feriado \(DCTF \(2011\-V2\.2\)\)” para “Selecionar Feriado”\.

__OS3534__

__RN43__

O título da tela de Relatório de Conferência deve ser alterado de “Critério para Seleção para Relatório de Feriados \(DCTF \(2011\-V2\.2\)\)” para “Critério para Seleção para Relatório de Feriados”\.

__OS3534__

__RN44__

O título da tela do Relatório de Conferência deve ser alterado de “Relatório de Feriados \(DCTF \(2011\-V2\.2\)\)” para “Relatório de Feriados”\.

__OS3534__

__RN45__

O título da tela “Dados Iniciais \(DCTF Mensal 2011\-V2\.2\)” deverá ser alterado para “Dados Iniciais” dos seguintes menus:

Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Empresa 

__OU__

 Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Dados Iniciais >> Por Estabelecimento

__OS3534__

__RN46__

O título da tela de pesquisa de registros já cadastrados deve ser alterado de “Dados Iniciais \(DCTF Mensal 2011\-V2\.2\)” para “Dados Iniciais”\.

__OS3534__

__RN47__

O título da tela de Relatório de Conferência deve ser alterado de “Critério para Seleção para Relatório de Dados Iniciais \(DCTF \(2011\-V2\.2\)\)” para “Critério para Seleção para Relatório de Dados Iniciais”\.

__OS3534__

__RN48__

O título da tela do Relatório de Conferência deve ser alterado de “Relatório de Dados Iniciais \(DCTF \(2011\-V2\.2\)\)” para “Relatório de Dados Iniciais”\.

__OS3534__

__RN49__

O título da tela “Geração DCTF \(Mensal 2011\-V2\.2\)” deverá ser alterado para “Geração DCTF” dos seguintes menus:

Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Empresa 

__OU__

 Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Geração DCTF >> Por Estabelecimento

__OS3534__

__RN50__

O título da tela “Digitação da Ficha de Débito \(Mensal 2011\-V2\.2\)” deverá ser alterado para “Digitação da Ficha de Débito” do seguinte menu:

Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Digitação da Ficha de Débito

__OS3534__

__RN51__

O título da tela de pesquisa de registros já cadastrados deve ser alterado de “Selecionar Ficha de Débito: \(DCTF Mensal 2011\-V2\.2\)” para “Selecionar Ficha de Débito”\.

__OS3534__

__RN52__

O título da tela de Relatório de Conferência deve ser alterado de “Critério para Seleção para Relatório de Fichas de Débito \(DCTF \(2011\-V2\.2\)\)” para “Critério para Seleção para Relatório de Fichas de Débito”\.

__OS3534__

__RN53__

O título da tela do Relatório de Conferência deve ser alterado de “Relatório de Fichas de Débito \(DCTF \(2011\-V2\.2\)\)” para “Relatório de Fichas de Débito”\.

__OS3534__

__RN54__

O título da tela “Pagamento de Débitos \(Mensal 2011\-V2\.2\)” deverá ser alterado para “Pagamento de Débitos” do seguinte menu:

Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Digitação da Ficha de Débito

__OS3534__

__RN55__

O título da tela de pesquisa de registros já cadastrados deve ser alterado de “Selecionar Ficha de Débito: \(DCTF Mensal 2011\-V2\.2\)” para “Selecionar Ficha de Débito”\.

__OS3534__

__RN56__

O título da tela “Relatório de Status – Ficha de Débito \(DCTF 2011\-V2\.2\)” deverá ser alterado para “Relatório de Status – Ficha de Débito” do seguinte menu:

Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Relatórios >> Status – Ficha de Débito

__OS3534__

__RN57__

O título da tela do Relatório de Conferência deve ser alterado de “Relatório de Status – Ficha de Débito \(DCTF 2011\-V2\.2\)” para “Relatório de Status – Ficha de Débito”\.

__OS3534__

__RN58__

O título da tela “Relatório de Pagamento de Débitos \(DCTF Mensal 2011\-V2\.2\)” deverá ser alterado para “Relatório de Pagamento de Débitos” do seguinte menu:

Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Relatórios >> Pagamento de Débitos

__OS3534__

__RN59__

O título da tela do Relatório de Conferência deve ser alterado de “Relatório de Pagamento de Débitos \(DCTF Mensal 2011\-V2\.2\)” para “Relatório de Pagamento de Débitos”\.

__OS3534__

__RN60__

O título da tela “Geração – Declaração de Débitos e Créditos \(DCTF Mensal 2011 – V2\.2\)” deverá ser alterado para “Geração – Declaração de Débitos e Créditos” dos seguintes menus:

Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Meio Magnético – Declaração Débito e Crédito >> Geração >> Por Empresa

__OU__

Outras Obrigações >> DCTF >> DCTF Mensal \(2011\-V2\.2\) >> Meio Magnético – Declaração Débito e Crédito >> Geração >> Por Estabelecimento

__OS3534__

__RN61__

O título do menu de geração do Relatório de Conferência deve ser alterado de “DCTF Mensal 2011\-V2\.2” para “Relatório de Conferência”\.

__OS3534__

__RN62__

O título da tela do Relatório de Conferência deve ser alterado de “Relatório de Conferência \(DCTF Mensal 2011\-V2\.2\)” para “Relatório de Conferência”\.

__OS3534__

__RN63__

O título do Relatório de Conferência deve ser alterado de “Relatório de Conferência \(DCTF Mensal 2011\-V2\.2\)” para “Relatório de Conferência”\.

__OS3534__

__RN64__

O campo “Versão DCTF” da tela de Dados Iniciais da DCTF do módulo Obrigações de Tributos Federais \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Dados Iniciais >> Por Empresa\) deverá ser omitido da tela, visto que para a gravação da versão no arquivo a ser gerado a sistemática é diferente – ver RN10\.

__OBS:__ a inibição desse campo é importante pois foi identificado que parte da funcionalidade desse campo não foi excluída corretamente e hoje ao selecionar qualquer opção é gerada mensagem de erro não prevista no sistema\.

__OS3534__

__RN65__

O campo “Versão” da tela de Geração da Declaração dos Débitos e Créditos tanto por Empresa quanto por Estabelecimento, deverá ser alterado do valor atual “202” para o valor “230”\. 

Isso se faz necessário em virtude da nova versão da DCTF\. Além disso, é importante frisar que esse campo é meramente informativo e não influi no arquivo\. Além disso, o campo 09 – Versão do registro Header da Declaração não é recuperado e informado nesse campo\.

\[__ALTERADO CH5725\_2013__\]

O campo “Versão” da tela de Geração da Declaração dos Débitos e Créditos tanto por Empresa quanto por Estabelecimento, deverá ser alterado do valor atual “240” para o valor “250\.

__OS3534__

__CH5725\_2013__

__RN66__

Caso no processo de geração da DCTF, o parâmetro “Débitos de SCP/INC” não esteja informado na TACES14 \(menu: Tabelas Internas >> Manter >> Tabelas\) do módulo Ferramentas para algum Código de Receita que esteja sendo gerado, o sistema deverá exibir a seguinte mensagem de erro no Log de Processos do módulo Obrigações de Tributos Federais e não deverá gerar a Ficha de Débito:

“Código de Receita não parametrizado na TACES14 do módulo Ferramentas”\.

O Código de Receita deverá ser informado para facilitar a correção da parametrização por parte do usuário\.

__OS4259__

__RN67__

__Informações das Fichas de Débito – Tipo R10__

__Campo 17 – O saldo desse débito será dividido em quotas__

Deverá ser gravado nas posições 86 a 86 se o saldo do débito será dividido em quotas\. Essa informação deve ser recuperada de acordo com a opção informada no campo “Quota” da tela de Pagamento de Débitos \(menu: Outras Obrigações >> DCTF >> DCTF Mensal >> Pagamento de Débitos\.

A regra para gravação é a seguinte:

- Se o valor do campo “Quota” for igual a “0”, gravar “0”
- Se o valor do campo “Quota” for diferente de “0”, gravar “1”\.

__OBS:__ Para geração a partir de DARF Complementar \(SAFX751\), sempre será gerado como “0”, pois não teremos situação de Quotas para DARFs Complementares\.

__CH110112/2014__

__RN68__

Alteração da periodicidade dos Códigos de Receita da TACES14 a seguir para X – Decendial:

846802

IRRF \- Rendimentos de capital \- Operações Day Trade

056103

IRRF \- Rendimentos do trabalho \- Trabalho assalariado no Pais/Ausente no exterior a servico do Pais

056106

IRRF \- Rendimentos do trabalho \- Trabalho assalariado no Pais/Ausente no exterior a servico do Pais

058805

IRRF \- Rendimentos do trabalho \- Trabalho sem vinculo empregaticio

170805

IRRF \- Outros rendimentos \- Remuneracao de servicos profissionais prestados por pessoa juridica/Serv

320805

IRRF \- Rendimentos de capital \- Alugueis e royalties pagos a pessoa fisica

322305

IRRF \- Rendimentos do trabalho \- Resgate de previdencia privada e Fapi \- Nao optantes pela tributaca

327705

IRRF \- Rendimentos de capital \- Rendimentos de partes beneficiarias ou de fundador

328005

IRRF \- Outros rendimentos \- Servicos prestados por associados de cooperativas de trabalho

520405

IRRF \- Outros rendimentos \- Juros e indenizacoes por lucros cessantes

556505

IRRF \- Rendimentos do trabalho \- Beneficio e resgate de previdencia privada e FAPI \- Optantes pela t

592805

IRRF \- Outros rendimentos \- Rendimentos decorrentes de decisao da Justica Federal

593605

IRRF \- Rendimentos do trabalho \- Rendimentos decorrentes de decisao da Justica do Trabalho

594405

IRRF \- Outros rendimentos \- Pagamentos de pessoa juridica a pessoa juridica por servicos de factorin

689105

IRRF \- Outros rendimentos \- Vida Gerador de Beneficio Livre \(VGBL\)

690405

IRRF \- Outros rendimentos \- Indenizacao por danos morais

804505

IRRF \- Outros rendimentos \- Comissoes e corretagens pagas a pessoa juridica/Servicos de propaganda p

049005

IRRF \- Aplic em fundos de conv de deb ext/Lucros/Bonif/Dividendos \- Rend de resid ou dom no exterior

092403

IRRF \- Rendimentos de capital \- Ficart e demais rendimentos de capital

867302

IRRF \- Outros rendimentos \- Jogos de bingo permanente ou eventual \- Premios em bens, servicos ou din

523204

IRRF \- Rendimentos de capital \- Aplicacoes financeiras em fundos de investimento imobiliario \- Resga

527302

IRRF \- Rendimentos de capital \- Operacoes de Swap

528604

IRRF \- Rendimentos de residentes ou domiciliados no exterior \- Aplicacoes financeiras/ Entidades de

555702

IRRF \- Ganhos liquidos em operacoes em bolsas e assemelhados

680002

IRRF \- Rendimentos de capital \- Aplicacoes financeiras em fundos de investimento \- Renda fixa

681302

IRRF \- Rendimentos de capital \- Aplicacoes financeiras em fundos de investimento \- Acoes

945302

IRRF \- Rendimentos de residentes ou domiciliados no exterior \- Juros remuneratorios do capital propr

__CH11595\_2014__

__RN69__

__Ajustar a tela de geração do Meio Magnético da DCTF__:

__Módulo__: Federal >> Obrigações de Tributos Federais

__Menu__: Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Meio Magnético – Declaração de Débito e Crédito >> Geração >> Por Empresa __OU __Por Estabelecimento

Exibir no campo “Versão” a descrição “310”, “320”, “330” quando o mês e ano forem maiores ou iguais a agosto de 2014\.

__OS4620__

__OS4741__

__MFS\_3385__

__RN70__

__Registro Header da Declaração – Campo 09 – Versão__

Quando a geração do arquivo for de um período maior ou igual a agosto de 2014, o campo 09 – Versão, posições de 37 a 39, deve ser gerado com a versão “310”, “320”, “330”\.

__OS4620__

__MFS\_3385__

__RN71__

__Registro R01__

Quando a geração do arquivo for de um período maior ou igual a agosto de 2014, a estrutura do registro R01 deve ser alterada para demonstrar, depois do campo “13 – PJ com Débitos de SCP a serem Declarados”, na posição 59, a estrutura abaixo indicada:

__Ordem__

__Campo__

__Início__

__Fim__

__Tam__

__Form\.__

__Origem__

14

Empresa optante pelo Simples Nacional

59

59

1

N

Campo “Empresa Optante pelo Simples Nacional” de Dados Iniciais\*\.

15

PJ optante pela CPRB

60

60

1

N

Campo “PJ Optante pelo CPRB” de Dados Iniciais\*\.

16

Critério de Reconhecimento das Variações Monetárias dos Direitos de Crédito e das Obrigações do Contribuinte, em Função da Taxa de Câmbio

61

61

1

N

Campo “Critério de Reconhecimento das Variações Monetárias dos Direitos de Crédito e das Obrigações do Contribuinte, em Função da Taxa de Câmbio” de Dados Iniciais\*\.

17

Reservado

62

73

12

Zero\(s\)

Preencher com zeros até completar a posição\.

18

Regime de Apuração da Contribuição para o PIS/Pasep e da Cofins

74

74

1

N

Campo “Regime de Apuração da Contribuição para o PIS/Pasep e da Cofins” de Dados Iniciais\*\.

19

Situação da PJ no mês da declaração

75

75

1

N

Campo “Situação da PJ no mês da declaração” de Dados Iniciais\*\.

20

Opções referentes à Lei 12\.973/2014 para o ano\-calendário de 2014

76

76

1

N

Campo “Opções referentes à Lei 12\.973/2014 para o ano\-calendário de 2014” de Dados Iniciais\*\.

21

Reservado

77

86

10

Branco\(s\)

Preencher com brancos até completar a posição\.

22

Delimitador do registro

87

88

2

EOL

EOL

Obs: nas versões anteriores à “330” da DCTF os campos 14 e 15 que foram incluídos agora eram representados pelo campo 13, um tipo Reservado de 2 posições\.

\* Acesso à tela de Dados Iniciais:

__Módulo:__ Federal >> Obrigações de Tributos Federais

__Menu:__ Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Dados Iniciais >> 

Por Empresa __OU __Por Estabelecimento

__OS4620__

__MFS\_3385__

__RN72__

__Registro R02__

Quando a geração do arquivo for de um período maior ou igual a agosto de 2014, os campos “16 – Telefone” e “18 – FAX” passam a ser gerados com tamanho de 9 caracteres, consequentemente houve alteração da estrutura do registro a partir do campo “16 – Telefone”, pois as posições inicial e final dos campos subsequentes foram alteradas, conforme segue:

__Ordem__

__Campo__

__Início__

__Fim__

__Tam__

__Form\.__

16

Telefone

303

311

9

XN

17

DDD do Fax

312

315

4

XN

18

Fax

316

324

9

XN

19

Caixa Postal

325

330

6

XN

20

UF da Caixa Postal

331

332

2

X

21

CEP da Caixa Postal

333

340

8

XN

22

Correio Eletrônico

341

380

40

X

23

Reservado

381

390

10

Branco\(s\)

24

Delimitador de Registro

391

392

2

EOL

A informação dos campos telefone e fax continuam a ser geradas a partir do cadastro do estabelecimento, considerando as 9 primeiras posições do campo\.

__OS4620__

__RN73__

__Registro R03__

Quando a geração do arquivo for de um período maior ou igual a agosto de 2014, os campos “09 \- Telefone \- Representante”, “12 \- Fax \- Representante”, “19 \- Telefone \- Responsável” e “22 \- Fax \- Responsável” passam a ser gerados com tamanho de 9 caracteres, consequentemente houve alteração da estrutura do registro a partir do campo “09 \- Telefone \- Representante”, pois as posições inicial e final dos campos subsequentes foram alteradas, conforme segue:

__Ordem__

__Campo__

__Início__

__Fim__

__Tam__

__Form\.__

09

Telefone \- Representante

108

116

9

XN

10

Ramal \- Representante

117

121

5

XN

11

DDD do Fax \- Representante

122

125

4

XN

12

Fax \- Representante

126

134

9

XN

13

Correio Eletrônico \- Representante

135

174

40

X

14

Nome do Responsável

175

234

60

X

15

CPF \- Responsável

235

245

11

CPF

16

CRC \- Responsável

246

260

15

X

17

UF do CRC \- Responsável

261

262

2

X

18

DDD do Telefone \- Responsável

263

266

4

XN

19

Telefone \- Responsável

267

275

9

XN

20

Ramal \- Responsável

276

280

5

XN

21

DDD do Fax \- Responsável

281

284

4

XN

22

Fax \- Responsável

285

293

9

XN

23

Correio Eletrônico \- Responsável

294

333

40

X

24

Reservado

334

343

10

Branco\(s\)

25

Delimitador de Registro

344

345

2

EOL

A informação dos campos telefone e fax continuam a ser geradas a partir do cadastro do responsável, considerando responsáveis parametrizados em Dados Iniciais da obrigação e demonstrando as 9 primeiras posições do campo\.

__OS4620__

__RN74__

__Registro R14__

Quando a geração do arquivo for de um período maior ou igual a agosto de 2014, o campo “16 \- Motivo da Suspensão” será gerado com 2 caracteres, consequentemente houve alteração da estrutura do registro a partir do campo “16 \- Motivo da Suspensão”, pois as posições inicial e final dos campos subsequentes foram alteradas, conforme segue:

__Ordem__

__Campo__

__Início__

__Fim__

__Tam__

__Form\.__

16

Motivo da Suspensão

85

86

2

N

17

Depósito

87

87

1

N

18

Reservado

88

88

1

Zero\(s\)

19

Número do Processo

89

112

24

XN

20

Vara

113

114

2

XN

21

Município

115

164

50

X

22

UF

165

166

2

X

23

Identificação do Depósito

167

186

20

XN

24

Período de Apuração

187

194

8

DATA

25

CPF/CNPJ

195

208

14

CPF/CNPJ

26

Código da Receita

209

212

4

N

27

Data do Vencimento

213

220

8

DATA

28

Valor do Principal

221

234

14

R\+

29

Valor da Multa

235

248

14

R\+

30

Valor dos Juros

249

262

14

R\+

31

Reservado

263

272

10

Branco\(s\)

32

Delimitador de Registro

273

274

2

EOL

A origem deste campo é a tela de Pagamento de Débitos \(__Módulo:__ Federal >> Obrigações de Tributos Federais / __Menu:__ Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Pagamento de Débitos\), sendo considerado o Motivo da Suspensão associado ao tipo de pagamento Suspensão de Débito\. Este campo foi ajustado para gravar duas posições e seu conteúdo foi revisto, conforme solicitado pelo layout 3\.1\.

__OS4620__

__RN75__

__Registro R24__

Quando a geração do arquivo for de um período maior ou igual a agosto de 2014, o campo “16 \- Motivo da Suspensão” será gerado com 2 caracteres, consequentemente houve alteração da estrutura do registro a partir do campo “16 \- Motivo da Suspensão”, pois as posições inicial e final dos campos subsequentes foram alteradas, conforme segue:

__Ordem__

__Campo__

__Início__

__Fim__

__Tam__

__Form\.__

16

Motivo da Suspensão

85

86

2

N

17

Depósito

87

87

1

N

18

Reservado

88

88

1

Zero\(s\)

19

Número do Processo

89

112

24

XN

20

Vara

113

114

2

XN

21

Município

115

164

50

X

22

UF

165

166

2

X

23

Identificação do Depósito

167

186

20

XN

24

Período de Apuração

187

194

8

DATA

25

CPF/CNPJ

195

208

14

CPF/CNPJ

26

Código da Receita

209

212

4

N

27

Data do Vencimento

213

220

8

DATA

28

Valor do Principal

221

234

14

R\+

29

Valor da Multa

235

248

14

R\+

30

Valor dos Juros

249

262

14

R\+

31

Reservado

263

272

10

Branco\(s\)

32

Delimitador de Registro

273

274

2

EOL

A origem deste campo é a tela de Pagamento de Débitos \(__Módulo:__ Federal >> Obrigações de Tributos Federais / __Menu:__ Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Pagamento de Débitos\), sendo considerado o Motivo da Suspensão associado ao tipo de pagamento Suspensão de Débito\. Este campo foi ajustado para gravar duas posições e seu conteúdo foi revisto, conforme solicitado pelo layout 3\.1\.

__OS4620__

__RN76__

Quando a geração do arquivo for de um período maior ou igual a agosto de 2014, os Registros R13, R23 e R33 não devem ser gerados\.

__OS4620__

__RN77__

__Relatório de Conferência__

__Módulo__: Federal >> Obrigações de Tributos Federais

__Menu__: Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Meio Magnético – Declaração de Débito e Crédito >> Relatório de Conferência >> DCTF Mensal

O relatório de conferência deve ser ajustado para que seja possível a recuperação e demonstração do arquivo da DCTF na versão 3\.1, sobretudo no que diz respeito aos novos campos incluídos em “Dados Iniciais”\.

__OS4620__

__RN78__

__Registro R15__

Quando a geração do arquivo for de um período maior ou igual a agosto de 2014, a estrutura do registro R15 deve ser alterada para demonstrar a partir do campo 15 da seguinte forma:

__Ordem__

__Campo__

__Início__

__Fim__

__Tam__

__Form\.__

15

Número do Processo

71

91

21

NPADM

16

Valor Parcelado do Débito

92

105

14

R\+

17

Reservado

106

115

10

Branco\(s\)

18

Delimitador de Registro

116

117

2

EOL

__Módulo:__ Federal >> Obrigações de Tributos Federais

__Menu:__ Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Dados Iniciais >> 

Por Empresa __OU __Por Estabelecimento

__MFS3385__

__RN79__

__Registro R25__

Quando a geração do arquivo for de um período maior ou igual a agosto de 2014, a estrutura do registro R25 deve ser alterada para demonstrar a partir do campo 15 da seguinte forma:

__Ordem__

__Campo__

__Início__

__Fim__

__Tam__

__Form\.__

15

Número do Processo

71

91

21

NPADM

16

Valor Parcelado do Débito

92

105

14

R\+

17

Reservado

106

115

10

Branco\(s\)

18

Delimitador de Registro

116

117

2

EOL

__Módulo:__ Federal >> Obrigações de Tributos Federais

__Menu:__ Outras Obrigações >> DCTF >> DCTF Mensal \(a partir de 01/01/2006\) >> Dados Iniciais >> 

Por Empresa __OU __Por Estabelecimento

__MFS3385__

__RN80__

Ao gerar a DCTF por “Retenções” ou “DARF’s”, o sistema deverá considerar todos os lançamentos fichas da DCTF, pelos códigos DARFs selecionado na tela Código do DARF do módulo: Data Warehouse >>Menu: Manutenção >> Códigos >> Código do DARF

Incluir a mensagem de atenção: Para a geração da DCTF é necessário a parametrização dos Códigos Darfs no Módulo: Data Warehouse >>Menu: Manutenção >> Códigos >> Código do DARF

__MFS\-644857__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

