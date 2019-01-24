# FSND-LogAnalysis

## Project Rubric
[Project Rubric](https://review.udacity.com/#!/rubrics/277/view)

## How to run program
###### Run the following to create tables for news data db
```
psql -d news -f newsdata.sql
```
###### Connect to the database
```
psql -d news 
```
###### Create Views
```
CREATE VIEW totallogsbydate AS 
SELECT date(time) AS Date, count(date(time)) AS All_Logs_Total 
FROM log 
GROUP BY Date 
ORDER BY Date;
```
```
CREATE VIEW totalerrorsbydate AS
SELECT date(time) AS Date, count(date(time)) AS Error_Total FROM log 
WHERE status = '404 NOT FOUND' 
GROUP BY Date 
ORDER BY Date;
```
```
CREATE VIEW errorrate AS
SELECT totallogsbydate.date AS date, ((totalerrorsbydate.error_total::float/ all_logs_total::float)*100) AS percent
FROM totallogsbydate
LEFT OUTER JOIN totalerrorsbydate ON (totallogsbydate.date = totalerrorsbydate.date);
```
###### run python program
```
python loganalysis.py
```
###### Validate output
```
1. What are the most popular three articles of all time? 
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views

2. Who are the most popular authors of all time? 
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views

3. On which days did more than 1% of requests lead to errors? 
2016-07-17 - 2.2626862468% errors
```

## Program design
- each of the questions are answered using a single query
- minimize use of views if you can
- comment areas of code that are personally new to me in relation to using DB API
- attempt to match output format suggested in sample
