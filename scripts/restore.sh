cd $(cd $(dirname ${BASH_SOURCE[0]})/..; pwd)

pip install -r server/requirements.txt
sqlite server/src/erp.db < server/database.sql

cd client
npm install