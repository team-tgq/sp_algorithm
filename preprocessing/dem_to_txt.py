from services import read_dem

# 假设这是你的DEM高程数组
dem_data = read_dem.Dem("../data/Copernicus_DSM_COG_10_N00_00_W062_00_DEM.tif", 30)

height_array = dem_data.height.copy()

# 指定要写入的文件路径
file_path = "../output/csv/mountain.txt"

# 将数组写入文件
with open(file_path, 'w') as f:
    for row in height_array:
        # 将每行转换为以逗号分隔的字符串，并写入文件
        line = ','.join(map(str, row))
        f.write(line + '\n')

print(f"文件已保存到 {file_path}")
