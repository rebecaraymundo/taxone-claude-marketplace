# MTZ_GIA_SP_Tela_Codigo_de_DIPAM_B_x_CFOPs_ou_Natureza_Reg30

- **Fonte:** MTZ_GIA_SP_Tela_Codigo_de_DIPAM_B_x_CFOPs_ou_Natureza_Reg30.docx
- **Modificado:** 2022-09-28
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Nova Gia V8\.0 / DIPAM\-B – Reg\.30

Tela de Código de DIPAM\-B x CFOP´s – Reg\.30

Tela de Código de DIPAM\-B x CFOP´s/ Natureza de Operação – Reg\.30

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

CH12822\_2015

Lara Aline

<a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK19"></a>Inclusão de tratamento para recuperação de estabelecimentos da opção “Replicar p/ os Estabelecimentos”\.

MFS\-13943

Andréa Rocha

Inclusão do código 2\.7 da DIPAM para atender as empresas que fazem vendas presenciais com saídas em outro estabelecimento\.

MFS42617

Andréa Rocha

Inclusão de uma coluna nova para o código 12 da DIPAM\-B

MFS90036

Aline Melo

Ajuste na regra do campo “Replicar para os Estabelecimentos”\.

Sumário

[1\.	Regras dos Campos	3](#_Toc393375277)

# <a id="_Toc350763252"></a><a id="_Toc393375277"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\GIA\-SP\\Parâmetros\\Nova Gia V8\.0 \(V0210\)\\DIPAM\-B – Reg\.30\\Código de DIPAM\-B x CFOP´s – Reg\.30 ou Código de DIPAM\-B x CFOP´s/ Natureza de Operação – Reg\.30

__Título da tela: __Código de DIPAM\-B x CFOP´s – Reg\.30 ou Código de DIPAM\-B x CFOP´s/ Natureza de Operação – Reg\.30\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

DIPAM \- B

Texto

S

S

Formato:

Check Box

Default:

Habilitado

Nesse campo o usuário poderá selecionar o código de item da DIPAM que deseja parametrizar o CFOP ou Natureza para geração das informações de forma automática no Registro 30\.

__\[ALTERADA – MFS\-13943\]__

__Conteúdo:__

11\-Compra de Mercadoria;

22\-Operações de Vendas realizadas por Autônomos;

23\-Transporte Interestadual e Intermunicipal;

24\-Serviço de Comunicação;

25\-Fornecimento de Energia Elétrica;

26\-Rateio do valor adicionado;

27\-Vendas presenciais com saídas/ vendas efetuadas em estab\. diverso de onde ocorreu a transação/negociação inicial;

31\-Multas / auto infração;

35\-Ajustes\.

MFS\-13943

Lançar NF Escrituradas

Texto

S

S

Formato:

Listbox

Default:

Habilitado

Nesse campo o usuário poderá selecionar a forma de lançar a nota fiscal escriturada para o código 12  da DIPAM\.

Este campo é uma lista fixa de opções:

\- Sim

\- Não

Somente deve ser habilitado  para a operação “SPDIPAM12”\.

Default = Não

MFS42617

Replicar para os Estabelecimentos

Texto

N

S

Formato:

Check Box

Default:

Habilitado

Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos\.

__\[ALTERADA – CH12822\_2015\]__

Ao clicar na opção “Replicar”, serão disponibilizados para seleção do usuário os estabelecimentos com UF igual a ”SP” da Empresa do login, com exceção do estabelecimento já informado no campo “Estabelecimento”\.

MFS90036

Ao clicar na opção “Replicar” serão disponibilizados somente os  estabelecimentos selecionados no campo “Replicar para os Estabelecimentos” da tela de Dados Iniciais\. Os campos devem vir desmarcados e podem ser marcados um de cada vez ou através do botão “Marcar Todos”\.

Ao salvar a operação com esta opção ativada, a parametrização feita será gravada para o estabelecimento informado, e também replicada para todos os estabelecimentos selecionados na opção da replicação\. 

Para facilitar, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”\.

CH12822\_2015

MFS90036

