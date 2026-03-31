# MTZ-OTF-Dados_Iniciais

- **Fonte:** MTZ-OTF-Dados_Iniciais.docx
- **Modificado:** 2026-03-05
- **Tamanho:** 40 KB

---

# Módulo – OTF – DCTF

Dados Iniciais

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3299

DCTF \- Gerar versão 1\.9 da DCTF

Esse documento tem como objetivo alterar a geração da DCTF para que a mesma passe a atender a nova versão 1\.9 disponibilizada\.

OS3941

Obrigações de Tributos Federais – Gerar DCTF com Número de Referência do DARF

O cliente BNDES gera a DCTF a partir do módulo Obrigações de Tributos Federais do produto Mastersaf DW\. Ocorre que o cliente alega que o Número de Referência do DARF, informado no próprio DARF, deveria constar na DCTF e não o Número de Referência automático gerado pelo produto\.

Verificamos que esse Número de Referência automático gerado pelo sistema funciona como uma espécie de ID para amarrar as informações, logo a solução que está sendo proposta é a criação de um parâmetro para que o cliente opte por gerar essa informação\.

Caso o cliente opte por não informar esse Número de Referência no DARF – que originalmente vem do Controle de Tributos – a informação não deverá ser informada na DCTF conforme base legal informada pelo cliente\.

OS4259

Obrigações de Tributos Federais – Gerar Campo 19 do Registro R10 da DCTF a partir do Código de Receita

O objetivo dessa OS é permitir que os débitos de SCP/INC/Demais que são gerados no campo 19 – Débito de SCP/INC da Ficha 10 – Débito Apurado e Créditos Vinculados tenham correlação com o Código de Receita gerado nessa ficha\.

OS4620

DCTF – Ajustes versão 3\.1

Ajustar a parametrização da DCTF de modo que atenda ao solicitado na versão 3\.1 do layout da obrigação\.

CH21391\_2014

Geração do campo 19 do registro R10 

Ajuste na regra do parâmetro “Débitos de SCP a partir da parametrização de SCP/INC para a Ficha R10”\.

OS4741

DCTF – Ajustes versão 3\.2

Ajustar a parametrização da DCTF de modo que atenda ao solicitado na versão 3\.2 do layout da obrigação\.

MFS3385

DCT\- Ajustes Versao 3\.3

Ajustar a parametrização da DCTF de modo que atenda ao solicitado na versão 3\.3 do layout da obrigação\.

MFS11919

DCTF\- Ajustes Versao 3\.4

Ajustar a parametrização da DCTF de modo que atenda ao solicitado na versão 3\.4 do layout da obrigação\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__PJ com Débitos de INC a serem Declarados__

Esse campo deve ser um checkbox com as seguintes opções:

0, quando o campo estiver desmarcado

1, quando o campo estiver marcado

Quando esse campo estiver marcado, o campo PJ com Débitos de SCP a serem Declarados deve ser desmarcado\. E vice\-versa\.

__OS3299__

__RN02__

PJ iniciou atividades no mês da declaração

Esse campo deve ser um checkbox com as seguintes opções:

0, quando o campo estiver desmarcado

1, quando o campo estiver marcado

\[__OS4620__\] Se o Mês e o Ano forem maior ou igual a Agosto de 2014 este campo deve estar desabilitado\.

__OS3299__

__OS4620__

__RN03__

__Meses com ausência de débito a declarar__

Janeiro: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Fevereiro: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Março: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Abril: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Maio: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Junho: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Julho: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Agosto: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Setembro: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Outubro: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Novembro: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Dezembro: deve ser um checkbox e deve ser as seguintes opções: 0, quando o campo estiver desmarcado e 1, quando o campo estiver marcado\.

Esses campos devem estar desabilitados por default\.

Se o campo Tipo Situação = “Não se Aplica \(Normal\)” e o Mês = “Dezembro”, todos os campos devem ser habilitados

Se o campo Tipo Situação <> “Não se Aplica \(Normal\)”, todos os campos devem ser habilitados

\[__OS4620__\] Se o Mês e o Ano forem maior ou igual a Agosto de 2014 este campo deve permanecer desabilitado\.

__OS3299__

__OS4620__

__RN04__

