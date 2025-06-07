from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

def main(session: Session):
    df = session.table("students")

    df_result = df.with_column("total_marks", col("subject1") + col("subject2") + col("subject3") + col("subject4")) \
                  .with_column("percentage", (col("total_marks") / 400) * 100)

    df_result.write.mode("overwrite").save_as_table("students_result")