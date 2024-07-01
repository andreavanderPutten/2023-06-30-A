from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getSquadre():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(t.teamcode), t.
        from lahmansbaseballdb.teams t """

        cursor.execute(query, )

        for row in cursor:
            result.append([row["codice"],row["nome"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(squadra):
            conn = DBConnect.get_connection()

            result = []

            cursor = conn.cursor(dictionary=True)
            query = """select distinct year 
            from teams 
            where name = %s
            order by ASC"""

            cursor.execute(query,(squadra,))

            for row in cursor:
                result.append(row)

            cursor.close()
            conn.close()
            return result
