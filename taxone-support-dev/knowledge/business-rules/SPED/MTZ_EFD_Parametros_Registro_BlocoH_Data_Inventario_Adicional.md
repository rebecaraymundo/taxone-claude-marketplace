# MTZ_EFD_Parametros_Registro_BlocoH_Data_Inventario_Adicional

> Fonte: MTZ_EFD_Parametros_Registro_BlocoH_Data_Inventario_Adicional.docx






THOMSON REUTERS

Módulo EFD Escrituração Fiscal Digital
Tela de Data do Inventário Adicional




DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	3
2.	Layout de Tela	5

## Regras dos Campos


Localização da tela: Menu SPED,  Módulo: EFD Escrituração Fiscal Digital, item de menu Parâmetros  Registros (Bloco H)  Data do Inventário Adicional

Título da tela: Data do Inventário Adicional

Considerações Gerais:

Poderão ser parametrizado “N” (vários) códigos nessa parametrização.

Opções da barra de menu:

NOVO – Limpa todos os campos da tela, com exceção do estabelecimento, permitindo a inclusão de um novo registro;

ABRE – Ao clicar nesta opção, serão exibidos para seleção do usuário todos os dados já parametrizados. O usuário poderá selecionar um registro, e seus dados serão exibidos em tela para consulta / alteração / exclusão;

EXCLUI – Permite a exclusão dos dados.

CONFIRMA – Salva os dados incluídos ou alterados.

RELATÓRIO – Para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado.

FECHA – Fecha a janela da parametrização.
















## Layout de Tela





| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS4106 | Criação do documento | Criação da Tela Data do Inventário Adicional | 06/05/2016 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N | Formato: <COD ESTAB> - <RAZÃO SOCIAL> | Neste campo será exibido o Estabelecimento escolhido pelo usuário, na Tela de Login do Sistema, não tendo a opção de escolha de outro Estabelecimento, apenas será habilitado para seleção caso o usuário não entre com o Estabelecimento na Tela de Login e esses Estabelecimentos serão os pertencentes à Empresa selecionada na Tela de Login do Sistema.  Tratamento: Se o Estabelecimento não for selecionado na Tela de Login e não for selecionado no parâmetro, ao salvar, emitir a mensagem: “Estabelecimento deve ser preenchido”. | MFS4106 |
| Período de Geração | Data | S | S | Default: Habilitado | Este campo é de preenchimento obrigatório deverá ser informado o período de geração correspondente da geração do Sped Fiscal. | MFS4106 |
| Data do Inventário | Data | S | S | Default: Habilitado | Este campo é de preenchimento obrigatório deverá ser informada a data de inventário correspondente ao período de geração informado. | MFS4106 |
| Legislação | Alfanumérico | N | S | Default: Habilitado | Este campo é de preenchimento não obrigatório e nele será possível detalhar qual a Legislação (Lei/Decreto/Portaria etc...) foi responsável pelo a inclusão da data do inventário adicional na geração no Bloco H do Sped Fiscal.  Características do Campo Tamanho: 150 | MFS4106 |
