# MTZ_REINF_Tela_Conferencia_Previa_Cadastros

- **Fonte:** MTZ_REINF_Tela_Conferencia_Previa_Cadastros.docx
- **Modificado:** 2025-06-20
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Conferência Prévia dos Cadastros

SPED – Reinf

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-10757

Elenilson Coutinho

Inclusão da Tela de Conferência Prévia dos Cadastros \(R\-1070\) do EFD – Reinf

MFS\-10758

Elenilson Coutinho

Inclusão da Tela de Conferência Prévia dos Cadastros \(R\-1000\) do EFD – Reinf\.\.\.

MFS13810

Lara Aline

Ajuste no layout de tela do evento R\-1070 \(Campo Autoria da Ação Judicial\)\.

MFS14462

Lara Aline

Inclusão do campo Versão\.

MFS18226

Lara Aline

Inclusão observação sobre o evento R\-1000 de Limpeza\.

MFS\-58345

Alessandra Cristina Navatta

Reestruturação do Menu

MFS\-81450

Alessandra Cristina Navatta

Alteração das Informação do Evento R\-1000, atendendo o layout Versão 2\.1

MFS\-79881

Alessandra Cristina Navatta

Inclusão das Informações do Evento R\-1050, atendendo o layout Versão 2\.1

[MFS\-90863](https://jira.thomsonreuters.com/browse/MFS-90863)

Alessandra Cristina Navatta

Alteração da versão 2\.1 para 2\.1\.1 

Não há regras a serem ajustada neste arquivo\.

MFS\-523048

Alessandra Cristina Navatta

Inclusão do campo Indicativo de Entidade Vinculada a União, para atendimento do evento R\-1000, versão 2\.1\.1\.

MFS\-840399

Alessandra Cristina Navatta

Inclusão do campo Indicador de Pertencimento do IRRF, para atendimento do evento R\-1000 \(campo indPertIRRF\), versão 2\.1\.2 \(Nota Técnica 02/2025\)

Sumário

[1\.	Regras dos Campos	3](#_Toc494792479)

# <a id="_Toc350763252"></a><a id="_Toc494792479"></a>Regras dos Campos 

__Localização da tela:__ Módulo: SPED >> EFD – Reinf

__                                   __Menu: REINF >> Conferência Prévia >> Cadastros

__Título da tela: __Conferência Prévia dos Cadastros

Obs: Ao abrir a tela de conferência deverá abrir uma subtela para seleção do Estabelecimento\.

         __Título da tela: __Selecionar Estabelecimento de Conferência Prévia dos Cadastros

__\[MFS18226\]__

Obs: O evento R\-1000 de Limpeza não será apresentada na tela de conferência dos cadastros, esse evento será demostrado apenas no Painel de Controles de Eventos\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento 

TextBox

S

N

Formato: Código \+ Estabelecimento

Irá demonstrar o estabelecimento selecionado na chamada da subtela de seleção\.

MFS\-10757

MFS\-10758

Versão

TextBox

S

N

Irá demostrar a versão de Leiaute da EFD\-REINF

MFS\-14462

Eventos\-Reinf 

Pasta

S

N

Irá demonstrar os eventos de cadastros pré\-gerados \(R\-1000, R\-1050 e R1070\), conforme seleção de estabelecimento na subtela de seleção\.

MFS\-10757

MFS\-10758

MFS\-79881

R\-1000 – Informações do Contribuinte

Identificação do Contribuinte

Tipo de Inscrição

Textbox

S

N

MFS\-10758

Número de Inscrição 

Textbox

S

N

MFS\-10758

Validade Inicial 

Textbox

S

N

MFS\-10758

Validade Final 

Textbox

N

N

MFS\-10758

Ocorrências

Data da Ocorrência  

Textbox

S

N

MFS\-10758

Operação

Textbox

S

N

MFS\-10758

<a id="_Hlk481182996"></a>Classificação Tributária

Textbox

S

N

MFS\-10758

Escrituração na ECD

Textbox

N

N

MFS\-10758

Desoneração Folha

Textbox

S

N

MFS\-10758

Acordo de Isenção 

Textbox

S

N

MFS\-10758

Situação PJ

Textbox

N

N

MFS\-10758

Indicativo de Entidade Vinculada a União

Textbox

N

N

MFS\-523048

Data da Transformação de Entidade Beneficente de Assistência Social Isenta de Contribuições Sociais em Sociedade com Fins Lucrativos \- Art\. 13 \- Lei 11096/2005

Textbox

N

N

MFS\-81450

Indicador de Pertencimento do IRRF

Texto

__N__

N

Só deve ser exibida informação, se o parâmetro Pertencimento do IRRF, a tela de Informações do Contribuinte estiver marcado\.Neste caso, apresentar Sim 

MFS\-840399

Nome do Contato 

Textbox

S

N

MFS\-10758

CPF do Contato

Textbox

S

N

MFS\-10758

Telefone Fixo 

Textbox

N

N

MFS\-10758

Celular

Textbox

N

N

MFS\-10758

Email

Textbox

N

N

MFS\-10758

Validade Final

Textbox

S

N

MFS\-10758

Nova Validade Final

Textbox

S

N

MFS\-10758

Situação

Textbox

S

N

MFS\-10758

Informação da Software House

CNPJ

Textbox

S

N

MFS\-10758

Razão Social 

Textbox

S

N

MFS\-10758

Nome do Contato

Textbox

S

N

MFS\-10758

Telefone 

Textbox

N

N

MFS\-10758

Email

Textbox

N

N

MFS\-10758

R\-1050 – Tabela de Entidades Ligadas

Informações Relacionadas a Entidades Ligadas

Classificação da Entidade Ligada

Textbox

S

N

MFS\-79881

CNPJ

Textbox

S

N

MFS\-79881

Início Validade

Textbox

S

N

MFS\-79881

Fim Validade

Textbox

__N__

N

MFS\-79881

Ocorrências

Data da Ocorrência  

Textbox

S

N

MFS\-79881

Operação

Textbox

S

N

MFS\-79881

Classificação da Entidade Ligada

Textbox

S

N

MFS\-79881

Validade Final

Textbox

S

N

MFS\-79881

Nova Validade Final

Textbox

S

N

MFS\-79881

Situação

Textbox

S

N

MFS\-79881

R\-1070 – Tabela de Processos Administrativos/Judiciais

Identificação do Processo

Tipo do Processo 

Textbox

S

N

Irá demonstrar o tipo de inscrição do estabelecimento\.

1\-CNPJ

MFS\-10757

Número do Processo

Textbox

S

N

Irá demonstrar o número de inscrição do estabelecimento\.

MFS\-10757

Validade Inicial

Textbox

S

N

MFS\-10757

Validade Final

Textbox

N

N

MFS\-10757

Autoria da Ação Judicial

Textbox

N

N

MFS13810

Ocorrências

Data da Ocorrência

Textbox

S

N

MFS\-10757

Operação

Textbox

S

N

MFS\-10757

UF Seção Judiciária

Textbox

S

N

MFS\-10757

Município

Textbox

N

N

MFS\-10757

Identificação da Vara

Textbox

S

N

MFS\-10757

Autoria da Ação Judicial

Textbox

N

N

MFS\-10757

MFS13810

Validade Final

Textbox

S

N

MFS\-10757

Nova Validade Final

Textbox

S

N

MFS\-10757

Situação

Textbox

S

N

MFS\-10757

Suspensão de Exigibilidade de Tributos

Código da Suspensão

Textbox

N

N

MFS\-10757

Indicador de Suspensão 

Textbox

S

N

MFS\-10757

Data Decisão

Textbox

S

N

MFS\-10757

Indicador de Depósito

Textbox

S

N

MFS\-10757

