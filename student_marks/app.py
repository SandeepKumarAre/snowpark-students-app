from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

def main(session: Session):
    df = session.table("snowpark_app.snowparkapp_schema.students")
    df_result = df.with_column("total", col("maths") + col("physics") + col("chemistry") + col("english")) \
                  .with_column("percentage", ((col("maths") + col("physics") + col("chemistry") + col("english")) / 400) * 100)

    df_result.write.mode("overwrite").save_as_table("snowpark_app.snowparkapp_schema.students_results")




# from snowflake.snowpark import Session
# from snowflake.snowpark.functions import col

# def main(session: Session):
#     df = session.table("students")
#     print(f"conneccted to table and shape of table {df.shape}")

#     df_result = df.with_column("total_marks", col("subject1") + col("subject2") + col("subject3") + col("subject4")) \
#                   .with_column("percentage", (col("total_marks") / 400) * 100)
#     print("Computations are completed")
#     df_result.write.mode("overwrite").save_as_table("students_result")
#     print("Done")