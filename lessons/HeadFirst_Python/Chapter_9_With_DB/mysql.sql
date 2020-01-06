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

select *
from log;

-- кол-во записей
select count(*)
from log;

-- список самых повторяющихся букв
select count(letters) as 'count', letters
from log
group by letters
order by count desc
limit 1;

-- список ip
select distinct ip
from log;

-- самый используемый браузер
select count(letters) as 'count', browser_string
from log
group by browser_string
order by count desc
limit 1;
