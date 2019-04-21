

class Disciplina:
    '''
    Abstração de uma disciplina, possui os atributos Nome e carga Horária
    '''
    def __init__(self, nome: str, carga_horaria: int) -> None:
        self._nome =  nome
        self._carga_horaria =  carga_horaria
        
        
        
    
    def get_nome(self) -> str:
        '''
        Acessor do atributo nome
        '''
        return self._nome

    def get_carga_horaria(self) -> int:
        '''
        Acessor do atributo cargar horaria
        '''
        return self._carga_horaria


class Pessoa:
    '''
    Abstração de uma pessoa no Modelo, classe base para Aluno e Professor
    que contém dados pertencentes a ambos.
    '''
    def __init__(self, nome: str, telefone: int, email: float) -> None:
        self._nome = nome
        self._telefone =  telefone
        self._email =  email



    def get_nome(self) -> str:
        '''
        Acessor do atributo Nome
        '''
        return self._nome


    def get_telefone(self) -> int:
        '''
        Acessor do atributo telefone
        '''
        return self._telefone


    def set_telefone(self, novo_telefone: int) -> None:
        '''
        Mutador do atributo telefone deve checar se é um número inteiro e,
        caso contrário devolver um TypeError
        '''
        if not type(novo_telefone) == int:
            #valor de erro
            raise TypeError
        else:
            self._telefone =  novo_telefone

    def get_email(self) -> str:
        '''
        Acessor do atributo email
        '''
        return self._email

    def set_email(self, novo_email) -> None:
        '''
        Mutador do atributo email, deve checar se é um email válido
        (se possuir o caractere '@') e caso contrário devolver
        um ValueError
        '''
        if '@' not in novo_email:
            raise ValueError
        else:
            self._email = novo_email


class Aluno(Pessoa):

    def __init__(self, nome: str, telefone: int,
                 email: str, n_matricula: int) -> None:
        self._nome =  nome
        self._telefone =  telefone
        self._email  = email
        self._n_matricula =  n_matricula
        
        Pessoa.__init__(self,nome,telefone,email)
        self._disciplina = []

    def get_matricula(self) -> int:
        '''
        Acessor do atributo matricula
        '''
        return self._n_matricula


    def matricular(self, disciplina: Disciplina) -> None:
        '''
        Realiza matrícula do Aluno na disciplina
        '''
        return self._disciplina.append(disciplina)

        


       
    def lista_disciplinas(self) -> list:
        '''
        Devolve a lista de disciplinas em que o aluno esta matriculado
        '''
        return self._disciplina 

class Professor(Pessoa):
    '''
    Entidade professor do Modelo
    '''
    def __init__(self, nome, telefone, email):
        self._nome =  nome
        self._telefone =  telefone
        self._email =  email

        Pessoa.__init__(self,nome,telefone,email)
        self._disciplina_professor = []
        


        
        

    def ministra(self, disciplina: Disciplina) -> None:
        '''
        Atribui o professor como ministrante da disiciplina
        Um professor não pode dar mais de 200 horas de aula,
        Caso um professor tente atribuir mais de 200h devolve
        ValueError
            '''
        horas_de_aula = 0
        for horas in self.lista_disciplinas():
            horas_de_aula += horas._carga_horaria

        if horas_de_aula + disciplina._carga_horaria > 200:
            raise ValueError
        else:
            return self._disciplina_professor.append(disciplina)
        

        

    def lista_disciplinas(self) -> list:
        '''
        lista as disciplinas ministradas pelo professor
        '''
        
        return self._disciplina_professor
        
    
        
        
