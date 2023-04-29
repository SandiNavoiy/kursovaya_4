from scr.abc import VacancyStorage


class Vacancy(VacancyStorage):
    def __init__(self, job_title: str = None, url_job: str = None, payment_range = None, requirements: str = None):
        if isinstance(job_title, str):
            raise ValueError('Параметр "job_title" должен быть строкой')
        self.job_title = job_title  # описание проффесии запроса

        if isinstance(url_job, str):
            raise ValueError('Параметр "url_job" должен быть строкой')
        self.url_job = url_job  # урл запроса

        if isinstance(payment_range, str):
            raise ValueError('Параметр "payment_range" должен быть строкой')
        self.payment_range = payment_range  # уровень заработной платы(диапазон)

        if isinstance(requirements, str):
            raise ValueError('Параметр "requirements" должен быть строкой')
        self.requirements = requirements  # требования

    def read_file_favourites(self, file_name):
        """просмотр файла с избраными вакансиями"""
        with open(file_name, 'r', encoding="utf8") as file:
            f = file.read()
            print(f)

