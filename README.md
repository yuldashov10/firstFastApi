# firstFastApi

---

## Описание

- Тестовый проект, разработанный в книге "FastAPI - веб-разработка на Python" автора Билла Любановича.

---

## Команды

- Запуск `gunicorn`:

```shell
gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Базы данных

### Реляционные базы данных и SQL

Основные пакеты драйверов для `Python`

- sqlite
- psycopg
- asyncpg
- MySQLdb
- PyMySQL
- python-oracledb
- pyodbc
- pymssql
- ibm_db
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Records](https://github.com/kennethreitz/records)
- [EdgeDB](https://www.edgedb.com/)
- [EdgeQL](https://docs.edgedb.com/database/edgeql)

### Нереляционные (NoSQL) базы данных

- [Redis](https://redis.io/)
    - [redis-py](https://github.com/redis/redis-py)
- [MongoDB](https://www.mongodb.com/)
    - [PyMongo](https://pymongo.readthedocs.io)
    - Motor
- [Apache Cassandra](https://cassandra.apache.org/_/index.html)
    - [DataStax Driver for Apache Cassandra](https://github.com/datastax/python-driver)
- [Elasticsearch](https://www.elastic.co/elasticsearch)

---

## Файлы

- [python-multipart](https://github.com/Kludex/python-multipart/)
- [aiofiles](https://github.com/Tinche/aiofiles)


## Полезный материал

### Тестирование

- [locust](https://locust.io/)
- [PyPi: locust-grasshopper](https://pypi.org/project/locust-grasshopper/)

### HTTPS

- [Traefik](https://traefik.io/) -

### Облачные сервисы

- [FastAPI - Deployment](https://www.tutorialspoint.com/fastapi/fastapi_deployment.htm)
- [How to Deploy a FastAPI App on Heroku for Free](https://medium.com/towards-data-science/how-to-deploy-your-fastapi-app-on-heroku-for-free-8d4271a4ab9)
- [Deploying a FastAPI Application on Kubernetes](https://sumanta9090.medium.com/deploying-a-fastapi-application-on-kubernetes-a-step-by-step-guide-for-production-d74faac4ca36)

### Кэширование

- [functools — Higher-order functions and operations on callable objects](https://docs.python.org/3/library/functools.html)

### Очереди

- [Celery: Getting Started](https://docs.celeryq.dev/en/stable/getting-started/index.html)

### Python

- [PyPy](https://pypy.org/features.html)
- [PyPy: ускоряем Python](https://proglib.io/p/pypy-uskoryaem-python-s-minimalnymi-usiliyami-2020-11-26)
- [Cython: Basic Tutorial](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html#)
- [Modular: Mojo - Powerful CPU+GPU Programming](https://www.modular.com/mojo)

### Метрики

- [Prometheus](https://prometheus.io/)
- [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)
- [Grafana](https://grafana.com/)
- [Getting Started: Monitoring a FastAPI App with Grafana and Prometheus - A Step-by-Step Guide](https://dev.to/ken_mwaura1/getting-started-monitoring-a-fastapi-app-with-grafana-and-prometheus-a-step-by-step-guide-3fbn)
- [FastAPI Observability на сайте Grafana Labs](https://grafana.com/grafana/dashboards/16110-fastapi-observability/)
- [OpenTelemetry](https://opentelemetry.io/)
- [OpenTelemetry FastAPI Instrumentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/fastapi/fastapi.html)
- [Implementing OpenTelemetry in FastAPI - A Practical Guide](https://signoz.io/blog/opentelemetry-fastapi/)

### Базы данных

- [Му Experience with EdgeDB](https://divan.dev/posts/edgedb/)


### ИИ

- [Chroma](https://docs.trychroma.com/docs/overview/introduction)
- [Hugging Face](https://huggingface.co/)
- []()
- []()
