# Layout_4_0_ECF

- **Fonte:** Layout_4_0_ECF.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 37 KB

---

Layout 4\.0 \- ECF

__Data__

__MFS__

__Descrição__

__Autor__

26/02/2018

MFS\-16828

Criação do documento

Alessandra Cristina Navatta

Sumário

[1\.	Avaliação do Layout	2](#_Toc507581027)

[2\.	Atualização das tabelas	3](#_Toc507581028)

[1\.	Bloco 0	3](#_Toc507581029)

[2\.	Bloco W	4](#_Toc507581030)

[3\.	Bloco X	4](#_Toc507581031)

[4\.	Bloco Y	4](#_Toc507581032)

[5\.	Bloco V	5](#_Toc507581033)

[6\.	Bloco 9	6](#_Toc507581034)

[7\.	Atualização de Escrituração	6](#_Toc507581035)

[8\.	Integração ECD	6](#_Toc507581036)

[9\.	Considerações	6](#_Toc507581037)

# <a id="_Toc507581027"></a>Avaliação do Layout

A avaliação do layout 4\.0 foi realizada considerando as demandas já abertas no produto OneSource ECF, dentro dos sprints abaixo:

__R108 \(23/01/2018\)__

WI\-1321791: \[Layout 4\.0\] Avaliação de impactos da versão liberada em  19/12/17

__R109 \(06/02/2018\)__

WI\-1328639: \[Layout 4\.0\] Integração ECD \- Inclusão do arquivo de 2018 e Registro I157 \- Campos de Moeda Funcional

WI\-1332585: \[Layout 4\.0\] Incluir parâmetro do bloco V na tela de informações ECF

WI\-1337973: \[Layout 4\.0\] Atualização do perfil de geração da ECF

WI\-1340841: \[Layout 4\.0\] Testes integrados da versão \- Telas / Relatórios

WI\-1337965: \[Layout 4\.0\] Atualização de regras e listas de valores do bloco W

__R110 \(20/02/2018\)__

WI\-1332577: \[Layout 4\.0\] Atualização de tabelas dinâmicas e planos referenciais

WI\-1340856: \[Layout 4\.0\] Testes integrados da versão \- Cópia de associações / Integrações \- PAR2101

WI\-1340857: \[Layout 4\.0\] Testes integrados da versão \- Cópia de associações / Integrações \- PAR3005

WI\-1340858: \[Layout 4\.0\] Testes integrados da versão \- Cópia de associações / Integrações \- PAR3017

WI\-1340862: \[Layout 4\.0\] Testes integrados da versão \- Processamento em lotes

WI\-1332649: \[Layout 4\.0\] Atualização de regras e listas de valores dos blocos X e Y

WI\-1347408: \[Layout 4\.0\] Atualização de regras e listas de valores do bloco W

WI\-1347690: \[Layout 4\.0\] Testes integrados da versão \- Cópia de associações / Integrações \- PAR2105

WI\-1332572: \[Layout 4\.0\] Adequar rotina de Atualização de escriturações

WI\-1332806: \[Layout 4\.0\] Atualizar geração do arquivo magnético

__R111 \(06/03/2018\)__

WI\-1351632: \[Layout 4\.0\] Atualização de tabelas dinâmicas e planos referenciais

WI\-1349032: \[Layout 4\.0\] Testes integrados com a base da Brandili

WI\-1363099: \[Layout 4\.0\] Permitir a parametrização para utilização de tabelas dinâmicas

WI\-1364632: \[Layout 4\.0\] Realizar a migração do bloco W

WI\-1361266: \[Layout 4\.0\] Testes integrados com as soluções fiscais

WI\-1363069: \[Layout 4\.0\] Levantamento de tickets que geraram problemas na atualização da versão anterior

WI\-1332802: \[Layout 4\.0\] Criar tela para os registros do bloco V \- Declaração DEREX

WI\-1332800: \[Layout 4\.0\] Permitir a integração dos registros do bloco V \- Declaração DEREX

# <a id="_Toc507581028"></a>Atualização das tabelas

Tabela Dinâmica 

Tabela Referencial

Versão \(Ajuste RNG00003 e RNG00004\)

Perfil \(ajuste planilha Layout\_ECF\.xlsx\)

Código de Receita Novo 1895 \(Y570\)\. Iremos utilizar alguma tabela do DW?

Impactos:

- Tela Perfil
- Telas de Mapeamento e integrações
- Todas as telas que apresentam versão e integrações
- DARF e Bloco Y

Resumo da Primeira comparação realizada pelo time do OneSource

1. Comparação das tabelas dinâmicas com base na versão do PVA 4\.0\.1 \( 993 itens alterados, 537 itens excluídos e 1663 incluídos\)
2. Comparação do Plano Referencial \- L100 alteração da conta superior, L300B e U150B a conta era Analítica e mudou para Sintética\.

Verificar a nova comparação 

# <a id="_Toc507581029"></a>Bloco 0

__Registro 0000__

\- Inclusão de opção  0004 no campo 3 \- COD\_VER – Código da versão do layout\.

__Registro 0020 __

 \- Inclusão de campo\. Campo 33 tipo lista, opções válidas: \(S/N\)

Impactos:

- Tela de Informações ECF \(Incluir parâmetro na aba "Parâmetros Complementares" para a versão 4\.00 referente à Declaração DEREX\. 

Parâmetro: "Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações \(DEREX\)" 

- Geração do Bloco 0 \(inclusão do campo no registro 0020\)

\[0020\]

IND\_DEREX

\[S;N\]

 

 

# <a id="_Toc507581030"></a>Bloco W 

Criar versão 4\.0 \(planilha de validação\)

# <a id="_Toc507581031"></a>Bloco X 

- X300

Alteração da lista de opções\. Campo TIP\_MET até 3\.0 PVA e na 4\.0 PGE

 Até 3\.0

\[X300\]

TIP\_MET

\[PVE; PVA; PVV; CAP; PECEx\]

 

A partir da Versão 4\.0

\[X300\]

TIP\_MET

\[PVE; PGE; PVV; CAP; PECEx\]

 

 

 

 

- Para os demais registros, criar versão 4\.0

# <a id="_Toc507581032"></a>Bloco Y 

- Y600

Inclusão da opção 14 na validação país <> 105, se ind\_qualif\_socio = PF

- Y570

Incluído o código de receita 1895 na validação do registro \(escriturações a partir 01/01/2016\)\. Verificar qual tabela que vamos recuperar essa informação, \(no onesource FXD00045\)

Campos 5,7, e 8

- Y600

Alterada a regra da geração do registro Y600: Identificação e Remuneração de Sócios, Titulares, Dirigentes e Conselheiros para que o durante a cópia de uma escrituração de uma versão para outra, o campo Lucros e Dividendos não seja copiado, sendo atualização na informação na tela Informações Econômicas e Gerais \(Blocos X e Y\)\.

- Para os demais registros, criar versão 4\.0

# <a id="_Toc507581033"></a>Bloco V

Criação do Bloco V –  Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações \(DEREX\)\.

\- 6 registros – Obrigatório se parâmetro inserido na tela de Informações ECF estiver marcado \(check\-box\)

Registros

Nível

V001

1

V010

2

V020

3

V030

3

V100

4

V990

Impactos:

- Tela: permitir CRUD dos registros abaixo:

Registro V010: DEREX \- Instituição  
Registro V020: Responsável pela Movimentação   
Registro V030: DEREX – Período \- Mês  
Registro V100: Demonstrativo dos recursos em moeda estrangeira decorrentes do recebimento de exportações 

- Integração: permitir integração dos registros abaixo:

Registro V010: DEREX \- Instituição  
Registro V020: Responsável pela Movimentação   
Registro V030: DEREX – Período \- Mês  
Registro V100: Demonstrativo dos recursos em moeda estrangeira decorrentes do recebimento de exportações 

- Geração: Bloco 0, 9 e V

# <a id="_Toc507581034"></a>Bloco 9

Ajustar o Bloco 9 para contemplar o bloco V \(criação de contadores\)

# <a id="_Toc507581035"></a>Atualização de Escrituração

\-Ajustar a rotina, permitindo a atualização para a versão 4\.0

\-Incluir na atualização a migração do bloco W

# <a id="_Toc507581036"></a>Integração ECD

Ajuste na integração ECD, para aceitar dados de 2018 e inclusão de campo de moeda functional\.

# <a id="_Toc507581037"></a>Considerações 

Há uma demanda sinalizada como \[Layout 4\.0\], mas, não está relacionada a mudança de layout\. Verificar se deve ser tratada:

WI\-1363099: \[Layout 4\.0\] Permitir a parametrização para utilização de tabelas dinâmicas

 

Solução que será adotada pelo Onesource: criar um parâmetro na tela de Informações ECF, para o usuário indicar se quer ou não que validamos a existência de parametrização de tabela dinâmica\. 

Atualmente o produto obriga ter uma associação de tabela dinâmica, mas existia uma regra no OneSource que permitia para o Lucro Presumido e Imune/Isentas, não ter essa associação \(esta regra foi excluída recentemente\)\.

__Atenção:__ Foi identificado no processe de atualização de escrituração, quando não existia mapeamento de tabela dinâmica na base, mas havia ajuste manual de valores, esses ajustes não eram copiados para a nova escrituração\. Este ponto está sendo revisto no OneSource\.

