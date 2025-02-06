#!/bin/sh

echo "Checking if migration is needed..."
if python3 manage.py showmigrations | grep '\[ \]'; then
    echo "Running database migrations..."
    python3 manage.py migrate
else
    echo "Migrations are already applied."
fi

echo "Checking if seeding is needed..."
if ! python3 manage.py shell -c "from users.models import CustomUser; print(CustomUser.objects.exists())" | grep "True"; then
    echo "Seeding database with initial data..."
    python3 manage.py seed
else
    echo "Database already seeded."
fi

echo "Starting Django server..."
python3 manage.py runserver 0.0.0.0:8000
