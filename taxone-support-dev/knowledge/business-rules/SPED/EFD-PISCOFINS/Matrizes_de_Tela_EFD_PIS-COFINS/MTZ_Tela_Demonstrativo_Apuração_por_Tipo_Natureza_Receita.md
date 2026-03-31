# MTZ_Tela_Demonstrativo_Apuração_por_Tipo_Natureza_Receita

- **Fonte:** MTZ_Tela_Demonstrativo_Apuração_por_Tipo_Natureza_Receita.docx
- **Modificado:** 2020-07-28
- **Tamanho:** 76 KB

---

THOMSON REUTERS

Matriz da tela/relatório Demonstrativo da Apuração por Tipo de Natureza da Receita 

__Localização:__

__Módulo__: SPED >> EFD\-Escrituração Fiscal Digital das Contribuições

__Menu__:      Obrigação          >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Natureza da Receita

                 Obrigação SCP >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Natureza da Receita

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3583

Alteração – Tela de Emissão do Relatório Demonstrativo da Apuração

Criação da tela de Emissão do Relatório Demonstrativo da Apuração “Por Tipo de Natureza de Crédito’’ 

OS4316\-B

Marcos G\. de Paula

Duplicação da tela e relatório com seleção da apuração por SCP\.

MFS37761

Liliane V\. Assaf

Para o TAX ONE habilitar apenas a opção sintético, pois o relatório analítico passa a ser disponibilizado na opção de menu “Relatórios 🡪 Demonstrativo da Apuração \(Crédito / Contribuição / Natureza da Receita\)”

Sumário

[1\.	TELA A SER DESENVOLVIDA	1](#_Toc46856067)

[1\.1\.	Diagrama de Casos de Uso	1](#_Toc46856068)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	1](#_Toc46856069)

[1\.1\.1\.1\.1\.	Fluxo Principal	1](#_Toc46856070)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	1](#_Toc46856071)

[2\.	Regras dos Campos	1](#_Toc46856072)

[3\.	Sugestão de Layout	1](#_Toc46856073)

[4\.	Relatório	1](#_Toc46856074)

# <a id="_Toc46856067"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc46856068"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc46856069"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

Usuário do Sistema\.

__Pré\- Condições__

Estar logado no produto MasterSAF DW\.

__Pós\-Condições__

Não se aplica\.

<a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a>

### <a id="_Toc46856070"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a><a id="_Toc46856071"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc46856072"></a>Regras dos Campos 

__Localização da tela:__ 

	Módulo: SPED >> EFD\-Escrituração Fiscal Digital das Contribuições

	Menu: Obrigação          >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Natureza da Receita

                 Obrigação SCP >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Natureza da Receita

	As informações que serão demonstradas na tela são baseadas no apurado no processo de geração dos registros\. 

No acesso à tela deve ser demonstrada a tela padrão de seleção dos registros gerados, considerando as seguintes informações: Estabelecimento, *Código da SCP\**, Tipo do Livro, Data da Apuração Inicial, Data da Apuração Final, Indicador de Situação da Apuração, Indicador de Validade da Apuração, Data da Realização da Apuração, Descrição da Obs, Id Reg e Código do Layout\.

*\*Caso seja gerado por SCP\.*

	

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Tipo

Texto

S

S

Formato: 

Radio Button Group

Default: 

Habilitado

Sintético

Deve ser informado o tipo de relatório que é emitido\.

__Conteúdo:__

- Analítico 
- Sintético

__Considerações: __

- \[MFS37761\]

No TAX ONE o relatório Analítico passou a ser gerado através da opção de menu “Relatórios >> Demonstrativo de Apuração \(Crédito/Contribuição/Natureza da Receita\)”\. Desta forma, apenas a opção Sintético fica habilitada para utilização\. No DW as duas opções Sintético e Analítico permanecem habilitadas\.

OS3583

MFS37761

Cód\. Sit\. Tributária Específica

Texto

N

S

Formato: 

Combo Box

Default: 

Habilitado e Desmarcado

O campo Cód\. Sit\. Tributária Específica deve possuir as opções abaixo\.  

            < > 	   Opção Branco

04

Operação Tributável Monofásica \- Revenda a Alíquota Zero

05

Operação Tributável por Substituição Tributária

06

Operação Tributável a Alíquota Zero

07

Operação Isenta da Contribuição

08

Operação sem Incidência da Contribuição

09

Operação com Suspensão da Contribuição

OS3583

Registro

Texto

S

S

Formato: 

Check Box

Default: 

Habilitado e Todos Marcados

Esse campo deve possuir as opções abaixo\. O campo é de preenchimento obrigatório\. Além disso, por default  todas as opções devem ficar marcados\.

M400 – 

M410 – 

M800 – 

M810 – 

OS3583

\.

# <a id="_Toc534379369"></a><a id="_Toc46856073"></a>Sugestão de Layout

# <a id="_Toc534379370"></a><a id="_Toc46856074"></a>Relatório

__Ver documento matriz MTZ\_Relatorio\_de\_Demonstrativo\_da\_Apuracao\_EFD\_PISPASEP\-COFINS\.doc__

