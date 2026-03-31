# MTZ-OTF-Emitir_Informe_de_Rendimentos_por_Nome

- **Fonte:** MTZ-OTF-Emitir_Informe_de_Rendimentos_por_Nome.docx
- **Modificado:** 2021-10-07
- **Tamanho:** 38 KB

---

# Módulo – Obrigações de Tributos Federais 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3133

Obrigações de Tributos Federais \- Gerar Informes de Rendimento de Funcionários Demitidos e Não Demitidos

O objetivo dessa OS é criar um parâmetro na geração dos Informes de Rendimento por Nome e por Código para que o cliente possa definir se serão gerados Informes de Rendimento de funcionários Demitidos ou Não Demitidos\. Esse parâmetro já existe hoje na geração dos Informes de Rendimento por Centro de Custo\.

OS3532

Obrigações de Tributos Federais – Gerar Informes de Rendimento de Funcionários de acordo com a IN RFB nº 1\.215, de 15/12/2011 \(Rendimentos Recebidos Acumuladamente\) criados a partir da DIRF 2012

Trata\-se do INFOLEGIS 251/11 A  que disponibiliza as alterações para o Informe de Rendimentos relacionado à DIRF 2012\.

OS3878

Obrigações de Tributos Federais – Emissão de Informe de Rendimentos por Código e Nome

O objetivo dessa O\.S contemplará a habilitação dos campos “Funcionário Inicial e Funcionario Final” tanto da tela “Emissão De Declaração de Rendimento – Por Código” quanto na tela “Emissão De Declaração de Rendimento – Por Nome”\.

Como escopo da atualização, teremos:

- Criar uma regra para que os campos “Funcionario Inicial e Funcionário Final” sejam habilitados mesmo que os campos “Empresa e Estabelecimento” estejam em “Todos”\. Essa regra contemplará as telas “Emissão De Declaração de Rendimento – Por Código” e “Emissão De Declaração de Rendimento – Por Nome”\.

OS4700

Alteração rodapé referente à Instrução Normativa 1\.522, de 05 de dezembro de 2014\.

Alteração do rodapé referente à Instrução Normativa para seguinte descrição 2014:

Aprovado pela Instrução Normativa RFB nº 1\.522, de 05 de dezembro de 2014, para Rendimentos Outros e Empregados\.

MFS8975

Informe de Rendimento DIRF2017

Alteração no quadro 3 linha 3 e quadro 5 linhas 1 e 2\. 

Alteração do Rodapé\.

CH24840\_2017 \(MFS\-15649\)

Alteração do Quadro 6 – Rendimentos Recebidos Acumuladamente

Este documento tem como objetivo alterar a geração do Quadro 6 – Rendimentos Recebidos Acumuladamente, para considerar o registro do funcionário independente se houver movimentação financeira, atendendo o cenário em que podem ocorrer pagamentos efetuados por processos trabalhistas após a última movimentação financeira do empregado\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Deverá ser criado o flag “Emitir Funcionários Demitidos” na tela de emissão dos Informes de Rendimento por Nome\. 

Por default esse flag deve ficar SELECIONADO\. 

__OS3133__

__RN02__

A regra para a geração dos Informes de Rendimentos através desse flag é a seguinte:

- Caso o flag “Emitir Funcionários Demitidos” esteja SELECIONADO, devem ser recuperados os Informes de TODOS os funcionários que estejam trabalhando ou não na empresa\. Nesse caso devem ser recuperados os funcionários ativos e os demitidos, para tanto o campo “Data Demissão” do Cadastro de Funcionários \(menu: Manutenção >> Cadastros >> Controle de Funcionário >> Funcionários\) do módulo DW poderá estar preenchido ou não preenchido\.
- Caso o flag “Emitir Funcionários Demitidos” esteja DESMARCADO, devem ser recuperados os Informes dos funcionários que estejam trabalhando na empresa\. Nesse caso devem ser recuperados os funcionários ativos, para tanto o campo “Data Demissão” do Cadastro de Funcionários \(menu: Manutenção >> Cadastros >> Controle de Funcionário >> Funcionários\) do módulo DW não deverá estar preenchido\.

__OS3133__

__RN03__

O layout do Informe de Rendimentos deverá ser alterado para que fique igual ao layout proposto pela RFB através da IN RFB 1\.215, de 15 de Dezembro de 2011\.

O layout está disponibilizado no documento de requisito da OS3532\.

__OS3532__

__RN04__

No logotipo do Ministério da Fazenda – Secretaria da Receita Federal, o texto “SECRETARIA DA RECEITA FEDERAL” deverá ser alterado para “SECRETARIA DA RECEITA FEDERAL DO BRASIL”\.

__OS3532__

__RN05__

Abaixo do novo texto – SECRETARIA DA RECEITA FEDERAL DO BRASIL – deverá ser incluído o texto “Imposto sobre a Renda da Pessoa Física”\.

__OS3532__

__RN06__

