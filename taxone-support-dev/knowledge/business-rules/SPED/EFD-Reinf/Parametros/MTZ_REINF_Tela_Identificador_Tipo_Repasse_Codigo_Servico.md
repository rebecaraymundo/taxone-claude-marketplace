# MTZ_REINF_Tela_Identificador_Tipo_Repasse_Codigo_Servico

- **Fonte:** MTZ_REINF_Tela_Identificador_Tipo_Repasse_Codigo_Servico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 71 KB

---

THOMSON REUTERS

Identificador do Tipo de Repasse por Código de Serviço

SPED – Reinf

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS11670

EFD\- Reinf

Inclusão da Tela de Identificador do Tipo de Repasse

MFS12777

EFD\- Reinf

Alteração no nome da tela para “Identificador do Tipo de Repasse por Código de Serviço”

MFS13367

Lara Aline

Inclusão da opção Patrocínio no campo Tipo de Repasse

MFS13857

Lara Aline

Inclusão campo Informar Código/Descrição para Pesquisa

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc355275051)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc355275052)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc355275053)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc355275054)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Localizar registros \(Exemplo\)	4](#_Toc355275055)

[2\.	Regras dos Campos	5](#_Toc355275056)

# <a id="_Toc350763252"></a><a id="_Toc355275056"></a>Regras dos Campos 

__Localização da tela:__ Módulo: SPED >> EFD – Reinf

__                                   __Menu: REINF >> Parâmetros >> Identificador do Tipo de Repasse >> Por Código de Serviço

__Título da tela: __Identificador do Tipo de Repasse por Código de Serviço

Obs: Ao abrir a tela de conferência deverá abrir uma subtela para seleção do Grupo\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Grupo Serviço

TextBox

S

N

Default: Desabilitado

Deverá apresentar o grupo conforme apresentado no modal ao abrir a tela\.

MFS\-11670

Estabelecimento

Texto

S

N

Default: Desabilitado

Deverá apresentar o estabelecimento conforme apresentado no modal ao abrir a tela\.

MFS\-11670

Tipo de Repasse

Drop Down

S

S

Deverá listar as seguintes opções:

\[Alteração MFS13367\]

\- Patrocínio

\- Licenciamento de Marcas e Símbolos

\- Publicidades

\- Propaganda

\- Transmissão de Espetáculo

Caso não preenchido deverá apresentar a seguinte mensagem:

“Tipo de Repasse deve ser preenchido”

MFS\-11670

MFS\-13367

Informar Código/Descrição para Pesquisa

ComboBox

N

S

Default: não selecionado

Este campo é destinado para pesquisa de Código de Serviço via código ou descrição\.

Campos Código e Descrição são Checkbox\.

MFS13857

Código de Serviço

Checkbox

S

S

Deverá listar os códigos de serviços conforme SAFX2018\.

Caso não preenchido deverá apresentar a seguinte mensagem:

“Ao menos um código de serviço deve ser selecionado”

MFS\-11670

Selecionar Todos

Button

N

N

Se selecionado irá selecionar todos os estabelecimentos listados em tela\.

MFS\-11670

Desmarcar Todos

Button

N

N

Se selecionado irá desmarcar todos os estabelecimentos listados em tela\.

MFS\-11670

Replicar para os Estabelecimentos

Checkbox

S

S

Quando selecionado deverá permitir replicar a parametrização para outros estabelecimentos\.

MFS\-11670

Selecionar Todos

Button

N

N

Se selecionado irá selecionar todos os estabelecimentos listados em tela\.

MFS\-11670

Desmarcar Todos

Button

N

N

Se selecionado irá desmarcar todos os estabelecimentos listados em tela\.

MFS\-11670

