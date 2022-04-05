# Escalacao
get_equipes = 'SELECT equipe FROM escalacao;'
get_usuarios_equipe = 'SELECT user FROM escalacao WHERE equipe=%s'
set_equipe_usuarios = 'UPDATE escalacao SET users=array_append(users, %s) WHERE equipe=%s;'