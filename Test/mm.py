import openpyxl
from googletrans import Translator
if __name__ == '__main__':

        # 设置目标语言
        target_lang = 'en'

        # 加载 Excel 文件
        excel_file = '/Users/zengli/downloads/mm.xlsx'
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

        # 初始化翻译器
        translator = Translator(service_urls=['translate.google.com'])

        # 遍历第一个工作表的每个单元格，并进行翻译
        for row in sheet.iter_rows():
            for cell in row:
                # 获取单元格的值
                cell_value = cell.value

                # 使用 Google Translate 进行翻译
                translated_text = translator.translate(cell_value, dest=target_lang).text

                # 将翻译结果写回单元格
                cell.value = translated_text

        # 保存修改后的 Excel 文件
        translated_file = '/Users/zengli/downloads/mm.xlsx'
        workbook.save(translated_file)