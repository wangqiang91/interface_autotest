-- 创建数据库：
create database interface_autotest;
-- 创建存储执行测试用例的表；
use interface_autotest;
create table executed_test_cases(
    `id` bigint unsigned NOT NULL primary KEY AUTO_INCREMENT COMMENT '记录id',
    `case_id` VARCHAR(20) NOT NULL DEFAULT 'test_000' COMMENT '用例id',
    `case_name` VARCHAR(50) DEFAULT '' COMMENT '用例名称',
    `url` text CHARACTER SET utf8  NOT NULL  COMMENT '接口链接',
    `method` VARCHAR(20) DEFAULT '' COMMENT '接口方法',
    `headers` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '接口请求头',
    `data` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '请求体',
    `rely_id` VARCHAR(20) DEFAULT '' COMMENT '依赖用例id',
    `rely_field` VARCHAR(100) DEFAULT '' COMMENT '依赖依次取值',
    `case_field` VARCHAR(30) DEFAULT '' COMMENT '依赖字段名称',
    `expect` VARCHAR(255) DEFAULT '' COMMENT '期望值',
    `min_length` int unsigned NOT NULL DEFAULT '0' COMMENT 'text格式下最小长度',
    `is_pass` tinyint unsigned NOT NULL DEFAULT '1' COMMENT '是否通过 1-通过,0-不通过',
    `execute_time` VARCHAR(50) DEFAULT '' COMMENT '用例执行时间',
    `spend_time` VARCHAR(10) DEFAULT '' COMMENT '执行该条用例花费时间',
    `error_message` text CHARACTER SET utf8  NOT NULL  COMMENT '错误信息',
    `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '写入数据库时间'
)

