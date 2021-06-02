cd $(Split-Path -Parent $MyInvocation.MyCommand.Definition)
cd ..

pip install -r server/requirements.txt
sqlite server/src/erp.db < server/database.sql

cd client
npm install