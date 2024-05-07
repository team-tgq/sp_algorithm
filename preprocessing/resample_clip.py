from osgeo import gdal

# 已经在ArcGis中将分辨率通过双线性插值重采样为5m,再此调用GDAL库将网格数裁切为1000*1000
input_dem_path = '../data/Copernicus_DSM_COG__Resam.tif'
output_dem_path = '../data/RC_Copernicus_DSM_COG_10_N00_00_W062_00_DEM.tif'

# 设置裁剪参数
xmin, ymin = 0, 0  # 替换为实际的起始坐标
xmax, ymax = xmin + 5000, ymin + 5000  # 根据需要调整5000米的增量

# 打开原始DEM
src_ds = gdal.Open(input_dem_path)
if src_ds is None:
    print("Failed to open the DEM file.")

# 使用gdal的Translate函数裁剪DEM
translate_options = gdal.TranslateOptions(projWin=[xmin, ymax, xmax, ymin])  # 注意坐标顺序
clipped_ds = gdal.Translate(output_dem_path, src_ds, options=translate_options)
clipped_ds = None  # 关闭文件

# 清理
src_ds = None
print("Clipping complete. Output saved to:", output_dem_path)
