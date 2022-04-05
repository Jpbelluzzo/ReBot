# Escalacao
get_equipes = 'SELECT UPPER(equipe) FROM escalacao;'
get_usuarios_equipe = 'SELECT users FROM escalacao WHERE equipe=%s'
set_equipe_usuarios = 'UPDATE escalacao SET users=array_append(users, %s) WHERE UPPER(equipe)=UPPER(%s);'