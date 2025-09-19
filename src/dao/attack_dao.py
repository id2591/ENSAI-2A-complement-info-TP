from typing import List, Optional
from dao.type_attack_dao import TypeAttackDAO
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from business_object.attack.abstract_attack import AbstractAttack
from business_object.attack.attack_factory import AttackFactory


class AttackDao(metaclass=Singleton):
    def add_attack(self, attack: AbstractAttack) -> bool:
        """
        Add an attack to the database
        """
        created = False

        # Get the id type
        id_attack_type = TypeAttackDAO().find_id_by_label(attack.type)
        if id_attack_type is None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tp.attack (id_attack_type, attack_name,        "
                    " power, accuracy, element, attack_description)             "
                    "VALUES                                                     "
                    "(%(id_attack_type)s, %(name)s, %(power)s, %(accuracy)s,    "
                    " %(element)s, %(description)s)                             "
                    "RETURNING id_attack;",
                    {
                        "id_attack_type": id_attack_type,
                        "name": attack.name,
                        "power": attack.power,
                        "accuracy": attack.accuracy,
                        "element": attack.element,
                        "description": attack.description,
                    },
                )
                res = cursor.fetchone()
        if res:
            attack.id = res["id_attack"]
            created = True

        return created
    

    def find_attack_by_id(self, id: int) -> AbstractAttack:
        """
        Get all attack type names and return a list

        :return: An attack
        :rtype: An AbstractAttack
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        a.id_attack,
                        a.power,
                        a.accuracy,
                        a.element,
                        a.attack_name,
                        a.attack_description,
                        at.attack_type_name,
                    FROM tp.attack a
                    JOIN tp.attack_type at
                        ON a.id_attack_type = at.id_attack_type
                    WHERE a.id_attack = %(id_attack)s
                    """,
                    {
                        "id_attack": id,
                    },
                )
                row = cursor.fetchone()
        
        if row is None:
            return None
        else:
            return AttackFactory().instantiate_attack(
                type=row["attack_type_name"],
                id=row["id_attack"],
                power=row["power"],
                name=row["attack_name"],
                description=row["attack_description"],
                accuracy=row["accuracy"],
                element=row["element"]
            )


    def find_all_attacks(self) -> List[str]:
        """
        Get all attack type names and return a list

        :return: A list of all attacks
        :rtype: List of str
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    
                )

                # to store raw results
                res = cursor.fetchall()

        # Create an empty list to store formatted results
        attack: List[str] = []

        # if the SQL query returned results (ie. res not None)
        if res:
            for row in res:
                type_attack.append(row["attack_name"])

                print(row["id_attack"])
                print(row["attack_name"])
                print(row["attack_description"])

        return attack

if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv
    from business_object.attack.physical_attack import PhysicalFormulaAttack

    dotenv.load_dotenv(override=True)

    # Création d'une attaque et ajout en BDD
    mon_attaque = PhysicalFormulaAttack(
        power=50,
        name="chatouille",
        description="guili-guilis",
        accuracy=90,
        element="Normal",
    )

    succes = AttackDao().add_attack(mon_attaque)
    print("Attack created in database : " + str(succes))
