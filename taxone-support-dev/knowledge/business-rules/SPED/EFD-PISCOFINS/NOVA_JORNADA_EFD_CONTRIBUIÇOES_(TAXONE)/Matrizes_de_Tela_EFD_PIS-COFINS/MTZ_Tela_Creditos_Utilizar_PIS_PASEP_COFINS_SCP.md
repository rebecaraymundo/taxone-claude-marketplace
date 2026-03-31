# MTZ_Tela_Creditos_Utilizar_PIS_PASEP_COFINS_SCP

- **Fonte:** MTZ_Tela_Creditos_Utilizar_PIS_PASEP_COFINS_SCP.docx
- **Modificado:** 2022-12-08
- **Tamanho:** 102 KB

---

THOMSON REUTERS

Matriz da tela Controle de Créditos Fiscais \- PIS/PASEP e COFINS \- menu SCP

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4316\-B

Marcos G\. de Paula

Duplicação da tela com seleção da apuração por SCP\.

MFS28515

Andréa Rocha

Alterar a tela para não mostrar os créditos disponíveis com o status de cancelado\.

15/10/2019

MFS34355

Liliane Assaf

Alteração no tratamento dos créditos prescritos com mais de 5 anos\.

28/06/2020

MFS57866

Andréa Rocha

Alteração no tratamento dos créditos prescritos com mais de 5 anos\.  Criação de um parâmetro para indicar se os créditos com mais de 5 anos podem ser usados ou não\.  Assim, ficam as duas opções disponíveis para o usuário escolher a forma de tratar os créditos\.

09/03/2020

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc378091802)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc378091803)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc378091804)

[1\.1\.1\.1\.1\.	Fluxo Principal	4](#_Toc378091805)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Novo Registro	4](#_Toc378091806)

[2\.	Regras dos Campos	4](#_Toc378091807)

# <a id="_Toc378091802"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc378091803"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc378091804"></a>UC001 – Manutenção da Estrutura Padrão

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

### <a id="_Toc378091805"></a>Fluxo Principal 

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc378091806"></a><a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>Fluxo Alternativo 1 – Novo Registro

__Ações do Ator__

__Ações do Sistema__

__Fim do fluxo Alternativo__

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc378091807"></a>Regras dos Campos 

__Localização da tela:__ 

	Módulo: SPED >> EFD\-Escrituração Fiscal Digital das Contribuições

	Menu: Obrigação SCP >> Manutenção >> Controle dos Créditos Fiscais – PIS/PASEP

e

Menu: Obrigação SCP >> Manutenção >> Controle dos Créditos Fiscais – COFINS

	Esta tela deverá ser uma replica da tela de Créditos a Utilizar na Apuração disponível no menu Obrigação >> Manutenção >> Controle dos Créditos Fiscais – PIS/PASEP e Obrigação >> Manutenção >> Controle dos Créditos Fiscais – COFINS\.

As informações que serão demonstradas na tela são baseadas no apurado no processo de geração dos registros\. No acesso à tela deve ser demonstrada a tela padrão de seleção dos registros gerados, considerando as seguintes informações: Estabelecimento, Código da SCP, Tipo do Livro, Data da Apuração Inicial, Data da Apuração Final, Indicador de Situação da Apuração, Indicador de Validade da Apuração, Data da Realização da Apuração, Descrição da Obs, Id Reg e Código do Layout\.

__\[MFS28515\] alterada pela \[MFS34355\]__

Regras para o Quadro de__ __Crédito Disponível:

__\[MFS57866\] __Criação de um parâmetro para indicar se os créditos com mais de 5 anos podem ser usados ou não\.

Se o parâmetro “Utilizar os créditos superiores a 60 meses” estiver desmarcado

     Os créditos que tiverem um período maior que 5 anos, ou seja, a diferença entre o mês/ano do    

     crédito e a data da apuração for maior que 5 anos, serão demonstrados com o campo  

     "Cancelado por Prazo de Prescrição" marcado\.

     Caso o usuário tente utilizar um crédito que esteja com "Cancelado por Prazo de Prescrição"   

     marcado, ou seja, com mais de 5 anos, o sistema exibirá a mensagem abaixo e impedirá a  

     utilização do crédito:

     “Atenção, o crédito selecionado está com Status Cancelado por Prazo de Prescrição pois possui    

      mais de 5 anos e por isso não poderá ser utilizado\.”

Se o parâmetro “Utilizar os créditos superiores a 60 meses” estiver marcado

     O campo "Cancelado por Prazo de Prescrição" vai ficar habilitado para o usuário marcar ou    

     Desmarcar, ou seja, o usuário escolhe se o crédito está cancelado ou não\.  

     Caso o usuário tente utilizar um crédito que esteja com "Cancelado por Prazo de Prescrição"   

     marcado, ou seja, com mais de 5 anos, o sistema exibirá a mensagem abaixo e impedirá a  

     utilização do crédito:

     “Atenção, o crédito selecionado está com Status Cancelado por Prazo de Prescrição pois possui    

      mais de 5 anos e por isso não poderá ser utilizado\.”

     Se o campo "Cancelado por Prazo de Prescrição" estiver desmarcado, os créditos que tiverem um  

     período maior que 5 anos, ou seja, a diferença entre o mês/ano do crédito e a data da apuração 

     for maior que 5 anos, quando for selecionado para a utilização, deve\-se dar uma mensagem:

    “Atenção, o crédito selecionado possui mais de 5 anos\. Favor verificar se o mesmo está prescrito\.”\.     

     A mensagem será para informar o usuário, mas não impedirá a utilização do crédito\.

Obs\.: O parâmetro “Utilizar os créditos superiores a 60 meses” está disponível na tela de Dados Iniciais \(Parâmetros 🡪 Dados Iniciais\)\.

