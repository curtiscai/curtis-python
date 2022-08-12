from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


def file_plit(src_folder, des_folder):
    """
    拆分pdf
    """
    file_list = list(src_folder.glob('*.pdf'))
    step = 5
    for pdf in file_list:
        input_file = PdfFileReader(str(pdf))
        pages = input_file.getNumPages()
        if pages <= step:
            print(f'【{pdf.name}】页数为{pages}，小于等于每份页数{step}，不做拆分')
            continue
        parts = pages // step + 1
        for pt in range(parts):
            start = step * pt
            if pt != (parts - 1):
                end = start + step - 1
            else:
                end = pages - 1
            output_file = PdfFileWriter()
            for pn in range(start, end + 1):
                output_file.addPage(input_file.getPage(pn))
                pt_name = f'{pdf.stem}_第{pt + 1}部分.pdf'
                pt_file = des_folder / pt_name
                with open(pt_file, 'wb') as f_out:
                    output_file.write(f_out)
        print(f'【{pdf.name}】页数为{pages}，拆分为{parts}部分')


src_folder = Path('E:/PythonProjects/yjy-python/curtis-python/file/pdf/src_folder')
des_folder = Path('E:/PythonProjects/yjy-python/curtis-python/file/pdf/des_folder')
# file_plit(src_folder, des_folder)



src_folder = Path('E:/PythonProjects/yjy-python/curtis-python/file/pdf/des_folder')
des_file = Path('E:/PythonProjects/yjy-python/curtis-python/file/pdf/des_folder/合并后的文件.pdf')
if not des_file.parent.exists():
    des_file.parent.mkdir(parents=True)
file_list = list(src_folder.glob('*.pdf'))
merger = PdfFileMerger()
outputPages = 0
for pdf in file_list:
    inputfile = PdfFileReader(str(pdf))
    merger.append(inputfile)
    pageCount = inputfile.getNumPages()
    print(f'{pdf.name}  页数：{pageCount}')
    outputPages += pageCount
merger.write(str(des_file))
merger.close()
print(f'\n合并后的总页数：{outputPages}')
