# MTZ-Relatorios_Documento_Fiscal_ICMS_IPI

- **Fonte:** MTZ-Relatorios_Documento_Fiscal_ICMS_IPI.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

	

THOMSON REUTERS

__ICMS – Relatório de Conferência \- Documento Fiscal ICMS/IPI__

__Localização: __Módulo ICMS,  Menu Operacional 🡪 Conferências 🡪 Documento Fiscal ICMS/IPI

##### DOCUMENTO DE REQUISITO

__Data__

__OS/CH__

__Nome__

__Descrição__

29/12/2014

OS4692

Jefferson Mota

Permiti a seleção de todos os Estabelecimentos de mesma UF \-  Relatório de Documento Fiscal ICMS/IPI\.

A OS4692 alterou este relatório para mudança, Incluindo filtro por UF no relatório de Conferência ICMS/IPI, de forma que sejam geradas as informações de TODOS os Estabelecimentos daquela determinada UF\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

__RN01__

__Regra do Relatório de Documento Fiscal ICMS/IPI \- Inclusão de Filtro por UF:__

__Localização: __Módulo ICMS  

__Menu:__ Operacional 🡪 Conferências 🡪 Documento Fiscal ICMS/IPI

__Regra Geral:__ O filtro por UF, será incluído antes do campo de indicação do estabelecimento e quando for selecionada uma UF específica, serão listados apenas os estabelecimentos pertencentes a UF\. Se for selecionado a opção “Todos” do campo estabelecimento, o relatório será gerado considerando todos os estabelecimentos da UF selecionada\.

\-  O novo campo  “__UF__” deve ser um combo Box e deve exibir todas as UF’s para seleção do usuário, com os critérios abaixo:

1 \- A primeira opção de seleção deve ser NULO, caso o usuário não queira utilizar esse filtro;

2 \- Caso o usuário selecione determinada UF, somente devem ser gerados os dados referentes a UF selecionada\.

Também deverá ser verificado as condições à seguir:

 Se a __UF__ não for selecionada,  deverá considerar o Estabelecimento selecionado no campo “Estabelecimento”\.

Se não,

Se for selecionado “Todos” os estabelecimento, o relatório será gerado considerando todos os estabelecimentos de todas as UF\.

Se não,

Se o usuário selecionar uma UF específica, serão listados apenas os estabelecimentos pertencentes a UF indicada\.

E

Se caso for selecionado “Todos” os estabelecimentos, o relatório será gerado considerando todos os estabelecimentos da UF selecionada\. 

__OS4692__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

