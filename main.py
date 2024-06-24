from src.get_vacancy import get_company, get_vacancies, get_vacancies_list
from src.config import config
from src.ulils import create_database, save_data_to_database
import psycopg2


if __name__ == '__main__':
    params = config()
    data = get_vacancies(get_company())
    vacancies = get_vacancies_list(data)
    create_database("vacancy", params)
    save_data_to_database(vacancies, "vacancy", params)

