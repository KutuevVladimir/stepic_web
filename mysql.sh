#!/usr/bin/env bash
sudo /etc/init.d/mysql restart
mysql -u root -e "CREATE DATABASE stepic_db;"
mysql -u root -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'sql';"
mysql -u root -e "GRANT ALL ON stepic_db.* TO 'django'@'localhost';"
mysql -u root -e "FLUSH PRIVILEGES;"
