from structure.models import *

def run():
    organizations = Organization.objects.all() # Доступные организации(универы)
    for organization in organizations:
        print(organization.title)
        collegial_bodies = organization.collegial_bodies.all() # Доступные коллегиальные органы
        for collegial_body in collegial_bodies:
            print('---', collegial_body.title)
            """ 
                В структуре коллегиального органа могут быть
                как сотрудники, так и административные органы 
            """
            positions = collegial_body.positions.all() # Имеющиеся должности
            for position in positions:
                employees = position.persons.all() # Сотрудники с определенной должностью
                for employee in employees:
                    print('------', position.title, employee.fullname)
            administrative_bodies = collegial_body.administrative_bodies.all() # Доступные административные органы 
            for administrative_body in administrative_bodies:
                """ 
                    В структуре административного органа могут быть только руководящие лица
                """
                print('------', administrative_body.title)
                directors = administrative_body.directors.all() # Имеющиеся руководители
                for director in directors:
                    """ 
                        Руководящие лица могут иметь как сотрудников, так и свои подразделения
                    """
                    print('---------', director.title, director.person.fullname)
                    subdivisions = director.subdivisions.all()  # Имеющиеся подразделения
                    for subdivision in subdivisions:
                        """ 
                            В структуре подразделения могут быть 
                            как сотрудники, так и руководящие лица
                        """
                        print('------------', subdivision.title)
                        subdivision_directors = subdivision.directors.all() # Имеющиеся руководители подразделения
                        for subdivision_director in subdivision_directors:
                            """ 
                                Руководящие лица могут иметь только сотрудников
                            """
                            print('---------------', subdivision_director.title, subdivision_director.person.fullname)
                            positions = subdivision_director.positions.all()   # Имеющиеся должности
                            for position in positions:
                                employees = position.persons.all() # Сотрудники с определенной должностью
                                for employee in employees:
                                    print('------------------', position.title, employee.fullname)
                        positions = subdivision.positions.all()   # Имеющиеся должности
                        for position in positions:
                            employees = position.persons.all() # Сотрудники с определенной должностью
                            for employee in employees:
                                print('---------------', position.title, employee.fullname)
                    positions = director.positions.all()   # Имеющиеся должности
                    for position in positions:
                        employees = position.persons.all() # Сотрудники с определенной должностью
                        for employee in employees:
                            print('------------', position.title, employee.fullname)

