#!/bin/bash
# flask_boilerplate.sh

if [ -z "$1" ]
then
  echo "No project name supplied"
  exit 1
fi

PROJECT_NAME=$1

mkdir -p $PROJECT_NAME/{app/{models,views,controllers,services,repositories,schemas,blueprints,extensions,static,templates},tests,migrations}

touch $PROJECT_NAME/app/{__init__.py,models/__init__.py,views/__init__.py,controllers/__init__.py,services/__init__.py,repositories/__init__.py,schemas/__init__.py,blueprints/__init__.py,extensions/__init__.py}
touch $PROJECT_NAME/manage.py $PROJECT_NAME/config.py $PROJECT_NAME/requirements.txt $PROJECT_NAME/.env

echo "Flask project $PROJECT_NAME has been created successfully!"
