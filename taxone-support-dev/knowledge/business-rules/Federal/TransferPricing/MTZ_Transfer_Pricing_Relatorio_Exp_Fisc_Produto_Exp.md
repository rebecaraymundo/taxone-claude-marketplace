# MTZ_Transfer_Pricing_Relatorio_Exp_Fisc_Produto_Exp

- **Fonte:** MTZ_Transfer_Pricing_Relatorio_Exp_Fisc_Produto_Exp.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Relatório de Exposição Fiscal por Produto \(Exportação\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-5401

Inclusão de botão “Exportar para Excel”

Botão irá exportar o conteúdo do relatório para um doc \.xls

Sumário

[1\.	TELA A SER DESENVOLVIDA	3](#_Toc402370510)

[1\.1\.	Diagrama de Casos de Uso	3](#_Toc402370511)

[1\.1\.1\.	UC001 – Manutenção da Estrutura Padrão	3](#_Toc402370512)

[1\.1\.1\.1\.1\.	Fluxo Principal	3](#_Toc402370513)

[1\.1\.1\.1\.2\.	Fluxo Alternativo 1 – Localizar registros \(Exemplo\)	4](#_Toc402370514)

[2\.	REGRAS DOS CAMPOS	5](#_Toc402370515)

[2\.1\.	Layout da Tela	5](#_Toc402370516)

[3\.	REGRAS DE GERAÇÃO DO RELATÓRIO	5](#_Toc402370517)

[3\.1\.	Layout do Relatório	6](#_Toc402370518)

# <a id="_Toc402370510"></a>TELA A SER DESENVOLVIDA

\[Incluir o diagrama de caso de uso e casos de uso correspondentes, conforme exemplos a seguir\]

## <a id="_Toc350763243"></a><a id="_Toc402370511"></a>Diagrama de Casos de Uso 

__ __

__UC Estrutura Padrão__

__Usuário __

__UC001 – Manutenção da   __

__Estrutura Padrão__

Manutenção Padrão

## <a id="_Toc350763244"></a><a id="_Toc402370512"></a>UC001 – Manutenção da Estrutura Padrão

\[Descrever a ação deste caso de uso\. 

Ex\.: Este caso de uso descreve o processo de Cadastro de Estrutura Padrão\.\]

__Documentação do Caso de Uso__

__Ator Principal__

\[Quem executará o evento\. Ex\.: Usuário do sistema\]\.

__Pré\- Condições__

\[Condições necessárias para execução\. Ex\.: Estabelecimento cadastrado\]

__Pós\-Condições__

\[Resultado após executar caso de uso\. Ex\.: Informação armazenada no banco de dados\]

### <a id="_Toc332809652"></a><a id="_Toc332888915"></a><a id="_Toc350763245"></a><a id="_Toc402370513"></a>Fluxo Principal 

\[Descrever a ação principal que será realizada na tela especificada\.

 Ex\.: O usuário deseja realizar o cadastro de uma estrutura padrão\.

__Ações do Ator__

__Ações do Sistema__

### <a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>

### <a id="_Toc402370514"></a>Fluxo Alternativo 1 – Localizar registros \(Exemplo\)

__Ações do Ator__

__Ações do Sistema__

# <a id="_Toc350763252"></a><a id="_Toc402370515"></a>REGRAS DOS CAMPOS 

__Localização da tela:__ \[Caminho de acesso à tela\. Ex\.: \\Menu\\Manutenção – Digitação – Consulta\\Tabelas Gerais\\Cadastros\]

__Título da tela: __\[Nome da tela\. Ex\.: Manutenção de Estrutura Padrão\]

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

\[Campo especificado na tela\]

Ex\.: Código do Material\]

Tipo da informação

Ex\.:

Texto,

Numérico,

Data\]

S/N

Editá\-vel

S/N\]

Formato: 

DD/MM/AA, 0,000, 

Default: Habilitado/Desabilitado

Definições do campo\. 

Ex\.: Permite que o usuário informe o código do material

\[OS / CH\]

## <a id="_Toc402370516"></a>Layout da Tela

\[sugestão de layout da tela\]

# <a id="_Toc402370517"></a>REGRAS DE GERAÇÃO DO RELATÓRIO

#  

__Origem das informações para geração:__ Para geração deste relatório deverá existir cadastro de produto e selecionado os métodos para cálculo\.

__Regra de seleção:__ O objetivo deste relatório será apresentar a exposição fiscal de por produtos \(Importação\) conforme seleção por empresa\.

__Regra de agrupamento: __

__Ordenação: __

#     REGRA DOS CAMPOS

__                    Localização da tela: __

                    TranferPricing

                        Menu: Relatório 🡪  Exp\. Fisc\./ Produto \(Exp\)

__Título do Relatório: __Exposição Fiscal por Produto \(Exportação\)

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Exportar para Excel

Botão

N

N

Quando acionado irá exportar o conteúdo do relatório para um documento \.xls\.

MFS5401

