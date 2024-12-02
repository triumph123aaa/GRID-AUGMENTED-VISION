from PIL import Image, ImageDraw
import os
from pathlib import Path

def add_grid(image_path, output_path, grid_size=(9, 9), opacity=0.3):
    """
    在图片上添加均匀的网格
    
    参数:
    image_path: 输入图片路径
    output_path: 输出图片路径
    grid_size: 网格大小，默认为(9, 9)
    opacity: 网格线透明度，默认为0.3
    """
    # 打开图片
    img = Image.open(image_path)
    
    # 创建一个透明的图层用于绘制网格
    grid_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(grid_layer)
    
    # 计算网格间距
    cell_width = img.width / grid_size[0]
    cell_height = img.height / grid_size[1]
    
    # 设置线条颜色（黑色）和透明度
    line_color = (0, 0, 0, int(255 * opacity))
    
    # 画垂直线
    for i in range(1, grid_size[0]):
        x = i * cell_width
        draw.line([(x, 0), (x, img.height)], fill=line_color, width=1)
    
    # 画水平线
    for i in range(1, grid_size[1]):
        y = i * cell_height
        draw.line([(0, y), (img.width, y)], fill=line_color, width=1)
    
    # 将原图转换为RGBA模式（如果不是的话）
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # 合并原图和网格图层
    result = Image.alpha_composite(img, grid_layer)
    
    # 保存结果
    result.save(output_path, 'PNG')

def process_folder(input_folder, output_folder):
    """
    处理文件夹中的所有图片
    
    参数:
    input_folder: 输入文件夹路径
    output_folder: 输出文件夹路径
    """
    # 创建输出文件夹（如果不存在）
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # 支持的图片格式
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    
    # 处理所有图片
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(image_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f'grid_{filename}')
            
            try:
                add_grid(input_path, output_path)
                print(f'成功处理: {filename}')
            except Exception as e:
                print(f'处理 {filename} 时出错: {str(e)}')

# 使用示例
if __name__ == '__main__':
    input_folder = r'C:\Users\lenovo\Desktop\dataimage'  # 输入文件夹路径
    output_folder = r'C:\Users\lenovo\Desktop\outimage'  # 输出文件夹路径
    process_folder(input_folder, output_folder)
