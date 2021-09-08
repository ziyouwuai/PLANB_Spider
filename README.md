# PLAN B Spider




#### 安装教程

```bash
 $ pip3 install -r requirements.txt
```

#### 使用说明

#### 创建表
```sql
CREATE TABLE `zufangluntan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zufang_type` varchar(10) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '租房类型',
  `zufang_title` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '租房标题',
  `author_name` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '作者名称',
  `publish_time` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '发布时间',
  `reply` int(11) DEFAULT NULL COMMENT '回复数量',
  `review` int(11) DEFAULT NULL COMMENT '被查看数量',
  `fabiao_name` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '发布人姓名',
  `fabiao_time` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '最后发表时间',
  `fang_desc` varchar(1000) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '租房详情描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='租房论坛'
```
#### 启动配置
```markdown
    1. 修改config中配置
    2. cd zufangluntan
    3. scrapy crawl zufangluntan 或者 python3 run.py
```


