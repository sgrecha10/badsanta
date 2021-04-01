# badsanta

1. Нужно изменить кодировку БД на UTF8. Переводил вручную, в DBeaver.
2. Нужно перевести таблицы из MyISAM в InnoDB. Переводил вручную, в DBeaver.

ОШИБКИ

1. Ошибка "SQL Error [1067] [42000]: Invalid default value for 'date0' Invalid default value for 'date0' Invalid default value for 'date0'"
   Лечение: заходим в контейнер в бд и устанавливаем новое значение переменной sql_mode.

   $ docker exec -it badsanta_mysql bash
   :/# mysql -u root -p mysql -D disco


2. Ошибка "SQL Error [1031] [HY000]: Table storage engine for '#sql-1_1b' doesn't have this option"
   Лечение: для каждой глючной таблицы изменить ROW_FORMAT
   mysql> ALTER TABLE `types2` ROW_FORMAT = DEFAULT ;



