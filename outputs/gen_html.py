import os

def generate_html(folder_path, output_file):
    # 获取文件夹中的所有视频文件
    video_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp4', '.avi', '.mkv'))]

    # 创建HTML文件并写入视频标签
    with open(output_file, 'w') as html_file:
        html_file.write('<html>\n')
        html_file.write('<body>\n')
        for video_file in video_files:
            html_file.write(f'<video controls width="500"> <source src={folder_path}/{video_file} type="video/mp4" /></video>\n')
        html_file.write('</body>\n')
        html_file.write('</html>\n')

 
folder_path = 'simple_video_sample/svd'
output_file = 'result.html'
generate_html(folder_path, output_file)
