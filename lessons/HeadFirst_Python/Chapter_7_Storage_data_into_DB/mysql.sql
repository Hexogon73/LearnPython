CREATE USER 'vsearch'
  IDENTIFIED BY 'vsearchpasswd';
GRANT ALL
  ON vsearchlogDB.*
  TO 'vsearch'
  WITH GRANT OPTION;


--  cd C:\Program Files\MySQL\MySQL Server 8.0\bin
--  mysql -u vsearch -p vsearchlogDB
--  vsearchpasswd

create table log
(
    id             int auto_increment primary key,
    ts             timestamp default current_timestamp,
    phrase         varchar(128) not null,
    letters        varchar(32)  not null,
    ip             varchar(16)  not null,
    browser_string varchar(256) not null,
    results        varchar(64)  not null
);
describe log;
select * from log;