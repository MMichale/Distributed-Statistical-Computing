#!/bin/bash

PWD=$(cd $(dirname $0); pwd)
cd $PWD 1> /dev/null 2>&1

TASKNAME=stock_day_avg
# python location on hadoop
# PY27='/fli/tools/python2.7.tar.gz'
# hadoop client
# HADOOP_HOME=/home/users/fli/hadoop/bin/hadoop
HADOOP_INPUT_DIR=/user/devel/2020210972bicheng/stocks.txt
HADOOP_OUTPUT_DIR=/user/devel/2020210972bicheng/output

echo $HADOOP_HOME
echo $HADOOP_INPUT_DIR
echo $HADOOP_OUTPUT_DIR

hadoop fs -rm -r $HADOOP_OUTPUT_DIR

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar \
-D mapred.job.name=TASKNAME \
-D mapred.job.priority=NORMAL \
-D stream.memory.limit=1000 \
-D mapred.map.tasks=10 \
-D mapred.reduce.tasks=7 \
-D mapred.job.map.capacity=100 \
-D mapred.job.map.capacity=100 \
-input ${HADOOP_INPUT_DIR} \
-output ${HADOOP_OUTPUT_DIR} \
-mapper "$PWD/stock_day_avg.R" \
-file "$PWD/stock_day_avg.R"
# -cacheArchive ${PY27}#py27 \
# -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

# following are others generic command, if use ,please put them above streaming Options
# -D mapred.compress.map.output=True # if output of map is compressed
# -D mapred.map.output.comression.codec=org.apache.hadoop.io.compress.GzipCodec # compress mode
# -D mapred.output.compress=True # if output of reduce is compressed
# -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec # compress mode
# -D stream.map.output.field.separator=. # default \t
# -D stream.num.map.output.key.fields=4 # default the part before the first \t serves as the key
# -D stream.reduce.output.field.separator=.
# -D stream.num.reduce.output.key.fields=4
# -D map.output.key.field.separator=. # Sets the delimiter inside the Key in the Map output
# -D mapreduce.partition.keypartitioner.options=-k1,2 # equal -D num.key.fields.for.partition=2
# This is effectively equivalent to specifying the first two fields 
# as the primary key and the next two fields as the secondary. The primary key is used for partitioning, and the combination of the primary and secondary keys is used for sorting.
    


if [ $? -ne 0 ]; then
    echo 'error'
    exit 1
fi
hadoop fs -touchz ${HADOOP_OUTPUT_DIR}/done

hadoop fs -ls $HADOOP_OUTPUT_DIR | cat

exit 0