from arquivo import Arquivo

__author__ = 'mae'


class EventoDAO(object):
    def salvar_evento(self,id,nome):
         evento_arquivo=Arquivo()
         evento_arquivo.salvar("evento.csv",[id,nome])


if __name__ == "__main__":
    evento_dao=EventoDAO()
    evento_dao.salvar_evento("1","Nome do Evento")
