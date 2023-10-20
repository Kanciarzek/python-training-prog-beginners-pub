# wymaga pip install pyspark

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, ArrayType, IntegerType, StringType, DateType
from pyspark.sql.functions import lit, col, count, when, max



schema_salaries = StructType([StructField("emp_no", IntegerType(), False),
                              StructField("salary", IntegerType(), False),
                              StructField("from_date", DateType(), False),
                              StructField("to_date", DateType(), False),
                              ])

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
departments = spark.read.csv("../data/departments.csv", schema=schema_department,
                             header=True)
dept_emp = spark.read.csv("../data/dept_emp.csv", schema=schema_dept_emp, header=True)
dept_manager = spark.read.csv("../data/dept_manager.csv", schema=schema_dept_manager,
                              header=True)

employees = spark.read.csv("../data/employees.csv", schema=schema_employees, header=True)
salaries = spark.read.csv("../data/salaries.csv", schema=schema_salaries, header=True)
titles = spark.read.csv("../data/titles.csv", schema=schema_titles, header=True)

salaries.select("*").where("from_date > '1994-06-22'").show()
salaries.where(salaries["from_date"] > "1994-06-22").show()
salaries.where(col("from_date") > lit("1994-06-22")).show()
salaries.withColumn("test", lit(1)).show()
salaries.createOrReplaceTempView("salaries")
spark.sql("SELECT * FROM salaries WHERE from_date > '1994-06-22'").show()

joined = dept_emp \
    .join(employees, dept_emp['emp_no'] == employees['emp_no'])
joined.show()
stats = joined.groupby('dept_no').agg(
    count(when(col("gender") == 'M', True)).alias("Males"),
    count(when(col("gender") == 'F', True)).alias("Females")
)
stats.show()
joined2 = stats \
    .join(departments, departments['dept_no'] == stats['dept_no']) \
    .select(["dept_name", "Males", "Females"]).show()
departments.createOrReplaceTempView("departments")
dept_emp.createOrReplaceTempView("dept_emp")
employees.createOrReplaceTempView("employees")
result = spark.sql("SELECT dept_name, Males, Females "
          "FROM "
          "( SELECT dept_no, COUNT(CASE WHEN gender = 'M' THEN TRUE END) AS Males, COUNT(CASE WHEN gender = 'F' THEN TRUE END) AS Females "
          "FROM dept_emp AS de JOIN employees as e ON de.emp_no = e.emp_no "
          "GROUP BY dept_no ) AS j "
          "JOIN departments AS d ON d.dept_no = j.dept_no")


result.coalesce(1).write.csv('test.csv', header=True)  # na pewno zapisze do 1 pliku kosztem wydajności (coalesce)


