
import pandas as pd


# 读取配置文件
def read_config(file_path):
    config_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            key, value = line.strip().split('=')
            config_dict[key] = value.strip('"')
    return config_dict


# 读取Excel文件
def read_excel(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name=sheet_name)


# 查找并生成翻译结果
def generate_translations(config_dict, df):
    ar_dict = {}
    hi_dict = {}
    # 将Excel数据转换为字典格式
    translation_dict = {str(row['En']).lower(): {'ar': row['Arbic'], 'hi': row['Hindi']} for index, row in df.iterrows()}

    # 遍历配置数据，查找翻译
    for key, english_value in config_dict.items():
        english_value = english_value.split('"')[1].lower()
        if english_value in translation_dict:
            ar_dict[key] = translation_dict[english_value]['ar']
            hi_dict[key] = translation_dict[english_value]['hi']
        else:
            ar_dict[key] = ''
            hi_dict[key] = ''

    return ar_dict, hi_dict


# 写入文件
def write_config(file_path, config_dict):
    with open(file_path, 'w', encoding='utf-8') as f:
        for key, value in config_dict.items():
            f.write(f'{key}="{value}";\n')


# 主函数
def main():
    config_en_file_path = '/Users/zengli/PycharmProjects/pythonProject/H100/Multilingual/config_en'  # 替换为你的config_en文件路径
    excel_file_path = '/Users/zengli/PycharmProjects/pythonProject/H100/Multilingual/configExcel.xlsx'  # 替换为你的Excel文件路径
    # sheet_name = 'booking'  # 替换为你的工作表名称


    # 读取文件
    config_en_dict = read_config(config_en_file_path)
    # df = read_excel(excel_file_path, sheet_name)

    xls = pd.ExcelFile(excel_file_path)
    all_data = pd.DataFrame()
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)  # 读取指定sheet的数据
        df['sheet_name'] = sheet_name  # 可选：添加一列来标识这个数据来自哪个sheet
        all_data = pd.concat([all_data, df], ignore_index=True)  # 合并数据


    # 查找翻译
    ar_dict, hi_dict = generate_translations(config_en_dict, all_data)

    # 写入文件
    write_config('config_ar', ar_dict)
    write_config('config_hi', hi_dict)


if __name__ == "__main__":
    main()
