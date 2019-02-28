create table weather_data (
  id int not null auto_increment comment '主键',
  name varchar(80) COLLATE utf8_bin null default '' comment '地区',
  time datetime not null default CURRENT_TIMESTAMP comment '时间',
  weather varchar(50) COLLATE utf8_bin not null default '' comment '天气',
  max_temp int not null default 100 comment '最高温度',
  min_temp int not null default 100 comment '最低温度',
  cur_temp int not null default 100 comment '当前温度',
  humidity int not null default 100 comment '当前湿度',
  wind_dir varchar(50) not null default '' comment '风向',
  wind_power int not null default -1 comment '风力',
  rays int not null default -1 comment '紫外线',
  pm int not null default -1 comment 'PM值',
  primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin comment '天气数据';