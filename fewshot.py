import pandas as pd
import json


class FewShot:
    def __init__(self, file_paths=None):
        self.df = pd.DataFrame()
        self.unique_tags = set()
        
        if file_paths is None:
            file_paths = ["Data/hisham_sarwar_processed.json",
                          "Data/irfan_malik_processed.json",
                          "Data/usman_asif_processed.json"]
        
        self.load_posts(file_paths)

    def load_posts(self, file_paths):
        for file_path in file_paths:
            with open(file_path, encoding="utf-8") as f:
                posts = json.load(f)
                temp_df = pd.json_normalize(posts)
                temp_df['length'] = temp_df['line_count'].apply(self.categorize_length)
                
                all_tags = temp_df['tags'].apply(lambda x: x).sum()
                self.unique_tags.update(all_tags)
                

                self.df = pd.concat([self.df, temp_df], ignore_index=True)

    def get_filtered_posts(self, length, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &  
            (self.df['length'] == length)  
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return list(self.unique_tags)


if __name__ == "__main__":
    fs = FewShot(["Data/hisham_sarwar_processed.json", "Data/irfan_malik_processed.json", "Data/usman_asif_processed.json"])
    posts = fs.get_filtered_posts("Medium", "Artificial Intelligence")
    print(posts)
