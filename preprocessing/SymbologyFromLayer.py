"""
同一可视域符号系统，由于该环境没有arcpy解释器，以下代码在ArcgIS的python命令行执行
"""
import arcpy


# 符号系统源文件 手动先确定格式+
symbology_source = r"可视域_旋转\final_view_29.tif"

# 循环遍历目标栅格文件并应用符号系统
for i in range(29):  # 假设你有从 final_view_0.tif 到 final_view_29.tif 总计30个文件
    target_raster = rf"可视域_旋转\final_view_{i}.tif"
    # 应用符号系统
    arcpy.management.ApplySymbologyFromLayer(target_raster, symbology_source, None, "MAINTAIN")
    print(f"Applied symbology to {target_raster} from {symbology_source}")
