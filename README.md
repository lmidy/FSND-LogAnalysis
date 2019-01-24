# FSND-LogAnalysis

## Project Rubric
[Project Rubric](https://review.udacity.com/#!/rubrics/277/view)

## How to run program
###### Run the following to create tables for news data db
'''
psql -d news -f newsdata.sql
'''
###### Connect to the database
'''
psql -d news 
'''
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

## Program design
- each of the questions are answered using a single query
- minimize use of views if you can
- comment areas of code that are personally new to me in relation to using DB API
- attempt to match output format suggested in sample
