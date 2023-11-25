import os

def generate_video_list(folder_path, output_file):
    with open(output_file, 'w') as f:
        f.write("# 视频列表\n\n")
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith((".mp4", ".avi", ".mov")):
                    video_path = os.path.join(root, file)
                    video_name = os.path.splitext(file)[0]
                    f.write(f"- [{video_name}]({video_path})\n")

# 使用示例
folder_path = "simple_video_sample/svd"
output_file = "simple_video_sample/svd/readmd.md"
generate_video_list(folder_path, output_file)
