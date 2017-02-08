hadoop fs -mkdir myinput
hadoop fs -put forum_node.tsv myinput

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper mapper_toptags.py -reducer reducer_toptags.py -file mapper_toptags.py -file reducer_toptags.py -input myinput/forum_node.tsv -output output_toptags
hadoop fs -cat output_toptags/part-00000 > Top_tags_output.csv

echo "1 completed"

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper mapper_PA_length.py -reducer reducer_PA_length.py -file mapper_PA_length.py -file reducer_PA_length.py -input myinput/forum_node.tsv -output output_PA_length
hadoop fs -cat output_PA_length/part-00000 > Post_and_Answer_length_output.csv

echo "2 completed"

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper student_time_mapper.py -reducer student_time_reducer.py -file student_time_mapper.py -file student_time_reducer.py -input myinput/forum_node.tsv -output output_student_time
hadoop fs -cat output_PA_length/part-00000 > Student_peak_active_time_output.csv

echo "3 completed"

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper mapper_StudyGroups.py -reducer reducer_StudyGroups.py -file mapper_StudyGroups.py -file reducer_StudyGroups.py -input myinput/forum_node.tsv -output output_StudyGroups
hadoop fs -cat output_StudyGroups/part-00000 > StudyGroups_output.csv

echo "all done"


hadoop fs -rm -r output_StudyGroups
hadoop fs -rm -r output_student_time
hadoop fs -rm -r output_PA_length
hadoop fs -rm -r output_toptags

