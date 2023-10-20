# Pyspark Warsztaty
## Wprowadzenie
Jest to platforma programistyczną dla obliczeń rozproszonych. 

Wiele informacji można zaleźć online w dokumentacji: https://spark.apache.org/docs/latest/ oraz w książce: https://databricks.com/p/ebook/learning-spark-from-oreilly

Aplikację Sparkową można uruchamiać nie tylko na wielu wątkach procesora naszej maszyny, lecz obliczenia mogą być dokonywane w klastrze obliczeniowym. Na tych warsztatach skupimy się na części czysto programistycznej.

Inną platformą, nieco starszą, jest Apache Hadoop. Jest to otwarta platforma programistyczna napisana w języku Java przeznaczona do rozproszonego składowania i przetwarzania wielkich zbiorów danych przy pomocy klastrów komputerowych.
W skład tej platformy wchodzi: Hadoop MapReduce, HDFS i Apache Hadoop YARN.
### Z czego się składa Spark
![](https://i.ibb.co/JjLCTSW/spark1.png)
### Podstawowe pojęcia
#### Aplikacja
Program użytkownika napisany z użyciem API Sparka. Składa się z następujących elementów: Spark driver (sterownik) oraz executor (wykonawca) w klastrze.
#### SparkSession
Obiekt, który pozwala na interakcję ze Sparkowym API. Używając powłoki sparkowej (Sparkshell) Spark driver inicjuje obiekt SparkSession dla Ciebie. Pisząc własną aplikację, musisz sam stworzyć taki obiekt.
#### Job
Równoległe obliczenie składające się z wielu tasków wywoływane akcją sparkową (np. poleceniem save(), show(), collect())
#### Stage
Każdy job jest podzielony na mniejsze zbiory tasków zwany Stage'ami.
#### Task
Pojedyncza jednostka pracy wysyłana do Spark executora.
### Przykład - akcje i operacje, leniwa ewaluacja
Uruchom poniższy kod w interaktywnej konsoli sparka:
```python
sc = spark.SparkContext
txt = sc.textFile('pan-tadeusz.txt')  
filtered = txt.filter(lambda x: 'a' in x)
filtered.count()
```
Jest to dosyć prosty przykład zliczający ilość linii w pliku tekstowym.
### Możemy skorzystać z jakiegoś IDE
Teraz stworzymy własną aplikację:
```python
from pyspark import SparkContext, SparkConf  
  
spark_config = SparkConf().setMaster("local[*]")  
sc = SparkContext(conf=spark_config)  
  
txt = sc.textFile('pan-tadeusz.txt')  
print(txt.filter(lambda x: 'a' in x).count())
```
W przypadku wykorzystywania jakiegoś środowiska programistycznego przydatne może być zainstalowanie biblioteki `pyspark-stubs` - wspomaga ona wykrywanie klas obiektów i podpowiadanie dostępnych metod.
```
pip install pyspark-stubs
```
## RDD

RDD - Resilient Distributed Dataset

Jest to "odporny na uszkodzenia" zbiór elementów, na których można pracować równolegle. Istnieją dwa sposoby tworzenia RDD: zrównoleglenie istniejącej kolekcji lub odwołanie się do zestawu danych w zewnętrznym systemie pamięci masowej, takim jak system plików, HDFS, HBase lub dowolne źródło danych oferujące format danych wejściowych Hadoopa.

#### Zad 1. 
Uzupełnij poniższy kod tak, aby na wyjście dostać przybliżenie liczby pi.
```python
import random
NUM_SAMPLES = 10_000_000  
  
def inside(_):  
    x, y = random.random(), random.random()  
    return x*x + y*y < 1  
  
  
count = sc.parallelize(range(0, NUM_SAMPLES)).???  
print(f"Pi wynosi około {4 * count/NUM_SAMPLES}")
```
Poniższy przykład obrazuje metody takie, jak `map()`, `for_each()`, czy `flatMap()`.
```python
from pyspark import SparkContext, SparkConf  
  
spark_config = SparkConf().setMaster("local[*]")  
sc = SparkContext(conf=spark_config)  
  
file = sc.textFile("pan-tadeusz.txt")  
file.map(lambda x: x.upper()).foreach(print)  
  
print(file.flatMap(lambda x: x.split(' ')).count())  
  
a = file.collect()  
print(a)
```
RDD posiadają wiele dodatkowych metod, szczególnie w wypadku gdy kolekcja składa się z elementów: klucz-wartość.
```python
lines = sc.textFile("pan-tadeusz.txt")  
pairs = lines.flatMap(lambda x: x.split(' ')).map(lambda s: (s, 1))  
counts = pairs.reduceByKey(lambda a, b: a + b)
``` 
#### Zad2.
Poniższy kod jest nieco przekombinowany. Uprość go tak, aby nie zmienić wyniku.
```python
people = sc.parallelize(  
    [(1, ["Jan", "Kowalski", 20]), (2, ["Wojciech", "Jaruzelski", 31]), (3, ["Rafał", "Kawa", 50]), (4, ["Adam", "Roman", 35]), (5, ["Monika", "Ogórek", 25])])
bills = sc.parallelize([(1, 100), (2, 200), (1, 50), (4, 20), (5, 120), (5, 80), (1, 20)])  
joined = people.join(bills)  
# print(joined.collect())  
joined_list = joined.mapValues(lambda x: x[0] + [x[1]])  
# print(joined_list.collect())  
print(joined_list.foldByKey(0, lambda x, y: x + y[3]).collect())
```
## DataFrame
Korzystaliśmy do tej pory z dosyć niskopoziomowego obiektu. Przejdziemy teraz na wyższy poziom abstrakcji.
Będzie używać tzw. DataFrame'ów - jest to struktura danych inspirowana pandasowymi DataFrame'ami. Jest to tabela, gdzie każda kolumna jest określonego typu (liczba całkowita, string, tablica, liczba rzeczywista, data, czas itp.) niczym kolumny tabeli w bazie danych. Podobieństwo nie jest przypadkowe, gdyż możemy wykorzystać język SQL do operacji na DF.
### Jak stworzyć DataFrame?
Jedną z opcji jest zdefiniowanie schematu dataframe'a i umieszczenie w nim danych, jak pokazano w przykładzie poniżej:
```python
from pyspark.sql import SparkSession  
from pyspark.sql.types import StructType, StructField, ArrayType, IntegerType, StringType  
  
schema = "`Id` INT, `First` STRING, `Last` STRING, `Url` STRING, `Published` STRING, `Hits` INT, `Campaigns` ARRAY<STRING>"  
# alternatywnie  
schema2 = StructType([StructField("Id", IntegerType(), False),  
  StructField("First", StringType(), False),  
  StructField("Last", StringType(), False),  
  StructField("Url", StringType(), False),  
  StructField("Published", StringType(), False),  
  StructField("Hits", IntegerType(), False),  
  StructField("Campaigns", ArrayType(StringType(), True), False)])  
  
data = [[1, "Jules", "Damji", "https://tinyurl.1", "1/4/2016", 4535, ["twitter", "LinkedIn"]],  
  [2, "Brooke", "Wenig", "https://tinyurl.2", "5/5/2018", 8908, ["twitter", "LinkedIn"]],  
  [3, "Denny", "Lee", "https://tinyurl.3", "6/7/2019", 7659, ["web", "twitter", "FB", "LinkedIn"]],  
  [4, "Tathagata", "Das", "https://tinyurl.4", "5/12/2018", 10568, ["twitter", "FB"]],  
  [5, "Matei", "Zaharia", "https://tinyurl.5", "5/14/2014", 40578, ["web", "twitter", "FB", "LinkedIn"]],  
  [6, "Reynold", "Xin", "https://tinyurl.6", "3/2/2015", 25568, ["twitter", "LinkedIn"]]  
        ]  
  
spark = SparkSession.builder.master("local[*]").getOrCreate()  
blogs_df = spark.createDataFrame(data, schema)  
blogs_df.show()  
print(blogs_df.printSchema())
```
Innym sposobem jest wczytanie danych bezpośrednio z pliku. Możemy wtedy zlecić Sparkowi, aby sam odkrył schemat tabeli lub zrobił to ręcznie.

```python  
spark = SparkSession.builder.master("local[*]").getOrCreate()  
salaries = spark.read.csv("data/salaries.csv", inferSchema=True, header=True)  
salaries.show()  
salaries.printSchema()
```

Dzieje się to, przez ustawienie argumentu `inferSchema` na wartość `True`. 
#### Zad 4.
Jak widać na powyższym przykładzie nie działa to idealnie - ewidentnie mamy daty, ale Spark traktuje je jako pola typu `string`. Twoim zadaniem jest stworzenie odpowiedniego schematu tabeli i podanie go jako odpowiedni argument metody `csv()`.

### Działania na DataFrame'ach

Załadujmy wszystkie dataframe'y z folderu data.
```python
from pyspark.sql import SparkSession  
from pyspark.sql.functions import lit, col  
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType  
  
schema_salaries = ???
  
schema_department = StructType([  
  StructField("dept_no", StringType(), False),  
  StructField("dept_name", StringType(), False)  
])  
  
schema_dept_emp = StructType([  
  StructField("emp_no", IntegerType(), False),  
  StructField("dept_no", StringType(), False),  
  StructField("from_date", DateType(), False),  
  StructField("to_date", DateType(), False)  
])  
  
schema_dept_manager = StructType([  
  StructField("dept_no", StringType(), False),  
  StructField("emp_no", IntegerType(), False),  
  StructField("from_date", DateType(), False),  
  StructField("to_date", DateType(), False)  
])  
  
schema_employees = StructType([  
  StructField("emp_no", IntegerType(), False),  
  StructField("birth_date", DateType(), False),  
  StructField("first_name", StringType(), False),  
  StructField("last_name", StringType(), False),  
  StructField("gender", StringType(), False),  
  StructField("hire_date", DateType(), False)  
])  
  
schema_titles = StructType([  
  StructField("emp_no", IntegerType(), False),  
  StructField("title", StringType(), False),  
  StructField("from_date", DateType(), False),  
  StructField("to_date", DateType(), False)  
])
spark = SparkSession.builder.master("local[*]").getOrCreate()  
  
departments = spark.read.csv("data/departments.csv", schema=schema_department, header=True)  
dept_emp = spark.read.csv("data/dept_emp.csv", schema=schema_dept_emp, header=True)  
dept_manager = spark.read.csv("data/dept_manager.csv", schema=schema_dept_manager, header=True)  
employees = spark.read.csv("data/employees.csv", schema=schema_employees, header=True)  
salaries = spark.read.csv("data/salaries.csv", schema=schema_salaries, header=True)  
titles = spark.read.csv("data/titles.csv", schema=schema_titles, header=True)  

```
Wykonajmy przykładową operację na DF salaries.
```python
salaries.select("*").where("from_date > '1994-06-22'").show()  
salaries.where(salaries["from_date"] > "1994-06-22").show()  
salaries.where(col("from_date") > lit("1994-06-22")).show()  
  
salaries.createOrReplaceTempView("salaries")  
spark.sql("SELECT * FROM salaries WHERE from_date > '1994-06-22'").show()
```
Wszystkie powyższe operacje są równoważne. Zwracamy wszystkie wiersze, gdzie data początkowa (kolumna from_date) jest późniejsza niż 1994-06-22.

Zwróć uwagę, że bez operacji `show()` nic się nie wykona - nawet plik nie zostałby wczytany. Spark działa "leniwie", czyli nie wykonuje operacji, dopóki nie musi, czyli nie zostanie wywołana akcja (jak `show()`, `collect()`, czy `save()`). Dzięki temu, gdy stworzymy odpowiednio złożone zapytanie, Spark może je zoptymalizować przed wykonaniem. Używa do tego optymalizatora zwanego Catalyst.

Zobaczmy bardziej skomplikowany przykład.
```python
  
joined = dept_emp \  
    .join(employees, dept_emp['emp_no'] == employees['emp_no'])  
  
joined.show()  
  
stats = joined.groupby('dept_no').agg(  
    count(when(col("gender") == 'M', True)).alias("Males"),  
  count(when(col("gender") == 'F', True)).alias("Females")  
)  
  
stats.show()  
  
joined2 = stats\  
    .join(departments, departments['dept_no'] == stats['dept_no'])\  
    .select(["dept_name", "Males", "Females"]).show()  
  
departments.createOrReplaceTempView("departments")  
dept_emp.createOrReplaceTempView("dept_emp")  
employees.createOrReplaceTempView("employees")  
  
spark.sql("SELECT dept_name, Males, Females "  
 "FROM " 
 "( SELECT dept_no, COUNT(CASE WHEN gender = 'M' THEN TRUE END) AS Males, COUNT(CASE WHEN gender = 'F' THEN TRUE END) AS Females "  
 "FROM dept_emp AS de JOIN employees as e ON de.emp_no = e.emp_no " 
 "GROUP BY dept_no ) AS j " 
 "JOIN departments AS d ON d.dept_no = j.dept_no").show()
```

#### Zad 5.
Napisz kod, który zwróci DF z następującymi kolumnami: imię pracownika, nazwisko pracownika oraz pole zawierające informację, czy jest obecnie zatrudniony.

#### Zad 6.
Napisz kod, który zwróci DF z następującymi kolumnami: nazwa departamentu, średnia pensja obecnie zatrudnionych pracowników w tym departamencie.


### DataFrame a RDD

Z punktu widzenia Pythona DataFrame skłąda się z RDD, który przechowuje obiekt klasy Row. Z DataFrame możemy odwołać się do RDD przez pole `.rdd` na przykład:
```
joined2.rdd.foreach(print)
```
W drugą stronę też możemy dokonać przekształcenia RDD składającego się z obiektów Row lub dowolnej kolekcji do DF za pomocą metody `.toDF()`.

```python
from pyspark import SparkContext, SparkConf  
from pyspark.sql import SparkSession  
  
spark_config = SparkConf().setMaster("local[*]")  
sc = SparkContext(conf=spark_config)  
  
people = sc.parallelize(  
    [(1, ["Jan", "Kowalski", 20]), (2, ["Wojciech", "Jaruzelski", 31]), (3, ["Rafał", "Kawa", 50]), (4, ["Adam", "Roman", 35]),  
  (5, ["Monika", "Ogórek", 25])])  
  
spark = SparkSession(sc)  
people.map(lambda x: x[1]).toDF().show()
```
Pamiętaj! Bez zainicjalizowanej sesji sparka nie możemy używać DF (metoda toDF nie będzie dostępna).

### Zapis do pliku
Zapis dataframe'u do pliku odbywa się za pomocą metody `write`. Jako, że PySpark wykonuje zadania równolegle, to powstanie tyle plików, na ile tasków zostaną podzielone nasze obliczenia, w folderze o nazwie, którą podaliśmy. PySpark nie ma problemu z odczytem takich danych, lecz jeżeli mamy taką potrzebę to możemy wymusić zapis do jednego pliku, jak w poniższym przykładzie:
```python
resultDF.coalesce(1).write.csv("filename")
``` 

## MLlib
Skupimy się na 2 zadaniach uczenia maszynowego. Regresji i klasyfikacji.
Musimy mieć zainstalowany pakiet numpy.
```bash
pip install numpy==1.19.3
```
Omówię poniższy przykład - rozwiązujemy problem klasyfikacji, gdzie część przykładów należy do klasy 1, a część do klasy 0. Możemy to sobie wyobrażać, że np. mamy na wejście naszego klasyfikatora wyniki badań pacjentów, a na wyjściu mamy wartość 1 - pacjent ma nowotwór złośliwy lub 0 - brak nowotworu złośliwego.
```python
from pyspark.ml.classification import LogisticRegression  
from pyspark.ml.evaluation import MulticlassClassificationEvaluator  
from pyspark.mllib.classification import LogisticRegressionModel  
from pyspark.sql import SparkSession  
  
spark = SparkSession.builder.master("local[*]").getOrCreate()  
  
data = spark.read.format("libsvm").load("mllib/sample_libsvm_data.txt")  
data.show(truncate=False)  
  
trainingData, testData = data.randomSplit([0.7, 0.3])  
  
lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)  
  
lrModel: LogisticRegressionModel = lr.fit(trainingData)  
  
print("Coefficients: " + str(lrModel.coefficients))  
print("Intercept: " + str(lrModel.intercept))  
  
predictions = lrModel.transform(testData)  
  
predictions.show()  
  
print(f"Train set sccuracy: {lrModel.summary.accuracy}")  
  
test_accuracy = MulticlassClassificationEvaluator(metricName="accuracy").evaluate(predictions)  
  
print(f"Test set sccuracy: {test_accuracy}")
```
Poniżej mamy przykład zadania regresji - przewidujemy wartość ceny za nocleg na podstawie parametrów nieruchomości. W przeciwieństwie do poprzedniego przykładu, nie mamy tu danych w formacie gotowym do podania argument metody `fit()`, tu używamy obiektu `VectorAssembler`.
```python
from pyspark.ml.evaluation import RegressionEvaluator  
from pyspark.sql import SparkSession  
from pyspark.ml.feature import VectorAssembler  
from pyspark.ml.regression import LinearRegression  
  
spark = SparkSession.builder.master("local[*]").getOrCreate()  
  
filePath = "mllib/sf-airbnb-clean.parquet"  
airbnbDF = spark.read.parquet(filePath)  
airbnbDF = airbnbDF.select("bedrooms", "bathrooms", "number_of_reviews", "price")  
airbnbDF.show(5)  
  
trainDF, testDF = airbnbDF.randomSplit([0.8, 0.2])  
  
vecAssembler = VectorAssembler(inputCols=["bedrooms", "bathrooms", "number_of_reviews"], outputCol="features")  
vecTrainDF = vecAssembler.transform(trainDF)  
vecTestDF = vecAssembler.transform(testDF)  
  
lr = LinearRegression(featuresCol="features", labelCol="price", maxIter=20)  
lrModel = lr.fit(vecTrainDF)  
  
print(f"Mean absolute error on train set: {lrModel.summary.meanAbsoluteError}")  
  
predictions = lrModel.transform(vecTestDF)  
  
mean_test_error = RegressionEvaluator(metricName="mae", labelCol="price").evaluate(predictions)  
  
print(f"Mean absolute error on test set: {mean_test_error}")
```

#### Zad 7. 
Dopisz fragment kodu do predykcji ceny wynajmu, dzięki któremu będziesz mógł dokonać predykcji dla swoich parametrów.

#### Zad 8.
Na podstawie poprzednich przykładów i dokumentacji: https://spark.apache.org/docs/latest/ml-classification-regression.html stwórz swój algorytm klasyfikacji ręcznie pisanych cyfr ze zbioru MNIST. Dane można pobrać stąd: https://pjreddie.com/projects/mnist-in-csv/ Możesz wybrać dowolny algorytm klasyfikacji spośród tych dostępnych w module mllib.
