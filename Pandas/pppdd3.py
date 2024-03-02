import pandas as pd
student_data:[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
      column_names = ["student_id", "age"]
      result_dataframe = pd.DataFrame(student_data, columns=column_names)
      return result_dataframe


