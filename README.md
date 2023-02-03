# Code Review: Airflow pt 1

#### By Drew White

#### Code Review - Demonstrating the use of Apache Airflow. 

## Technologies Used


* Python
* Apache Airflow
* Docker

</br>

## Description:
<img src="./images/apple_dag.png" width=60% height=60%>

- In the `code_review.py` - DAG
- DAG contains the following tasks:
  -  Task 1. An `echo_to_file` task that uses a Bash operator. This task will echo name, and redirect the output into a file called `code_review.txt` that's in the same directory as the `code_review.py` file
  -  Task 2. A `greeting` task that uses a Python operator to call a Python function called `print_hello()`, it opens `code_review.txt`, reads your name from that file, and prints a greeting that includes your name.
  -  Task 3. A task using a Bash operator, which echos `"picking three random apples"`.
  -  Tasks 4, 5, and 6 are three Python operator tasks that will run simultaneously. Each task:
        - [x] Has a unique task ID
        - [x] Use a python_callable, `random_apple`. This function should randomly select an apple from the `APPLES` list, put it into a string, and print that string
  -  Task 7.  DAG ends with an empty operator.

<br>

## Setup/Installation Requirements

* Clone by inputting following into terminal: 
  ```bash
  git clone https://github.com/Drewrwhite/data_week_11.git
  ```
* Navigate to directory:
  ```bash
  cd <directory>
  ```
* Create a virtual environment:
  ```bash
  python3.7 -m venv venv
  ```
* Activate virtual environment:
  ```bash
  source venv/bin/activate
  ```
* Install requirements:
  ```bash
  pip install -r requirements.txt
  ```
* Open directory in VSCode:
  ```bash
  code .
  ```
* Run setup:
  ```bash
  sh setup.sh
  ```
* Navigate to dsa-airflow:
  ```bash
  cd dsa-airflow
  ```
* Download docker compose yml:
  ```bash
  curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
  ```
* Write airflow uid and airflow gid into a .env file:
  ```bash
  echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
  ```
* Make directories for logs and plugins:
  ```bash
  mkdir ./logs ./plugins
  ```
* Initialize airlflow:
  ```bash
  docker-compose up airflow-init
  ```
* Start docker containers:
  ```bash
  docker-compose up
  ```
* Open up Airflow in browser:
  ```bash
  http://0.0.0.0:8080/home
  ```
* When done using Airflow:
  ```bash
  docker-compose down --volumes --remove-orphans
  ```
  ```bash
  docker system prune -f --volumes
  ```
</br>

## Known Bugs

* No known bugs

<br>

## License

[MIT](./license.txt)

_If you find any issues, please reach out at: **d.white0002@gmail.com**._

Copyright (c) _2023_ _Drew White_

</br>
