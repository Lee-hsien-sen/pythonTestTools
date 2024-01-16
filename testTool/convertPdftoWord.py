"""
#pdf转word工具
#
"""

from pdf2docx import Converter


def convert_pdf_to_word(input_path, output_path):
    try:
        # 创建转换器对象
        converter = Converter(input_path)

        # 将 PDF 转换为 Word 文档
        converter.convert(output_path)

        # 关闭转换器
        converter.close()

        print("转换完成！")
    except Exception as e:
        print("转换失败:", str(e))


if __name__ == '__main__':
    # 调用函数进行转换
    pdf_file = "/Users/zengli/Documents/柠檬班软件测试面试宝典{400页800pdf）.pdf"  # 输入的 PDF 文件路径
    word_file = "/Users/zengli/Documents/output.docx"  # 输出的 Word 文件路径
    convert_pdf_to_word(pdf_file, word_file)
