## 主要学习一些SQL语句的知识
EDR 
SELECT 查询语句
SQL不区分大小写
真实情境很少用到DROP和CREATE语句，需要很高的权限，往往数据管理员才可以

每个 SQL 查询
每个查询至少有一个 SELECT 和 FROM 语句。 SELECT 语句用于放置要显示数据的列。 FROM 语句用于放置要从中提取数据的表。
```sql
    SELECT *  
    FROM orders;
```

大写命令（SELECT、FROM），小写查询中的其他内容是常见做法。


表和变量名中不需要空格
通常在列名中使用下划线，避免使用空格。 在 SQL 中使用空格有点麻烦。 在 Postgres 中，如果列或表名称中有空格，就需要使用双引号括住这些列/表名称（例如：FROM \"Table Name\"，而不是 FROM table_name）。在其他环境中，可能会使用方括号（例如：FROM [Table Name]）。

在查询中使用空格
SQL 查询忽略空格，因此可以根据需要在代码之间添加尽可能多的空格和空行，并且查询结果是相同的。

LIMIT 数字
显示返回结果的行数

19  
```sql
SELECT *
FROM demo.orders
ORDER BY occurred_at
LIMIT 10
```
默认升序排列（ascending)
末尾加DESC：降序排列

20
```sql
SELECT account_id,total_amt_usd
FROM orders
ORDER BY account_id,total_amt_usd DESC
-- id递增，且在id相同的前提下，total_amt_usd降序排列
SELECT account_id,total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC,account_id
-- total_amt_usd严格降序排列
```
22
```sql
SELECT *
FROM orders
WHERE count_id=4251
ORDER BY occurred_at
LIMIT 100
```
WHERE要放在FROM之后，ORDER BY或LIMIT之前
支持非值查找，用单引号括起来

25
derived column(派生列)：将现有列进行组合
```sql
SELECT account_id,
       occurred_at,
       standard_qty,
       gloss_qty,
       poster_qty,
       gloss_qty + poster_qty AS nonstandard_qty
FROM orders
```
可以添加新的列，名字为：nonstandard_qty
命名惯例，无代码和空格

**练习**：
编写一个查询，查找每个订单海报纸的收入百分比。 只需使用以 _usd 结尾的列。 （在这个查询中试一下不使用总列）。包含 id 和 account_id 字段

```sql
SELECT id,account_id,poster_amt_usd/(standard_amt_usd+gloss_amt_usd+poster_amt_usd) AS post_per
FROM orders
LIMIT 10
```

26
LIKE 寻找包含某个字段的信息
需要使用通配符(wildcard),下面的通配符是%
```sql
SELECT *
FROM web_events_full
WHERE referer_url LIKE '%google%';
```
%代表任意数量的字符

27
IN
```sql
SELECT *
FROM accounts
WHERE name IN('Walmart','Apple')
```
''将字符串括起来，值可以直接输入
```sql    
SELECT *
FROM accounts
WHERE account_id IN(1001,1021)
```
调出账户里的1001号和1021号的信息
28
NOT
```sql
SELECT sales_rep_id,name
FROM accounts
WHERE sales_rep_id NOT IN(321500,321570)
ORDER BY sales_rep_id
```
29
AND和BETWEEN
```sql
SELECT *
FROM orders
WHERE occurred_at >= '2016-04-01' AND occurred_at <= '2016-10-01'
ORDER BY occurred_at DESC
```
**练习**
使用客户表查找所有不以 'C' 开始但以 's' 结尾的公司名
```sql
select name
FROM accounts
WHERE name NOT LIKE 'C%' and name LIKE '%s'
```
**练习**
```sql
SELECT *
FROM web_events
WHERE channel IN('organic','adwords') AND occurred_at BETWEEN '2016-01-01' AND '2017-01-01'
ORDER BY occurred_at DESC
--BETWEEN 一般情况下不包括端点值，假设时间是 00:00:00（即午夜），这就是我们将右边的时间点设置为 '2017-01-01' 的原因了
```
30
```sql
SELECT account_id,
       occurred_at,
       standard_qty,
       gloss_qty,
       poster_qty
FROM orders
WHERE (standard_qty = 0 OR gloss_qty = 0 OR poster_qty = 0)
AND occurred at >= '2016-10-01'
```
**练习**
查找以 'C' 或 'W' 开头的所有公司名 (company names)，主要联系人 (primary contact) 包含 'ana' 或 'Ana'，但不包含 'eana
```sql
SELECT *
FROM accounts
WHERE name LIKE 'C%' OR name LIKE 'W%' 
	  AND(primary_poc LIKE '%ana%' OR primary_poc LIKE '%Ana%')
      AND primary_poc NOT LIKE '%eana%'
```

**SQL命令概述**
语句 | 使用方法 |  其他详细信息
- | :-: | -: 
SELECT | SELECT Col1,Col2,...| 提供你需要的列 
FROM | FROM Table | 提供列所在的表格 
LIMIT | LIMIT | 10
ORDER BY |ORDER BY Col|根据列命令表格。与 DESC 一起使用
WHERE| WHERE Col > 5|用于过滤结果的一个条件语句
LIKE| WHERE Col LIKE '%me%'|仅提取出列文本中具有 'me' 的行
IN|WHERE Col IN ('Y', 'N') |仅过滤行对应的列为 'Y' 或 'N'
NOT| WHERE Col NOT IN ('Y', "N')|NOT 经常与 LIKE 和 IN 一起使用
AND| WHERE Col1 > 5 AND Col2 < 3|过滤两个或多个条件必须为真的行
OR|WHERE Col1 > 5 OR Col2 < 3 | 过滤一个条件必须为真的行
BETWEEN| WHERE Col BETWEEN 3 AND 5 | 一般情况下，语法比使用 AND 简单一些

**其他**

- 不区分大小写
- 关键词顺序很重要
```sql
SELECT col1, col2
FROM table1
WHERE col3  > 5 AND col4 LIKE '%os%'
ORDER BY col5
LIMIT 10;
```

**移动平均值**
移动平均值用于将数据线性化，以便更容易观察长期趋势，也不会因日常波动而错乱。例如，假设你想可视化服装零售店的销售趋势。从每天的数据开始，而图表看起来太不稳定，因为更多的人在周末购物，所以销售额会在周末飙升。
使用移动平均值可使每日波动平滑一些，也可以观察长期趋势。










