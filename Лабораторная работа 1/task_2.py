# TODO Найдите количество книг, которое можно разместить на дискете

disk_size = 1.44 * 1024 ** 2
page_count = 100
line_count = 50
symbol_count = 25
bytes_for_one_symbol = 4

total_symbols = page_count * line_count * symbol_count
total_bytes = total_symbols * bytes_for_one_symbol
book_count = int (disk_size // total_bytes)

print("Количество книг, помещающихся на дискету:", book_count)
