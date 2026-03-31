# MTZ-VAFMG_Tela_Dados_Iniciais_EFD-Fiscal

- **Fonte:** MTZ-VAFMG_Tela_Dados_Iniciais_EFD-Fiscal.docx
- **Modificado:** 2020-10-29
- **Tamanho:** 76 KB

---

THOMSON REUTERS

Módulo Sped Fiscal

Manutenção dos Dados Iniciais – DAMEF\-EFD Fiscal

__Localização__: Menu Estadual, Módulo: VAF\-MG, item DAMEF\-EFD FISCAL 🡪 Dados Iniciais

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS44425

Liliane Assaf

Criação da tela em atendimento a Portaria SRE 175/2020\. 

15/10/2020

Sumário

[1\.	Regras Gerais	2](#_Toc451260495)

[2\.	Layout da Tela	2](#_Toc451260496)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc451260497)

# <a id="_Toc451260495"></a>Regras Gerais

Essa funcionalidade foi criada como cópia da janela de Dados Inicias existente no menu Preliminares >> Manutenção de Dados Iniciais\.

A tela de Dados Inicias do menu Preliminares >> Manutenção de Dados Iniciais apresenta os campos usados na Geração do Relatório da VAF do menu Obrigações, refere à versão anterior à Portaria SRE No 175 de 17 de julho de 2020\. 

A tela de Dados Iniciais do menu DAMEF\-EFD FISCAL, apresenta os campos necessários para a Geração do Relatório \(Portaria SRE 175/2020\)\.   

Para ano\-exercício A PARTIR DE 2020, então:

    Utlizar a tela de Dados Iniciais do menu DAMEF\-EFD FISCAL\.

Para ano\-exercício ANTERIOR A 2020, então:

    Utlizar a tela de Dados Iniciais do menu Preliminares\.

# <a id="_Toc451260496"></a>Layout da Tela

Estabelecimento: \[xxxxxxxxxxxxxxxxxxxxxxxxx        \\/\]

Exercício:             \[xxxx\]

Ano\-Base:               \[xxxx\]

Tipo de Contribuinte: \[xxxxxxxxxxxxxxxxxxxxxxxxx   \\/\]        

Perfil de Apresentação da EFD: \[A                            \\/\]        

Mês em que o Estabelecimento mudou de Município:  \[ Janeiro                   \\/\]

\- Valores para as Entradas\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

|  Ajuste de Transferência: \[               0,00\]                     |

|  Autuações Fiscais:          \[                0,00\]                    |

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- 

\- Valores para as Saídas\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

|  Ajuste de Transferência: \[               0,00\]                     |

|  Autuações Fiscais:          \[                0,00\]                    |

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- 

\- Exclusões do Valor Adicionado Fiscal \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-

|  Subcontratação Serviço de Transporte \(Entradas\)      \[               0,00\]   |

|  Ajuste Entradas:                 \[               0,00\]                                             |

|  Extraordinárias Entradas:   \[                0,00\]                                            |

|  Ajuste Saídas:                    \[               0,00\]                                             |

|  Extraordinárias Saídas:      \[                0,00\]                                            |

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- 

Tabela Física: EST\_VAFMG\_DD\_INIC 

__Botões da barra de menu__:

NOVO

Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro\.

ABRE

Ao clicar nesta opção, será aberta a janela para seleção das parametrizações já cadastradas para consulta ou manutenção\. 	

EXCLUI

Esta opção permite a exclusão da parametrização do estabelecimento em questão\. 

CONFIRMA

Opção para salvar as informações incluídas ou alteradas\.

RELATÓRIO

Esta opção permite imprimir os dados da parametrização\. Trata\-se de opção padrão das telas de manutenção do sistema\. 

FECHA

Fecha a tela da manutenção\.

  

# <a id="_Toc451260497"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Alfanumérico 

__S__

S

Neste campo será exibido o Estabelecimento escolhido pelo usuário, na Tela de Login do Sistema, não tendo a opção de escolha de outro Estabelecimento, apenas será habilitado para seleção caso o usuário não entre com o Estabelecimento na Tela de Login\.

__Tratamento:__

- Deverão ser considerados apenas os estabelecimentos do estado MG;

Se o Estabelecimento não for selecionado na Tela de Login e não for selecionado no parâmetro, ao salvar, emitir a mensagem: *“O campo estabelecimento deve ser preenchido”\.*

Exercício

Numérico

S

S

AAAA

Nesse campo deve ser preenchido o ano do exercício\. Serão aceitos anos a partir de 2020\.

Ao salvar se o campo não estiver preenchido, emitir a mensagem: “*O campo exercício deve ser preenchido*”\.

Caso o campo seja preenchido com um ano anterior a 2020, emitir mensagem de aviso:

*“Os Dados Inicias da DAMEF de exercícios anteriores a 2020 devem ser incluídos via opção disponível no menu Preliminares >> Manutenção de Dados Iniciais\. Deseja realmente salvar o registro? \[Sim\]  \[Não\]”*

Ano\-Base

Numérico

N

S

AAAA

Nesse campo deve ser preenchido o ano base\.

Tipo de Contribuinte

Alfanumérico

S

S

Listbox

Lista composta pelas opções:

\- Especial

\- Outros

\- Regular

\- Transportador

Ao salvar o registro, se o campo não estiver preenchido, emitir a mensagem: “*O campo tipo de contribuinte deve ser preenchido*”\.

Ao salvar o registro, se o campo estiver preenchido com a opção Outros, exibir a seguinte mensagem:

*“Tipo de Contribuinte preenchido com valor inválido\. A opção Outros deixou de ser válida para a DAMEF a partir da Portaria 175/2*020\. Favor ajustar a opção para o Tipo de Contribuinte\.”

A opção Outros é disponibilizada na tela de Dados Iniciais do menu Preliminares\.

Perfil de Apresentação da EFD

Alfanumérico

S

S

Listbox

Lista composta pelas opções:

\- A

\- B

Ao salvar se o campo não estiver preenchido, emitir a mensagem\. 

Mês em que o Estabelecimento mudou de Município

Alfanumérico

N

S

Listbox

Lista composta pelos meses \(janeiro a dezembro\):

\- Janeiro

\- Fevereiro

\.\.\.

\- Dezembro

Campo não obrigatório\.

Gravar 1 para janeiro, 2 para fevereiro, \.\.\., 12 para dezembro\.

Ajuste de Transferência

Numérico

N

S

0,00

Valor apresentado no quadro “Valores para as Entradas”\.

Autuações Fiscais

Numérico

N

S

0,00

Valor apresentado no quadro “Valores para as Entradas”\.

Ajuste de Transferência

Numérico

N

S

0,00

Valor apresentado no quadro “Valores para as Saídas”\.

Autuações Fiscais

Numérico

N

S

0,00

Valor apresentado no quadro “Valores para as Saídas”\.

Subcontratação Serviço de Transporte \(Entradas\)      

Numérico

N

S

0,00

Valor apresentado no quadro “Exclusões do Valor adicionado Fiscal”\.

Ajuste Entradas

Numérico

N

S

0,00

Valor apresentado no quadro “Exclusões do Valor adicionado Fiscal”\.

Extraordinárias Entradas

Numérico

N

S

0,00

Valor apresentado no quadro “Exclusões do Valor adicionado Fiscal”\.

Ajuste Saídas

Numérico

N

S

0,00

Valor apresentado no quadro “Exclusões do Valor adicionado Fiscal”\.

Extraordinárias Saídas

Numérico

N

S

0,00

Valor apresentado no quadro “Exclusões do Valor adicionado Fiscal”\.

       = = = = = =

