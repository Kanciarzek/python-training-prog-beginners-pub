import random
from pyspark import SparkContext, SparkConf

spark_config = SparkConf().setMaster("local[*]")
sc = SparkContext(conf=spark_config)

# txt = sc.textFile('pan-tadeusz.txt')
# print(txt.filter(lambda x: 'a' in x).count())

NUM_SAMPLES = 100_000_000

def inside(_):
    x, y = random.random(), random.random()
    return x*x + y*y < 1


count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
print(f"Pi wynosi około {(4.0 * count / NUM_SAMPLES)}")


