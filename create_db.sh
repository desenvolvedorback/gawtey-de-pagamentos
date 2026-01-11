#!/bin/bash
# Use dentro do container backend para rodar alembic
alembic upgrade head
psql $DATABASE_URL -c "SELECT 1"
# Use dentro do container backend para testar a conexao com o banco
python -c "import psycopg2; conn = psycopg2.connect('$DATABASE_URL'); conn.close()"
# Use dentro do container backend para testar a conexao com o banco
echo "Database setup completed."
# Use dentro do container backend para rodar alembic
echo "Database setup completed."