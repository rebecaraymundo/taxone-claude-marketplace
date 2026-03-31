# MTZ_Tela_Apuracao_PIS_PASEP_SCP

- **Fonte:** MTZ_Tela_Apuracao_PIS_PASEP_SCP.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Matriz da tela Apuração PIS/PASEP \- menu SCP

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4316\-B

Marcos G\. de Paula

Duplicação da tela com inclusão do campo Código da SCP\.

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

	Menu: Obrigações SCP >> Manutenção >> Apuração PIS/PASEP

	Esta tela deverá ser uma replica da tela de Apuração PIS/PASEP disponível no menu Obrigações >> Manutenção >> Apuração PIS/PASEP, contemplando a inclusão do campo Código da SCP que servirá para detalhar a qual SCP se refere a apuração\.

As informações que serão demonstradas na tela são baseadas no apurado no processo de geração dos registros\. No acesso à tela deve ser demonstrada a tela padrão de seleção dos registros gerados, considerando as seguintes informações: Estabelecimento, Código da SCP, Tipo do Livro, Data da Apuração Inicial, Data da Apuração Final, Indicador de Situação da Apuração, Indicador de Validade da Apuração, Data da Realização da Apuração, Descrição da Obs, Id Reg e Código do Layout\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Código da SCP

Editbox

N

N

‘

Deverá carregar a informação selecionada referente ao campo no acesso à tela\.

Quando se tratar do arquivo do Sócio Ostensivo, exibir a descrição: “Ostensivo”\.

OS4316\-B

*\* Descrição não disponível em tela*