No lado direito ao logo, o texto “COMPROVANTE DE RENDIMENTOS PAGOS E DE RETENÇÃO DE IMPOSTO DE RENDA NA FONTE” deverá ser alterado para “COMPROVANTE DE RENDIMENTOS PAGOS E DE IMPOSTO SOBRE A RENDA RETIDO NA FONTE”\.

__OS3532__

__RN07__

Antes do quadro 1 – Fonte Pagadora Pessoa Jurídica ou Física, deverá ser incluído um quadro uma mensagem no Informe de Rendimentos com a seguinte informação:

__“Verifique as condições e o prazo para a apresentação da Declaração do Imposto sobre a Renda da Pessoa Física para este ano\-calendário no sítio da Secretaria da Receita Federal do Brasil na Internet, no endereço <__[__www\.receita\.fazenda\.gov\.br__](http://www.receita.fazenda.gov.br)__>\.”__

__OS3532__

__RN08__

No quadro 1 – Fonte Pagadora Pessoa Jurídica ou Física, o campo “Nome Empresarial/Nome” deverá ser alterado para “Nome Empresarial/Nome Completo”\.

__OS3532__

__RN09__

Os campos “CNPJ/CPF” e “Nome Empresarial/Nome Completo” do quadro 1 – Fonte Pagadora Pessoa Jurídica ou Física, deverão ser invertidos de ordem\.

__OS3532__

__RN10__

Os campos “Endereço”, “Cidade”, “UF” e “Telefone”, deverão ser excluídos do quadro 1 – Fonte Pagadora Pessoa Jurídica ou Física\.

__OS3532__

__RN11__

O campo “Descrição do Rendimento” do quadro 2 – Pessoa Física Beneficiária dos Rendimentos deverá ter sua descrição alterada para “Natureza do Rendimento”\.

__OS3532__

__RN12__

O quadro “3 – Rendimentos Tributáveis, Deduções e Imposto Retido na Fonte” deverá ter sua descrição alterada para “3 – Rendimentos Tributáveis, Deduções e Imposto sobre a Renda Retido na Fonte”\.

__OS3532__

__RN13__

Os quadros “Informações Complementares” e “Responsável pelas Informações” deverão ter suas numerações alteradas, devido à entrada do quadro “6 – Rendimentos Recebidos Acumuladamente – Art\. 12\-A da Lei nº 7\.713, de 1988 \(sujeitos à tributação exclusiva\)”\.

__OS3532__

__RN14__

Deverá ser criado o quadro 6 – Rendimentos Recebidos Acumuladamente, logo após o quadro 5 – Rendimentos sujeitos à Tributação exclusiva \(rendimento líquido\)\.

__OS3532__

__RN15__

O quadro “6 – Rendimentos Recebidos Acumuladamente” será um quadro cujas informações de rendimentos não serão parametrizáveis como o restante do Informe de Rendimentos – vide parametrização por Verba do módulo Obrigações de Tributos Federais\. 

__OS3532__

__RN16__

Para que as informações do quadro 6 – Rendimentos Recebidos Acumuladamente sejam geradas e exibidas, o seguinte critério de filtro deverá ser realizado:

__\[ALTERADA \- CH24840\_2017 \(MFS\-15649\)\]__

1. Ao gerar os Informes de Rendimento através das rotinas de “Geração de Dados” \(menu: Rendimentos >> Rendimentos Empregados >> Geração dos Dados\) e “Geração de Dados por Funcionário” \(menu: Rendimentos >> Rendimentos Empregados >> Geração dos Dados por Funcionário\), o sistema irá gerar as informações dos funcionários para o Ano Calendário informado;
2. Ao gerar as informações do Funcionário da SAFX15 \(recuperando em que não são necessárias as informações das verbas pela SAFX21, pois podem ocorrer pagamentos efetuados por processos trabalhistas após a última movimentação financeira do empregado\), o sistema irá verificar se esse Funcionário possui registro para o Ano Calendário informado na tabela SAFX181\. Caso existam informações, o quadro 6 – Rendimentos Recebidos Acumuladamente gera com os valores informados nessa tabela\.

Caso não existam informações do Funcionário no Ano Calendário informado na tabela SAFX181, o quadro 6 – Rendimentos Recebidos Acumuladamente gera com valores zerados \(ex: 0,00\)\.

Caso um mesmo Funcionário/Beneficiário possua mais de um registro na tabela SAFX181, o sistema deverá gerar outro quadro – denominado de 6\.2 – Número do Processo \(para os Rendimentos Recebidos Acumuladamente\) com essas informações\. Para cada registro existente desse mesmo Funcionário/Beneficiário na SAFX181 os quadros serão criados um após o outro na seqüência \(ex: 6\.1, 6\.2, 6\.3, etc\.\)\.

Caso um Funcionário/Beneficiário possua mais de um registro cujo campo XXXX = Pago pelo Declarante, a quebra do quadro 6 – Rendimentos Recebidos Acumuladamente será realizada pelo campo “Natureza do Rendimento”\.

__OS3532__

__CH24840\_2017 \(MFS\-15649\)__

__RN17__

As informações dos rendimentos pertencentes ao quadro 6 – Rendimentos Recebidos Acumuladamente serão recuperadas da seguinte maneira:

- __6\.1 Número do Processo:__ essa informação deverá ser recuperada a partir do campo “Número do Processo/Requerimento” da SAFX181\.
- __Quantidade de Meses:__ esse campo deverá ser informado com o somatório do campo “Quantidade de Meses” da SAFX181\.
- __Natureza do Rendimento:__ essa informação deverá ser recuperada a partir do campo “Natureza de Rendimento recebido acumuladamente” da SAFX181\.

Após exibir as informações básicas dos rendimentos recebidos acumuladamente, deverá ser informado as informações pertinentes aos rendimentos recebidos acumuladamente:

- __1 – Total dos rendimentos tributáveis \(inclusive férias e décimo terceiro salário\): __esse campo deverá ser informado com o somatório da coluna “Rendimentos Tributáveis” da SAFX181\.
- __2 – Exclusão: despesas com ação judicial:__ esse campo deverá ser informado com o somatório da coluna “Despesas Ação Judicial” da SAFX181\.
- __3 – Dedução: Contribuição previdenciária oficial:__ esse campo deverá ser informado com o somatório da coluna “Previdência Oficial” da SAFX181\.
- __4 – Dedução: Pensão alimentícia \(preencher também o quadro 7\): __esse campo deverá ser informado com o somatório da coluna “Pensão Alimentícia” da SAFX181\.
- __5 – Imposto sobre a renda retido na fonte: __esse campo deverá ser informado com o somatório da coluna “Imposto Retido” da SAFX181\.
- __6 – Rendimentos isentos de pensão, proventos de aposentadoria ou reforma por moléstia grave ou aposentadoria ou reforma por acidente em serviço: __esse campo deverá ser informado com o somatório da coluna “Rendimentos Isentos Moléstia Grave” da SAFX181\.

__OS3532__

__RN18__

O rodapé do quadro 8 – Responsável pelas Informações deverá ser preenchido com o seguinte texto, caso o campo “Ano Base” seja igual a 2011:

“Aprovado pela IN RFB nº 1\.215, de 15 de novembro de 2011”

__OS3532__

__RN19__

O parâmetro “Imprimir Endereço do Remetente e Destinatário no verso do Informe de Rendimentos” deverá ser inibido da tela de Emissão do Informe de Rendimentos, devido o observado durante o desenvolvimento/homologação da OS3532\.

Ao inibir o parâmetro, essa funcionalidade não poderá ser utilizada\. Vale salientar que essa alteração é em caráter provisório, até que a funcionalidade do parâmetro seja revista\.

__CH3878/2012__

__RN20__

Se selecionar Todas "Empresas" e todos "Estabelecimentos" e o ano:

\- Habilitar o campo "Funcionário Inicial"\.

\- Habilitar o campo "Funcionário Final"\.

Obs: serão  recuperados todos os funcionários de todos os estabelecimentos e e todas as empresas\.

Caso existam um mesmo funcionário com datas de validade distintas, recuperar sempre o mais atual de acordo com o ano informado no campo ano na emissão da geração do informe de rendimento\.

__OS3878__

__RN21__

Se selecionar uma "Empresa" e todos "Estabelecimentos" habilitar:

\- Habilitar o campo "Funcionário Inicial"\.

\- Habilitar o campo "Funcionário Final"\.

Obs: serão recuperados todos os funcionários de todos os estabelecimentos da empresa selecionada\.

Caso existam um mesmo funcionário com datas de validade distintas, recuperar sempre o mais atual de acordo com o ano informado no campo ano na emissão da geração do informe de rendimento\.

__OS3878__

__RN28__

O rodapé do quadro 8 – Responsável pelas Informações deverá ser preenchido com o seguinte texto, caso o campo “Ano Base” seja igual a 2014:

“Aprovado pela IN RFB nº 1\.522, de 05 de dezembro de 2014”

\[MFS8975\]

Caso ano base for igual a 2016:

“Aprovado pela Instrução Normativa RFB n° 1682, de dezembro de 2016”

__OS4700__

__MFS8975__

__RN29__

Bloco 3 – \(Rendimentos Tributáveis, Deduções e Imposto sobre a Renda Retido na Fonte\)\. 

Alterar a linha 3 com a seguinte descrição: 

“Contribuição a entidade de previdência complementar, pública ou privada e a fundos de aposentadoria Programada individual \(Fapi\) \{Preencher também o quadro 7\}”

__MFS8975__

__RN30__

Bloco 5 – \(Rendimento Sujeitos à Tributação Exclusiva\)\. 

Alterar as linhas 1 e 2 com a seguintes descrições respectivamente: 

13° \(Décimo terceiro\) salário

Imposto sobre a renda retido na fonte sobre 13° \(décimo terceiro\) salário\.

__MFS8975__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

