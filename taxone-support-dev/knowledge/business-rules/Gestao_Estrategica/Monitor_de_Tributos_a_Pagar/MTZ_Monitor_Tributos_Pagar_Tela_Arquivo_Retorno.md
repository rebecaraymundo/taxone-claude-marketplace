# MTZ_Monitor_Tributos_Pagar_Tela_Arquivo_Retorno

- **Fonte:** MTZ_Monitor_Tributos_Pagar_Tela_Arquivo_Retorno.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 77 KB

---

THOMSON REUTERS

Parâmetros do Arquivo de Retorno 

Tela de Parâmetros do Arquivo de Retorno

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-5048

Arquivo de Retorno 

Criação da Tela Arquivo de Retorno

MFS\-6310

Geração do Arquivo de Impostos Apurados

Retirar os impostos ICMS e ICMS\-ST 

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc455764647)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc455764648)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc455764649)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc455764650)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Localizar registros \(Exemplo\)	4](#_Toc455764651)

[2\.	Regras dos Campos	5](#_Toc455764652)

[3\.	Regras dos Campos	8](#_Toc455764653)

# <a id="_Toc455764647"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc455764648"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc455764649"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

\[Quem executará o evento\. Ex\.: Usuário do sistema\]\.

__Pré\- Condições__

\[Condições necessárias para execução\. Ex\.: Estabelecimento cadastrado\]

__Pós\-Condições__

\[Resultado após executar caso de uso\. Ex\.: Informação armazenada no banco de dados\]

### <a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a><a id="_Toc455764650"></a>Fluxo Principal 

\[Descrever a ação principal que será realizada na tela especificada\.

 Ex\.: O usuário deseja realizar o cadastro de uma estrutura padrão\.

__Ações do Ator__

__Ações do Sistema__

\[Descrever a interação do ator com o sistema\. 

Ex\.: O usuário acessa a tela de estrutura padrão\]\.

\[Descrever a ação esperada do sistema

Ex\.:O sistema apresenta a tela, conforme as regras definidas no tópico “Regras dos Campos”\.\]

\[Ex\.:O usuário preenche os campos da Manutenção de Estrutura do Produto\.

__<<Fluxo Alternativo 1>>__

\[Ex\.:O sistema apresenta os campos preenchidos\.\]

### <a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>

### <a id="_Toc455764651"></a>Fluxo Alternativo 1 – Localizar registros \(Exemplo\)

__Ações do Ator__

__Ações do Sistema__

O usuário clica no botão “Localizar”\.

O sistema apresenta os registros cadastrados, de acordo com os parâmetros informados\.

__Fim do fluxo Alternativo__

# <a id="_Toc350763252"></a><a id="_Toc455764652"></a>Regras dos Campos 

__Localização da tela:__ Módulo: Solução Complementar >> Tax Monitor

                           Menu: Importação >> Arquivo de Retorno

__Título da tela: __Parâmetros do Arquivo de Retorno

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

Drop Down 

S

S

Default: Preenchido

Este campo permite ao usuário informar o estabelecimento a ser consultado\.

Deverá conter a opção “Todos”, conforme permissão do usuário\.

MFS\-5048

Data inicial

Data 

S

S

DD/MM/AAAA

Este campo permite ao usuário informar a data inicial de geração do arquivo para consulta\.

Caso não preenchido informa a seguinte mensagem:

“A Data Inicial deve ser preenchida”

MFS\-5048

Data Final 

Data

S

S

DD/MM/AAAA

Este campo permite ao usuário informar a data Final de geração do arquivo para consulta\.

Caso não preenchido informa a seguinte mensagem:

“A Data Final deve ser preenchida”

MFS\-5048

Grupo Tributo

Drop Down

S

S

Default: Não selecionado

Este campo permite ao usuário informar o grupo que pertence o tributo, será listado:

     Todos

1 – Federal

2 – Estadual 

3 – Municipal 

4 – Previdenciário

Caso não preenchido informa a seguinte mensagem:

 “O Grupo Tributo deve ser preenchido“\.

Obs: Não serão apresentados os respectivos “números” dos tributos, apenas a descrição\. Estes números serão a referencia para o campo “grupo\_tributo” da TFIX140\.

MFS\-5048

Tributo

Drop Down

S

S

Default: Não selecionado

Será habilitado quando for informado o Grupo Tributo, demonstrando apenas os Tributos relacionados ao Grupo indicado, conforme regras abaixo:

- Todos
- IRPJ
- IRRF
- CSLL
- PIS/PASEP
- COFINS 
- IPI
- PIS/PASEP \(PRÓPRIO\) 
- COFINS \(PRÓPRIO\)

MFS\-6310

Para o Grupo Municipal, demonstrar as opções:

- ISS

Para o Grupo Previdenciário, demonstrar a opção:

- INSS

Caso o campo “Tributo” não esteja preenchido, deve ser exibida a seguinte mensagem de erro: “O Tributo deve ser preenchido”\.

Obs: Caso a opção “Todos” esteja preenchido no campo “Grupo tributo” este campo deverá ser desabilitado\.

MFS\-5048

MFS\-6310

Diretório

Pasta

S

S

Ao clicar na pasta, deverá abrir uma janela ao usuário, possibilitando que o mesmo indique o caminho na Raiz de pastas do Sistema, onde esteja localizado o arquivo TXT ou XML que deseja fazer a Importação\. 

Se o campo não for preenchido, sistema deve exibir a seguinte mensagem: “Informe Diretório”\.

MFS\-5048

Iniciar Importação

Button

S

N

Botão para iniciar o processo de importação\. Ao clicar no botão será exibida a tela “Importação do Arquivo de Retorno" com todos os campos de parâmetros desabilitados, onde o usuário poderá finalizar a importação dos arquivos\.

MFS\-5048

# <a id="_Toc455764653"></a>Regras dos Campos 

__Localização da tela:__ Módulo: Solução Complementar >> Tax Monitor

                           Menu: Importação >> Arquivo de Retorno >> Após clicar no botão “Iniciar Importação”

__Título da tela: __Importação do Arquivo de Retorno

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Parâmetro 

Aba

N

N

Esta aba permite ao usuário parametrizar as informações necessárias para importação do arquivo de retorno\.

MFS\-5048

Processos

Aba

N

N

Esta aba permite ao usuário, gerenciar todo o processo de importação do arquivo de retorno\.

MFS\-5048

Log

Aba

N

N

Esta aba permite ao usuário visualizar o log do processo de importação do arquivo\. Serão estes:

- “Arquivo Rejeitado\. Processo de importação não realizado verifique o painel de resultados”\.
- “Arquivo Divergente”\. Processo de importação realizado, porém com divergência de valores\. Verifique o painel de resultados\.
- “Arquivo importado com sucesso”
- Arquivo IDXXX não importado\. Geração do registro com status de “Cancelado” para o ID Geração: XXX
- Arquivo IDXXX não importado\. Estrutura XML inválida\.

MFS\-5048

Tipo de Execução

Radio Button

N

S

Default Selecionado: Imediata

Este Campo permite ao usuário programar a importação do arquivo de retorno\. Programação que pode ser:

Imediata \- Processo de importação realizado naquele exato momento\. 

Programada – Processo de importação automático programado para a data e hora desejada pelo usuário\.

MFS\-5048

Data/Hora de Execução

Texto

N

S

Default: Desabilitado

Este campo permite ao usuário informar a data e hora desejada para importação do arquivo \(Processo automático\)\.

Campo será habilitado apenas quanto o campo Tipo de Execução na opção “Programada” for selecionado\.

MFS\-5048

Executar

Botão

N

N

Quando acionado o sistema irá iniciar o processo de importação dos arquivos de retorno\.

MFS\-5048

Estabelecimento

Campo informativo, desabilitado\.

MFS\-5048

Data Inicial

Campo informativo, desabilitado\.

MFS\-5048

Data final 

Campo informativo, desabilitado\.

MFS\-5048

Grupo Tributo 

Campo informativo, desabilitado\.

MFS\-5048

Tributo

Campo informativo, desabilitado\.

MFS\-5048

Diretório

Campo informativo, desabilitado\.

MFS\-5048

Arquivos de Retorno

Checbox

S

S

Defaut: Não selecionado

Nesta tela serão demonstrados os arquivos de retorno conforme definição dos parâmetros de seleção da tela “Parâmetros do Arquivo de Retorno”\.

Obs: Ao menos um \(1\) arquivo deve ser selecionado, caso contrário exibir a seguinte mensagem: “Informar arquivo de retorno a ser importado”\.

MFS\-5048

