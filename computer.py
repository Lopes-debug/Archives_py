from pathlib import Path  #acessar caminho de pastas do note
import shutil  #mover e fazer cópias dos arquivos

# printar caminho onde o python está trabalhando
# print(Path.cwd())

# salvar o caminho da pasta na variável
# local = Path('C:/Users/leand/OneDrive/Documentos/hashtag/f_archives_folders/Arquivos_Lojas')

# ler cada arquivo do local
# arquivos = Path.iterdir(local)

# percorrer cada arquivo para exibir cada arquivo
# for arquivo in arquivos:
#     print(arquivo)

# criar nova pasta
# pasta_nova = Path('caminho onde criará a pasta nova').mkdir()

# verificar se arquivo está dentro da pasta
# if (local / Path('201801_Amazonas Shopping_AM.csv')).exists():  #caminho / nome do arquivo
#     print('existe')

# # criar cópia de um arquivo
# arquivo_original = Path('Arquivos_Lojas/')
# copia = Path('pasta_di_colina/test')
# shutil.copy2('Arquivos_Lojas\201801_Barra Shopping_RJ.csv' , 'f_archives_folders\test_barra.csv') #local exato do arquivo original, local da copia e nome da copia


# EXERCICIO 1

# local = Path(r'C:\Users\leand\OneDrive\Documentos\hashtag\f_archives_folders\Arquivos_Lojas')

# arquivos = Path.iterdir(local)

## MINHA TENTATIVA
# RJ, SP MG AM, GO
# for arquivo in arquivos:
#     # identificar arquivos do mesmo Estado
#     string = str(arquivo)
#     pos = string.find('201801')
#     if 'RJ' in string[pos:]:
#         # criar copia dos arquivos e salvar em pastas separadas
#         shutil.copy2(local,r'C:\Users\leand\OneDrive\Documentos\hashtag\f_archives_folders\Arquivos_Lojas\pasta_di_colina\{}copia.csv'.format(arquivo))


## GABARITO

# estados = ['RJ','SP','MG','AM','GO']
# for estado in estados:
#     Path(r'C:\Users\leand\OneDrive\Documentos\hashtag\f_archives_folders\Arquivos_Lojas\pasta_di_colina\{}folder.csv'.format(estado)).mkdir()

# definir caminho dos arquivos
caminho = Path(r'C:\Users\leand\OneDrive\Documentos\hashtag\f_archives_folders\Arquivos_Lojas')
arquivos = caminho.iterdir()
#  percorrer arquivos
for arquivo in arquivos:
# filtrar arquivos
    arquivo_name = arquivo.name
    if arquivo_name[-3:] == 'csv':
        estados = arquivo_name[-6:-4]
# mover cada arquivo para sua pasta destino
        caminho2 = Path(r'C:\Users\leand\OneDrive\Documentos\hashtag\f_archives_folders\Arquivos_Lojas\pasta_di_colina')
        local_final = caminho2 / Path('{}folder.csv/{}'.format(estados, arquivo_name))
        shutil.move(arquivo , local_final)




