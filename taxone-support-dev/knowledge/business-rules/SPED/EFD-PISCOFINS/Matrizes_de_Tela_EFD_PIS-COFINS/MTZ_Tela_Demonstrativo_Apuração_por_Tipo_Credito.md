# MTZ_Tela_Demonstrativo_Apuração_por_Tipo_Credito

- **Fonte:** MTZ_Tela_Demonstrativo_Apuração_por_Tipo_Credito.docx
- **Modificado:** 2020-07-28
- **Tamanho:** 77 KB

---

THOMSON REUTERS

Matriz da tela/relatório Demonstrativo da Apuração por Tipo de Crédito 

__Localização:__

__Módulo__: SPED >> EFD\-Escrituração Fiscal Digital das Contribuições

__Menu__:      Obrigação          >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Crédito

                 Obrigação SCP >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Crédito

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS3169\-GE13D

Telas de Emissão do Relatório Demonstrativo da Apuração e alteração da tela Geração dos Registros

Criação das telas de Emissão do Relatório Demonstrativo da Apuração “Por Tipo de Crédito’’ e ‘’Por Tipo de Contribuição’’\. Também na tela de Geração dos Registros a inclusão do parâmetro ‘’Gerar Relatórios Demonstrativos da Apuração no Período Informado’’

OS3583

Alteração – Tela de Emissão do Relatório Demonstrativo da Apuração

Criação da tela de Emissão do Relatório Demonstrativo da Apuração “Por Tipo de Natureza de Crédito’’ 

OS3631

Telas de Emissão do Relatório Demonstrativo da Apuração 

Alteração da tela de Emissão do Relatório Demonstrativo da Apuração ‘’Por Tipo de Contribuição’’ – inclusão dos filtros Cód\. Situação Tributária e Cód\. Registro\.

OS4316\-B

Marcos G\. de Paula

Duplicação da tela e relatório com seleção da apuração por SCP\.

MFS37761

Liliane V\. Assaf

Para o TAX ONE habilitar apenas a opção sintético, pois o relatório analítico passa a ser disponibilizado na opção de menu “Relatórios 🡪 Demonstrativo da Apuração \(Crédito / Contribuição / Natureza da Receita\)”

Sumário

[1\.	TELA A SER DESENVOLVIDA	1](#_Toc46856096)

[1\.1\.	Diagrama de Casos de Uso	1](#_Toc46856097)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	1](#_Toc46856098)

[1\.1\.1\.1\.1\.	Fluxo Principal	1](#_Toc46856099)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	1](#_Toc46856100)

[2\.	Regras dos Campos	1](#_Toc46856101)

[3\.	Sugestão de Layout	1](#_Toc46856102)

[4\.	Relatório	1](#_Toc46856103)

# <a id="_Toc46856096"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc46856097"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc46856098"></a>UC001 – Manutenção da Estrutura Padrão

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

### <a id="_Toc46856099"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc46856100"></a><a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc46856101"></a>Regras dos Campos 

__Localização da tela:__ 

	Módulo: SPED >> EFD\-Escrituração Fiscal Digital das Contribuições

	Menu: Obrigação          >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Crédito

                 Obrigação SCP >> Demonstrativos >> Emissão de Relatório Demonstrativo de Apuração >> Por Tipo de Crédito

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

- Se o usuário optar em emitir o Relatório Analítico, após a emissão é apresentado cada documento fiscal gerado no registro A100/A170, C100/C170, C190/C195, C395/C396, C500/C505, D100/D105, D500/D505, F100, F120, F130, F150, F205, F210 e F800 vinculado a composição no detalhamento do tipo de crédito\. 
- Se o usuário optar em emitir o Relatório Sintético, após emissão é apresentado à totalização dos valores de cada registro vinculado a composição do tipo de contribuição\.
- \[MFS37761\]:

No TAX ONE o relatório Analítico passou a ser gerado através da opção de menu “Relatórios >> Demonstrativo de Apuração \(Crédito/Contribuição/Natureza da Receita\)”\. Desta forma, apenas a opção Sintético fica habilitada para utilização\. No DW as duas opções Sintético e Analítico permanecem habilitadas\.

OS3169\-GE13D

MFS37761

Tipo Crédito

Texto

N

S

Formato: 

Combo Box

Default: 

Habilitado e Desmarcado

Neste campo deverá apresentada uma lista recuperada da TFIX98\.  Além de apresentar as opções da TFIX98, deve apresentar a opção branca

OS3169\-GE13D

Nat\. Base de Crédito

Texto

N

S

Formato: 

Combo Box

Default: 

Habilitado e Desmarcado

Esse campo deve possuir as opções abaixo\.  Esse campo não é de preenchimento Obrigatório\.

      < > \(opção Branco\)

1. Aquisição de bens para revenda
2. Aquisição de bens utilizados como insumo
3. Aquisição de serviços utilizados como insumo
4. Energia elétrica e térmica, inclusive sob a forma de vapor 
5. Aluguéis de prédios
6. Aluguéis de máquinas e equipamentos
7. Armazenagem de mercadoria e frete na operação de venda
8. Contraprestações de arrendamento mercantil
9. Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito sobre encargos de depreciação\)\.
10. Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado \(crédito com base no valor de aquisição\)\.
11. Amortização e Depreciação de edificações e benfeitorias em imóveis
12. Devolução de Vendas Sujeitas à Incidência Não\-Cumulativa
13. Outras Operações com Direito a Crédito
14. Atividade de Transporte de Cargas – Subcontratação
15. Atividade Imobiliária – Custo Incorrido de Unidade Imobiliária
16. Atividade Imobiliária – Custo Orçado de unidade não concluída
17. Atividade de Prestação de Serviços de Limpeza, Conservação e Manutenção – vale\-transporte, vale\-refeição ou vale\-alimentação, fardamento ou uniforme
18. Estoque de abertura de bens

OS3169\-GE13D

Registro

Texto

S

S

Formato: 

Check Box

Default: 

Habilitado e Todos Marcados

Esse campo deve possuir as opções abaixo\. O campo é de preenchimento obrigatório\. Além disso, por default  todas as opções: M100, M105,  M500, M505 devem ficar marcados\.

M100 – Crédito de PIS/PASEP Relativo ao Período

M105 – Detalhamento da Base de Calculo do Crédito Apurado no Período – PIS/PASEP

M500 – Crédito da COFINS Relativo ao Período

M505 – Detalhamento da Base de Calculo do Crédito Apurado no Período – COFINS 

OS3169\-GE13D

# <a id="_Toc534379369"></a><a id="_Toc46856102"></a>Sugestão de Layout

# <a id="_Toc534379370"></a><a id="_Toc46856103"></a>Relatório

__Ver documento matriz MTZ\_Relatorio\_de\_Demonstrativo\_da\_Apuracao\_EFD\_PISPASEP\-COFINS\.doc__