__Critério de Reconhecimento das Variações Monetárias dos Direitos de Crédito e das Obrigações do Contribuinte em Função de Taxa de Câmbio: \(Campo 17 do layout\)__

__\[ALTERADA – MFS11919\]__

Deve ser um listbox e exibir as seguintes opções:

0 – Não se Aplica

1 – Caixa

2 – Competência

3 – Regime de Caixa – Portaria Ministerial

Campo tipo dropdownlist\. Quando o Mês e o Ano forem maior ou igual a Agosto de 2014, exibir as opções:

0 – Não preenchido 

1 – Regime de Caixa 

2 – Regime de Competência 

3 – Regime de Caixa – Portaria Ministerial Elevada oscilação da taxa de câmbio4 – Não se aplica 

5 – Sem alteração do regime

Default: "0" \- Não preenchido

__OS3299__

__OS4620__

__MFS11919__

__RN05__

__Regime de Apuração da Contribuição para o PIS/Pasep e/ou da Cofins: \(Campo 19 do layout\)__

__\[ALTERADA – MFS11919\]__

Deve ser um listbox e exibir as seguintes opções:

0 – Não se Aplica Não Preenchido

1 – Não Cumulativo

2 – Cumulativo

3 – Não Cumulativo e cumulativo

4 – Não se Aplica

__OS3299__

__MFS11919__

__RN06__

Deverá ser criado um parâmetro chamado “Considerar Número de Referência do DARF” na tela de Dados Iniciais do módulo Obrigações de Tributos Federais\.

Por default esse parâmetro deverá ficar desmarcado\. Caso o mesmo fique desmarcado a geração da DCTF irá considerar o campo NRO\_REFERENCIA da tabela X75\_DCTF ou NRO\_REFERENCIA\_X751 da tabela X751\_DCTF\_COMPL\. Caso o parâmetro esteja selecionado será considerado o NUM\_REF\_DARF da X75\_DCTF ou X751\_DCTF\_COMPL\.

__OS3941__

__RN07__

Deverá ser criado o parâmetro “Débitos de SCP a partir da Parametrização de SCP/INC para a Ficha R10” na tela parametrização de Dados Iniciais da DCTF\.

Por default esse parâmetro ficará desmarcado\. Caso o mesmo seja selecionado, os parâmetros “PJ com Débitos de SCP a serem Declarados” e “PJ com Débitos de INC a serem Declarados”  ficarão desabilitados, caso contrário, não\.

O parâmetro “Débitos de SCP a partir da Parametrização de SCP/INC para a Ficha R10” não deverá ser disponibilizado no relatório de conferência dessa tela

__OS4259__

__CH21391\_2014__

__RN08__

__PJ esteve inativa desde o início do ano\-calendário/data da sua constituição até o mês anterior ao desta DCTF__

\[__OS4620__\] Se o Mês e o Ano forem maior ou igual a Agosto de 2014 este campo deve estar desabilitado\.

__OS4620__

__RN09__

__PJ este obrigada à Apresentação da DCTF Semestral no Ano Anterior__

\[__OS4620__\] Se o Mês e o Ano forem maior ou igual a Agosto de 2014 este campo deve estar desabilitado\.

__OS4620__

__RN10__

__Situação da PJ no mês da declaração \(Campo 20 do layout\)__

__\[ALTERADA – MFS11919\]__

Campo do tipo dropdownlist com as opções:

"0" \- Não se aplica 

"1" \- PJ iniciou atividades teve sua inscrição no CNPJ efetivada ou entrou em atividade no mês da declaração 

"2" – PJ foi excluída do Simples no mês da declaração 

"3" \- Surgimento de nova PJ em razão de fusão ou cisão no mês da declaração 

"4" \- PJ não se enquadra em nenhuma das situações anteriores no mês da declaração

Default: "1" \- PJ teve sua inscrição no CNPJ efetivada ou entrou em atividade no mês da declaração

Este campo deve ser habilitado somente se Mês e o Ano forem maior ou igual a Agosto de 2014

__OS4620__

__MFS11919__

__RN11__

__Opções referentes à Lei 12\.973/2014 para o ano\-calendário de 2014 \(Campo 21 do layout\)__

__\[ALTERADA – MFS11919\]__

Campo tipo dropdownlist com as opções:

"0" \- Não se aplica Não Preenchido

"1" \- Aplicação das disposições contidas nos arts\. 1º e 2º e 4º a 70 

