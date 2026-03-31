# MTZ-ICMS-Relatorio_Sub_Apuracao_Totais_Doctos_Eletronicos

- **Fonte:** MTZ-ICMS-Relatorio_Sub_Apuracao_Totais_Doctos_Eletronicos.docx
- **Modificado:** 2025-01-30
- **Tamanho:** 84 KB

---

THOMSON REUTERS

Módulo ICMS – Sub Apurações 

Relatório dos Totais dos Documentos Eletrônicos \(Ap\. Assistida – RS\)

__Localização__: Menu Estadual, módulo ICMS, menu Apuração <a id="OLE_LINK28"></a><a id="OLE_LINK32"></a>🡪 Sub Apurações do SPED  Fiscal 🡪 Relatórios 🡪 Totais dos Documentos Eletrônicos \(Ap\. Assistida – RS\) 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS36420__

Relatório de Conferência dos Totais dos Documentos Eletrônicos

Criação do relatório de conferência dos valores dos documentos eletrônicos

06/05/2020

Sumário

[1\.	Regras Gerais	2](#_Toc39748722)

[2\.	Layout da Tela	2](#_Toc39748723)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc39748724)

[4\.	Recuperação dos Dados	5](#_Toc39748725)

[5\.	Layout	5](#_Toc39748726)

[6\.	Preenchimento dos Campos	5](#_Toc39748727)

# <a id="_Toc39748722"></a>Regras Gerais

Este relatório tem por objetivo demonstrar os totais dos documentos eletrônicos referentes ao regime especial do RS \(projeto “Apuração Assistida – RS”\)\. 

Os valores destes documentos são totalizados e armazenados em tabelas durante a geração das sub\-apurações, e posteriormente, serão gerados no Sped Fiscal como ajustes \(E111\) e valores declaratórios \(E115\)\. 

Trata\-se dos ajustes e valores declaratórios gerados a partir dos documentos eletrônicos *não *escriturados no registro C100 do Sped Fiscal, conforme orienta o regime especial do RS, referente ao projeto “Apuração Assistida – RS”\.

A princípio, o regime especial abrange apenas as notas de consumidor eletrônica \(NFC\-e\. Mod 65\), por isso os lançamentos que serão demonstrados no relatórios totalizam apenas os valores destas notas\.

- Os totais do ICMS destas notas são gerados por CFOP, e no Sped Fiscal originam registros E111;
- Os totais do valor contábil também são gerados por CFOP, e no Sped Fiscal originam registros E115;

# <a id="_Toc39748723"></a>Layout da Tela

*Obs: O modelo da tela segue o padrão do relatório das Sub\-Apurações \(menu “Relatórios > Sub Apurações”\), mas não tem o campo “UF”, já que trata\-se de regime especial do RS, e portanto, somente estabelecimento do RS poderão ter estes valores calculados\.  *

   Data da Apuração: 99/99/9999

   \[   \]  Inscrição Estadual Única

   Estabelecimentos:                                                                                                             

   \[   \]  XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       <Selecionar todos>

   \[   \]  XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       <Desmarcar todos>

   \[   \]  XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

   \[   \]  XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

   \[   \]  XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# <a id="_Toc39748724"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato / Default__

__Regra__

Data da Apuração 

Data

S

S

\(DDMMAAAA\)

Neste campo o usuário informará a data da apuração para a emissão do relatório\.

Deve ser uma data válida\.

Inscrição Estadual Única

   Checkbox 

   N

   N

Default = desmarcado

Este campo indica se a geração das sub\-apurações é realizada por Inscrição Estadual Única ou não, e serve para o filtro dos estabelecimentos no quadro “Estabelecimentos”, da seguinte forma:

Quando marcado, serão exibidos *apenas* os estabelecimentos centralizadores \(conforme a parametrização da Inscrição Estadual Única no módulo “Controle das Obrigações Estaduais”\); 

Quando desmarcado, serão exibidos todos os estabelecimentos;

Estabelecimentos

Alfanumérico 

__     __S 

S

Neste campo é exibida a lista dos estabelecimentos para seleção do usuário\. Serão disponibilizados apenas os estabelecimentos que atendam às seguintes condições:

\- Somente Estabelecimentos da empresa do login;

\- Somente Estabelecimentos da UF do __RS__;

\- Dependendo do campo “Inscrição Estadal Única”, serão

  exibidos apenas os estabelecimentos centralizadores; 

Selecionar todos

N

N

Esta opção é um facilitador que permite a marcação de todos os estabelecimentos simultaneamente\.    

Desmarcar todos

N

N

Esta opção é um facilitador que permite desmarcar todos os estabelecimentos simultaneamente\.    

	

# <a id="_Toc506457465"></a><a id="_Toc39748725"></a>Recuperação dos Dados

Será gerado um relatório para cada estabelecimento selecionado em tela\.

O relatório exibirá, para cada estabelecimento, os totais do ICMS e os totais do valor contábil das notas eletrônicas \(a princípio, serão apenas as notas de consumidor eletrônica, Mod 65, conforme já citado nas regras gerais acima\)\.

Origem dos dados: Estes valores são originados de tabelas diferentes, da seguinte forma:

Totais do ICMS 

Tabela dos Valores de ICMS dos Documentos Eletrônicos

Totais do valor contábil

Tabela das Informações Adicionais \(Valores Declaratórios\) do Sped Fiscal \(EFD\_REG\_E115\)

Em cada uma destas tabelas, os valores são totalizados e armazenados por CFOP, desta forma, o volume de dados de cada estabelecimento é bem pequeno, já que serão apenas os CFOP’s específicos de cada tipo de documento eletrônico\. 

Critérios da recuperação dos dados para as duas tabelas:

__Tabela__

__Critérios para recuperação dos dados__

Tabela dos Valores de ICMS dos Documentos Eletrônicos

\- Código Empresa = código da empresa do login;

\- Código Estabelecimento = código do estabelecimento selecionado em tela;

\- Data Apuração = data da apuração informada em tela 

\- Tipo da Apuração = “0” \(indica Apuração “normal”\)

\- Registro = “E111”;

Tabela das Informações Adicionais \(Valores Declaratórios\) do Sped Fiscal \(EFD\_REG\_E115\)

\- Código Empresa = código da empresa do login;

\- Código Estabelecimento = código do estabelecimento selecionado em tela;

\- Data Final  do Período = data da apuração informada em tela 

\- Código da Informação Adicional = código de informação adicional parametrizado 

   no Sped Fiscal, menu “Parâmetros > Apuração Assistida – RS”, campo “Valor 

   Declaratório do Total das NFC\-e \(E115\)” \(quadro “Apuração Assistida – RS”\)\.

Para recuperar a parametrização, considerar o estabelecimento da geração\.

*\(Não é necessário verificar a existência da parametrização, pois este procedimento  já é feito no momento de gerar estes valores, durante o processo de Geração das Sub\-Apurações\)*

Obs\.: Esta é a tabela “oficial” do Sped para as informações adicionais do registro E115\. Por isso, é necessário filtrar também pelo Código de Informação Adicional, que será um código específico para esta finalidade\.

Os dados recuperados das duas tabelas, serão demonstrados no relatório, seguindo o layout e as regras de preenchimento dos campos definidos nos itens a seguir:

# <a id="_Toc39748726"></a>Layout

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                                                           Data: 99/99/9999        Página: 9999

Filial: XXXXXX – XXXXXXXXXXXXXXXXXXXXXXXX                                                Insc\.Estadual: XXXXXXXXXXXXXX   CNPJ: XXXXXXXXXXXXXX

                                                 Totais dos Documentos Eletrônicos \(Ap\. Assistida – RS\) 

                                                                  Data da Apuração: 99/99/9999

__Totais do ICMS \(E111\)__:

	

  Código de Ajuste                                               Descrição Complementar                                                     Valor

         XXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    999\.999\.999\.999,99

         XXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    999\.999\.999\.999,99

         XXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    999\.999\.999\.999,99

         XXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    999\.999\.999\.999,99

                    

                                                                                                                                                                        __Total do ICMS:__  999\.999\.999\.999,99

__Totais do Valor Contábil \(E115\)__:

 Código Inf\. Adicional                                            Descrição Complementar                                                    Valor

         XXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    999\.999\.999\.999,99

         XXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    999\.999\.999\.999,99

         XXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    999\.999\.999\.999,99

         XXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    999\.999\.999\.999,99

                                                                                                                                                        __Total do Valor Contábil:__  999\.999\.999\.999,99

	                   

<a id="_Toc39748727"></a>

# Preenchimento dos Campos

Linhas de cabeçalho:

Primeira de cabeçalho

Informações desta linha: 

\- Razão social da empresa;

\- Data da emissão do relatório;

\- Número da página;

Segunda linha de cabeçalho

Informações desta linha: 

\- Campo “Filial” – Código e razão social do estabelecimento em questão;

\- Inscrição estadual do estabelecimento na sua UF;

\- CNPJ do estabelecimento; 

Terceira linha de cabeçalho

\- Título do relatório: “Totais dos Documentos Eletrônicos \(Ap\. Assistida – RS\)”; 

Quarta linha de cabeçalho

\- Data da Apuração informada em tela;

	

Linhas sob o título: __“Totais  do ICMS \(E111\)”__

Código de Ajuste

Código de Ajuste da Tabela dos Valores de ICMS dos Documentos Eletrônicos

Descrição Complementar

Descrição da Tabela dos Valores de ICMS dos Documentos Eletrônicos

Valor

Valor da Tabela dos Valores de ICMS dos Documentos Eletrônicos

Linha __“Total do ICMS”__: 

   Nesta linha será demonstrado o total da coluna “Valor” de todas as linhas de total do ICMS\.

	

Linhas sob o título: __“Totais  do Valor Contábil \(E115\)”__

Código Inf\. Adicional

Código de Informação Adicional da Tabela das Informações Adicionais \(Valores Declaratórios\) do Sped Fiscal

Descrição Complementar

Descrição da Tabela das Informações Adicionais \(Valores Declaratórios\) do Sped Fiscal

Valor

Valor da Informação Adicional da Tabela das Informações Adicionais \(Valores Declaratórios\) do Sped Fiscal

Linha __“Total do Valor Contábil”__: 

   Nesta linha será demonstrado o total da coluna “Valor” de todas as linhas de total do Valor Contábil\.

= = = = = =

