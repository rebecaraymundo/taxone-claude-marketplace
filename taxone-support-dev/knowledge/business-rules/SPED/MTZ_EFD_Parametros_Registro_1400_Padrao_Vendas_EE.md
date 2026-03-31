# MTZ_EFD_Parametros_Registro_1400_Padrao_Vendas_EE

> Fonte: MTZ_EFD_Parametros_Registro_1400_Padrao_Vendas_EE.doc

Módulo Sped Fiscal – Parametrização das Operações Específicas de Venda de Energia Elétrica (Modelo 55) p/o Cálculo do Valor Adicionado (registro 1400)

Localização: Menu Estadual, Módulo EFD, menu Parâmetros( Registro 1400 ( Padrão ( Operações Específicas de Venda de EE (Modelo 55)
 
                                                                                                                                                                                         ( CFOP
                                                                                                                                                                                         ( CFOP / Natureza de Operação


DOCUMENTO DE REQUISITO

DR	Descrição	Alteração	Data Alteração		OS4045	Alterações na Geração do Registro 1400 do Sped Fiscal 	Criação do documento	28/05/2013		

RN00	Regra Geral:

Esta parametrização foi criada na OS4045 para atender a legislação de SC em relação à inclusão das operações de vendas “diferenciadas” de energia elétrica no cálculo do valor adicionado (registro 1400). Ver detalhes no requisito da OS4045.

Na opção “Por CFOP / Natureza de Operação”:
Apenas na opção de parametrização por CFOP e Natureza, na abertura da tela, será exibida uma janela para seleção do Grupo de Estabelecimento a ser utilizado para acessar a tabela de relacionamento CFOP X Naturezas (SAFX2081). 
Na janela de seleção serão exibidos os seguintes Grupos de Estabelecimentos:
  
  Se for informado estabelecimento no login
         Neste caso a janela exibirá apenas os Grupos referentes ao estabelecimento informado; 
   Senão
        Neste caso serão exibidos todos os Grupos referentes a estabelecimentos da Empresa, de forma geral;

(verificar as regras específicas de funcionamento de cada campo nas regras descritas a seguir)
		RN01	Campo Estabelecimento:

Na opção “Por CFOP”:

Este campo exibirá o Estabelecimento informado no login, ou a lista dos Estabelecimentos da Empresa, quando não for informado nenhum estabelecimento no login.

Na opção “Por CFOP / Natureza de Operação”:

Neste caso, será exibido o Estabelecimento selecionado pelo usuário através da janela de seleção dos Grupos de Estabelecimento, exibida na abertura da tela, ou da opção de seleção de grupo disponível na barra de menu.
O campo não será habilitado para alteração, pois a alteração do Grupo de Estabelecimento a ser utilizado só poderá ser feita através da opção de seleção de grupo da barra de menu.
		RN02	Campo Grupo Natureza:

(campo específico do menu de parametrização por CFOP e Natureza de Operação)

Neste campo será exibido o Grupo de Relacionamento selecionado pelo usuário através da janela de seleção dos grupos, exibida na abertura da tela, ou da opção de seleção de grupo disponível na barra de menu.

Este campo não é habilitado para alteração, pois a alteração do grupo só poderá ser feita através da opção de seleção de grupo da barra de menu.
  		RN03	Campo CFOP’s:

(campo específico do menu de parametrização por CFOP)

No quadro dos CFOP’s será exibida  lista dos CFOP’s, considerando apenas os CFOP’s de saída.
Nos casos em que existir mais de um registro do mesmo CFOP, mas com diferentes datas de validade, será exibida apenas uma ocorrência do CFOP.
		RN04	Campo CFOP’s / Naturezas de Operação:

(campo específico do menu de parametrização por CFOP e Natureza de Operação)

No quadro dos CFOP’s e Naturezas será exibida a lista das as combinações de CFOP + Natureza existentes na Tabela de Associação CFOP x Naturezas (SAFX2081). 
Serão considerados apenas os CFOP’s, de saída.
Serão consideradas apenas as naturezas de operação associadas ao grupo informado pelo usuário na abertura da tela (ver RN00). 
		RN05	Campo Replicar p/os Estabelecimentos:
Este campo aparecerá desmarcado por default, e quando selecionado, os dados parametrizados serão replicados para os estabelecimentos selecionados pelo usuário no quadro dos Estabelecimentos.