"2" \- Aplicação das disposições contidas nos arts\. 76 a 92 

"3" \- Aplicação das disposições contidas nos arts\. 1º e 2º e 4º a 70 e 76 a 92 

"4" \- Não optante

Default: "0" \- Não Preenchido

Este campo deve ser habilitado somente se Mês e o Ano forem maior ou igual a Agosto de 2014

__OS4620__

__MFS11919__

__RN12__

__Qualificação PF/PJ \(Campo 11 do layout\)__

__\[ALTERADA – MFS3385\]__

__\[ALTERADA – MFS11919\]__

Campo tipo dropdownlist com as opções:

“01” – Financeira Agências de Fomento e demais entidades elencadas no § 1° do art\. 22 da Lei n° 8\.212/1991

“02” \- Sociedade Seguradora e de Capitalização ou Entidade Aberta de Previdência Complementar \(com fins lucrativos\)

“03” \- Sociedade Corretora Autônoma de Seguros

“04” \- Cooperativa de Crédito

“05” \- Entidade Fechada de Previdência Complementar ou Entidade Aberta de Previdência Complementar \(sem fins lucrativos\)

“06” \- Sociedade Cooperativa

“07” \- PJ em Geral 

“08” \- Sociedade Cooperativa de Produção Agropecuária ou de Consumo

“09” – Autarquia ou Fundação Pública 

“10” – Estado, Distrito Federal, Município ou Órgão Público da Administração Direta

“11” – Empresa Pública, Sociedade de Economia Mista e demais PJ de que trata o inc\. III do art\. 34 da Lei nº 10\.833/2003

Quando o Mês e o Ano indicados forem maior ou igual a Agosto de 2014, exibir __também__ a opção:

“12” – Mais de uma qualificação durante o mês

__Default: __“01” \- Agências de Fomento e demais entidades elencadas no § 1° do art\. 22 da Lei n° 8\.212/1991

__OS4741__

__MFS3385__

__MFS11919__

__RN13__

__Empresa PJ Optante pelo Simples Nacional \(Campo 14 do layout\)__

__\[ALTERADA – MFS11919\]__

Esse campo deve ser um checkbox com as seguintes opções:

0, quando o campo estiver desmarcado

1, quando o campo estiver marcado

EXCECOES:

Desabilitar este campo quando o ano do fato gerador for menor que dezembro de 2015\.

Esta informação não constará no relatório, que deverá ser totalmente revisto posteriormente\.

__MFS3385__

__MFS11919__

__RN14__

__PJ Optante pelo CPRB \(Campo 15 do layout\)__

Esse campo deve ser um checkbox com as seguintes opções:

0, quando o campo estiver desmarcado

1, quando o campo estiver marcado

EXCECOES:

Desabilitar este campo quando o ano do fato gerador for menor que dezembro de 2015\.

Esta informação não constará no relatório, que deverá ser totalmente revisto posteriormente\.

__MFS3385__

__RN15__

__PJ inativa no mês da declaração \(Campo 16 do layout\) __

__\[ALTERADA – MFS11919\]__

Esse campo deve ser um checkbox com as seguintes opções:

0, quando o campo estiver desmarcado

1, quando o campo estiver marcado

EXCECOES:

Desabilitar este campo quando o ano do fato gerador for menor que 2016\.\.

__MFS11919__

__RN16__

__Tributação do Lucro \(campo 10 layout\)__

Campo tipo lista com as opções:

"0" – Real/Trimestral

"1" – Real/Estimativa

"2" – Presumido

"3" – Arbitrado

"4" – Imune do IRPJ

"5" – Isenta do IRPJ

__\[ALTERADA – MFS11919\]__

Incluir novas opções:

"8" – Declarante não é Contribuinte do IRPJ

"9" – Não preenchido

__Default: __"0" – Real/Trimestral

__MFS11919__

__RN17__

__Período__

__Data Inicial__: Campo preenchido automaticamente pelo sistema, assumido como padrão o primeiro dia do mês\. Pode ser alterado no caso de declarações especiais \(extinção, fusão etc\.\)

__Data Final__: Campo preenchido automaticamente pelo sistema assumindo como padrão o último dia do mês\. No caso de declarações especiais, é assumida a Data do Evento\.

__OS3299__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

