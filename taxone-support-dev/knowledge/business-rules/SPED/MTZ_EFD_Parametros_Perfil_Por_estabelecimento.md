# MTZ_EFD_Parametros_Perfil_Por_estabelecimento

> Fonte: MTZ_EFD_Parametros_Perfil_Por_estabelecimento.doc

Módulo Sped Fiscal – Perfil Por Estabelecimento

Módulo: SPED ( EFD – Escrituração Fiscal Digital
Menu: Parâmetros ( Perfil por estabelecimento

DOCUMENTO DE REQUISITO

DR	Nome	Descrição	Data Alteração		OS-2388-A7	Criação do menu “Perfil por estabelecimento”	Criação de uma tela para associação do perfil ao estabelecimento.	29/06/2011		
REGRAS DE NEGÓCIO


Regra 	Descrição	DR		RN00	Regras gerais

(espaço reservado para regras genéricas, que não dizem respeito a campos específicos)

		


RN01	Criação do menu “Perfil por Estabelecimento”

Criar um menu “Perfil por Estabelecimento” dentro de “Parâmetros”, como segue abaixo:

Módulo: SPED ( EFD – Escrituração Fiscal Digital
Menu: Parâmetros ( Perfil por Estabelecimento.

	


OS-2388-A7		


RN02	Criação de nova tela para associar os estabelecimentos ao perfil:

Criação de uma nova tela com a descrição “Perfil por estabelecimento – EFD – Escrituração Fiscal Digital”.
Esta nova tela deverá ser posicionada no seguinte local:

Módulo: SPED ( EFD – Escrituração Fiscal Digital
Menu: Parâmetros ( Perfil por Estabelecimento

Campos:

              Perfil (Cod./Desc.):
              O cliente poderá pesquisar o perfil o perfil desejado conforme o que foi cadastrado no menu “Perfil. Vide caminho na regra RN01.
A pesquisa será feita quando o cliente clicar no menu abrir da própria barra do Mastersaf.


              Leiaute: Preencher o campo Layout automaticamente após a escolha do perfil, conforme o que foi cadastrado no menu “Perfil”. Vide caminho na regra RN01.

              Estabelecimentos:
              Abaixo deste campo deve conter uma lista de Checkbox’s com todos estabelecimentos da empresa, onde o cliente selecionará apenas os que interessam para o perfil escolhido.


Botões:

Selecionar Todos: Ao ser ativado, selecionar todos estabelecimentos.
Desmarcar Todos: Ao ser ativado, desmarcar todos estabelecimentos.

	


OS-2388-A7