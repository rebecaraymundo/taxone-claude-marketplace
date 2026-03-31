# MTZ-CIAP-Manutencao_Dados_do_Calculo_Mod_C

- **Fonte:** MTZ-CIAP-Manutencao_Dados_do_Calculo_Mod_C.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 64 KB

---

THOMSON REUTERS

                                                                        __Módulo Ativo Permanente \(CIAP\)__

__ __

__                                           Manutenção dos Dados do Cálculo – Modelo C__

__Localização__: Menu Estadual, Módulo: CIAP, menu Movimento 🡪 Manutenção Dados de Cálculo 🡪 Modelo C 🡪 Cálculo Geral dos Créditos

__Localização__: Menu Estadual, Módulo: CIAP, menu Movimento 🡪 Manutenção Dados de Cálculo 🡪 Modelo C 🡪 Demonstrativo das Bases de Crédito

__Localização__: Menu Estadual, Módulo: CIAP, menu Movimento 🡪 Manutenção Dados de Cálculo p/ Inscrição Estadual –PIM  🡪 Cálculo Geral dos Créditos

__Localização__: Menu Estadual, Módulo: CIAP, menu Movimento 🡪 Manutenção Dados de Cálculo p/ Inscrição Estadual –PIM  🡪 Demonstrativo das Bases de Crédito

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4459

Alteração Modelo C \(frações diferenciadas\)

Alterações no Modelo C para mostrar os resultados separados por fração \(IN50 e Ajuste SINIEF\)  \(__RN03__ e __RN04__\)

08/04/2014

\(criação do Doc\)

REGRAS DE NEGÓCIO

__RN00__

__Regras gerais__

Os dados gerados no cálculo do CIAP do Modelo C podem ser consultados da seguinte forma:

__No menu “Cálculo Geral dos Créditos”:__

Neste menu são exibidos os valores totais calculados para o período\.

Tabelas: APT\_DEM\_CR\_MENSAL ou APT\_DEM\_CR\_MENSAL\_IES \(no caso de geração p/IE\-PIM\)

__No menu “Demonstrativo das Bases de Crédito”:__

Neste menu são exibidos os valores calculados para cada Bem\.

Tabelas: APT\_DEM\_BASE\_CR ou APT\_DEM\_BASE\_CR\_IES \(no caso de geração p/IE\-PIM\)

__RN01__

__Menu “Cálculo Geral dos Créditos”__  \(valores do resultado do período\)

Campo “__Fração__”__ __*–*__ __Campo criado na __OS4459__ para compor a chave da tabela que contém o resultado do período \(tabelas

APT\_DEM\_CR\_MENSAL ou APT\_DEM\_CR\_MENSAL\_IES\)\. Campo numérico de 2 posições, de preenchimento obrigatório\.

Campo “__Total Geral do Crédito do Período \(EFD – Bloco G\)__” – Neste campo é exibido o total geral do CIAP, calculado de acordo com as regras do Bloco G\. Seu conteúdo é sempre o total geral do CIAP, independente de existir no período mais de uma linha de resultado, separados por fração\. Nestes casos, como este valor é o valor final do CIAP, o valor apresentado será sempre o mesmo para todos os registros de resultado do período, de diferentes frações\.

__RN02__

__Menu “Demonstrativo das Bases de Crédito__”  \(valores gerados para cada Bem\)

Campo “__Fração__”__ __*–*__ __Campo criado na __OS4459__\. Neste campo é exibida a fração referente ao Bem em questão \(campo

                               N\.CIAP\)\. Campo numérico de 3 posições, de preenchimento *não* obrigatório\.

